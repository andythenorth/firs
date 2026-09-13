#!/usr/bin/env python3

from pathlib import Path
import re
import sys


REPLACEMENTS = (
    (
        re.compile(r"\bSTR_CARGO_NAME_([A-Z0-9_]+)\b"),
        lambda m: f"STR_CARGO_{m.group(1)}_NAME",
    ),
    (
        re.compile(r"\bSTR_CARGO_UNIT_([A-Z0-9_]+)\b"),
        lambda m: f"STR_CARGO_{m.group(1)}_CARGO_UNIT",
    ),
    (
        re.compile(r"\bSTR_CID_([A-Z0-9_]+)\b"),
        lambda m: f"STR_CARGO_{m.group(1)}_CID",
    ),
)


# Legacy unit token suffixes which were normalised by the TOML migration.
LEGACY_REPLACEMENTS = {
    "STR_CARGO_FMSP_CARGO_UNIT": "STR_CARGO_FARM_SUPPLIES_CARGO_UNIT",
    "STR_CARGO_PETROL_CARGO_UNIT": "STR_CARGO_PETROLEUM_FUELS_CARGO_UNIT",
}


def migrate_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    migrated = original

    for pattern, replacement in REPLACEMENTS:
        migrated = pattern.sub(replacement, migrated)

    for old, new in LEGACY_REPLACEMENTS.items():
        migrated = migrated.replace(old, new)

    if migrated == original:
        return False

    path.write_text(migrated, encoding="utf-8")
    print(path)
    return True


def main(directory: str) -> None:
    root = Path(directory)

    changed = 0

    for path in sorted(root.glob("*.py")):
        if migrate_file(path):
            changed += 1

    print(f"{changed} files changed")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(
            f"Usage: {sys.argv[0]} path/to/cargo/definitions"
        )

    main(sys.argv[1])
