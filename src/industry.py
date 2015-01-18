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

from industries import registered_industries

class Tile(object):
    """ Base class to hold industry tiles"""
    def __init__(self, id):
        self.id = id

class Sprite(object):
    """Base class to hold simple sprites (using numbers from a base set)"""
    def __init__(self, sprite_number, sprite_number_snow='', xoffset=0, yoffset=0, zoffset=0, xextent=16, yextent=16, zextent=16, always_draw=0):
        self.sprite_number = sprite_number # can also provide raw nml with the sprite number for things like controlling animation frame
        self.sprite_number_snow = (sprite_number, sprite_number_snow)[sprite_number_snow!=''] # set a snow sprite explicitly (optional).
        # optional parameters for offsets and extents for the *spritelayout* to use with this sprite (read nml spritelayout docs to see use)
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.zoffset = zoffset # set extents to x/y/z sizes of largest sprite in spriteset, or omit for default (16)
        self.xextent = xextent
        self.yextent = yextent
        self.zextent = zextent
        self.always_draw = always_draw

class SmokeSprite(object):
    """Base class to handle smoke sprites (using smoke sprite numbers from a base set)"""
    def __init__(self, smoke_type, xoffset=0, yoffset=0, zoffset=0, hide_sprite=0, animation_frame_offset=0):
        # animation_frame_offset can be used to desynchronise animations in the same tile (or in some cases within the same industry as an alternative to animation triggers)
        # defaults
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.zoffset = zoffset
        self.xextent = 16
        self.yextent = 16
        self.zextent = 16
        self.hide_sprite = hide_sprite
        if smoke_type == 'dark_smoke_small':
            self.sprite_number = '2040 + (animation_frame / 4)'
            self.zoffset = str(self.zoffset) + '+ animation_frame'
            self.xextent = 11
            self.zextent = 7
            self.hide_sprite = 'animation_frame > 19'
        if smoke_type == 'white_smoke_small':
            self.sprite_number = '3079 + (animation_frame / 4)'
            self.zoffset = str(self.zoffset) + '+ animation_frame'
            self.xextent = 11
            self.zextent = 7
            self.hide_sprite = 'animation_frame > 19'
        if smoke_type == 'white_smoke_big':
            self.sprite_number = '3701 + ((animation_frame + ' + str(animation_frame_offset) + ')%8)'
            self.xextent = 15
            self.yextent = 7
            self.zextent = 7


class Spriteset(object):
    """Base class to hold industry spritesets"""
    # !! arguably this should be two different classes, one for building/feature spritesets, and one for ground spritesets
    def __init__(self, id, sprites=[], type='', xoffset=0, yoffset=0, zoffset=0, xextent=16, yextent=16,
                 zextent=16, animation_rate = 0, always_draw=0, num_sprites_to_autofill = 1):
        self.id = id
        self.sprites = sprites # a list of sprites 6-tuples in format (x, y, w, h, xoffs, yoffs)
        self.type = type # set to ground or other special types, or omit for default (building, greeble, foundations etc - graphics from png named same as industry)
        self.animation_rate = animation_rate # (must be int) optional multiplier to tile's animation rate, set to 1 for same as tile, >1 for faster; leave default (0) to disable animation; < 1 isn't valid and nml won't compile it
        self.num_sprites_to_autofill = num_sprites_to_autofill # create n sprites per sprite passed (optional convenience method for use where spriteset sizes must match; set value to same as size of largest spriteset)
        # optional parameters for offsets and extents for the *spritelayout* to use with this sprite (read nml spritelayout docs to see use)
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.zoffset = zoffset
        self.xextent = xextent # set extents to x/y/z sizes of largest sprite in spriteset, or omit for default (16)
        self.yextent = yextent
        self.zextent = zextent
        self.always_draw = always_draw

    def get_ground_tile_x_start(self, type):
        return {'mud': 0, 'concrete': 80, 'cobble': 150, 'snow': 220, 'slab': 290, 'empty':360}[type]


class SpriteLayout(object):
    """Base class to hold spritelayouts for industry spritelayouts"""
    def __init__(self, id, ground_sprite, ground_overlay, building_sprites, smoke_sprites=[], fences=[]):
        self.id = id
        self.ground_sprite = ground_sprite
        self.ground_overlay = ground_overlay
        self.building_sprites = building_sprites
        self.smoke_sprites = smoke_sprites
        self.fences = fences # a simple list of keywords.  Valid values: 'ne', 'se', 'sw', 'nw'.  Order is arbitrary.


