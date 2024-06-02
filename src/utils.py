import os.path
import codecs  # used for writing files - more unicode friendly than standard open() module
import tomllib

currentdir = os.curdir

import global_constants
from polar_fox import git_info
from polar_fox.utils import echo_message as echo_message
from polar_fox.utils import dos_palette_to_rgb as dos_palette_to_rgb
from polar_fox.utils import unescape_chameleon_output as unescape_chameleon_output
from polar_fox.utils import split_nml_string_lines as split_nml_string_lines
from polar_fox.utils import (
    unwrap_nml_string_declaration as unwrap_nml_string_declaration,
)


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


def get_lang_data(lang):
    global_pragma = {}
    lang_strings = {}
    with open(os.path.join(currentdir, "src", "lang", lang + ".toml"), "rb") as fp:
        lang_source = tomllib.load(fp)

    for node_name, node_value in lang_source.items():
        if node_name == "GLOBAL_PRAGMA":
            # explicit handling of global pragma items
            global_pragma["grflangid"] = node_value["grflangid"]
            global_pragma["plural"] = node_value["plural"]
            if node_value.get("gender", False):
                global_pragma["gender"] = node_value["gender"]
            if node_value.get("case", False):
                global_pragma["case"] = node_value["case"]
        else:
            lang_strings[node_name] = node_value["base"]

    return {"global_pragma": global_pragma, "lang_strings": lang_strings}


class DwordGrfID(object):
    """
    grfids in game and bananas are presented as dwords, so it would be more convenient all round to use the dword
    however nml wants grfids as literals, so this class stores a dword, and converts it to an *nml* literal on demand
    """

    def __init__(self, grfid):
        self.grfid_as_dword = grfid  # keep the grfid around in case it's wanted for docs etc (as yet unknown)
        # split to bytes
        split = [
            self.grfid_as_dword[i : i + 2]
            for i in range(0, len(self.grfid_as_dword), 2)
        ]
        self.grfid = "\\" + "\\".join(
            split
        )  # note the leading '\' that nml requires (escaped as double \\ for python)


class LiteralGrfID(object):
    """
    store a literal grfid directly, which is convenient for nml
    but most grfids are found in the wild as dwords, in which case it's simpler to use the class for dword grfids instead ;)
    """

    def __init__(self, grfid):
        # grfid should be passed using r"literal", to avoid python interpreting \ chars as escapes
        self.grfid = grfid
