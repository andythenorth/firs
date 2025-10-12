import os
# note that we use tomlkit here, not standard library tomllib, as we need write, and tomllib is read-only
import tomlkit

# List of strings to be removed from the TOML files
dead_strings = [
    "STR_CARGO_NAME_AMMONIUM_NITRATE",
    "STR_CARGO_NAME_BAUXITE",
    "STR_CARGO_NAME_ETHYLENE",
    "STR_CARGO_NAME_FIBRES",
    "STR_CARGO_NAME_FORMIC_ACID",
    "STR_CARGO_NAME_FURNITURE",
    "STR_CARGO_NAME_METHANE",
    "STR_CARGO_NAME_PROPYLENE",
    "STR_CARGO_NAME_SUGAR_BEET",
    "STR_CARGO_NAME_RECYCLABLES",
    "STR_CARGO_NAME_UREA",
    "STR_CARGO_UNIT_AMMONIUM_NITRATE",
    "STR_CARGO_UNIT_ETHYLENE",
    "STR_CARGO_UNIT_BAUXITE",
    "STR_CARGO_UNIT_FIBRES",
    "STR_CARGO_UNIT_FORMIC_ACID",
    "STR_CARGO_UNIT_FURNITURE",
    "STR_CARGO_UNIT_METHANE",
    "STR_CARGO_UNIT_PROPYLENE",
    "STR_CARGO_UNIT_SUGAR_BEET",
    "STR_CARGO_UNIT_RECYCLABLES",
    "STR_CID_AMMONIUM_NITRATE",
    "STR_CID_BAUXITE",
    "STR_CID_FIBRES",
    "STR_CID_FORMIC_ACID",
    "STR_CID_SUGAR_BEET",
    "STR_CID_RECYCLABLES",
]

def delete_string(dead_strings, file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lang_source = tomlkit.load(file)

    for string_id in dead_strings:
        if string_id in lang_source:
            print(f"Removing {string_id} from {file_path}")
            del lang_source[string_id]

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(tomlkit.dumps(lang_source))

    print("removed", dead_strings)

def main():
    lang_dir = os.path.join('src', 'grf', 'lang')
    for filename in os.listdir(lang_dir):
        if filename.endswith(".toml"):
            file_path = os.path.join(lang_dir, filename)
            delete_string(dead_strings, file_path)

if __name__ == "__main__":
    main()
