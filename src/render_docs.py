import codecs  # used for writing files - more unicode friendly than standard open() module
import tomllib
import shutil
import sys
import os

currentdir = os.curdir
from time import time

import markdown
from PIL import Image

import utils as utils
import global_constants as global_constants
from polar_fox import git_info
import firs
from grf.incompatible_grfs import incompatible_grfs
from docs.doc_helper import DocHelper

docs_src = os.path.join(currentdir, "src", "docs")
docs_output_path = os.path.join(currentdir, "docs")
if os.path.exists(docs_output_path):
    shutil.rmtree(docs_output_path)
os.mkdir(docs_output_path)
os.mkdir(os.path.join(docs_output_path, "html"))

shutil.copy(os.path.join(docs_src, "index.html"), docs_output_path)

static_dir_src = os.path.join(docs_src, "static")
static_dir_dst = os.path.join(docs_output_path, "html", "static")
shutil.copytree(static_dir_src, static_dir_dst)
shutil.copy(os.path.join(docs_src, "index.html"), docs_output_path)
# we'll be processing some extra images and saving them into the img dir
images_dir_dst = os.path.join(static_dir_dst, "img")

from chameleon import PageTemplateLoader  # chameleon used in most template cases

# setup the places we look for templates
docs_templates = PageTemplateLoader(os.path.join(docs_src, "templates"), format="text")

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)

metadata = {}
metadata.update(global_constants.metadata)

economy_schemas = {}


def render_docs(
    doc_list, file_type, doc_helper, use_markdown=False, source_is_repo_root=False
):
    if source_is_repo_root:
        templates = PageTemplateLoader(os.path.join(currentdir), format="text")
    else:
        templates = docs_templates

    for doc_name in doc_list:
        template = templates[
            doc_name + (".md" if use_markdown else ".pt")
        ]  # .pt is the conventional extension for chameleon page templates
        doc = template(
            firs=firs,
            economy_schemas=economy_schemas,
            incompatible_grfs=incompatible_grfs,
            global_constants=global_constants,
            makefile_args=makefile_args,
            git_info=git_info,
            metadata=metadata,
            utils=utils,
            doc_helper=doc_helper,
            doc_name=doc_name,
        )
        if use_markdown and file_type == "html":
            # if the source is markdown, we need to render markdown to html, and wrap the result in some boilerplate html
            markdown_wrapper = docs_templates["markdown_wrapper.pt"]
            doc = markdown_wrapper(
                content=markdown.markdown(doc),
                global_constants=global_constants,
                makefile_args=makefile_args,
                git_info=git_info,
                metadata=metadata,
                utils=utils,
                doc_helper=doc_helper,
                doc_name=doc_name,
            )
        if file_type == "html":
            subdir = "html"
        elif file_type == "css":
            subdir = os.path.join("html", "static", "css")
        else:
            subdir = ""
        # save the results of templating
        doc_file = codecs.open(
            os.path.join(docs_output_path, subdir, doc_name + "." + file_type),
            "w",
            "utf8",
        )
        doc_file.write(doc)
        doc_file.close()


def main():
    start = time()
    print("[RENDER DOCS]")

    firs.main()

    lang_strings = utils.get_lang_data("grf", "english")["lang_strings"]

    # we also have some strings which are docs-only, so get those
    # should be in a dedicated method probably, but eh
    with open(
        os.path.join(currentdir, "src", "docs", "extra_strings.toml"), "rb"
    ) as fp:
        extra_strings_source = tomllib.load(fp)
    for node_name, node_value in extra_strings_source.items():
        lang_strings[node_name] = node_value["base"]
    # print(lang_strings)

    for economy in firs.economy_manager:
        enabled_cargos = [
            cargo for cargo in firs.cargo_manager if cargo.id in economy.cargo_ids
        ]
        enabled_industries = [
            industry
            for industry in firs.industry_manager
            if industry.economy_variations[economy.id].enabled
        ]
        economy_schemas[economy] = {
            "enabled_cargos": enabled_cargos,
            "enabled_industries": enabled_industries,
        }

    doc_helper = DocHelper(
        firs=firs,
        lang_strings=lang_strings,
        economy_schemas=economy_schemas,
    )

    # copy the cargo icons to an oversized image so they're legible
    cargo_icons_src = os.path.join(currentdir, "src", "graphics", "cargoicons.png")
    cargo_icons_spritesheet = Image.open(os.path.join(cargo_icons_src))
    processed_cargo_icons_spritesheet = cargo_icons_spritesheet.resize(
        (2 * cargo_icons_spritesheet.size[0], 2 * cargo_icons_spritesheet.size[1]),
        resample=Image.Resampling.NEAREST,
    )
    output_path = os.path.join(images_dir_dst, "cargoicons.png")
    processed_cargo_icons_spritesheet.save(output_path, optimize=True, transparency=0)

    # render standard docs from a list
    html_docs = [
        "get_started",
        "code_reference",
        "economies",
        "cargos",
        "industries",
        "translations",
    ]
    txt_docs = ["readme"]
    license_docs = ["license"]
    markdown_docs = ["changelog"]
    graph_docs = ["cargoflow"]
    stylesheets = ["cargoflow_styles"]

    render_docs(html_docs, "html", doc_helper)
    render_docs(txt_docs, "txt", doc_helper)
    render_docs(
        license_docs,
        "txt",
        doc_helper,
        source_is_repo_root=True,
    )
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(
        markdown_docs, "txt", doc_helper, use_markdown=True, source_is_repo_root=True
    )
    render_docs(
        markdown_docs, "html", doc_helper, use_markdown=True, source_is_repo_root=True
    )
    render_docs(graph_docs, "dotall", doc_helper)
    render_docs(stylesheets, "css", doc_helper)

    # cargoflow wrappers are just different enough to not fit generic render_docs() case without making it painfully convoluted
    for economy in firs.economy_manager:
        template = docs_templates["cargoflow_wrapper.pt"]
        result = template(economy=economy, doc_helper=doc_helper)
        doc_name = "cargoflow_" + doc_helper.get_economy_name_char_safe(economy)
        doc_file = codecs.open(
            os.path.join(docs_output_path, "html", doc_name + ".html"), "w", "utf8"
        )
        doc_file.write(result)
        doc_file.close()

    print(
        "[RENDER DOCS]",
        "- complete",
        format((time() - start), ".2f") + "s",
    )


if __name__ == "__main__":
    main()
