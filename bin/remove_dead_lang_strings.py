import os
# note that we use tomlkit here, not standard library tomllib, as we need write, and tomllib is read-only
import tomlkit

# List of strings to be removed from the TOML files
dead_strings = [
    "STR_CARGO_NAME_FERROCHROME",
    "STR_CARGO_NAME_METAL",
    "STR_CARGO_NAME_PACKAGING",
    "STR_CARGO_NAME_STEEL_SECTIONS",
    "STR_CARGO_UNIT_FERROCHROME",
    "STR_CARGO_UNIT_METAL",
    "STR_CARGO_UNIT_PACKAGING",
    "STR_CARGO_UNIT_STEEL_SECTIONS",
    "STR_CID_FERROCHROME",
    "STR_CID_METAL",
    "STR_CID_PACKAGING",
    "STR_CID_STEEL_SECTIONS",
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
