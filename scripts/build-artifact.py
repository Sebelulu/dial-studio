#!/usr/bin/env python3
"""Build the claude.ai artifact copy of Dial Studio from index.html.

The artifact runs inside claude.ai, where the PWA pieces (manifest, icons,
service worker) don't apply, so they are stripped. Everything else is identical.

Usage: python3 scripts/build-artifact.py OUTPUT.html
"""
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text(encoding="utf-8")

# PWA-only head tags
pwa_head = re.compile(
    r'^<(?:meta name="theme-color"|link rel="manifest"|link rel="icon"|link rel="apple-touch-icon"'
    r'|meta name="apple-mobile-web-app-[a-z-]+")[^>]*>\n',
    re.M,
)
out, n_head = pwa_head.subn("", src)

# service worker registration block
sw = re.compile(r"<script>\nif \('serviceWorker' in navigator[\s\S]*?</script>\n")
out, n_sw = sw.subn("", out)

if n_head == 0 or n_sw != 1:
    sys.exit(f"build-artifact: expected PWA tags and one service worker block, found {n_head} tags and {n_sw} blocks")

dest = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "dial-studio-artifact.html")
dest.write_text(out, encoding="utf-8")
print(f"wrote {dest} ({len(out):,} bytes; removed {n_head} PWA tags and the service worker)")
