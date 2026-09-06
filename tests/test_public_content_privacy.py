import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("privacy_audit", ROOT / "scripts/audit_public_content.py")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class PublicContentPrivacyTests(unittest.TestCase):
    def test_anonymous_workflow_and_official_documentation_are_allowed(self):
        text = "先核对账户证据。参考 https://advertising.amazon.com/resources 。"
        self.assertEqual(AUDIT.inspect_file("references/guide.md", text.encode()), [])

    def test_creator_attribution_is_rejected(self):
        text = "作者" + "：" + "合成测试讲者"
        self.assertIn("personal_attribution", AUDIT.inspect_file("SKILL.md", text.encode()))

    def test_social_source_url_is_rejected(self):
        url = "https://www." + "douyin.com" + "/user/synthetic-fixture"
        self.assertIn("social_source_url", AUDIT.inspect_file("guide.md", url.encode()))

    def test_raw_transcripts_are_rejected_even_without_identity_terms(self):
        self.assertIn("private_or_raw_material", AUDIT.inspect_file("transcripts/sample.txt", b"generic content"))

    def test_replacing_a_reviewed_logo_requires_new_review(self):
        self.assertIn("unreviewed_binary", AUDIT.inspect_file("assets/sealeap-logo.png", b"\x89PNG\xffnew content"))

    def test_escaped_identity_and_filename_are_checked(self):
        label = "合成测试讲者"
        escaped = "".join("\\u%04x" % ord(char) for char in label).encode()
        self.assertIn("known_identity", AUDIT.inspect_file("guide.json", escaped, [label]))
        self.assertIn("known_identity", AUDIT.inspect_file(label + ".md", b"generic content", [label]))

    def test_report_does_not_echo_identity(self):
        label = "合成测试讲者"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / (label + ".md")).write_text(label)
            result = AUDIT.audit(root, [label])
        self.assertFalse(result["ok"])
        self.assertNotIn(label, str(result))

    def test_symlink_is_rejected_without_reading_its_target(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "outside.md").symlink_to(root.parent / "nonexistent-private-material")
            result = AUDIT.audit(root)
        self.assertEqual(result["errors"][0]["categories"], ["symlink_or_submodule"])


if __name__ == "__main__":
    unittest.main()
