"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

import global_constants as global_constants
import utils as utils

# firs is imported, but main is not called in this module, this relies on firs already being present in the context
import firs


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
        self.units_of_cargo = kwargs["units_of_cargo"]
        self.items_of_cargo = kwargs["items_of_cargo"]
        self.penalty_lowerbound = kwargs["penalty_lowerbound"]
        self.single_penalty_length = kwargs["single_penalty_length"]
        self.price_factor = kwargs["price_factor"]
        self.capacity_multiplier = kwargs["capacity_multiplier"]
        # except for PASS and MAIL town growth effect and multiplier are not set by FIRS, as they are of limited use
        self.town_growth_effect = kwargs.get("town_growth_effect", "TOWNGROWTH_NONE")
        self.town_growth_multiplier = "1.0"
        # vulcan properties are optional, and are used by FIRS GS
        self.vulcan_town_effect = kwargs.get("vulcan_town_effect", None)
        # not nml properties
        # suppress nml warnings about animated pixels
        self.allow_animated_pixels = kwargs.get("allow_animated_pixels", False)
        # icon indices relate to position of icon in cargo icons spritesheet
        self.icon_indices = kwargs["icon_indices"]
        # housekeeping
        self.sprites_complete = kwargs.get("sprites_complete", False)
        self.economy_variations = {}
        for economy in firs.economy_manager:
            if self.id in economy.cargo_ids:
                # create an economy variation
                numeric_id = economy.cargo_ids.index(self.id)
                self.economy_variations[economy] = {"numeric_id": numeric_id}

        if len(self.economy_variations) == 0:
            utils.echo_message(self.id + " is not used in any economy")

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

    def get_property(self, property_name, economy):
        # straightforward lookup of a property, doesn't try to handle failure case of property not found; don't look up props that don't exist
        if economy is not None and property_name in self.economy_variations[economy]:
            return self.economy_variations[economy].get(property_name)
        else:
            return getattr(self, property_name)

    def get_property_declaration(self, property_name, economy=None):
        value = self.get_property(property_name, economy)
        return property_name + ": " + str(value) + ";"

    def validate_cargo_classes(self):
        # as of October 2024, I concluded that whilst the fundamental classes are useful, the extra 'exclude only' classes are not worth the candle
        # (1) there's no clear heuristic for when to set them or not
        # - IRL both pipe and farm machines are 'oversized', but STPP was setting CC_OVERSIZED, whilst FMSP was not
        # - there's no compelling evidence about how, or even if, these extra classes are useful to vehicle set authors
        # (2) setting them is likely to lead to unpredictable effects which are hard to reason about, whereas not setting them is easy to reason about
        # https://newgrf-specs.tt-wiki.net/wiki/Action0/Cargos#CargoClasses_.2816.29 and https://newgrf-specs.tt-wiki.net/wiki/NML:Cargos#Cargo_classes

        # so we only permit the fundamental classes
        allowed_cargo_classes = [
            "CC_PASSENGERS",
            "CC_MAIL",
            "CC_EXPRESS",
            "CC_ARMOURED",
            "CC_BULK",
            "CC_PIECE_GOODS",
            "CC_LIQUID",
            "NO_CARGO_CLASS",
        ]
        for cargo_class in self.cargo_classes:
            if cargo_class not in allowed_cargo_classes:
                raise BaseException(
                    self.id
                    + " defines cargo class "
                    + cargo_class
                    + " which is not permitted."
                )

    @property
    def properties_for_gs(self):
        result = {}
        result["cargo_label"] = self.cargo_label
        result["id"] = self.id
        result["vulcan_town_effect"] = self.vulcan_town_effect
        return result
