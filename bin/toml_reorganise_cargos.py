#!/usr/bin/env python3

from pathlib import Path
import sys

import tomlkit
from tomlkit.items import Comment, Whitespace


UNIT_ALIASES = {
    "FARM_SUPPLIES": "FMSP",
    "PETROLEUM_FUELS": "PETROL",
}


def report_unexpected(doc) -> None:
    for item in doc.body:
        if isinstance(item, Comment):
            print(f"COMMENT: {item.as_string().rstrip()}")

        elif isinstance(item, Whitespace):
            continue

        else:
            key, value = item

            if key is None:
                print(f"UNEXPECTED: {item!r}")
                continue

            key = str(key)

            if not (
                key.startswith("STR_CARGO_NAME_")
                or key.startswith("STR_CARGO_UNIT_")
                or key.startswith("STR_CID_")
            ):
                print(f"UNEXPECTED NODE: {key}")

            trivia = getattr(value, "trivia", None)
            if trivia and trivia.comment:
                print(f"COMMENT on {key}: {trivia.comment}")


def main(path_str: str) -> None:
    path = Path(path_str)

    with path.open("r", encoding="utf-8") as f:
        doc = tomlkit.load(f)

    report_unexpected(doc)

    cargo_names = [
        key.removeprefix("STR_CARGO_NAME_")
        for key in doc
        if key.startswith("STR_CARGO_NAME_")
    ]

    reordered = tomlkit.document()
    moved = set()

    for cargo in cargo_names:
        unit_suffix = UNIT_ALIASES.get(cargo, cargo)

        for key in (
            f"STR_CARGO_NAME_{cargo}",
            f"STR_CARGO_UNIT_{unit_suffix}",
            f"STR_CID_{cargo}",
        ):
            if key in doc:
                reordered.add(key, doc[key])
                moved.add(key)
            else:
                print(f"MISSING: {key}")

    for key in doc:
        if key not in moved:
            print(f"UNMATCHED: {key}")
            reordered.add(key, doc[key])

    backup = path.with_suffix(path.suffix + ".bak")
    backup.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")

    with path.open("w", encoding="utf-8") as f:
        tomlkit.dump(reordered, f)

    print(f"Reordered {path}")
    print(f"Backup: {backup}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"Usage: {sys.argv[0]} cargos.toml")

    main(sys.argv[1])
