print("[RENDER NML] render nml")

import codecs  # used for writing files - more unicode friendly than standard open() module

import sys
import os

currentdir = os.curdir
from time import time

import firs
import utils
import global_constants
from polar_fox import git_info
from incompatible_grfs import incompatible_grfs
from perm_storage_mappings import perm_storage_mappings, get_perm_num

registered_cargos = firs.registered_cargos
registered_industries = firs.registered_industries
registered_economies = firs.registered_economies
incompatible_industries = firs.incompatible_industries

from chameleon import PageTemplateLoader  # chameleon used in most template cases

# setup the places we look for templates
templates = PageTemplateLoader(
    os.path.join(currentdir, "src", "templates"), format="text"
)

generated_nml_path = os.path.join(firs.generated_files_path, "nml")
if not os.path.exists(generated_nml_path):
    os.mkdir(generated_nml_path)

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)


def render_header_item_nml(header_item):
    template = templates[header_item + ".pynml"]
    result = utils.unescape_chameleon_output(
        template(
            registered_industries=registered_industries,
            registered_cargos=registered_cargos,
            economies=registered_economies,
            perm_storage_mappings=perm_storage_mappings,
            get_perm_num=get_perm_num,
            incompatible_grfs=incompatible_grfs,
            global_constants=global_constants,
            graphics_temp_storage=global_constants.graphics_temp_storage,  # convenience measure
            makefile_args=makefile_args,
            utils=utils,
            sys=sys,
            git_info=git_info,
        )
    )
    # write the nml per vehicle to disk, it aids debugging
    # ! clunky split to get rid of the extension - temporary artefact of migrating away from CPP
    header_item_name = header_item.split(".")[0]
    nml_file = os.path.join(generated_nml_path, header_item_name + ".nml")
    nml = codecs.open(nml_file, "w", "utf8")
    nml.write(result)
    nml.close()
    # also return the nml directly for writing to the concatenated nml, don't faff around opening the generated nml files from disk
    return result


def render_industry_nml(industry):
    only_build_test_industry = makefile_args.get("test_industry", None)
    if not only_build_test_industry or only_build_test_industry == industry.id:
        result = industry.render_nml(
            incompatible_industries=incompatible_industries,
        )
    else:
        result = ""
    # write the nml per vehicle to disk, it aids debugging
    nml_file = codecs.open(
        os.path.join(generated_nml_path, industry.id + ".nml"), "w", "utf8"
    )
    nml_file.write(result)
    nml_file.close()
    # also return the nml directly for writing to the concatenated nml, don't faff around opening the generated nml files from disk
    return result


def main():
    start = time()
    grf_nml = codecs.open(
        os.path.join(firs.generated_files_path, "firs.nml"), "w", "utf8"
    )
    header_items = [
        # items that must be defined first
        "header",
        "checks",
        "parameters",
        "sprite_templates",
        # items for which order is not significant, so alphabetise for simplicity
        "buildings",
        "cargos",
        "colour",
        "construction_states",
        "fences",
        "ground",
        "jetty_foundations_and_surface",
        "location_check_procedures_industry",
        "magic_trees",
        "perm_storage_mappings",
        "randomise_primary_production_on_build",
        "terrain",
        # items that depend on procedures defined above, so must be defined last
        "objects",
    ]
    for header_item in header_items:
        grf_nml.write(render_header_item_nml(header_item))

    # multiprocessing was tried here and removed as it was empirically slower in testing (due to overhead of starting extra pythons probably)
    for industry in registered_industries:
        grf_nml.write(render_industry_nml(industry))
    grf_nml.close()
    # eh, how long does this take anyway?
    print(format((time() - start), ".2f") + "s")


if __name__ == "__main__":
    main()
