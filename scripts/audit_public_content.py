#!/usr/bin/env python3
"""Audit publishable files without echoing identities, credentials or source text.

Optional --terms-file points to a private JSON list kept outside the repository.
Use --revision to inspect a Git tree, or --history to inspect every reachable tree.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess


FORBIDDEN_PARTS = {".source-materials", "transcripts", "__pycache__"}
REVIEWED_BRAND_IMAGES = {
    "assets/amazon-ads-logo.png": {"37f3a8519003acec9e166ff23dc28cc9f12db0c69c9772ba920d22a2fc248107"},
    "assets/sealeap-logo.png": {
        "1b27c85750119f6ebe9f67023106085d137e5a7ba0569b65315ed324cc7caa2d",
        "54698775cfce6360c78164478cf9d271e79c5b4d9d8468dfaf69fdecfbd02a50",
    },
    "assets/amazon-advertising-logo-dark.png": {"b8f06d397934f8af3f428cb1dea8901471ec8caac854f6a2b7d7c87187fb172d"},
    "assets/amazon-advertising-logo-light.png": {"2f06b788c5a963593dbcf9aa78695352e2e08217f6be97e7b8f806f0dc6fdf5f"},
}
PATTERNS = {
    "personal_attribution": re.compile(
        r"^\s*(?:[-*>]\s*)?(?:讲师|作者|主讲人|博主|昵称|抖音号|微信号|小红书号)(?:标注)?\s*[:：]\s*\S", re.M
    ),
    "social_source_url": re.compile(
        r"https?://(?:[^\s/]+\.)?(?:douyin\.com|iesdouyin\.com|xiaohongshu\.com|xhslink\.com|mp\.weixin\.qq\.com)(?:[/:?\s]|$)", re.I
    ),
    "source_identity_field": re.compile(
        r"[\"'](?:nickname|author_name|screen_name|sec_uid|aweme_id|note_url)[\"']\s*:\s*[\"']\S", re.I
    ),
    "credential": re.compile(
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bgh[pousr]_[A-Za-z0-9]{30,}|\bAKIA[A-Z0-9]{16}\b|\bsk-[A-Za-z0-9_-]{24,}"
    ),
    "private_local_path": re.compile(r"/(?:Users|home)/[^\s/]+/"),
}


def identity_pattern(term):
    escaped = re.escape(term)
    return re.compile(r"(?<![A-Za-z0-9_])" + escaped + r"(?![A-Za-z0-9_])" if term.isascii() else escaped)


def inspect_file(path, data, terms=()):
    findings = []
    parts = Path(path).parts
    if FORBIDDEN_PARTS.intersection(parts) or Path(path).name.startswith(".env"):
        findings.append("private_or_raw_material")
    try:
        text = data.decode("utf-8")
    except UnicodeError:
        # New or modified images require inspection, including their metadata.
        if hashlib.sha256(data).hexdigest() not in REVIEWED_BRAND_IMAGES.get(path, set()):
            findings.append("unreviewed_binary")
        return findings
    # Match escaped identifiers in JSON/quoted metadata as well as plain text.
    decoded = re.sub(r"\\u([0-9a-fA-F]{4})", lambda match: chr(int(match.group(1), 16)), text)
    decoded = decoded.replace(r"\/", "/")
    for label, pattern in PATTERNS.items():
        if pattern.search(decoded):
            findings.append(label)
    if any(identity_pattern(term).search(decoded) or identity_pattern(term).search(path) for term in terms):
        findings.append("known_identity")
    return findings


def files_in_worktree(root):
    for directory, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(name for name in dirs if name != ".git")
        for name in sorted(dirs + files):
            path = Path(directory) / name
            if path.is_symlink():
                yield str(path.relative_to(root)), None
        dirs[:] = [name for name in dirs if not (Path(directory) / name).is_symlink()]
        for name in sorted(files):
            path = Path(directory) / name
            if not path.is_symlink():
                yield str(path.relative_to(root)), path.read_bytes()


def files_in_revision(root, revision):
    rows = subprocess.check_output(["git", "ls-tree", "-rz", revision], cwd=root).split(b"\0")
    for row in rows:
        if not row:
            continue
        metadata, raw_path = row.split(b"\t", 1)
        mode, kind, oid = metadata.split()
        path = raw_path.decode("utf-8")
        if mode == b"120000" or kind != b"blob":
            yield path, None
        else:
            yield path, subprocess.check_output(["git", "cat-file", "blob", oid.decode()], cwd=root)


def audit(root, terms=(), revision=None, history=None):
    errors = []
    files = 0
    revisions = subprocess.check_output(["git", "rev-list", history], cwd=root, text=True).splitlines() if history else [revision]
    for rev in revisions:
        entries = files_in_revision(root, rev) if rev else files_in_worktree(root)
        for path, data in entries:
            files += 1
            labels = ["symlink_or_submodule"] if data is None else inspect_file(path, data, terms)
            if labels:
                safe_path = path
                for term in terms:
                    safe_path = identity_pattern(term).sub("[redacted]", safe_path)
                error = {"path": safe_path, "categories": labels}
                if rev:
                    error["revision"] = rev
                errors.append(error)
    return {
        "ok": not errors,
        "files_scanned": files,
        "revisions_scanned": len(revisions) if revision or history else 0,
        "private_identity_list_used": bool(terms),
        "scope": "reachable_history" if history else "git_tree" if revision else "working_tree",
        "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--terms-file", type=Path)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--revision")
    group.add_argument("--history")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    terms = json.loads(args.terms_file.read_text()) if args.terms_file else []
    if not isinstance(terms, list) or any(not isinstance(term, str) or len(term) < 2 for term in terms):
        parser.error("private terms must be a JSON list of strings of at least two characters")
    result = audit(args.root.resolve(), terms, args.revision, args.history)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
