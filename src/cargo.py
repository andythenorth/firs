"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

import os.path
currentdir = os.curdir

# add to the module search path
src_path = os.path.join(currentdir, 'src')

import utils as utils

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(src_path, 'templates'), format='text')
industry_templates = PageTemplateLoader(os.path.join(src_path, 'industries'), format='text')

from economies import registered_economies
from cargos import registered_cargos

class Cargo(object):
    """ Base class to hold cargos"""
    def __init__(self, id, **kwargs):
        self.id = id
        self.cargo_label = kwargs['cargo_label']
        self.type_name = kwargs['type_name']
        self.unit_name = kwargs['unit_name']
        self.type_abbreviation = kwargs['type_abbreviation']
        self.sprite = kwargs['sprite']
        self.weight = kwargs['weight']
        self.cargo_payment_list_colour = kwargs['cargo_payment_list_colour']
        self.station_list_colour = self.cargo_payment_list_colour # use same value for both cargo colour properties
        self.is_freight = kwargs['is_freight']
        self.cargo_classes = kwargs['cargo_classes']
        self.town_growth_effect = kwargs['town_growth_effect']
        self.town_growth_multiplier = kwargs['town_growth_multiplier']
        self.units_of_cargo = kwargs['units_of_cargo']
        self.items_of_cargo = kwargs['items_of_cargo']
        self.penalty_lowerbound = kwargs['penalty_lowerbound']
        self.single_penalty_length = kwargs['single_penalty_length']
        self.price_factor = kwargs['price_factor']
        self.capacity_multiplier = kwargs['capacity_multiplier']
        # not nml properties
        self.allow_animated_pixels = kwargs.get('allow_animated_pixels', False) # suppress nml warnings about animated pixels
        self.icon_indices = kwargs['icon_indices'] # icon indices relate to position of icon in cargo icons spritesheet
        self.economy_variations = {}
        for economy in registered_economies:
            if self.id in economy.cargos:
                numeric_id = economy.cargos.index(self.id)
                # As of May 2015, OTTD requires some cargos in specific slots, otherwise default houses break
                mandatory_numeric_ids = {'PASS': 0, 'MAIL': 2, 'GOOD': 5, 'FOOD': 11}
                for key, value in mandatory_numeric_ids.items():
                    if self.cargo_label == key and numeric_id != value:
                        raise Exception("Economy " + economy.id + ": has cargo " + self.id + " in position " + str(numeric_id) + "; needs to be in position " + str(value))
                self.economy_variations[economy] = {'numeric_id': numeric_id}
        # guard against overlapping price factors, which obscures cargos on the payment curves chart
        for cargo in registered_cargos:
            if cargo.price_factor == self.price_factor:
                utils.echo_message("Cargo " + self.id + " has overlapping price_factor with cargo " + cargo.id)
        # guard against overlapping cargo colours, cargo colours are intended to be unique within FIRS
        for cargo in registered_cargos:
            if cargo.cargo_payment_list_colour == self.cargo_payment_list_colour:
                utils.echo_message("Cargo " + self.id + " has overlapping cargo_payment_list_colour with cargo " + cargo.id)
        # guard against overlapping icon indices, icons should be unique per cargo
        # if two cargos use same icon (1) don't, copy-paste, then adjust some pixels for one of them (2) see 1
        for cargo in registered_cargos:
            if cargo.icon_indices == self.icon_indices:
                utils.echo_message("Cargo " + self.id + " has overlapping icon_indices with cargo " + cargo.id)


    def get_numeric_id(self, economy):
        return self.economy_variations[economy].get('numeric_id')

    def get_cargo_label(self):
        # wrap cargo labels in " chars because nml needs them as string literals (we store them - by design - as python strings)
        return '"' + self.cargo_label + '"'

    def get_property(self, property_name, economy):
        # straightforward lookup of a property, doesn't try to handle failure case of property not found; don't look up props that don't exist
        if economy is not None and property_name in self.economy_variations[economy]:
            return self.economy_variations[economy].get(property_name)
        else:
            return getattr(self, property_name)

    def get_property_declaration(self, property_name, economy=None):
        value = self.get_property(property_name, economy)
        return property_name + ': ' + str(value) + ';'

    def register(self):
        if len(self.economy_variations) == 0:
            utils.echo_message(self.id + ' is not used in any economy')
        registered_cargos.append(self)
