import colorsys

import utils as utils
import global_constants as global_constants

# firs is imported, but main is not called in this module, this relies on firs already being present in the context
import firs

class DocHelper(object):
    palette = utils.dos_palette_to_rgb()

    def __init__(
        self,
        lang_strings,
    ):
        self.lang_strings = lang_strings

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
        # order of dict key corresponds to sort order of cargos when pretty-printed
        pretty_names = {
            "CC_PASSENGERS": "Passengers",
            "CC_MAIL": "Mail",
            "CC_EXPRESS": "Express",
            "CC_ARMOURED": "Armoured",
            "CC_PIECE_GOODS": "Piece Goods",
            "CC_OPEN_BULK": "Open Bulk",
            "CC_COVERED_BULK": "Covered Bulk",
            "CC_LIQUID": "Liquid",
            "CC_GAS": "Gas",
            "CC_POWDERIZED": "Powderized",
            "CC_FLATBED": "Flatbed",
            "CC_REFRIGERATED": "Refrigerated",
            "CC_WEIRD": "Weird",
            "CC_FOOD_GRADE": "Food-Grade",
            "CC_NON_FOOD_GRADE": "Non-Food-Grade",
        }
        for cargo_class in cargo.cargo_classes:
            if cargo_class not in pretty_names:
                utils.echo_message(
                    "cargo class "
                    + cargo_class
                    + " is not pretty-printable (used in cargo "
                    + cargo.id
                    + ")"
                )

        for cargo_class in pretty_names:
            if cargo_class in cargo.cargo_classes:
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
        for economy in firs.economy_manager:
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
            (self.get_cargo_name(cargo), cargo) for cargo in firs.cargo_manager
        )
        return sorted(result.items())

    def get_industries_sorted_by_name(self):
        # industries don't store the name as a python attr, but we often need to iterate over their names in A-Z order
        # note the list slice so that we sort on the first name in alpha-order for industries with multiple names
        result = dict(
            (self.get_industry_all_names(industry)[0], industry)
            for industry in firs.industry_manager
        )
        return sorted(result.items())

    def get_economy_extra_info(self, economy):
        return self.lang_strings.get("ECONOMY_INFO_" + economy.id, "")

    def get_cargo_extra_info(self, cargo):
        return self.lang_strings.get("CARGO_INFO_" + cargo.id.upper(), "")

    def get_industry_extra_info(self, industry):
        return self.lang_strings.get("INDUSTRY_INFO_" + industry.id.upper(), "")

    def industry_is_unused(self, industry, economy):
        if industry in economy.industries:
            return False
        else:
            return True

    def industries_accepting_cargo_for_economy(self, cargo, economy):
        result = set()
        if cargo in economy.cargos:
            for industry in economy.industries:
                cargo_label_list = industry.get_accepted_cargo_labels_by_economy(economy)
                for cargo_label in cargo_label_list:
                    if cargo.cargo_label == cargo_label:
                        result.add(industry)
        result = sorted(result, key=self.get_industry_name)
        return result

    def industries_producing_cargo_for_economy(self, cargo, economy):
        result = set()
        if cargo in economy.cargos:
            for industry in economy.industries:
                cargo_list = industry.get_prod_cargo_types(economy)
                for cargo_label, output_ratio in cargo_list:
                    if cargo.cargo_label == cargo_label:
                        result.add(industry)
        result = sorted(result, key=self.get_industry_name)
        return result

    def cargo_is_unused_in_any_economy(self, cargo):
        result = 0
        for economy in firs.economy_manager:
            result += len(self.industries_accepting_cargo_for_economy(cargo, economy))
            result += len(self.industries_producing_cargo_for_economy(cargo, economy))
        if result == 0:
            return True
        else:
            return False

    def cargo_is_unused(self, cargo, economy):
        result = 0
        result += len(self.industries_accepting_cargo_for_economy(cargo, economy))
        result += len(self.industries_producing_cargo_for_economy(cargo, economy))
        if result == 0:
            return True
        else:
            return False

    def get_cargo_objects_from_labels(self, cargo_list):
        result = []
        for cargo_label in cargo_list:
            for cargo in firs.cargo_manager:
                if cargo_label == cargo.cargo_label:
                    result.append(cargo)
        return result

    def cargos_produced_by_industry(self, industry, economy):
        result = self.get_cargo_objects_from_labels(
            [label for label, output_ratio in industry.get_prod_cargo_types(economy)]
        )
        result = sorted(result, key=self.get_cargo_name)
        return result

    def cargos_accepted_by_industry(self, industry, economy):
        result = self.get_cargo_objects_from_labels(
            industry.get_accepted_cargo_labels_by_economy(economy)
        )
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
        for cargo in firs.cargo_manager:
            if cargo.id == node:
                return "C_" + node
        for industry in firs.industry_manager:
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
        for industry in firs.industry_manager:
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
