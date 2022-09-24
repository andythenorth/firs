print("[RENDER DOCS] render docs")

import codecs  # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os

currentdir = os.curdir
from time import time

import markdown
from PIL import Image
import colorsys

import utils as utils
import global_constants as global_constants
from polar_fox import git_info
import firs
from incompatible_grfs import incompatible_grfs

docs_src = os.path.join(currentdir, "src", "docs_templates")
docs_output_path = os.path.join(currentdir, "docs")
if os.path.exists(docs_output_path):
    shutil.rmtree(docs_output_path)
os.mkdir(docs_output_path)

shutil.copy(os.path.join(docs_src, "index.html"), docs_output_path)

static_dir_src = os.path.join(docs_src, "html", "static")
static_dir_dst = os.path.join(docs_output_path, "html", "static")
shutil.copytree(static_dir_src, static_dir_dst)
shutil.copy(os.path.join(docs_src, "index.html"), docs_output_path)
# we'll be processing some extra images and saving them into the img dir
images_dir_dst = os.path.join(static_dir_dst, "img")

from chameleon import PageTemplateLoader  # chameleon used in most template cases

# setup the places we look for templates
docs_templates = PageTemplateLoader(docs_src, format="text")


# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)

# get the strings from base lang file so they can be used in docs
base_lang_strings = utils.parse_base_lang()

metadata = {}
metadata.update(global_constants.metadata)

# default sort for docs is by id
registered_cargos = sorted(
    firs.registered_cargos, key=lambda registered_cargos: registered_cargos.id
)
registered_industries = sorted(
    firs.registered_industries,
    key=lambda registered_industries: registered_industries.id,
)
registered_economies = firs.registered_economies
economy_schemas = {}
palette = utils.dos_palette_to_rgb()