class IndustryLayout(object):
    """Base class to hold industry layouts"""
    def __init__(self, id, layout):
        self.id = id
        self.layout = layout # a list of 4-tuples (SE offset from N tile, SW offset from N tile, tile identifier, identifier of spriteset or next nml switch)

class IndustryProperties(object):
    """Base class to hold properties corresponding to nml industry item properties"""
    def __init__(self, **kwargs):
        # nml item properties, most of these should be provided as strings for insertion into nml.  See nml docs for meaning + acceptable values.
        self.substitute = kwargs.get('substitute', None)
        self.override = kwargs.get('override', None)
        self.name = kwargs.get('name', None)
        self.nearby_station_name = kwargs.get('nearby_station_name', None)
        self.layouts = kwargs.get('layouts', None) # !! automatic layout handling can be specified for this using 'AUTO' as the value
        self.accept_cargo_types = kwargs.get('accept_cargo_types', None)
        self.prod_cargo_types = kwargs.get('prod_cargo_types', None)
        self.prod_multiplier = kwargs.get('prod_multiplier', None)
        self.min_cargo_distr = kwargs.get('min_cargo_distr', None)
        self.input_multiplier_1 = kwargs.get('input_multiplier_1', None)
        self.input_multiplier_2 = kwargs.get('input_multiplier_2', None)
        self.input_multiplier_3 = kwargs.get('input_multiplier_3', None)
        self.prod_increase_msg = kwargs.get('prod_increase_msg', None)
        self.prod_decrease_msg = kwargs.get('prod_decrease_msg', None)
        self.new_ind_msg = kwargs.get('new_ind_msg', None)
        self.closure_msg = kwargs.get('closure_msg', None)
        self.prob_in_game = kwargs.get('prob_in_game', None)
        self.prob_random = kwargs.get('prob_random', None)
        self.prospect_chance = kwargs.get('prospect_chance', None)
        self.map_colour = kwargs.get('map_colour', None)
        self.life_type = kwargs.get('life_type', None)
        self.spec_flags = kwargs.get('spec_flags', '0')
        self.fund_cost_multiplier = kwargs.get('fund_cost_multiplier', None)
        self.remove_cost_multiplier = kwargs.get('remove_cost_multiplier', None)
        # not nml properties
        self.enabled = kwargs.get('enabled', False)
        self.override_default_construction_states = kwargs.get('override_default_construction_states', False)
        self.extra_text_industry = kwargs.get('extra_text_industry', None) # value is string(s) to return for corresponding nml cb, use 'STR_GENERIC_NEWLINE' in default property declaration if no string needed
        # nml properties we want to prevent being set for one reason or another
        if 'conflicting_ind_types' in kwargs:
            raise Exception("Don't set conflicting_ind_types property; use the FIRS location checks for conflicting industry (these are more flexible).")



