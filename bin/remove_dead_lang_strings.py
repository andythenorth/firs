import os
# note that we use tomlkit here, not standard library tomllib, as we need write, and tomllib is read-only
import tomlkit

# List of strings to be removed from the TOML files
dead_strings = [
    "STR_IND_PLAZA",
    "STR_IND_CIVIL_EXPLOSIVES_FACILITY",
    "STR_IND_BIOREFINERY",
    "STR_IND_FISHING_VILLAGE",
    "STR_IND_FOOD_MARKET",
    "STR_IND_MIXEDFARM",
    "STR_IND_SALT_MINE",
]

def delete_string(dead_strings, file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lang_source = tomlkit.load(file)

    matched = []
    for string_id in lang_source:
        # note that we also check for translated nodes with '.' extensions of node name
        if string_id in dead_strings or string_id.split(".")[0] in dead_strings:
            print(f"Removing {string_id} from {file_path}")
            matched.append(string_id)
            continue

    for string_id in matched:
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
