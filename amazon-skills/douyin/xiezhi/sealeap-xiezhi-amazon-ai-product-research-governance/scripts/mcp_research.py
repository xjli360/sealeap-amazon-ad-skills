#!/usr/bin/env python3
"""Safe, schema-first client for SIF, SellerSprite, and Apify MCP research.

Credentials are read only from environment variables. The client never accepts
tokens on the command line, never puts them in URLs, and never prints request
headers. Tool names and argument schemas are discovered at runtime.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import os
import re
import stat
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


PROTOCOL_VERSION = "2025-11-25"
SUPPORTED_PROTOCOLS = {
    "2025-11-25",
    "2025-06-18",
    "2025-03-26",
}
MAX_RESPONSE_BYTES = 10 * 1024 * 1024

PROVIDERS = {
    "sif": {
        "endpoint": "https://mcp.sif.com/mcp",
        "env": "SIF_MCP_SECRET_KEY",
        "header": "secret-key",
    },
    "sellersprite": {
        "endpoint": "https://mcp.sellersprite.com/mcp",
        "env": "SELLERSPRITE_MCP_SECRET_KEY",
        "header": "secret-key",
    },
    "apify": {
        "endpoint": "https://mcp.apify.com",
        "env": "APIFY_TOKEN",
        "header": "Authorization",
    },
}

APIFY_ANONYMOUS_TOOLS = {
    "search-actors",
    "fetch-actor-details",
    "search-apify-docs",
    "fetch-apify-docs",
}

SENSITIVE_ARGUMENT_KEYS = {
    "accesskey",
    "accesstoken",
    "apikey",
    "authorization",
    "bearertoken",
    "cookie",
    "credential",
    "credentials",
    "key",
    "mcptoken",
    "password",
    "refreshkey",
    "refreshtoken",
    "secret",
    "secretkey",
    "session",
    "sessionid",
    "token",
}

MUTATION_MARKERS = {
    "add",
    "archive",
    "change",
    "create",
    "delete",
    "del",
    "favorite",
    "insert",
    "publish",
    "remove",
    "save",
    "send",
    "set",
    "submit",
    "unpublish",
    "update",
    "upsert",
    "write",
}

PLACEHOLDER_VALUES = {
    "",
    "changeme",
    "replace-me",
    "replace_me",
    "your-secret",
    "your_secret",
    "your-token",
    "your_token",
}


class MCPError(RuntimeError):
    """Safe user-facing MCP error."""

    def __init__(self, message: str, *, response: Any = None):
        super().__init__(message)
        self.response = response


class NoRedirects(urllib.request.HTTPRedirectHandler):
    """Never forward provider credentials to a redirected endpoint."""

    def redirect_request(self, request, response, code, message, headers, newurl):
        raise MCPError(f"MCP HTTP redirect {code} refused; verify the provider endpoint.")


def redact_text(text: str, extra_secrets: tuple[str, ...] = ()) -> str:
    secrets = {
        os.environ.get(str(spec["env"]), "").strip()
        for spec in PROVIDERS.values()
    } | set(extra_secrets)
    for secret in sorted((value for value in secrets if value), key=len, reverse=True):
        for form in {
            secret, urllib.parse.quote(secret, safe=""), urllib.parse.quote_plus(secret),
            json.dumps(secret)[1:-1],
        }:
            text = text.replace(form, "[REDACTED]")
    return text


def redact_value(value: Any) -> Any:
    if isinstance(value, str):
        return redact_text(value)
    if isinstance(value, list):
        return [redact_value(item) for item in value]
    if isinstance(value, dict):
        return {redact_text(str(key)): redact_value(item) for key, item in value.items()}
    return value


def strict_json_loads(text: str) -> Any:
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise MCPError("JSON contains a duplicate object key.")
            result[key] = value
        return result

    def invalid_constant(value):
        raise MCPError("JSON contains a non-finite number.")

    return json.loads(text, object_pairs_hook=pairs, parse_constant=invalid_constant)


def normalized_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def parse_sse(body: str) -> list[str]:
    events: list[str] = []
    current: list[str] = []
    for line in body.splitlines():
        if line.startswith("data:"):
            current.append(line[5:].lstrip())
        elif not line.strip() and current:
            events.append("\n".join(current))
            current = []
    if current:
        events.append("\n".join(current))
    return events


def parse_messages(content_type: str, body: str) -> list[dict[str, Any]]:
    raw_messages = (
        parse_sse(body)
        if "text/event-stream" in content_type.lower()
        else [body]
    )
    messages: list[dict[str, Any]] = []
    for raw in raw_messages:
        value = raw.strip()
        if not value or value == "[DONE]":
            continue
        try:
            decoded = json.loads(value)
        except json.JSONDecodeError:
            continue
        if isinstance(decoded, dict):
            messages.append(decoded)
        elif isinstance(decoded, list):
            messages.extend(item for item in decoded if isinstance(item, dict))
    return messages


def read_arguments(raw: str | None, path: str | None) -> dict[str, Any]:
    if raw and path:
        raise MCPError("Use only one of --arguments or --arguments-file.")
    if path:
        value = strict_json_loads(Path(path).expanduser().read_text(encoding="utf-8"))
    elif raw:
        value = strict_json_loads(raw)
    else:
        value = {}
    if not isinstance(value, dict):
        raise MCPError("Tool arguments must be a JSON object.")
    reject_sensitive_arguments(value)
    return value


def reject_sensitive_arguments(value: Any, prefix: str = "arguments") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if normalized_key(str(key)) in SENSITIVE_ARGUMENT_KEYS:
                raise MCPError(
                    f"Refusing credential-like field at {prefix}.{key}; "
                    "credentials belong in environment variables only."
                )
            reject_sensitive_arguments(child, f"{prefix}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            reject_sensitive_arguments(child, f"{prefix}[{index}]")
    elif isinstance(value, str):
        if redact_text(value) != value:
            raise MCPError(f"Refusing an environment credential at {prefix}.")
        if re.search(
            r"(?i)(authorization|api[-_]?key|access[-_]?token|"
            r"secret[-_]?key|refresh[-_]?token|password)=",
            value,
        ):
            raise MCPError(
                f"Refusing credential-like value at {prefix}; "
                "remove secrets from tool arguments."
            )


def validate_schema(arguments: dict[str, Any], schema: dict[str, Any]) -> None:
    if not isinstance(schema, dict) or schema.get("type") != "object":
        raise MCPError("Tool inputSchema must describe an object.")
    try:
        from jsonschema import Draft202012Validator, SchemaError
        from jsonschema.validators import validator_for
        from referencing import Registry
        from referencing.exceptions import NoSuchResource
    except ImportError as exc:
        raise MCPError(
            "Schema validation requires jsonschema >= 4.18. Use a Python environment "
            "with jsonschema, or uv run --with 'jsonschema>=4.18,<5' python SCRIPT ..."
        ) from exc

    def reject_remote_ref(uri):
        raise NoSuchResource(ref=uri)

    if "$schema" in schema and not isinstance(schema["$schema"], str):
        raise MCPError("Invalid JSON Schema dialect.")
    validator_class = (
        validator_for(schema, default=None) if "$schema" in schema else Draft202012Validator
    )
    if validator_class is None:
        raise MCPError("Unsupported JSON Schema dialect; review the tool schema.")
    try:
        validator_class.check_schema(schema)
        validator = validator_class(schema, registry=Registry(retrieve=reject_remote_ref))
        error = next(validator.iter_errors(arguments), None)
    except SchemaError as exc:
        raise MCPError("The tool inputSchema is invalid.") from exc
    except Exception as exc:
        raise MCPError("Cannot resolve the schema locally; remote references are disabled.") from exc
    if error is not None:
        location = ".".join(str(part) for part in error.absolute_path) or "arguments"
        raise MCPError(f"inputSchema rejected {location} ({error.validator}).")


def load_schema_file(path: str, tool_name: str) -> dict[str, Any]:
    value = strict_json_loads(Path(path).expanduser().read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise MCPError("Schema file must contain a tool description or JSON Schema object.")
    if "inputSchema" in value:
        if value.get("name") != tool_name:
            raise MCPError("Schema file describes a different tool.")
        value = value["inputSchema"]
    if not isinstance(value, dict) or value.get("type") != "object":
        raise MCPError("Tool inputSchema must describe an object.")
    return value


def actor_run_approved(name: str, arguments: dict[str, Any], approved_actor: str | None) -> bool:
    if not approved_actor:
        return False
    if not re.fullmatch(r"[A-Za-z0-9_-]+/[A-Za-z0-9_-]+", approved_actor):
        raise MCPError("--approved-actor must be the reviewed owner/name identifier.")
    if name == "call-actor":
        if arguments.get("actor") != approved_actor:
            raise MCPError("Actor in the request does not match --approved-actor.")
        return True
    if name not in {approved_actor, approved_actor.replace("/", "-slash-"), approved_actor.replace("/", "--")}:
        raise MCPError("The selected Actor tool does not match --approved-actor.")
    return True


def tool_is_blocked(
    provider: str, tool: dict[str, Any], *, allow_actor_run: bool = False
) -> str | None:
    annotations = tool.get("annotations") or {}
    name = str(tool.get("name") or "")
    # A paid Actor run is not inherently read-only. Cost approval alone does
    # not authorize its effects; the exact Actor and input must be reviewed.
    apify_actor_call = provider == "apify" and (
        name == "call-actor"
        or "/" in name
        or "-slash-" in name
        or "--" in name
    )
    if apify_actor_call and not allow_actor_run:
        return "Actor execution needs --approved-actor owner/name after review of this Actor and input"
    if annotations.get("destructiveHint") is True and not apify_actor_call:
        return "tool declares destructiveHint=true"

    parts = {
        part
        for part in re.split(r"[^a-z0-9]+", re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", name).lower())
        if part
    }
    if parts & MUTATION_MARKERS:
        return "tool name looks mutating"

    if annotations.get("readOnlyHint") is False and not apify_actor_call:
        return "tool declares readOnlyHint=false"
    return None


def summarize_tool(tool: dict[str, Any]) -> dict[str, Any]:
    annotations = tool.get("annotations") or {}
    return {
        "name": tool.get("name"),
        "title": tool.get("title") or annotations.get("title"),
        "description": str(tool.get("description") or "")[:500],
        "readOnlyHint": annotations.get("readOnlyHint"),
        "destructiveHint": annotations.get("destructiveHint"),
    }


def build_apify_endpoint(selected: str | None) -> tuple[str, set[str]]:
    endpoint = str(PROVIDERS["apify"]["endpoint"])
    if not selected:
        return endpoint, set()
    names = {item.strip() for item in selected.split(",") if item.strip()}
    if not names:
        raise MCPError("--apify-tools did not contain a tool name.")
    for name in names:
        if not re.fullmatch(r"[A-Za-z0-9_./-]+", name):
            raise MCPError(f"Invalid Apify tool selector: {name}")
    query = urllib.parse.urlencode({"tools": ",".join(sorted(names))})
    return f"{endpoint}?{query}", names


def credential_for(provider: str, apify_tools: set[str]) -> str:
    spec = PROVIDERS[provider]
    value = os.environ.get(str(spec["env"]), "").strip()
    anonymous = provider == "apify" and apify_tools and apify_tools <= APIFY_ANONYMOUS_TOOLS
    if anonymous and not value:
        return ""
    if normalized_key(value) in {normalized_key(item) for item in PLACEHOLDER_VALUES}:
        raise MCPError(
            f"{spec['env']} is not configured. Inject it through a local "
            "secret manager or environment; never pass it on the command line."
        )
    if value.startswith("<") or value.upper().startswith("YOUR_"):
        raise MCPError(f"{spec['env']} still contains a placeholder.")
    if not re.fullmatch(r"[\x21-\x7e]+", value):
        raise MCPError(f"{spec['env']} must contain a valid token, not a placeholder or whitespace.")
    return value


def check_output(output: str | None, force: bool) -> None:
    if not output:
        return
    destination = Path(output).expanduser()
    if destination.is_symlink():
        raise MCPError("Refusing a symlink output path.")
    if destination.exists():
        if not destination.is_file():
            raise MCPError("Output path is not a regular file.")
        if not force:
            raise MCPError(f"Output exists: {destination}. Use --force to replace it.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Verify write access before spending quota. Never truncate the destination.
    descriptor, probe = tempfile.mkstemp(prefix=".mcp-probe-", dir=destination.parent)
    os.close(descriptor)
    os.unlink(probe)


def write_output(value: Any, output: str | None, force: bool) -> None:
    rendered = json.dumps(redact_value(value), ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if not output:
        sys.stdout.write(rendered)
        return
    destination = Path(output).expanduser()
    check_output(output, force)
    descriptor, temporary = tempfile.mkstemp(prefix=".mcp-result-", dir=destination.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            os.fchmod(handle.fileno(), stat.S_IRUSR | stat.S_IWUSR)
            handle.write(rendered)
        if force:
            os.replace(temporary, destination)
        else:
            os.link(temporary, destination)
    except FileExistsError as exc:
        raise MCPError("Output was created by another process; result was not overwritten.") from exc
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def preserve_result(value: Any, args, state: str) -> str:
    """Keep run IDs and returned evidence after tool or destination failure."""
    parent = Path(args.output).expanduser().parent if args.output else None
    try:
        directory = Path(tempfile.mkdtemp(prefix="mcp-recovery-", dir=parent))
    except OSError:
        directory = Path(tempfile.mkdtemp(prefix="mcp-recovery-"))
    destination = directory / "response.json"
    write_output(
        {"state": state, "provider": args.provider, "tool": args.tool,
         "requested_output": args.output, "response": value, "retried": False},
        str(destination), False,
    )
    return str(destination)


class MCPClient:
    def __init__(
        self,
        provider: str,
        token: str,
        endpoint: str,
        timeout: float,
    ) -> None:
        self.provider = provider
        self.token = token
        self.endpoint = endpoint
        self.timeout = timeout
        self.protocol_version = PROTOCOL_VERSION
        self.session_id: str | None = None
        self.initialized = False
        self.request_id = 0
        self._tools: list[dict[str, Any]] | None = None
        self.opener = urllib.request.build_opener(NoRedirects())

    def _headers(self) -> dict[str, str]:
        spec = PROVIDERS[self.provider]
        headers = {
            "Accept": "application/json, text/event-stream",
            "Content-Type": "application/json",
            "User-Agent": "amazon-skill-mcp-research/1.0",
        }
        if self.token:
            if self.provider == "apify":
                headers[str(spec["header"])] = f"Bearer {self.token}"
            else:
                headers[str(spec["header"])] = self.token
        if self.initialized:
            headers["MCP-Protocol-Version"] = self.protocol_version
        if self.session_id:
            headers["Mcp-Session-Id"] = self.session_id
        return headers

    def _redact(self, text: str) -> str:
        return redact_text(text, (self.token,))

    def _read_response(self, response, content_type: str, request_id) -> list[dict[str, Any]]:
        if "text/event-stream" not in content_type.lower():
            body = response.read(MAX_RESPONSE_BYTES + 1)
            if len(body) > MAX_RESPONSE_BYTES:
                raise MCPError("MCP response exceeded the 10 MiB limit; request a smaller page.")
            return parse_messages(content_type, body.decode("utf-8", errors="replace"))
        # Return as soon as this request's result arrives; some servers keep
        # the SSE connection alive after sending it.
        messages = []
        event = []
        consumed = 0
        deadline = time.monotonic() + self.timeout
        while True:
            if time.monotonic() >= deadline:
                raise MCPError("MCP SSE response timed out before the matching result.")
            raw = response.readline(MAX_RESPONSE_BYTES - consumed + 1)
            consumed += len(raw)
            if consumed > MAX_RESPONSE_BYTES:
                raise MCPError("MCP response exceeded the 10 MiB limit; request a smaller page.")
            if raw and raw.strip():
                event.append(raw.decode("utf-8", errors="replace"))
                continue
            if event:
                messages.extend(parse_messages(content_type, "".join(event)))
                event = []
                if any(item.get("id") == request_id and ("result" in item or "error" in item)
                       for item in messages):
                    return messages
            if not raw:
                return messages

    def _post(
        self,
        payload: dict[str, Any],
        *,
        expect_response: bool,
    ) -> list[dict[str, Any]]:
        request = urllib.request.Request(
            self.endpoint,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers=self._headers(),
            method="POST",
        )
        try:
            with self.opener.open(request, timeout=self.timeout) as response:
                status = int(getattr(response, "status", 200))
                content_type = response.headers.get("Content-Type", "")
                session_id = response.headers.get("Mcp-Session-Id")
                messages = self._read_response(response, content_type, payload.get("id")) if expect_response else []
        except urllib.error.HTTPError as exc:
            # Error pages can echo headers and credentials. Status is enough
            # to classify transport/auth/quota failures without printing them.
            raise MCPError(f"MCP HTTP {exc.code}; response body withheld.") from exc
        except urllib.error.URLError as exc:
            raise MCPError(f"MCP connection failed: {self._redact(str(exc.reason))}") from exc

        if session_id:
            if not re.fullmatch(r"[\x21-\x7e]+", session_id):
                raise MCPError("Server returned an invalid Mcp-Session-Id.")
            self.session_id = session_id
        if status >= 400:
            raise MCPError(f"MCP HTTP {status}")
        if expect_response and not messages:
            raise MCPError("MCP response was not valid JSON or SSE JSON-RPC.")
        return messages

    def _rpc(self, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        self.request_id += 1
        request_id = self.request_id
        messages = self._post(
            {
                "jsonrpc": "2.0",
                "id": request_id,
                "method": method,
                "params": params or {},
            },
            expect_response=True,
        )
        response = next(
            (
                item
                for item in messages
                if item.get("id") == request_id
                and ("result" in item or "error" in item)
            ),
            None,
        )
        if response is None:
            raise MCPError(f"No JSON-RPC response matched request {request_id}.")
        if "error" in response:
            error = response.get("error") or {}
            raise MCPError(
                f"MCP error {error.get('code')}: "
                f"{self._redact(str(error.get('message') or 'unknown error'))}",
                response=response if method == "tools/call" else None,
            )
        result = response.get("result") or {}
        if not isinstance(result, dict):
            raise MCPError("MCP result must be an object.")
        return result

    def connect(self) -> dict[str, Any]:
        if self.initialized:
            return {}
        result = self._rpc(
            "initialize",
            {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {},
                "clientInfo": {
                    "name": "amazon-skill-mcp-research",
                    "version": "1.0",
                },
            },
        )
        negotiated = str(result.get("protocolVersion") or PROTOCOL_VERSION)
        if negotiated not in SUPPORTED_PROTOCOLS:
            raise MCPError(f"Unsupported negotiated MCP version: {negotiated}")
        self.protocol_version = negotiated
        self.initialized = True
        self._post(
            {
                "jsonrpc": "2.0",
                "method": "notifications/initialized",
            },
            expect_response=False,
        )
        return result

    def list_tools(self) -> list[dict[str, Any]]:
        if self._tools is not None:
            return self._tools
        self.connect()
        tools: list[dict[str, Any]] = []
        cursor: str | None = None
        seen_cursors: set[str] = set()
        for _ in range(50):
            params = {"cursor": cursor} if cursor else {}
            result = self._rpc("tools/list", params)
            page = result.get("tools") or []
            if not isinstance(page, list):
                raise MCPError("tools/list returned a non-list tools field.")
            tools.extend(item for item in page if isinstance(item, dict))
            next_cursor = result.get("nextCursor")
            if not next_cursor:
                self._tools = tools
                return tools
            cursor = str(next_cursor)
            if cursor in seen_cursors:
                raise MCPError("tools/list returned a repeated cursor.")
            seen_cursors.add(cursor)
        raise MCPError("tools/list exceeded 50 pages.")

    def find_tool(self, name: str) -> dict[str, Any]:
        matches = [tool for tool in self.list_tools() if tool.get("name") == name]
        if not matches:
            raise MCPError(
                f"Tool not found: {name}. Run list-tools or search-tools first."
            )
        return matches[0]

    def call_tool(
        self,
        name: str,
        arguments: dict[str, Any],
        *,
        allow_actor_run: bool = False,
    ) -> dict[str, Any]:
        reject_sensitive_arguments(arguments)
        tool = self.find_tool(name)
        blocked_reason = tool_is_blocked(self.provider, tool, allow_actor_run=allow_actor_run)
        if blocked_reason:
            raise MCPError(f"Refusing tool {name}: {blocked_reason}.")
        schema = tool.get("inputSchema")
        if not isinstance(schema, dict):
            raise MCPError(f"Tool {name} has an invalid inputSchema.")
        validate_schema(arguments, schema)
        if (tool.get("execution") or {}).get("taskSupport") == "required":
            raise MCPError("Tool requires MCP task execution, which this synchronous client does not support.")
        result = self._rpc(
            "tools/call",
            {"name": name, "arguments": arguments},
        )
        if result.get("isError") is True:
            text_parts = [
                str(item.get("text") or "")
                for item in result.get("content") or []
                if isinstance(item, dict) and item.get("type") == "text"
            ]
            raise MCPError(
                f"Tool {name} returned isError=true: "
                + self._redact(" ".join(text_parts))[:800],
                response=result,
            )
        return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Discover and call read-only SIF, SellerSprite, or Apify MCP tools. "
            "Credentials come from environment variables only."
        )
    )
    parser.add_argument("--provider", required=True, choices=sorted(PROVIDERS))
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument(
        "--apify-tools",
        help=(
            "Comma-separated Apify tool or Actor selectors. "
            "Never put a token in this value."
        ),
    )
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("doctor", help="Show safe configuration status; no network.")

    list_parser = commands.add_parser("list-tools", help="Discover current tools.")
    list_parser.add_argument("--full", action="store_true")
    list_parser.add_argument("--output")
    list_parser.add_argument("--force", action="store_true")

    search_parser = commands.add_parser(
        "search-tools", help="Search discovered names and descriptions."
    )
    search_parser.add_argument("--query", required=True)
    search_parser.add_argument("--output")
    search_parser.add_argument("--force", action="store_true")

    describe_parser = commands.add_parser(
        "describe", help="Print one tool and its live inputSchema."
    )
    describe_parser.add_argument("--tool", required=True)
    describe_parser.add_argument("--output")
    describe_parser.add_argument("--force", action="store_true")

    call_parser = commands.add_parser(
        "call", help="Call a discovered research tool after explicit cost approval."
    )
    call_parser.add_argument("--tool", required=True)
    call_parser.add_argument("--arguments")
    call_parser.add_argument("--arguments-file")
    call_parser.add_argument("--dry-run", action="store_true")
    call_parser.add_argument("--schema-file", help="Saved describe output for offline argument validation.")
    call_parser.add_argument(
        "--approved-actor",
        help="Exact owner/name of the Actor reviewed and authorized for this public-data research request.",
    )
    call_parser.add_argument(
        "--allow-cost",
        action="store_true",
        help="Acknowledge that this tool call may consume points or money.",
    )
    call_parser.add_argument("--output")
    call_parser.add_argument("--force", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if not math.isfinite(args.timeout) or args.timeout <= 0:
        raise MCPError("--timeout must be a positive finite number.")
    spec = PROVIDERS[args.provider]
    if args.provider == "apify":
        endpoint, selected_apify_tools = build_apify_endpoint(args.apify_tools)
    else:
        if args.apify_tools:
            raise MCPError("--apify-tools is valid only with --provider apify.")
        endpoint = str(spec["endpoint"])
        selected_apify_tools = set()

    if args.command == "doctor":
        try:
            configured = bool(credential_for(args.provider, selected_apify_tools))
        except MCPError:
            configured = False
        write_output(
            {
                "provider": args.provider,
                "endpoint": endpoint,
                "credential_env": spec["env"],
                "credential_configured": configured,
                "schema_validator_installed": importlib.util.find_spec("jsonschema") is not None,
                "token_in_url": False,
                "network_called": False,
                "apify_anonymous_mode": (
                    args.provider == "apify"
                    and bool(selected_apify_tools)
                    and selected_apify_tools <= APIFY_ANONYMOUS_TOOLS
                ),
            },
            None,
            False,
        )
        return 0

    check_output(getattr(args, "output", None), getattr(args, "force", False))
    if args.command == "call":
        arguments = read_arguments(args.arguments, args.arguments_file)
        if args.approved_actor and args.provider != "apify":
            raise MCPError("--approved-actor is valid only with --provider apify.")
        actor_approved = actor_run_approved(args.tool, arguments, args.approved_actor)
        if args.schema_file:
            validate_schema(arguments, load_schema_file(args.schema_file, args.tool))
        if args.dry_run:
            write_output(
                {
                    "provider": args.provider,
                    "endpoint": endpoint,
                    "tool": args.tool,
                    "arguments": arguments,
                    "credential_env": spec["env"],
                    "network_called": False,
                    "schema_checked": bool(args.schema_file),
                    "live_schema_checked": False,
                    "approved_actor": args.approved_actor,
                    "cost_limit_enforced_by_client": False,
                    "next": (
                        "Save describe output and use --schema-file for offline validation; review "
                        "the exact tool and arguments, obtain "
                        "approval for any quota or cost, then rerun with --allow-cost."
                    ),
                },
                args.output,
                args.force,
            )
            return 0
        if not args.allow_cost:
            raise MCPError(
                "tools/call may consume quota or money. Review provider, tool, "
                "arguments, and expected cost, then add --allow-cost."
            )
        if not args.output:
            raise MCPError("Use --output with a private result file for tools/call; stdout is for discovery and plans.")

    token = credential_for(args.provider, selected_apify_tools)
    client = MCPClient(args.provider, token, endpoint, args.timeout)

    if args.command == "list-tools":
        tools = client.list_tools()
        value: Any = tools if args.full else [summarize_tool(tool) for tool in tools]
    elif args.command == "search-tools":
        terms = [item for item in args.query.casefold().split() if item]
        value = [
            summarize_tool(tool)
            for tool in client.list_tools()
            if all(
                term
                in (
                    str(tool.get("name") or "")
                    + " "
                    + str(tool.get("title") or "")
                    + " "
                    + str(tool.get("description") or "")
                ).casefold()
                for term in terms
            )
        ]
    elif args.command == "describe":
        value = client.find_tool(args.tool)
    elif args.command == "call":
        try:
            value = client.call_tool(args.tool, arguments, allow_actor_run=actor_approved)
        except (MCPError, OSError) as exc:
            recovery = ""
            if getattr(exc, "response", None) is not None:
                try:
                    recovery = " Recovery evidence: " + preserve_result(exc.response, args, "tool_error")
                except (MCPError, OSError, ValueError):
                    recovery = " Recovery evidence could not be written."
            raise MCPError(
                f"{exc} No automatic retry was made. If tools/call reached the server, "
                "check its run or request status before retrying." + recovery
            ) from exc
    else:
        raise MCPError(f"Unsupported command: {args.command}")

    try:
        write_output(value, getattr(args, "output", None), getattr(args, "force", False))
    except (MCPError, OSError, ValueError) as exc:
        if args.command != "call":
            raise
        try:
            recovery = "Recovery evidence: " + preserve_result(value, args, "output_failed_after_call")
        except (MCPError, OSError, ValueError):
            recovery = "Recovery evidence could not be written."
        raise MCPError(
            f"The tool returned, but the output could not be saved. {recovery} "
            "No retry was made; inspect the existing run before calling again."
        ) from exc
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (MCPError, ValueError, OSError) as exc:
        print(redact_text(f"error: {exc}"), file=sys.stderr)
        raise SystemExit(2)
