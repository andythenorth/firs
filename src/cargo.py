"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

import os.path

import global_constants as global_constants
import utils as utils

currentdir = os.curdir

from chameleon import PageTemplateLoader  # chameleon used in most template cases

# setup the places we look for templates
templates = PageTemplateLoader(
    os.path.join(currentdir, "src", "templates"), format="text"
)

from economies import registered_economies
from cargos import registered_cargos

# this will be suboptimal for performance, as it will be imported multiple times per compile, causing duplicat TOML parsing
# fine for v4, but for v5, this might be better centralised?
from polar_fox.cargo_classes import cargo_classes

cargo_class_scheme = cargo_classes.CargoClassSchemes().default_scheme


class Cargo(object):
    """Base class to hold cargos"""

    def __init__(self, id, **kwargs):
        self.id = id
        self.cargo_label = kwargs["cargo_label"]
        self.type_name = kwargs["type_name"]
        self.unit_name = kwargs["unit_name"]
        self.type_abbreviation = kwargs["type_abbreviation"]
        self.sprite = kwargs["sprite"]
        self.weight = kwargs["weight"]
        self.is_freight = kwargs["is_freight"]
        self.cargo_classes = kwargs["cargo_classes"]
        self.town_growth_effect = kwargs["town_growth_effect"]
        self.town_growth_multiplier = kwargs["town_growth_multiplier"]
        self.units_of_cargo = kwargs["units_of_cargo"]
        self.items_of_cargo = kwargs["items_of_cargo"]
        self.penalty_lowerbound = kwargs["penalty_lowerbound"]
        self.single_penalty_length = kwargs["single_penalty_length"]
        self.price_factor = kwargs["price_factor"]
        self.capacity_multiplier = kwargs["capacity_multiplier"]
        # not nml properties
        self.allow_animated_pixels = kwargs.get(
            "allow_animated_pixels", False
        )  # suppress nml warnings about animated pixels
        self.icon_indices = kwargs[
            "icon_indices"
        ]  # icon indices relate to position of icon in cargo icons spritesheet
        self.economy_variations = {}
        for economy in registered_economies:
            if self.id in economy.cargo_ids:
                # create an economy variation
                numeric_id = economy.cargo_ids.index(self.id)
                # As of May 2015, OTTD requires some cargos in specific slots, otherwise default houses break
                mandatory_numeric_ids = {"PASS": 0, "MAIL": 2, "GOOD": 5, "FOOD": 11}
                for key, value in mandatory_numeric_ids.items():
                    if self.cargo_label == key and numeric_id != value:
                        raise Exception(
                            "Economy "
                            + economy.id
                            + ": has cargo "
                            + self.id
                            + " in position "
                            + str(numeric_id)
                            + "; needs to be in position "
                            + str(value)
                        )
                self.economy_variations[economy] = {"numeric_id": numeric_id}
        # validation
        self.validate_cargo_classes()
        self.validate_icon_indices()

    def validate_icon_indices(self):
        # guard against overlapping icon indices, icons should be unique per cargo
        # if two cargos use same icon (1) don't, copy-paste, then adjust some pixels for one of them (2) see 1
        for cargo in registered_cargos:
            if cargo.icon_indices == self.icon_indices:
                utils.echo_message(
                    "Cargo "
                    + self.id
                    + " has overlapping icon_indices with cargo "
                    + cargo.id
                )

    def validate_cargo_classes(self):
        # crude, not intended to solve everything
        disallowed_pairs = [("CC_FOOD_GRADE", "CC_NON_FOOD_GRADE")]
        for disallowed_pair in disallowed_pairs:
            if (disallowed_pair[0] in self.cargo_classes) and (
                disallowed_pair[1] in self.cargo_classes
            ):
                raise BaseException(
                    self.id
                    + " sets both "
                    + disallowed_pair[0]
                    + " and "
                    + disallowed_pair[1]
                    + " which is not supported"
                )
        for cargo_class in self.cargo_classes:
            # CC_GAS doesn't bother validating for food-grade bits as of 2024, food-grade gases tends to not be relevant
            if cargo_class in ["CC_EXPRESS", "CC_PIECE_GOODS", "CC_OPEN_BULK", "CC_COVERED_BULK", "CC_LIQUID", "CC_POWDERIZED"]:
                if ("CC_FOOD_GRADE" not in self.cargo_classes) and ("CC_NON_FOOD_GRADE" not in self.cargo_classes):
                    raise BaseException(self.id + " should set one of CC_FOOD_GRADE or CC_NON_FOOD_GRADE")

    def get_numeric_id(self, economy):
        return self.economy_variations[economy].get("numeric_id")

    def get_price_factor(self, economy):
        return 100

    def get_cargo_label(self):
        # wrap cargo labels in " chars because nml needs them as string literals (we store them - by design - as python strings)
        return '"' + self.cargo_label + '"'

    def get_cargo_colour(self, economy):
        # automatically provide a colour specific to the economy, don't attempt to provide a consistent colour across all economies, PITA to maintain
        return global_constants.valid_cargo_colours[self.get_numeric_id(economy)]

    def get_cargo_classes_for_nml(self):
        classes_mapped_to_bit_numbers = []
        for cargo_class in self.cargo_classes:
            classes_mapped_to_bit_numbers.append(
                str(
                    cargo_class_scheme.cargo_classes_taxonomy[cargo_class]["bit_number"]
                )
            )
        return "bitmask(" + ",".join(classes_mapped_to_bit_numbers) + ")"

    def get_property(self, property_name, economy):
        # straightforward lookup of a property, doesn't try to handle failure case of property not found; don't look up props that don't exist
        if economy is not None and property_name in self.economy_variations[economy]:
            return self.economy_variations[economy].get(property_name)
        else:
            return getattr(self, property_name)

    def get_property_declaration(self, property_name, economy=None):
        value = self.get_property(property_name, economy)
        return property_name + ": " + str(value) + ";"

    def register(self):
        if len(self.economy_variations) == 0:
            utils.echo_message(self.id + " is not used in any economy")
        registered_cargos.append(self)
