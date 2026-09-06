"""Offline regressions for the independently distributed social Skill client.

Run: uv run --no-project --with 'jsonschema>=4.18,<5' python -B -m unittest discover -s tests -p test_social_skill_mcp.py
No real credentials, providers, or paid requests are used.
"""

import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import Mock, patch
import urllib.error
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
CLIENT = ROOT / "amazon-skills/douyin/pixiu/sealeap-pixiu-amazon-account-compliance/scripts/mcp_research.py"
spec = importlib.util.spec_from_file_location("social_mcp", CLIENT)
mcp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mcp)
SCHEMA = {
    "type": "object",
    "properties": {
        "marketplace": {"type": "string", "enum": ["US", "JP"]},
        "limit": {"type": "integer", "minimum": 1, "maximum": 20},
        "query": {"type": "object", "properties": {"keyword": {"type": "string", "minLength": 1}},
                  "required": ["keyword"], "additionalProperties": False},
    },
    "required": ["marketplace", "query"],
    "additionalProperties": False,
}
VALID = {"marketplace": "JP", "limit": 5, "query": {"keyword": "rabbit tray"}}
TOOL = {"name": "keyword_research", "inputSchema": SCHEMA, "annotations": {"readOnlyHint": True}}


class ClientTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="social-mcp-test-")
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.env = patch.dict(os.environ, {item["env"]: "" for item in mcp.PROVIDERS.values()})
        self.env.start()
        self.addCleanup(self.env.stop)
        self.network = patch("socket.socket.connect", side_effect=AssertionError("External network forbidden"))
        self.network.start()
        self.addCleanup(self.network.stop)

    def cli(self, *arguments):
        output = io.StringIO()
        with patch("sys.argv", [str(CLIENT), *arguments]), contextlib.redirect_stdout(output):
            result = mcp.main()
        return result, output.getvalue()

    def tool_client(self, tool=TOOL, provider="sellersprite"):
        client = mcp.MCPClient(provider, "synthetic-test-token", "https://example.invalid", 2)
        client._tools = [tool]
        client._rpc = Mock(return_value={"content": [{"type": "text", "text": "synthetic result"}]})
        return client

    def test_valid_nested_schema(self):
        mcp.validate_schema(VALID, SCHEMA)

    def test_invalid_arguments_never_reach_business_rpc(self):
        invalid = [
            {**VALID, "marketplace": "DE"},
            {**VALID, "limit": "5"},
            {**VALID, "limit": True},
            {**VALID, "limit": 21},
            {**VALID, "limit": 0},
            {**VALID, "query": {}},
            {**VALID, "query": {"keyword": ""}},
            {**VALID, "extra": "unknown"},
        ]
        for arguments in invalid:
            with self.subTest(arguments=arguments):
                client = self.tool_client()
                with self.assertRaises(mcp.MCPError):
                    client.call_tool(TOOL["name"], arguments)
                client._rpc.assert_not_called()

    def test_local_refs_and_alternatives(self):
        schema = {"type": "object", "$defs": {"size": {"oneOf": [{"type": "integer"}, {"const": "all"}]}},
                  "properties": {"size": {"$ref": "#/$defs/size"}}, "required": ["size"]}
        mcp.validate_schema({"size": "all"}, schema)
        with self.assertRaises(mcp.MCPError):
            mcp.validate_schema({"size": "some"}, schema)

    def test_remote_schema_reference_does_not_open_network(self):
        schema = {"type": "object", "properties": {"size": {"$ref": "https://example.invalid/schema"}}}
        with self.assertRaises(mcp.MCPError):
            mcp.validate_schema({"size": 3}, schema)

    def test_draft07_schema_supported(self):
        mcp.validate_schema(VALID, {**SCHEMA, "$schema": "http://json-schema.org/draft-07/schema#"})

    def test_invalid_schema_dialect_fails(self):
        with self.assertRaises(mcp.MCPError):
            mcp.validate_schema(VALID, {**SCHEMA, "$schema": "https://example.invalid/dialect"})

    def test_duplicate_keys_and_nonfinite_numbers_rejected(self):
        for value in ('{"limit":1,"limit":9}', '{"limit":NaN}', '{"limit":Infinity}'):
            with self.subTest(value=value), self.assertRaises(mcp.MCPError):
                mcp.read_arguments(value, None)

    def test_doctor_and_dry_run_need_no_client_or_credentials(self):
        with patch.object(mcp, "MCPClient", side_effect=AssertionError("No network client expected")):
            _, doctor = self.cli("--provider", "sellersprite", "doctor")
            _, dry_run = self.cli("--provider", "sellersprite", "call", "--tool", "keyword_research", "--dry-run")
        self.assertFalse(json.loads(doctor)["credential_configured"])
        self.assertFalse(json.loads(dry_run)["network_called"])
        self.assertFalse(json.loads(dry_run)["schema_checked"])

    def test_doctor_rejects_placeholder(self):
        with patch.dict(os.environ, {"SELLERSPRITE_MCP_SECRET_KEY": "YOUR_TOKEN"}):
            _, output = self.cli("--provider", "sellersprite", "doctor")
        self.assertFalse(json.loads(output)["credential_configured"])

    def test_offline_schema_validation_and_tool_identity(self):
        saved = self.root / "tool.json"
        saved.write_text(json.dumps(TOOL))
        _, result = self.cli("--provider", "sellersprite", "call", "--tool", TOOL["name"],
                             "--arguments", json.dumps(VALID), "--schema-file", str(saved), "--dry-run")
        self.assertTrue(json.loads(result)["schema_checked"])
        self.assertFalse(json.loads(result)["live_schema_checked"])
        with self.assertRaises(mcp.MCPError):
            self.cli("--provider", "sellersprite", "call", "--tool", "wrong_tool",
                     "--arguments", json.dumps(VALID), "--schema-file", str(saved), "--dry-run")

    def test_offline_invalid_request_has_no_output(self):
        saved = self.root / "tool.json"
        result = self.root / "plan.json"
        saved.write_text(json.dumps(TOOL))
        with self.assertRaises(mcp.MCPError):
            self.cli("--provider", "sellersprite", "call", "--tool", TOOL["name"],
                     "--schema-file", str(saved), "--dry-run", "--output", str(result))
        self.assertFalse(result.exists())

    def test_cost_gate_precedes_network(self):
        with patch.object(mcp, "MCPClient", side_effect=AssertionError("No network client expected")):
            with self.assertRaises(mcp.MCPError):
                self.cli("--provider", "sellersprite", "call", "--tool", TOOL["name"])

    def test_existing_output_fails_before_paid_call(self):
        result = self.root / "result.json"
        result.write_text("previous evidence")
        with patch.object(mcp, "MCPClient", side_effect=AssertionError("No network client expected")):
            with self.assertRaises(mcp.MCPError):
                self.cli("--provider", "sellersprite", "call", "--tool", TOOL["name"],
                         "--allow-cost", "--output", str(result))
        self.assertEqual(result.read_text(), "previous evidence")

    def test_business_call_requires_output(self):
        with self.assertRaises(mcp.MCPError):
            self.cli("--provider", "sellersprite", "call", "--tool", TOOL["name"], "--allow-cost")

    def test_apify_cost_approval_is_not_actor_approval(self):
        tool = {"name": "call-actor", "inputSchema": {"type": "object"},
                "annotations": {"readOnlyHint": False, "destructiveHint": True}}
        client = self.tool_client(tool, "apify")
        with self.assertRaises(mcp.MCPError):
            client.call_tool("call-actor", {"actor": "example/public-scraper"})
        client._rpc.assert_not_called()

    def test_approved_actor_is_bound_to_exact_request(self):
        self.assertTrue(mcp.actor_run_approved("call-actor", {"actor": "example/public-scraper"}, "example/public-scraper"))
        with self.assertRaises(mcp.MCPError):
            mcp.actor_run_approved("call-actor", {"actor": "example/email-sender"}, "example/public-scraper")
        self.assertTrue(mcp.actor_run_approved("example--public-scraper", {}, "example/public-scraper"))

    def test_mutating_camel_case_name_blocked(self):
        self.assertIsNotNone(mcp.tool_is_blocked("sif", {"name": "sendMessage"}))

    def test_sse_returns_at_matching_result_without_waiting_for_eof(self):
        class Stream(io.BytesIO):
            def read(self, *args):
                raise AssertionError("Must not wait for the whole stream")

            def readline(self, *args):
                if self.tell() == len(self.getvalue()):
                    raise AssertionError("Must stop after the matching result")
                return super().readline(*args)

        data = b'data: {"jsonrpc":"2.0","method":"notifications/progress"}\n\ndata: {"jsonrpc":"2.0","id":7,"result":{"ok":true}}\n\n'
        client = self.tool_client()
        messages = client._read_response(Stream(data), "text/event-stream", 7)
        self.assertEqual(messages[-1]["result"], {"ok": True})

    def test_http_error_does_not_echo_secret_fragment(self):
        client = self.tool_client()
        client.opener.open = Mock(side_effect=urllib.error.HTTPError(
            "https://example.invalid", 401, "unauthorized", {}, io.BytesIO(b"x" * 490 + b"synthetic-test-token")))
        with self.assertRaises(mcp.MCPError) as caught:
            client._post({"id": 1}, expect_response=True)
        self.assertNotIn("synthetic", str(caught.exception))
        self.assertIn("401", str(caught.exception))

    def test_redirect_does_not_forward_credentials(self):
        handler = mcp.NoRedirects()
        with self.assertRaises(mcp.MCPError):
            handler.redirect_request(urllib.request.Request("https://example.invalid"), None,
                                     307, "redirect", {}, "https://other.invalid")

    def test_results_redact_secrets_and_remain_valid_json(self):
        result = self.root / "result.json"
        with patch.dict(os.environ, {"APIFY_TOKEN": 'fake-secret-"quoted"'}):
            mcp.write_output({"text": 'prefix fake-secret-"quoted" suffix', "success": True}, str(result), False)
        self.assertEqual(json.loads(result.read_text()), {"text": "prefix [REDACTED] suffix", "success": True})

    def test_force_write_keeps_output_private_and_refuses_symlink(self):
        result = self.root / "result.json"
        result.write_text("old")
        result.chmod(0o644)
        mcp.write_output({"ok": True}, str(result), True)
        self.assertEqual(stat.S_IMODE(result.stat().st_mode), 0o600)
        link = self.root / "linked.json"
        link.symlink_to(result)
        with self.assertRaises(mcp.MCPError):
            mcp.write_output({"replaced": True}, str(link), True)
        self.assertEqual(json.loads(result.read_text()), {"ok": True})

    def test_required_task_execution_fails_before_business_call(self):
        client = self.tool_client({**TOOL, "execution": {"taskSupport": "required"}})
        with self.assertRaises(mcp.MCPError):
            client.call_tool(TOOL["name"], VALID)
        client._rpc.assert_not_called()

    def test_valid_call_is_sent_once(self):
        client = self.tool_client()
        result = client.call_tool(TOOL["name"], VALID)
        self.assertIn("content", result)
        client._rpc.assert_called_once_with("tools/call", {"name": TOOL["name"], "arguments": VALID})

    def test_tool_error_preserves_run_id_without_replacing_old_result(self):
        result = self.root / "result.json"
        result.write_text("previous evidence")
        client = self.tool_client()
        response = {"isError": True, "structuredContent": {"runId": "synthetic-run-42"}, "content": []}
        client._rpc.return_value = response
        with patch.object(mcp, "credential_for", return_value="synthetic-test-token"), patch.object(mcp, "MCPClient", return_value=client):
            with self.assertRaisesRegex(mcp.MCPError, "Recovery evidence"):
                self.cli("--provider", "sellersprite", "call", "--tool", TOOL["name"], "--arguments", json.dumps(VALID),
                         "--allow-cost", "--output", str(result), "--force")
        self.assertEqual(result.read_text(), "previous evidence")
        recovery = list(self.root.glob("mcp-recovery-*/response.json"))
        self.assertEqual(len(recovery), 1)
        self.assertEqual(json.loads(recovery[0].read_text())["response"], response)
        client._rpc.assert_called_once()

    def test_write_failure_preserves_new_response_and_old_evidence(self):
        result = self.root / "result.json"
        result.write_text("previous evidence")
        client = self.tool_client()
        response = {"structuredContent": {"runId": "synthetic-run-43"}, "content": []}
        client._rpc.return_value = response
        with patch.object(mcp, "credential_for", return_value="synthetic-test-token"), patch.object(mcp, "MCPClient", return_value=client), patch.object(mcp.os, "replace", side_effect=OSError("Synthetic rename failure")):
            with self.assertRaisesRegex(mcp.MCPError, "Recovery evidence"):
                self.cli("--provider", "sellersprite", "call", "--tool", TOOL["name"], "--arguments", json.dumps(VALID),
                         "--allow-cost", "--output", str(result), "--force")
        self.assertEqual(result.read_text(), "previous evidence")
        recovery = list(self.root.glob("mcp-recovery-*/response.json"))
        self.assertEqual(json.loads(recovery[0].read_text())["response"], response)
        client._rpc.assert_called_once()


if __name__ == "__main__":
    unittest.main()
