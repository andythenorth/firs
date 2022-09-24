from PIL import Image
import os.path
import codecs  # used for writing files - more unicode friendly than standard open() module
import global_constants
from polar_fox import git_info
from polar_fox.utils import echo_message as echo_message
from polar_fox.utils import dos_palette_to_rgb as dos_palette_to_rgb
from polar_fox.utils import unescape_chameleon_output as unescape_chameleon_output
from polar_fox.utils import split_nml_string_lines as split_nml_string_lines
from polar_fox.utils import unwrap_nml_string_declaration as unwrap_nml_string_declaration


def get_makefile_args(sys):
    # get args passed by makefile
    if len(sys.argv) > 1:
        makefile_args = {
            "test_industry": sys.argv[1],
            "no_mp": sys.argv[2],
        }
    else:
        # provide any necessary defaults here
        makefile_args = {}
    return makefile_args


def get_docs_url():
    # not convinced this belongs in utils, but I can't find anywhere better to put it
    # could be in polar fox - method will be common to all grfs? - pass the project name as a var?
    # not convinced it's big enough to bother centralising TBH, too much close coupling has costs
    result = [global_constants.metadata["docs_url"]]
    if git_info.get_tag_exact_match() != "undefined":
        result.append(git_info.get_tag_exact_match())
    result.append("index.html")
    return "/".join(result)


def parse_base_lang():
    # pick out strings for docs, both from lang file, and extra strings that can't be in the lang file
    base_lang_file = codecs.open(
        os.path.join("src", "lang", "english.lng"), "r", "utf8"
    )
    strings = split_nml_string_lines(base_lang_file.readlines())

    extra_strings_file = codecs.open(
        os.path.join("src", "docs_templates", "extra_strings.lng"), "r", "utf8"
    )
    extra_strings = split_nml_string_lines(extra_strings_file.readlines())
    for i in extra_strings:
        strings[i] = extra_strings[i]

    return strings