class Industry(object):
    """Base class for all types of industry"""
    def __init__(self, id, graphics_change_dates=[], **kwargs):
        self.id = id
        self.graphics_change_dates = graphics_change_dates # 0-based, ordered list of dates for which graphics should change, match to graphics suffixed _1, _2, _3 etc.
        self.tiles = []
        self.sprites = []
        self.smoke_sprites = []
        self.spritesets = []
        self.spritelayouts = [] # by convention spritelayout is one word :P
        self.industry_layouts = []
        self.default_industry_properties = IndustryProperties(**kwargs)
        self.supply_requirements = kwargs.get('supply_requirements', self.set_supply_requirements_via_magic())
        self.economy_variations = {}
        for economy in global_constants.economies:
            self.add_economy_variation(economy)
        self.register()

    def register(self):
        registered_industries.append(self)

    def add_tile(self, *args, **kwargs):
        new_tile = Tile(*args, **kwargs)
        self.tiles.append(new_tile)
        return new_tile

    def add_sprite(self, *args, **kwargs):
        new_sprite = Sprite(*args, **kwargs)
        self.sprites.append(new_sprite)
        return new_sprite # returning the new obj isn't essential, but permits the caller giving it a reference for use elsewhere

    def add_smoke_sprite(self, *args, **kwargs):
        new_smoke_sprite = SmokeSprite(*args, **kwargs)
        self.smoke_sprites.append(new_smoke_sprite)
        return new_smoke_sprite # returning the new obj isn't essential, but permits the caller giving it a reference for use elsewhere

    def add_spriteset(self, *args, **kwargs):
        new_spriteset = Spriteset(*args, **kwargs)
        self.spritesets.append(new_spriteset)
        return new_spriteset # returning the new obj isn't essential, but permits the caller giving it a reference for use elsewhere

    def add_spritelayout(self, *args, **kwargs):
        new_spritelayout = SpriteLayout(*args, **kwargs)
        self.spritelayouts.append(new_spritelayout)
        return new_spritelayout # returning the new obj isn't essential, but permits the caller giving it a reference for use elsewhere

    def add_industry_layout(self, *args, **kwargs):
        new_industry_layout = IndustryLayout(*args, **kwargs)
        self.industry_layouts.append(new_industry_layout)
        return new_industry_layout # returning the new obj isn't essential, but permits the caller giving it a reference for use elsewhere

    def add_economy_variation(self, economy):
        self.economy_variations[economy] = IndustryProperties()

    def set_supply_requirements_via_magic(self):
        if 'ENSP' in self.default_industry_properties.accept_cargo_types:
            return global_constants.supply_requirements['ENSP']
        elif 'FMSP' in self.default_industry_properties.accept_cargo_types:
            return global_constants.supply_requirements['FMSP']
        else:
            return None

    def get_numeric_id(self):
        return global_constants.industry_numeric_ids[self.id]

    def get_graphics_file_path(self, date_variation_num=None, terrain='', construction_state_num=None):
         # don't use os.path.join here, this returns a string for use by nml
        if construction_state_num != None:
            return '"src/graphics/industries/' + self.id + '_construction_' + str(construction_state_num+1) + '.png"'
        else:
            return '"src/graphics/industries/' + self.id + '_' + str(date_variation_num + 1) + terrain + '.png"'

    def get_switch_name_for_construction_states(self):
        # industries use the default construction sprites (shared), or their own handled by automagic spritesets / spritelayouts (graphics in spritesheets with same layout as industry)
        if self.default_industry_properties.override_default_construction_states == True:
            return self.id + '_industry_graphics_switch_layouts'
        else:
            return 'spritelayout_default_construction_states'

    def get_date_conditions_for_hide_sprites(self, date_variation_index):
        random_offset = "5 * LOAD_TEMP(0) / 0x10000" # random is in nml at run-time, not compile-time python, so this is a string
        if len(self.graphics_change_dates) == 0:
            return "" # no date variations, just one set of graphics
        elif date_variation_index == 0:
            return "|| (current_year + " + random_offset + ") >= " + str(self.graphics_change_dates[date_variation_index]) # first set of graphics, hide after first change date
        elif date_variation_index == len(self.graphics_change_dates):
            return "|| (current_year + " + random_offset + ") < " + str(self.graphics_change_dates[date_variation_index - 1]) # last set of graphics, hide before last change date
        else:
            return "|| (current_year + " + random_offset + ") < " + str(self.graphics_change_dates[date_variation_index - 1]) + " || (current_year + " + random_offset + ") >= " + str(self.graphics_change_dates[date_variation_index])

    def get_spritesets(self):
        template = templates['spritesets.pynml']
        return utils.unescape_chameleon_output(template(industry=self))

    def get_spritelayouts(self):
        template = templates['spritelayouts.pynml']
        return utils.unescape_chameleon_output(template(industry=self))

    def get_industry_layouts_as_tilelayouts(self):
        template = templates['industry_layout_tilelayouts.pynml']
        return utils.unescape_chameleon_output(template(industry=self))

    def get_industry_layouts_as_property(self):
        # supports auto-magic layouts from layout objects, or layouts simply declared as a string for nml
        # or no layout declaration if over-riding a default industry
        if self.default_industry_properties.layouts == 'AUTO':
            template = templates['industry_layout_property.pynml'] # automagic case
            return 'layouts: ' + utils.unescape_chameleon_output(template(industry=self))
        elif self.default_industry_properties.layouts != None:
            return 'layouts: ' + self.default_industry_properties.layouts + ';' # simple case
        else:
            return

    def get_industry_layouts_as_graphic_switches(self):
        template = templates['industry_layout_graphics_switches.pynml']
        return utils.unescape_chameleon_output(template(industry=self))

    def get_fence_switches(self):
        template = templates['fence_switches.pynml']
        return utils.unescape_chameleon_output(template(industry=self))

    def get_primary_supplies_stuff(self):
        template = templates['primary_supplies_stuff.pynml']
        return utils.unescape_chameleon_output(template(industry=self))

    def get_industry_properties(self):
        template = templates['industry_properties.pynml']
        return utils.unescape_chameleon_output(template(industry=self, global_constants=global_constants))

    def get_extra_text_secondary(self):
        template = templates['extra_text_secondary.pynml']
        return utils.unescape_chameleon_output(template(industry=self, global_constants=global_constants))

    def get_property(self, property_name, economy):
        # does magic to get the property from the defaults if not set
        # that enables economies to over-ride selected properties and not bother setting others
        # doesn't try to handle failure case of property not found at all: don't look up props that don't exist
        default_value = getattr(self.default_industry_properties, property_name)
        if economy is None:
            value = default_value
        else:
            economy_value = getattr(self.economy_variations[economy], property_name)
            if economy_value is not None:
                value = economy_value
            else:
                value = default_value
        return value

    def get_property_declaration(self, property_name, economy=None):
        value = self.get_property(property_name, economy)
        # we don't want to render empty properties for nml
        if value == None or value == '':
            return
        else:
            return property_name + ': ' + value + ';'

    def cargo_list_sugar_magic(self, cargo_list, economy, climate):
        # magic to deal with special cases in cargo lists - clean up the list returned to templates etc
        # SGBT + SGCN should both be defined when accepted or produced, they are climate sensitive
        if climate == "CLIMATE_TROPIC":
            cargo_list = ["SGCN" if cargo=="SGBT" else cargo for cargo in cargo_list]
        if climate != "CLIMATE_TROPIC":
            cargo_list = ["SGBT" if cargo=="SGCN" else cargo for cargo in cargo_list]
        if cargo_list.count("SGCN") > 1 or cargo_list.count("SGBT") > 1:
            utils.echo_message("Too much SGBT or SGCN for " + self.id + ' in economy ' + economy)
        return cargo_list

    def get_accept_cargo_types(self, economy, climate):
        accept_cargo_types = self.get_property('accept_cargo_types', economy)
        accept_cargo_types = self.cargo_list_sugar_magic(accept_cargo_types, economy, climate)
        # guard against too many cargos being defined
        if len(accept_cargo_types) > 3:
            utils.echo_message("Too many accepted cargos defined for " + self.id + ' in economy ' + economy)
        return '[' + ','.join(accept_cargo_types) + ']'

    def get_prod_cargo_types(self, economy, climate):
        # ! don't call this when rendering docs, the sugar magic causes unwanted results
        prod_cargo_types = self.get_property('prod_cargo_types', economy)
        prod_cargo_types = self.cargo_list_sugar_magic(prod_cargo_types, economy, climate) # pass the cargos through horrid magic
        # guard against too many cargos being defined
        if len(prod_cargo_types) > 2:
            utils.echo_message("Too many produced cargos defined for " + self.id + ' in economy ' + economy)
        return '[' + ','.join(prod_cargo_types) + ']'

    def get_another_industry(self, id):
        for industry in registered_industries:
            if industry.id == id:
                return industry
        # if none found, that's an error, don't handle the error, just blow up

    def get_conditional_expressions_for_enabled_economies(self):
        # returns a string that can be used as the conditions in nml if() blocks for economy stuff
        enabled_economies = []
        for i, economy in enumerate(global_constants.economies):
            if self.economy_variations[economy].enabled:
                enabled_economies.append('economy==' + str(i))
        return ' || '.join(enabled_economies)

    def unpack_sprite_or_spriteset(self, sprite_or_spriteset, construction_state_num=3, terrain_type='', date_variation_num='0'):
        date_variation_suffix = '_' + str(date_variation_num)
        if terrain_type != '':
            suffix = '_' + terrain_type
        else:
            suffix = ''
        if isinstance(sprite_or_spriteset, Spriteset):
            if construction_state_num == 3 or self.default_industry_properties.override_default_construction_states == False:
                return sprite_or_spriteset.id + date_variation_suffix + suffix  + '(' + str(sprite_or_spriteset.animation_rate) + '* animation_frame)'
            else:
                return sprite_or_spriteset.id + '_spriteset_default_construction_state_' + str(construction_state_num) + '(' + str(sprite_or_spriteset.animation_rate) + '* animation_frame)'
        if isinstance(sprite_or_spriteset, Sprite):
            return getattr(sprite_or_spriteset, 'sprite_number' + suffix)

    def render_pnml(self):
        industry_template = industry_templates[self.id + '.pypnml']
        templated_pnml = utils.unescape_chameleon_output(industry_template(industry=self, global_constants=global_constants, utils=utils))
        return templated_pnml

