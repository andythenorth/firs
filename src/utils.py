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


def gs_list_repr(_list):
    # chameleon will render lists as ['foo', 'cabbage', '3']; squirrel wants them as ["foo", "cabbage", 3]
    result = []
    for item in _list:
        if isinstance(item, list):
            # this attempts to handle recursive items
            result.append(gs_list_repr(item))
        elif isinstance(item, (int, float)):
            result.append(str(item))
        elif isinstance(item, str):
            # strings need double quotes, whereas python repr will single quote them
            result.append('"' + item + '"')
        else:
            # extend if more types are needed
            raise Exception("gs_list_repr. Don't know what to do with " + str(item))
    return "[" + ",".join(result) + "]"


def gs_table_repr(_dict):
    # chameleon will render dicts as {'foo': 'cabbage', 'ham': 'eggs'}; squirrel wants them as tables in the form {"foo" = "cabbage", "ham" = "eggs"}
    result = []
    for key, value in _dict.items():
        kv_result = key + " = "
        if value == None:
            kv_result = kv_result + "null"
        elif isinstance(value, list):
            # this attempts to handle recursive items
            kv_result = kv_result + gs_list_repr(value)
        elif isinstance(value, dict):
            # this attempts to handle recursive items
            kv_result = kv_result + gs_table_repr(value)
        elif isinstance(value, bool):
            # python uses 'True' and 'False', squirrel uses 'true' and 'false'
            # note that bool must be checked before int/float, as True and False are also instances of int/float
            kv_result = kv_result + str(value).lower()
        elif isinstance(value, (int, float)):
            kv_result = kv_result + str(value)
        elif isinstance(value, str):
            # strings need double quotes, whereas python repr will single quote them
            kv_result = kv_result + '"' + value + '"'
        else:
            # extend if more types are needed
            raise Exception("gs_table_repr. Don't know what to do with " + str(value))
        result.append(kv_result)

    return "{" + ",".join(result) + "}"
