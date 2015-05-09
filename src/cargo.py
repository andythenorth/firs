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

import global_constants as global_constants
import utils as utils

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(src_path, 'templates'), format='text')
industry_templates = PageTemplateLoader(os.path.join(src_path, 'industries'), format='text')

economies = global_constants.economies
from cargos import registered_cargos

class Cargo(object):
    """ Base class to hold cargos"""
    def __init__(self, id, **kwargs):
        self.id = id
        self.cargo_label = kwargs['cargo_label']
        self.number = kwargs['number']
        self.type_name = kwargs['type_name']
        self.unit_name = kwargs['unit_name']
        self.type_abbreviation = kwargs['type_abbreviation']
        self.sprite = kwargs['sprite']
        self.weight = kwargs['weight']
        self.station_list_colour = kwargs['station_list_colour']
        self.cargo_payment_list_colour = kwargs['cargo_payment_list_colour']
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
        self.economy_variations = {}
        for economy in economies:
            self.add_economy_variation(economy)
        # icon indices relate to position of icon in cargo icons spritesheet
        self.icon_indices = kwargs['icon_indices']

    def add_economy_variation(self, economy):
        self.economy_variations[economy] = {'disabled': False}

    def get_property(self, property_name, economy):
        # straightforward lookup of a property, doesn't try to handle failure case of property not found; don't look up props that don't exist
        return self.economy_variations[economy].get(property_name)

    def get_property_declaration(self, property_name):
        return property_name + ': ' + getattr(self, property_name) + ';'

    def register(self):
        registered_cargos.append(self)

    def render_pnml(self):
        cargo_template = templates['cargo_props.pypnml']
        templated_pnml = utils.unescape_chameleon_output(cargo_template(cargo=self, economies=economies))
        return templated_pnml