class DocHelper(object):
    # dirty class to help do some doc formatting
    def get_economy_name(self, economy):
        string_id = "STR_PARAM_VALUE_ECONOMIES_" + economy.id
        name_string = base_lang_strings.get(string_id, "NO_NAME " + economy.id)
        return name_string.split(" Economy")[
            0
        ]  # name strings contain 'economy', I don't want that in docs

    def get_economy_name_char_safe(self, economy):
        # this uses _ not -, because it's also used in graphviz which chokes on -
        return self.get_economy_name(economy).replace(" ", "_").lower()

    def get_cargo_name(self, cargo):
        # cargos don't store the name directly as a python attr, but in lang - so look it up in base_lang using string id
        name = cargo.type_name
        string_id = utils.unwrap_nml_string_declaration(name)
        return base_lang_strings.get(string_id, "NO NAME " + str(name) + " " + cargo.id)

    def pretty_print_cargo_classes(self, cargo):
        result = []
        pretty_names = {
            "CC_ARMOURED": "Armoured",
            "CC_BULK": "Bulk (uncountable)",
            "CC_COVERED": "Covered (weather protected)",
            "CC_EXPRESS": "Express",
            "CC_HAZARDOUS": "Hazardous",
            "CC_LIQUID": "Liquid",
            "CC_MAIL": "Mail",
            "CC_NON_POURABLE": "Not Pourable",
            "CC_OVERSIZED": "Oversized",
            "CC_PASSENGERS": "Passengers",
            "CC_PIECE_GOODS": "Piece Goods (countable)",
            "CC_POWDERIZED": "Powderized",
            "CC_REFRIGERATED": "Refrigerated",
        }
        cargo_classes_as_literal = cargo.cargo_classes[8:-1]
        cargo_classes = [i.strip() for i in cargo_classes_as_literal.split(",")]
        for cargo_class in cargo_classes:
            if cargo_class not in pretty_names:
                utils.echo_message(
                    "cargo class "
                    + cargo_class
                    + " is not pretty-printable (used in cargo "
                    + cargo.id
                    + ")"
                )
            else:
                result.append(pretty_names[cargo_class])
        return ", ".join(result)

    def get_industry_name(self, industry, economy=None):
        # industries don't store the name directly as a python attr, but in lang - so look it up in base_lang using string id
        name = industry.get_property("name", economy)
        string_id = utils.unwrap_nml_string_declaration(name)
        if string_id not in base_lang_strings:
            utils.echo_message("Warning: string " + string_id + " missing for docs")
        return base_lang_strings.get(
            string_id, "NO NAME " + str(name) + " " + industry.id
        )

    def get_industry_all_name_strings(self, industry):
        # names can vary in each economy
        result = []
        for economy in economy_schemas:
            name = industry.get_property("name", economy)
            result.append(utils.unwrap_nml_string_declaration(name))
        return set(result)

    def get_industry_all_names(self, industry):
        # names can vary in each economy
        result = []
        for name_string in self.get_industry_all_name_strings(industry):
            result.append(
                base_lang_strings.get(
                    name_string, "NO NAME " + name_string + " " + industry.id
                )
            )
        return sorted(set(result))

    def get_nearby_station_name(self, industry):
        station_name = utils.unwrap_nml_string_declaration(
            industry.get_property("nearby_station_name", None)
        )
        return base_lang_strings[station_name]

    def get_registered_cargo_sorted_by_name(self):
        # cargos don't store the name as a python attr, but we often need to iterate over their names in A-Z order
        result = dict(
            (self.get_cargo_name(cargo), cargo) for cargo in registered_cargos
        )
        return sorted(result.items())

    def get_registered_industries_sorted_by_name(self):
        # industries don't store the name as a python attr, but we often need to iterate over their names in A-Z order
        # note the list slice so that we sort on the first name in alpha-order for industries with multiple names
        result = dict(
            (self.get_industry_all_names(industry)[0], industry)
            for industry in registered_industries
        )
        return sorted(result.items())

    def get_economy_extra_info(self, economy):
        return base_lang_strings.get("ECONOMY_INFO_" + economy.id, "")

    def get_cargo_extra_info(self, cargo):
        return base_lang_strings.get("CARGO_INFO_" + cargo.id.upper(), "")

    def get_industry_extra_info(self, industry):
        return base_lang_strings.get("INDUSTRY_INFO_" + industry.id.upper(), "")

    def industry_is_unused(self, industry, economy):
        if industry in economy_schemas[economy]["enabled_industries"]:
            return False
        else:
            return True

    def industries_producing_cargo(self, cargo, economy):
        result = set()
        if cargo in economy_schemas[economy]["enabled_cargos"]:
            for industry in economy_schemas[economy]["enabled_industries"]:
                cargo_list = industry.get_prod_cargo_types(economy)
                for cargo_label, output_ratio in cargo_list:
                    if cargo.cargo_label == cargo_label:
                        result.add(industry)
        result = sorted(result, key=self.get_industry_name)
        return result

    def industries_accepting_cargo(self, cargo, economy):
        result = set()
        if cargo in economy_schemas[economy]["enabled_cargos"]:
            for industry in economy_schemas[economy]["enabled_industries"]:
                cargo_list = industry.get_accept_cargo_types(economy)
                for cargo_label in cargo_list:
                    if cargo.cargo_label == cargo_label:
                        result.add(industry)
        result = sorted(result, key=self.get_industry_name)
        return result

    def cargo_is_unused_in_any_economy(self, cargo):
        result = 0
        for economy in registered_economies:
            result += len(self.industries_accepting_cargo(cargo, economy))
            result += len(self.industries_producing_cargo(cargo, economy))
        if result == 0:
            return True
        else:
            return False

    def cargo_is_unused(self, cargo, economy):
        result = 0
        result += len(self.industries_accepting_cargo(cargo, economy))
        result += len(self.industries_producing_cargo(cargo, economy))
        if result == 0:
            return True
        else:
            return False

    def get_cargo_objects_from_labels(self, cargo_list):
        result = []
        for cargo_label in cargo_list:
            for cargo in registered_cargos:
                if cargo_label == cargo.cargo_label:
                    result.append(cargo)
        return result

    def filter_cargos_by_active_in_economy(self, cargo_list, economy):
        # For industries, OpenTTD automatically filters non-active cargos in-game, but the docs need to do it manually
        result = []
        for cargo in cargo_list:
            if cargo in economy_schemas[economy]["enabled_cargos"]:
                result.append(cargo)
        return result

    def cargos_produced_by_industry(self, industry, economy):
        result = self.get_cargo_objects_from_labels(
            [label for label, output_ratio in industry.get_prod_cargo_types(economy)]
        )
        result = self.filter_cargos_by_active_in_economy(result, economy)
        result = sorted(result, key=self.get_cargo_name)
        return result

    def cargos_accepted_by_industry(self, industry, economy):
        result = self.get_cargo_objects_from_labels(
            industry.get_accept_cargo_types(economy)
        )
        result = self.filter_cargos_by_active_in_economy(result, economy)
        result = sorted(result, key=self.get_cargo_name)
        return result

    def get_industry_colour(self, industry):
        return palette[int(industry.get_property("map_colour", None))]

    def get_cargo_colour_as_hex_triple_with_hash(self, cargo, economy):
        colour_as_rgb = palette[int(cargo.get_cargo_colour(economy))]
        result = [
            i
            for i in colorsys.rgb_to_hsv(
                colour_as_rgb[0], colour_as_rgb[1], colour_as_rgb[2]
            )
        ]
        # darken colours that are too light
        result[2] = result[2] / 255 if (result[2] / 255) < 0.66 else 0.66
        # saturate colours that are unsaturated
        result[1] = result[1] * 2 if result[1] < 0.3 else result[1]
        result = ",".join([str(i) for i in result])
        return result

    def unpack_cargoflow_node_name(self, node):
        # there are some known exceptions for special nodes which are maintained as a manual list
        if node in [
            "T_town_industries",
            "T_towns_alcohol",
            "T_towns_food",
            "T_towns_goods",
            "T_towns_vehicles",
            "N_force_rank",
        ]:
            return node
        # then check cargos and industries
        for cargo in registered_cargos:
            if cargo.id == node:
                return "C_" + node
        for industry in registered_industries:
            if industry.id == node:
                return "I_" + node
        # fail if the node can't be unpacked
        raise Exception(
            "Unknown cargoflow node passed to doc_helper.unpack_cargoflow_node_name: "
            + node
        )

    def get_cargoflow_banned_cargos(self):
        return ["mail", "passengers"]

    def get_cargoflow_supply_cargos(self):
        return ["farm_supplies", "engineering_supplies"]

    def get_active_nav(self, doc_name, nav_link):
        return ("", "active")[doc_name == nav_link]


