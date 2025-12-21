#!/usr/bin/env python3
"""
Fix Photoshop-exported PNGs that trigger:
  libpng warning: iCCP: known incorrect sRGB profile

by removing the iCCP chunk in-place (no pixel re-encoding).

Usage:
  python strip_iccp_pngs.py /path/to/dir
  python strip_iccp_pngs.py /path/to/dir --recursive
  python strip_iccp_pngs.py /path/to/dir --backup
  python strip_iccp_pngs.py /path/to/dir --dry-run
"""

from __future__ import annotations

import argparse
import os
import struct
import tempfile
from pathlib import Path
from typing import Iterable

PNG_SIG = b"\x89PNG\r\n\x1a\n"


def iter_png_paths(root: Path, recursive: bool) -> Iterable[Path]:
    if recursive:
        yield from (p for p in root.rglob("*.png") if p.is_file())
    else:
        yield from (p for p in root.glob("*.png") if p.is_file())


def strip_iccp_chunk(png_bytes: bytes) -> tuple[bytes, bool]:
    """
    Return (new_png_bytes, changed).
    Removes iCCP chunks only; other chunks are preserved verbatim.
    """
    if len(png_bytes) < 8 or png_bytes[:8] != PNG_SIG:
        raise ValueError("Not a PNG (bad signature)")

    out = bytearray()
    out += PNG_SIG

    i = 8
    changed = False

    # PNG chunk format: length(4) type(4) data(length) crc(4)
    while i + 12 <= len(png_bytes):
        length = struct.unpack(">I", png_bytes[i : i + 4])[0]
        ctype = png_bytes[i + 4 : i + 8]
        chunk_total = 12 + length

        if i + chunk_total > len(png_bytes):
            raise ValueError("Corrupt PNG (chunk overruns file)")

        chunk = png_bytes[i : i + chunk_total]

        if ctype == b"iCCP":
            changed = True
            # skip it
        else:
            out += chunk

        i += chunk_total

        if ctype == b"IEND":
            break

    if not out.endswith(b"IEND\xaeB`\x82") and b"IEND" not in out[-64:]:
        # Not super strict, but helps catch weird truncations.
        pass

    return bytes(out), changed


def process_file(path: Path, backup: bool, dry_run: bool) -> bool:
    data = path.read_bytes()
    new_data, changed = strip_iccp_chunk(data)

    if not changed:
        return False

    if dry_run:
        return True

    if backup:
        bak = path.with_suffix(path.suffix + ".bak")
        if not bak.exists():
            bak.write_bytes(data)

    # Atomic-ish replace: write temp in same directory then replace
    tmp_fd, tmp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(tmp_fd, "wb") as f:
            f.write(new_data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_name, path)
    finally:
        try:
            if os.path.exists(tmp_name):
                os.remove(tmp_name)
        except OSError:
            pass

    return True


def main() -> int:
    ap = argparse.ArgumentParser(description="Strip iCCP chunks from PNGs in a directory (fix libpng iCCP warnings).")
    ap.add_argument("directory", type=Path, help="Target directory containing PNG files")
    ap.add_argument("--recursive", action="store_true", help="Recurse into subdirectories")
    ap.add_argument("--backup", action="store_true", help="Write a .bak backup alongside modified files (once)")
    ap.add_argument("--dry-run", action="store_true", help="Show what would change without writing files")
    args = ap.parse_args()

    root: Path = args.directory
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")

    changed_count = 0
    scanned = 0
    errors = 0

    for p in iter_png_paths(root, args.recursive):
        scanned += 1
        try:
            changed = process_file(p, backup=args.backup, dry_run=args.dry_run)
            if changed:
                changed_count += 1
                print(f"FIXED: {p}")
        except Exception as e:
            errors += 1
            print(f"ERROR: {p} -> {e}")

    print(f"\nScanned: {scanned}, Modified: {changed_count}, Errors: {errors}")
    return 0 if errors == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
