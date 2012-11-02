"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

import codecs # used for writing files - more unicode friendly than standard open() module

import os.path
currentdir = os.curdir

import global_constants as global_constants

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir,'sprites','nml','templates'), format='text')
industry_templates = PageTemplateLoader(os.path.join(currentdir,'sprites','nml','industries'), format='text')


def unescape_chameleon_output(escaped_nml):
    # chameleon html-escapes some characters; that's sane and secure for chameleon's intended web use, but not wanted for nml
    # there is probably a standard module for unescaping html entities, but this will do for now
    escaped_nml = '>'.join(escaped_nml.split('&gt;'))
    escaped_nml = '<'.join(escaped_nml.split('&lt;'))
    escaped_nml = '&'.join(escaped_nml.split('&amp;'))
    return escaped_nml


class Tile(object):
    """ Base class to hold industry tiles"""
    def __init__(self, id):
        self.id = id

class Sprite(object):
    """Base class to hold simple sprites (using numbers from a base set)"""
    def __init__(self, sprite_number, sprite_number_snow='', xoffset=0, yoffset=0, zoffset=0, xextent=16, yextent=16, zextent=16):
        self.sprite_number = sprite_number # can also provide raw nml with the sprite number for things like controlling animation frame
        self.sprite_number_snow = (sprite_number, sprite_number_snow)[sprite_number_snow!=''] # set a snow sprite explicitly (optional).
        # optional parameters for offsets and extents for the *spritelayout* to use with this sprite (read nml spritelayout docs to see use)
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.zoffset = zoffset # set extents to x/y/z sizes of largest sprite in spriteset, or omit for default (16)
        self.xextent = xextent
        self.yextent = yextent
        self.zextent = zextent

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
    def __init__(self, id, sprites=[], type='', xoffset=0, yoffset=0, zoffset=0, xextent=16, yextent=16, zextent=16, animation_rate = 0, num_sprites_to_autofill = 1):
        self.id = id
        self.sprites = sprites # a list of sprites 6-tuples in format (x, y, w, h, xoffs, yoffs)
        self.type = type # set to ground or other special types, or omit for default (building, greeble, foundations etc - graphics from png named same as industry)
        self.animation_rate = animation_rate # optional multiplier to tile's animation rate, set to 1 for same as tile, >1 for faster; leave default (0) to disable animation
        self.num_sprites_to_autofill = num_sprites_to_autofill # create n sprites per sprite passed (optional convenience method for use where spriteset sizes must match; set value to same as size of largest spriteset)
        # optional parameters for offsets and extents for the *spritelayout* to use with this sprite (read nml spritelayout docs to see use)
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.zoffset = zoffset
        self.xextent = xextent # set extents to x/y/z sizes of largest sprite in spriteset, or omit for default (16)
        self.yextent = yextent
        self.zextent = zextent

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
    def __init__(self, id, default_spritelayout, layout):
        self.id = id
        self.default_spritelayout = default_spritelayout
        self.layout = layout # a list of 4-tuples (SE offset from N tile, SW offset from N tile, tile identifier, identifier of spriteset or next nml switch)

class IndustryProperties(object):
    """Base class to hold properties corresponding to nml industry item properties"""
    def __init__(self, **kwargs):
        # nml item properties, most of these should be provided as strings for insertion into nml.  See nml docs for meaning + acceptable values.
        self.substitute = kwargs.get('substitute', None)
        self.name = kwargs.get('name', None)
        self.nearby_station_name = kwargs.get('nearby_station_name', None)
        self.layouts = kwargs.get('layouts', None) # !! needs to handle automatic layouts when present
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
        self.conflicting_ind_types = kwargs.get('conflicting_ind_types', None)
        self.life_type = kwargs.get('life_type', None)
        self.spec_flags = kwargs.get('spec_flags', None)
        self.fund_cost_multiplier = kwargs.get('fund_cost_multiplier', None)
        self.remove_cost_multiplier = kwargs.get('remove_cost_multiplier', None)



class Industry(object):
    """Base class for all types of industry"""
    def __init__(self, id, **kwargs):
        self.id = id
        self.graphics_file = '"sprites/graphics/industries/' + id + '.png"' # don't use os.path.join here, this is for nml
        self.graphics_file_snow = '"sprites/graphics/industries/' + id + '_snow.png"' # don't use os.path.join here, this is for nml
        self.tiles = []
        self.sprites = []
        self.smoke_sprites = []
        self.spritesets = []
        self.spritelayouts = [] # by convention spritelayout is one word :P
        self.industry_layouts = []
        self.default_industry_properties = IndustryProperties(**kwargs)
        self.economy_variations = {}
        for economy in global_constants.economies:
            self.add_economy_variation(economy)

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

    def add_economy_variation(self, economy, disabled=False, **kwargs):
        self.economy_variations[economy] = {'disabled':disabled, 'industry_properties': IndustryProperties(**kwargs)}

    def get_numeric_id(self):
        return global_constants.industry_numeric_ids[self.id]

    def get_spritesets(self):
        template = templates['spritesets.pynml']
        return unescape_chameleon_output(template(industry=self))

    def get_spritelayouts(self):
        template = templates['spritelayouts.pynml']
        return unescape_chameleon_output(template(industry=self))

    def get_industry_layouts_as_tilelayouts(self):
        template = templates['industry_layout_tilelayouts.pynml']
        return unescape_chameleon_output(template(industry=self))

    def get_industry_layouts_as_property(self):
        template = templates['industry_layout_property.pynml']
        return unescape_chameleon_output(template(industry=self))

    def get_industry_layouts_as_graphic_switches(self):
        template = templates['industry_layout_graphics_switches.pynml']
        return unescape_chameleon_output(template(industry=self))

    def get_fence_switches(self):
        template = templates['fence_switches.pynml']
        return unescape_chameleon_output(template(industry=self))

    def get_industry_properties(self):
        template = templates['industry_properties.pynml']
        return unescape_chameleon_output(template(industry=self, global_constants=global_constants))

    def get_conditional_expressions_for_enabled_economies(self):
        return "param[0]==1 || param[0]==2"

    def unpack_sprite_or_spriteset(self, sprite_or_spriteset, terrain_type=''):
        if terrain_type != '':
            suffix = '_' + terrain_type
        else:
            suffix = ''
        if isinstance(sprite_or_spriteset, Spriteset):
            return sprite_or_spriteset.id + suffix  + '(' + str(sprite_or_spriteset.animation_rate) + '* animation_frame)'
        if isinstance(sprite_or_spriteset, Sprite):
            return getattr(sprite_or_spriteset, 'sprite_number' + suffix)

    def render_and_save_pnml(self):
        industry_template = industry_templates[self.id + '.pypnml']
        templated_pnml = unescape_chameleon_output(industry_template(industry=self))

        # save the results of templating
        pnml = codecs.open(os.path.join(currentdir,'sprites','nml','generated_pnml', self.id + '.pnml'), 'w','utf8')
        pnml.write(templated_pnml)
        pnml.close()


