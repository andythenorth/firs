import firs
import utils
from polar_fox import git_info

import codecs
import os
import shutil
import sys

from time import time

currentdir = os.curdir
sys.path.append(os.path.join("src"))  # add to the module search path

from chameleon import PageTemplateLoader  # chameleon used in most template cases

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)


def render_lang(target, lang_name, lang_dst, dst_file_extension):
    templates = PageTemplateLoader(os.path.join(currentdir, "src", target, "templates"))
    lang_data = utils.get_lang_data(target, lang_name)
    lang_template = templates["lang_file.py" + dst_file_extension[1:]]
    # flatten the strings for rendering
    lang_strings_formatted_as_lng_lines = []
    longest_string_length = max([len(key)] for key in lang_data["lang_strings"].keys())[
        0
    ]
    for string_name, string_value in lang_data["lang_strings"].items():
        # note that stupid pretty formatting of generated output is just to ease debugging string generation when needed, otherwise not essential
        separator = ":".rjust(longest_string_length - len(string_name) + 7)
        lang_strings_formatted_as_lng_lines.append(
            string_name + separator + string_value
        )

    lang_content = utils.unescape_chameleon_output(
        lang_template(
            git_info=git_info,
            utils=utils,
            lang_data=lang_data,
            lang_strings_formatted_as_lng_lines=lang_strings_formatted_as_lng_lines,
        )
    )
    # we clean up some templating artefacts just to produce more readable output for debugging when needed, otherwise not essential
    lines = lang_content.split("\n")
    stripped_lines = [line.lstrip() for line in lines]
    cleaned_lang_content = "\n".join(stripped_lines)
    # write the output eh
    dst_file = codecs.open(
        os.path.join(lang_dst, lang_name + dst_file_extension), "w", "utf8"
    )
    dst_file.write(cleaned_lang_content)
    dst_file.close()


def main():
    start = time()
    print("[RENDER LANG]")

    firs.main()

    if "target" in makefile_args:
        targets = [makefile_args["target"]]
    else:
        targets = ["grf", "gs"]

    target_config = {
        "grf": [".lng", os.path.join(firs.generated_files_path, "lang")],
        "gs": [".txt", os.path.join(firs.generated_files_path, "gs", "lang")],
    }

    # render both grf and gs lang files here
    for target in targets:
        dst_file_extension = target_config[target][0]
        lang_dst = target_config[target][1]

        if os.path.exists(lang_dst):
            shutil.rmtree(lang_dst)
        os.makedirs(lang_dst)

        # we'll try and read any toml file in the lang dir, this requires that no other toml files are present there
        # possibly the installed languages should be handled by the roster when it parses the toml, not sure eh? (potato / potato?)
        for file_name in os.listdir(os.path.join("src", target, "lang")):
            if file_name.endswith(".toml"):
                lang_name = file_name.split(".")[0]
                render_lang(target, lang_name, lang_dst, dst_file_extension)

    print(
        "[RENDER LANG]",
        "- complete",
        format((time() - start), ".2f") + "s",
    )


if __name__ == "__main__":
    main()
