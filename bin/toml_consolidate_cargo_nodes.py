#!/usr/bin/env python3

from pathlib import Path
import sys

import tomlkit


# Existing legacy node names which don't match the cargo's canonical suffix.
UNIT_SUFFIX_TO_CARGO = {
    "FMSP": "FARM_SUPPLIES",
    "PETROL": "PETROLEUM_FUELS",
}


def canonical_unit_suffix_to_cargo(suffix: str) -> str:
    return UNIT_SUFFIX_TO_CARGO.get(suffix, suffix)


def find_cargos(doc) -> list[str]:
    """
    Return cargos in first-seen order, considering all three existing
    source-node types.
    """
    cargos = []
    seen = set()

    for key in doc:
        cargo = None

        if key.startswith("STR_CARGO_NAME_"):
            cargo = key.removeprefix("STR_CARGO_NAME_")

        elif key.startswith("STR_CARGO_UNIT_"):
            suffix = key.removeprefix("STR_CARGO_UNIT_")
            cargo = canonical_unit_suffix_to_cargo(suffix)

        elif key.startswith("STR_CID_"):
            cargo = key.removeprefix("STR_CID_")

        if cargo is not None and cargo not in seen:
            cargos.append(cargo)
            seen.add(cargo)

    return cargos


def source_keys_for(cargo: str) -> dict[str, str]:
    unit_suffix = cargo

    for legacy_suffix, canonical_cargo in UNIT_SUFFIX_TO_CARGO.items():
        if canonical_cargo == cargo:
            unit_suffix = legacy_suffix
            break

    return {
        "name": f"STR_CARGO_NAME_{cargo}",
        "cargo_unit": f"STR_CARGO_UNIT_{unit_suffix}",
        "cid": f"STR_CID_{cargo}",
    }


def main(source_str: str, destination_str: str) -> None:
    source_path = Path(source_str)
    destination_path = Path(destination_str)

    with source_path.open("r", encoding="utf-8") as f:
        source = tomlkit.load(f)

    destination = tomlkit.document()

    cargos = find_cargos(source)

    for cargo in cargos:
        dest_key = f"STR_CARGO_{cargo}"
        table = tomlkit.table()

        source_keys = source_keys_for(cargo)

        found_any = False

        for attr, source_key in source_keys.items():
            if source_key in source:
                source_table = source[source_key]

                if "base" in source_table:
                    table.add(attr, source_table["base"])
                    found_any = True
                else:
                    message = f"{source_key}: missing 'base' attribute"
                    print(f"MISSING ATTR: {message}")
                    table.add(
                        tomlkit.comment(
                            f"MISSING: {source_key} has no 'base' attribute"
                        )
                    )
            else:
                message = f"{source_key}"
                print(f"MISSING NODE: {message}")
                table.add(
                    tomlkit.comment(
                        f"MISSING: source node {source_key}"
                    )
                )

        if not found_any:
            # Defensive: shouldn't normally be reachable because the cargo
            # came from at least one recognised source node.
            print(f"MISSING CARGO DATA: {cargo}")
            table.add(
                tomlkit.comment(
                    f"MISSING: no source data found for cargo {cargo}"
                )
            )

        destination.add(dest_key, table)

    with destination_path.open("w", encoding="utf-8") as f:
        tomlkit.dump(destination, f)

    print()
    print(f"Source:      {source_path}")
    print(f"Destination: {destination_path}")
    print(f"Cargos:      {len(cargos)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(
            f"Usage: {sys.argv[0]} source.toml destination.toml"
        )

    main(sys.argv[1], sys.argv[2])