def render_docs(doc_list, file_type, use_markdown=False, source_is_repo_root=False):
    if source_is_repo_root:
        doc_path = os.path.join(currentdir)
    else:
        doc_path = docs_src

    docs_templates = PageTemplateLoader(doc_path, format="text")

    for doc_name in doc_list:
        template = docs_templates[
            doc_name + ".pt"
        ]  # .pt is the conventional extension for chameleon page templates
        doc = template(
            registered_cargos=registered_cargos,
            registered_industries=registered_industries,
            registered_economies=registered_economies,
            economy_schemas=economy_schemas,
            incompatible_grfs=incompatible_grfs,
            global_constants=global_constants,
            makefile_args=makefile_args,
            git_info=git_info,
            metadata=metadata,
            utils=utils,
            doc_helper=DocHelper(),
            doc_name=doc_name,
        )
        if use_markdown:
            # the doc might be in markdown format, if so we need to render markdown to html, and wrap the result in some boilerplate html
            markdown_wrapper = PageTemplateLoader(docs_src, format="text")[
                "markdown_wrapper.pt"
            ]
            doc = markdown_wrapper(
                content=markdown.markdown(doc),
                global_constants=global_constants,
                makefile_args=makefile_args,
                git_info=git_info,
                metadata=metadata,
                utils=utils,
                doc_helper=DocHelper(),
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
    for economy in registered_economies:
        enabled_cargos = [
            cargo for cargo in registered_cargos if cargo.id in economy.cargo_ids
        ]
        enabled_industries = [
            industry
            for industry in registered_industries
            if industry.economy_variations[economy.id].enabled
        ]
        economy_schemas[economy] = {
            "enabled_cargos": enabled_cargos,
            "enabled_industries": enabled_industries,
        }

    # copy the cargo icons to an oversized image so they're legible
    cargo_icons_src = os.path.join(
        currentdir, "src", "graphics", "other", "cargoicons.png"
    )
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

    render_docs(html_docs, "html")
    render_docs(txt_docs, "txt")
    render_docs(
        license_docs,
        "txt",
        source_is_repo_root=True,
    )
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(markdown_docs, "txt")
    render_docs(markdown_docs, "html", use_markdown=True)
    render_docs(graph_docs, "dotall")
    render_docs(stylesheets, "css")

    # cargoflow wrappers are just different enough to not fit generic render_docs() case without making it painfully convoluted
    for economy in registered_economies:
        template = docs_templates["cargoflow_wrapper.pt"]
        result = template(economy=economy, doc_helper=DocHelper())
        doc_name = "cargoflow_" + DocHelper().get_economy_name_char_safe(economy)
        doc_file = codecs.open(
            os.path.join(docs_output_path, "html", doc_name + ".html"), "w", "utf8"
        )
        doc_file.write(result)
        doc_file.close()
    # eh, how long does this take anyway?
    print(format((time() - start), ".2f") + "s")


if __name__ == "__main__":
    main()
