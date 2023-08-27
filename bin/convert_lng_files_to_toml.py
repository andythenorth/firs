# FIRS converted lang sources from .lng files to .toml in August 2023
# this script migrates existing lang files where possible to try and preserve translations
import os.path

currentdir = os.curdir

import codecs
import shutil
import sys
import tomlkit

sys.path.append(os.path.join("src"))  # add to the module search path

def parse_lng_file(lng_file):
    lng_lines = lng_file.readlines()
    global_pragma = {}
    for line in lng_lines:
        if "##" in line:
            pragma_split = line.split(" ", 1)
            # slice at 2 to strip the ## chars
            pragma_key = pragma_split[0][2:]
            pragma_value = pragma_split[1].rstrip()
            global_pragma[pragma_key] = pragma_value

    # this is fragile, playing one line python is silly :)
    lang_strings = dict(
        (line.split(":", 1)[0].strip(), line.split(":", 1)[1].strip())
        for line in lng_lines
        if ":" in line
    )
    return {"global_pragma": global_pragma, "lang_strings": lang_strings}


def write_toml(lang_data, lang_name, toml_dst):
    lang_as_toml = tomlkit.document()

    global_pragma_table = tomlkit.table()
    for pragma_key, pragma_value in lang_data["global_pragma"].items():
        global_pragma_table.add(pragma_key, pragma_value)
    lang_as_toml["GLOBAL_PRAGMA"] = global_pragma_table

    for lang_string_name, lang_string in lang_data["lang_strings"].items():
        # this might not handle string-local pragmas for case or gender, Horse didn't have any in translations as of August 2023
        lang_string_table = tomlkit.table()
        lang_string_table.add("base", lang_string)
        lang_as_toml[lang_string_name] = lang_string_table

    with codecs.open(
        os.path.join(toml_dst, lang_name + ".toml"),
        mode="w",
        encoding="utf-8",
    ) as toml_file:
        toml_file.write(tomlkit.dumps(lang_as_toml))


def main():
    print("Converting .lng to .toml...")

    toml_dst = os.path.join("src", "lang", "toml_conversion")
    if os.path.exists(toml_dst):
        shutil.rmtree(toml_dst)
    os.makedirs(toml_dst)

    for file_name in os.listdir(os.path.join("src", "lang")):
        if file_name.endswith('.lng'):
            lng_file = codecs.open(
                os.path.join("src", "lang", file_name),
                "r",
                encoding="utf-8",
            )
            lang_data = parse_lng_file(lng_file)
            lang_name = file_name.split(".")[0]
            print("...", lang_name)
            write_toml(lang_data, lang_name, toml_dst)
    print("Done")


if __name__ == "__main__":
    main()
