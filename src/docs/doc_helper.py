import colorsys

import utils as utils
import global_constants as global_constants


class DocHelper(object):
    palette = utils.dos_palette_to_rgb()

    def __init__(
        self,
        lang_strings,
        registered_industries,
        registered_cargos,
        registered_economies,
        economy_schemas,
    ):
        self.lang_strings = lang_strings
        self.registered_industries = registered_industries
        self.registered_cargos = registered_cargos
        self.registered_economies = registered_economies
        self.economy_schemas = economy_schemas

    # dirty class to help do some doc formatting
    def get_economy_name(self, economy):
        string_id = "STR_PARAM_VALUE_ECONOMIES_" + economy.id
        name_string = self.lang_strings.get(string_id, "NO_NAME " + economy.id)
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
        return self.lang_strings.get(string_id, "NO NAME " + str(name) + " " + cargo.id)

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
        if string_id not in self.lang_strings:
            utils.echo_message("Warning: string " + string_id + " missing for docs")
        return self.lang_strings.get(
            string_id, "NO NAME " + str(name) + " " + industry.id
        )

    def get_industry_all_name_strings(self, industry):
        # names can vary in each economy
        result = []
        for economy in self.economy_schemas:
            name = industry.get_property("name", economy)
            result.append(utils.unwrap_nml_string_declaration(name))
        return set(result)

    def get_industry_all_names(self, industry):
        # names can vary in each economy
        result = []
        for name_string in self.get_industry_all_name_strings(industry):
            result.append(
                self.lang_strings.get(
                    name_string, "NO NAME " + name_string + " " + industry.id
                )
            )
        return sorted(set(result))

    def get_nearby_station_name(self, industry):
        station_name = utils.unwrap_nml_string_declaration(
            industry.get_property("nearby_station_name", None)
        )
        return self.lang_strings[station_name]

    def get_registered_cargo_sorted_by_name(self):
        # cargos don't store the name as a python attr, but we often need to iterate over their names in A-Z order
        result = dict(
            (self.get_cargo_name(cargo), cargo) for cargo in self.registered_cargos
        )
        return sorted(result.items())

    def get_registered_industries_sorted_by_name(self):
        # industries don't store the name as a python attr, but we often need to iterate over their names in A-Z order
        # note the list slice so that we sort on the first name in alpha-order for industries with multiple names
        result = dict(
            (self.get_industry_all_names(industry)[0], industry)
            for industry in self.registered_industries
        )
        return sorted(result.items())

    def get_economy_extra_info(self, economy):
        return self.lang_strings.get("ECONOMY_INFO_" + economy.id, "")

    def get_cargo_extra_info(self, cargo):
        return self.lang_strings.get("CARGO_INFO_" + cargo.id.upper(), "")

    def get_industry_extra_info(self, industry):
        return self.lang_strings.get("INDUSTRY_INFO_" + industry.id.upper(), "")

    def industry_is_unused(self, industry, economy):
        if industry in self.economy_schemas[economy]["enabled_industries"]:
            return False
        else:
            return True

    def industries_producing_cargo(self, cargo, economy):
        result = set()
        if cargo in self.economy_schemas[economy]["enabled_cargos"]:
            for industry in self.economy_schemas[economy]["enabled_industries"]:
                cargo_list = industry.get_prod_cargo_types(economy)
                for cargo_label, output_ratio in cargo_list:
                    if cargo.cargo_label == cargo_label:
                        result.add(industry)
        result = sorted(result, key=self.get_industry_name)
        return result

    def industries_accepting_cargo(self, cargo, economy):
        result = set()
        if cargo in self.economy_schemas[economy]["enabled_cargos"]:
            for industry in self.economy_schemas[economy]["enabled_industries"]:
                cargo_list = industry.get_accept_cargo_types(economy)
                for cargo_label in cargo_list:
                    if cargo.cargo_label == cargo_label:
                        result.add(industry)
        result = sorted(result, key=self.get_industry_name)
        return result

    def cargo_is_unused_in_any_economy(self, cargo):
        result = 0
        for economy in self.registered_economies:
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
            for cargo in self.registered_cargos:
                if cargo_label == cargo.cargo_label:
                    result.append(cargo)
        return result

    def filter_cargos_by_active_in_economy(self, cargo_list, economy):
        # For industries, OpenTTD automatically filters non-active cargos in-game, but the docs need to do it manually
        result = []
        for cargo in cargo_list:
            if cargo in self.economy_schemas[economy]["enabled_cargos"]:
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
        return self.palette[int(industry.get_property("map_colour", None))]

    def get_cargo_colour_as_hex_triple_with_hash(self, cargo, economy):
        colour_as_rgb = self.palette[int(cargo.get_cargo_colour(economy))]
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
        for cargo in self.registered_cargos:
            if cargo.id == node:
                return "C_" + node
        for industry in self.registered_industries:
            if industry.id == node:
                return "I_" + node
        # fail if the node can't be unpacked
        raise Exception(
            "Unknown cargoflow node passed to doc_helper.unpack_cargoflow_node_name: "
            + node
        )

    def get_cargoflow_graph_tuning(self, economy):
        return economy.cargoflow_graph_tuning

    def get_cargoflow_banned_cargos(self):
        return ["mail", "passengers"]

    def get_cargoflow_supply_cargos(self):
        return [
            "farm_supplies",
            "engineering_supplies",
            "welding_consumables",
            "seals_belts_and_hoses",
        ]

    def get_cargoflow_wormhole_cargos(self, economy):
        result = {"by_industry": {}, "by_cargo": {}}

        # first find the industries from (1) cargoflow_graph_tuning (2) town industries
        # we want the actual industry, not the id
        all_wormhole_industries = []
        for industry in self.registered_industries:
            if industry.id in (
                economy.cargoflow_graph_tuning.get("wormhole_industries", [])
            ):
                all_wormhole_industries.append(industry)
            elif (
                getattr(industry, "town_industry_for_cargoflow", False)
                and industry.economy_variations[economy.id].enabled
            ):
                all_wormhole_industries.append(industry)

        # then structure the result by industry, for both wormhole industries and wormhole cargos
        for industry in all_wormhole_industries:
            result["by_industry"][industry.id] = []
            for cargo in self.cargos_accepted_by_industry(industry, economy):
                result["by_industry"][industry.id].append(cargo)
                if cargo.id not in result["by_cargo"].keys():
                    result["by_cargo"][cargo.id] = []
                result["by_cargo"][cargo.id].append(industry)
        return result

    def get_active_nav(self, doc_name, nav_link):
        return ("", "active")[doc_name == nav_link]
