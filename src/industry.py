"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from collections import deque

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

from economies import registered_economies
from industries import registered_industries

def get_another_industry(id):
    # utility function so that we can provide numeric ids in nml output, rather than relying identifiers
    # this enables compiling single-industries without nml barfing on missing identifiers (in location checks and such)
    for industry in registered_industries:
        if industry.id == id:
            return industry
    # if none found, that's an error, don't handle the error, just blow up


class Tile(object):
    """ Base class to hold industry tiles"""
    def __init__(self, industry_id, id, **kwargs):
        self.id = id
        self.numeric_id = global_constants.tile_numeric_ids.get(self.id, None) # use of get() here is temporary during migrations, not needed otherwise
        self.land_shape_flags = kwargs.get('land_shape_flags', '0')
        self.location_checks = kwargs.get('location_checks')
        # check for setting both land_shape_flags and location_checks
        # it's a cause of coder-error when I forget that land_shape_flags will be ignored when location_check is used
        # 'janky_industry_id_string' because an industry ID is needed, and I don't trivially have one here
        if self.land_shape_flags is not '0' and len(self.location_checks.get_render_tree(self.id, industry_id)) > 0:
            raise Exception("Tile " + self.id + ": land_shape_flags are set but will be ignored because the tile also uses location_checks cb.  Only set one of these attributes.")

        self.foundations = kwargs.get('foundations', None)
        # animation length (int), looping (bool), speed (int) should be set for all animations
        # basic tile animation plays consecutive-frames from the spriteset
        # spriteset can offset frames when multiple animations are used *on the same* tile (to avoid odd-looking sync effects)
        # for extended control, the anim_control cb is used, e.g.
        # - start/stop animation on conditions
        # - play non-consecutive frames
        # - de-sync animation for tiles that are repeated in an industry layout
        # switches for this are provided as macros defined in animation_macros.pynml
        # tiles should then set custom_anim_control={'macro':[MACRO NAME], 'triggers': 'bitmask([TRIGGERS])'}
        # generally macros are shared across industries, because animation has common cases
        # industry-specific macros are ok if really required
        self.animation_length = kwargs.get('animation_length', 1) # allowed values 1-253
        self.animation_looping = kwargs.get('animation_looping', False)
        self.animation_speed = kwargs.get('animation_speed', 0)
        self.custom_animation_control = kwargs.get('custom_animation_control', None)

    def get_expression_for_tile_acceptance(self, industry, economy):
        result = []
        accept_cargo_types = industry.get_property('accept_cargo_types', economy)
        for cargo in accept_cargo_types:
            result.append('[' + cargo + ', 8]')
        return ','.join(result)

    def get_animation_triggers(self):
        if self.custom_animation_control is None:
            return 'bitmask()'
        else:
            return self.custom_animation_control['animation_triggers']

    def animation_macros(self):
        template = templates["animation_macros.pynml"]
        return template.macros


class TileLocationChecks(object):
    """ Class to hold location checks for a tile """
    def __init__(self, **kwargs):
        self.always_allow_founder = kwargs.get('always_allow_founder', True) # occasionally this needs to be set False, e.g. for tiles that demand specific land shape
        self.disallow_slopes = kwargs.get('disallow_slopes', False)
        self.disallow_steep_slopes = kwargs.get('disallow_steep_slopes', False)
        self.disallow_industry_adjacent = kwargs.get('disallow_industry_adjacent', False)
        self.require_houses_nearby = kwargs.get('require_houses_nearby', False)
        self.require_road_adjacent = kwargs.get('require_road_adjacent', []) # any of ['nw', 'ne', 'se', 'nw']
        self.require_coast = kwargs.get('require_coast', False)
        self.disallow_above_snowline = kwargs.get('disallow_above_snowline', False)
        self.disallow_desert = kwargs.get('disallow_desert', False)
        self.disallow_coast = kwargs.get('disallow_coast', False)

    def get_render_tree(self, tile_id, industry_id):
        switch_prefix = tile_id + '_lc_'
        result = deque([])

        if self.always_allow_founder:
            result.appendleft(TileLocationCheckFounder())

        if self.disallow_slopes:
            result.appendleft(TileLocationCheckDisallowSlopes())

        if self.disallow_steep_slopes:
            result.appendleft(TileLocationCheckDisallowSteepSlopes())

        if self.disallow_industry_adjacent:
            result.append(TileLocationCheckDisallowIndustryAdjacent())

        if self.require_coast:
            result.append(TileLocationCheckRequireSea())
            result.append(TileLocationCheckRequireSlope())

        if self.require_houses_nearby:
            # !! possibly could be done simpler with a town zone check instead of a tile search
            # but didn't want to unpick CPP templating as part of snakebite
            search_points = [(0, 3), (3, 0), (0, -3), (-3, 0), (2, 2), (2, -2), (-2, 2), (3, 3),
                             (3, -3), (-3, 3), (-3, -3), (4, 4), (4, -4), (-4, 4), (-4, 4)]
            for search_offsets in search_points:
                result.append(TileLocationCheckRequireHousesNearby(search_offsets))

        for direction in self.require_road_adjacent:
            result.append(TileLocationCheckRequireRoadAdjacent(direction))

        if self.disallow_above_snowline:
            result.appendleft(TileLocationCheckDisallowAboveSnowline())

        if self.disallow_desert:
            result.appendleft(TileLocationCheckDisallowDesert())

        if self.disallow_coast:
            result.appendleft(TileLocationCheckDisallowCoast())

        # walk the tree, setting entry points and results (id of next switch) for each switch
        for count, lc in enumerate(result):
            lc.switch_entry_point = switch_prefix + str(count)
            # don't set the result for the last item - use the check's default allow/disallow value
            if count < len(result) - 1:
                # nasty hack with industry id due to not wanting to disturb CPP templating until snakebite is done
                lc.switch_result = industry_id + '_' + switch_prefix + str(count + 1)

        return list(reversed(result))


class TileLocationCheckDisallowSlopes(object):
    """ Prevent building on all slopes """
    def __init__(self):
        self.switch_result = None # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None

    def render(self):
        return 'TILE_DISALLOW_SLOPES(' + self.switch_entry_point + ', CB_RESULT_LOCATION_DISALLOW,' + self.switch_result + ')'


class TileLocationCheckDisallowSteepSlopes(object):
    """ Prevent building on steep slopes (but not normal slopes) """
    def __init__(self):
        self.switch_result = None # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None

    def render(self):
        return 'TILE_DISALLOW_STEEP_SLOPE(' + self.switch_entry_point + ', string(STR_ERR_LOCATION_NOT_ON_STEEP_SLOPE),' + self.switch_result + ')'


class TileLocationCheckDisallowIndustryAdjacent(object):
    """
        Prevent directly adjacent to another industry, used by most industries, but not all
        1. Makes it too hard for the game to find a location for some types (typically large flat industries)
        2. Not necessary for most town industries
    """
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = None

    def render(self):
        return 'TILE_DISALLOW_NEARBY_CLASS(' + self.switch_entry_point + ', TILE_CLASS_INDUSTRY, CB_RESULT_LOCATION_DISALLOW,' + self.switch_result + ')'


class TileLocationCheckRequireHousesNearby(object):
    """ Requires houses at offset x, y (to be fed by circular tile search) """
    def __init__(self, search_offsets):
        self.search_offsets = search_offsets
        self.switch_result = 'return CB_RESULT_LOCATION_DISALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = None

    def render(self):
        return 'CHECK_HOUSES_NEARBY(' + self.switch_entry_point + ',' + ','.join(str(i) for i in self.search_offsets) + ',' + self.switch_result + ')'


class TileLocationCheckRequireRoadAdjacent(object):
    """ Requires road on adjacent tile(s), with configurable directions """
    def __init__(self, direction):
        self.direction_map = {'nw': (0, -1), 'se': (0, 1), 'ne': (-1, 0), 'sw': (1, 0)}
        self.direction = direction
        self.switch_result = 'return CB_RESULT_LOCATION_DISALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = None

    def render(self):
        x_y_string = ','.join([str(offset) for offset in self.direction_map[self.direction]])
        return 'CHECK_ROAD_ADJACENT(' + self.switch_entry_point + ', ' + x_y_string + ',' + self.switch_result + ')'


class TileLocationCheckRequireSea(object):
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = None

    def render(self):
        return 'TILE_REQUIRE_SEA(' + self.switch_entry_point + ', ' + self.switch_result + ')'


class TileLocationCheckRequireSlope(object):
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = None

    def render(self):
        return 'TILE_CHECK_FLAT(' + self.switch_entry_point + ', return CB_RESULT_LOCATION_DISALLOW, ' + self.switch_result + ')'


class TileLocationCheckDisallowDesert(object):
    """ Prevent building on desert tiles """
    def __init__(self):
        self.switch_result = None # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None

    def render(self):
        return 'TILE_DISALLOW_TERRAIN(' + self.switch_entry_point + ',TILETYPE_DESERT, CB_RESULT_LOCATION_DISALLOW, ' + self.switch_result + ')'


class TileLocationCheckDisallowCoast(object):
    """ Prevent building on desert tiles """
    def __init__(self):
        self.switch_result = None # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None

    def render(self):
        return 'TILE_DISALLOW_COAST('  + self.switch_entry_point + ', CB_RESULT_LOCATION_DISALLOW, ' + self.switch_result + ')'


class TileLocationCheckDisallowAboveSnowline(object):
    """ Prevent building above snowline """
    def __init__(self):
        self.switch_result = None # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None

    def render(self):
        return 'TILE_CHECK_HEIGHT(' + self.switch_entry_point + ', 0, snowline_height, ' + self.switch_result + ', return string(STR_ERR_LOCATION_NOT_ABOVE_SNOWLINE))'


class TileLocationCheckFounder(object):
    """
        Used to over-ride non-essential checks when player is building
        Some tile checks relating to landscape are essential and are placed before player check
    """
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = None

    def render(self):
        return 'TILE_ALLOW_PLAYER (' + self.switch_entry_point + ',' + self.switch_result + ')'


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
    """ Base class to handle smoke sprites (using smoke sprite numbers from a base set) """
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
    """ Base class to hold industry spritesets """
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
    """ Base class to hold spritelayouts for industry spritelayouts """
    def __init__(self, id, ground_sprite, ground_overlay, building_sprites, smoke_sprites=[], fences=[], terrain_aware_ground=False):
        self.id = id
        self.ground_sprite = ground_sprite
        self.ground_overlay = ground_overlay
        self.building_sprites = building_sprites
        self.smoke_sprites = smoke_sprites
        self.fences = fences # a simple list of keywords.  Valid values: 'ne', 'se', 'sw', 'nw'.  Order is arbitrary.
        self.terrain_aware_ground = terrain_aware_ground # we don't draw terrain (and climate) aware ground unless explicitly required by the spritelayout, it makes nml compiles slower

class IndustryLayout(object):
    """ Base class to hold industry layouts """
    def __init__(self, id, layout):
        self.id = id
        self.layout = layout # a list of 4-tuples (SE offset from N tile, SW offset from N tile, tile identifier, identifier of spriteset or next nml switch)


class IndustryLocationChecks(object):
    """ Class to hold location checks for an industry """
    def __init__(self, **kwargs):
        self.incompatible = kwargs.get('incompatible', {})
        self.town_distance = kwargs.get('town_distance', None)
        self.coast_distance = kwargs.get('coast_distance', None)
        self.require_cluster = kwargs.get('require_cluster', None)
        # this is custom to grain mill, can be made generic if needed
        self.grain_mill_layouts_by_date = kwargs.get('grain_mill_layouts_by_date', None)

    def get_render_tree(self, switch_prefix):
        # this could be reimplemented to just use numeric switch suffixes, as per tile location check tree
        result = deque([IndustryLocationCheckFounder()])
        if self.require_cluster:
            result.append(IndustryLocationCheckRequireCluster(self.require_cluster))
        if self.town_distance:
            result.append(IndustryLocationCheckTownDistance(self.town_distance))
        if self.coast_distance:
            result.append(IndustryLocationCheckCoastDistance())
        if self.grain_mill_layouts_by_date:
            result.appendleft(IndustryLocationCheckGrainMillLayoutsByDate())
        for industry_type, distance in self.incompatible.items():
            result.append(IndustryLocationCheckIncompatible(industry_type, distance))
        prev = None
        for lc in reversed(result):
            lc.switch_entry_point = switch_prefix + lc.switch_entry_point
            if prev is not None:
                lc.switch_result = prev.switch_entry_point
            prev = lc
        result[0].switch_entry_point = switch_prefix + 'check_location'
        return list(reversed(result))


class IndustryLocationCheckTownDistance(object):
    """ Require location within min, max distance of a town """
    def __init__(self, town_distance):
        self.min_distance = town_distance[0]
        self.max_distance = town_distance[1]
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = 'town_distance'

    def render(self, **kwargs):
        return 'CHECK_TOWN_DISTANCE (' + self.switch_entry_point + ', ' + str(self.min_distance) + ',' + str(self.max_distance) + ',' + self.switch_result + ')'


class IndustryLocationCheckRequireCluster(object):
    """ Require industries to locate in n clusters """
    def __init__(self, require_cluster):
        self.industry_type = require_cluster[0]
        # use the numeric_id so that we can do single-industry compiles without nml barfing on missing identifiers
        self.industry_type_numeric_id = get_another_industry(self.industry_type).get_numeric_id()
        self.arbitrary_numbers = require_cluster[1] # not really arbitrary, I'm just being pissy because I don't know what div/mult do
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = str(self.industry_type_numeric_id)

    def render(self, **kwargs):
        return 'CHECK_NEARBY_CLUSTER(' + self.switch_entry_point + ', ' + str(self.industry_type_numeric_id) + ', ' +  ','.join([str(i) for i in self.arbitrary_numbers]) + ',' + 'return CB_RESULT_LOCATION_DISALLOW,' + self.switch_result + ')'


class IndustryLocationCheckIncompatible(object):
    """ Prevent locating near incompatible industry types """
    def __init__(self, industry_type, distance):
        self.industry_type = industry_type
        # use the numeric_id so that we can do single-industry compiles without nml barfing on missing identifiers
        self.industry_type_numeric_id = get_another_industry(industry_type).get_numeric_id()
        self.distance = distance
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = str(self.industry_type_numeric_id)

    def render(self, **kwargs):
        return 'CHECK_INCOMPATIBLE(' + self.switch_entry_point + ', ' + str(self.industry_type_numeric_id) + ', ' + str(self.distance) + ', CB_RESULT_LOCATION_DISALLOW, ' + self.switch_result + ')'


class IndustryLocationCheckFounder(object):
    """ Ensures player can build irrespective of _industry_ location checks (tile checks still apply) """
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = 'check_founder'

    def render(self, **kwargs):
        return 'CHECK_FOUNDER (' + self.switch_entry_point + ',' + self.switch_result + ')'


class IndustryLocationCheckCoastDistance(object):
    """ Maximum distance to coast (player can vary this with parameter) """
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = 'coast_distance'

    def render(self, industry):
        return 'CHECK_COAST_DISTANCE(' + self.switch_entry_point + ', 0, param_max_coastal_distance, CB_RESULT_LOCATION_DISALLOW,' + self.switch_result + ')'


class IndustryLocationCheckGrainMillLayoutsByDate(object):
    """ Custom check for Grain mill, layouts are restricted by date; this is a one-off, but could be made generic if needed """
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = 'check_date'

    def render(self, **kwargs):
        template = templates["industry_location_macros.pynml"]
        return template(conditions=['grain_mill_layouts_by_date'],
                        switch_result=self.switch_result,
                        switch_entry_point=self.switch_entry_point,
                        industry=kwargs['industry'])


class IndustryProperties(object):
    """ Base class to hold properties corresponding to nml industry item properties """
    def __init__(self, **kwargs):
        # nml item properties, most of these should be provided as strings for insertion into nml.  See nml docs for meaning + acceptable values.
        self.substitute = kwargs.get('substitute', None)
        self.override = kwargs.get('override', None)
        self.name = kwargs.get('name', None)
        self.nearby_station_name = kwargs.get('nearby_station_name', None)
        self.layouts = kwargs.get('layouts', None) # automatic layout handling can be specified for this using 'AUTO' as the value
        self.accept_cargo_types = kwargs.get('accept_cargo_types', None)
        self.prod_cargo_types = kwargs.get('prod_cargo_types', None)
        self.prod_multiplier = kwargs.get('prod_multiplier', None)
        self.min_cargo_distr = kwargs.get('min_cargo_distr', None)
        #  input multipliers must be explicitly 0 unless set, don't rely on sensible defaults
        self.input_multiplier_1 = kwargs.get('input_multiplier_1', '[0, 0]')
        self.input_multiplier_2 = kwargs.get('input_multiplier_2', '[0, 0]')
        self.input_multiplier_3 = kwargs.get('input_multiplier_3', '[0, 0]')
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
        self.extra_text_industry = kwargs.get('extra_text_industry', None) # value is string(s) to return for corresponding nml cb
        self.extra_text_fund = kwargs.get('extra_text_fund', None)
        # nml properties we want to prevent being set for one reason or another
        if 'conflicting_ind_types' in kwargs:
            raise Exception("Don't set conflicting_ind_types property; use the FIRS location checks for conflicting industry (these are more flexible).")


class Industry(object):
    """ Base class for all types of industry """
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
        self.location_checks = kwargs.get('location_checks')
        self.intro_year = kwargs.get('intro_year', 0) # ! possibly should be variable by economy?
        self.expiry_year = kwargs.get('expiry_year', global_constants.max_game_date) #  ! possibly should be variable by economy?
        self.economy_variations = {}
        for economy in registered_economies:
            self.add_economy_variation(economy)
        self.template = kwargs.get('template', None) # template will be set by subcass, and/or by individual industry instances

    def register(self):
        registered_industries.append(self)

    def add_tile(self, *args, **kwargs):
        new_tile = Tile(self.id, *args, **kwargs)
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
        self.economy_variations[economy.id] = IndustryProperties()

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

    def get_industry_layouts_as_property(self):
        # supports auto-magic layouts from layout objects, or layouts simply declared as a string for nml
        # or no layout declaration if over-riding a default industry
        if self.default_industry_properties.layouts == 'AUTO':
            # automagic case
            result = [industry_layout.id + '_tilelayout' for industry_layout in self.industry_layouts]
            return 'layouts: [' + ','.join(result) + '];'
        elif self.default_industry_properties.layouts != None:
            return 'layouts: ' + self.default_industry_properties.layouts + ';' # simple case
        else:
            return

    def get_extra_text_fund(self, economy):
        # some fund text options are orthogonal, there is no support for combining them currently
        # support for combined fund text could be added, it's just a substr tree eh?
        result = [] # use a list, because I want to warn if industry tries to set more than one result
        if self.intro_year != 0:
            result.append('string(STR_FUND_AVAILABLE_FROM, ' + str(self.intro_year) + ')')
        if self.expiry_year != global_constants.max_game_date:
            result.append('string(STR_FUND_AVAILABLE_UNTIL, ' + str(self.expiry_year) + ')')

        if self.get_property('extra_text_fund', economy) is not None:
            result.append(self.get_property('extra_text_fund', economy))

        # integrity check, no handling of multiple results currently so alert on that at compile time
        if len(result) > 1:
            utils.echo_message('Industry ' + self.id + ' wants more than one string for extra_text_fund, only one is supported currently')
            utils.echo_message(str(self.intro_year) + ' ' + str(self.expiry_year))

        # if no text is needed...
        if len(result) == 0:
            result.append('CB_RESULT_NO_TEXT')

        return 'return ' + result[0]

    def get_property(self, property_name, economy):
        # does magic to get the property from the defaults if not set
        # that enables economies to over-ride selected properties and not bother setting others
        # doesn't try to handle failure case of property not found at all: don't look up props that don't exist
        default_value = getattr(self.default_industry_properties, property_name)
        if economy is None:
            value = default_value
        else:
            economy_value = getattr(self.economy_variations[economy.id], property_name)
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

    def get_accept_cargo_types(self, economy):
        accept_cargo_types = self.get_property('accept_cargo_types', economy)
        # guard against too many cargos being defined
        if len(accept_cargo_types) > 3:
            utils.echo_message("Too many accepted cargos defined for " + self.id + ' in economy ' + economy.id)
        return '[' + ','.join(accept_cargo_types) + ']'

    def get_prod_cargo_types(self, economy):
        prod_cargo_types = self.get_property('prod_cargo_types', economy)
        # guard against too many cargos being defined
        if len(prod_cargo_types) > 2:
            utils.echo_message("Too many produced cargos defined for " + self.id + ' in economy ' + economy.id)
        return '[' + ','.join(prod_cargo_types) + ']'

    def get_another_industry(self, id):
        return get_another_industry(id)

    def get_conditional_expressions_for_enabled_economies(self):
        # returns a string that can be used as the conditions in nml if() blocks for economy stuff
        enabled_economies = []
        for i, economy in enumerate(registered_economies):
            if self.economy_variations[economy.id].enabled:
                enabled_economies.append('economy==' + str(i))
        return ' || '.join(enabled_economies)

    def get_expression_for_num_output_cargos_per_economy(self):
        # returns a string that is used to push 1 or 2 to temp storage as the number of industry output cargos
        # (secondary industries may have 1 or 2 output cargos; 0 is not a relevant option here)
        result = []
        for i, economy in enumerate(registered_economies):
            if self.economy_variations[economy.id].enabled:
                if len(self.get_property('prod_cargo_types', economy)) == 2:
                    result.append('economy==' + str(i))
        if len(result) == 0:
            return 1
        else:
            return '(' + ' || '.join(result) + ') ? 2 : 1'

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
        industry_template = templates[self.template]
        templated_pnml = utils.unescape_chameleon_output(industry_template(industry=self,
                                                         global_constants=global_constants,
                                                         economies=registered_economies,
                                                         utils=utils))
        return templated_pnml


class IndustryPrimary(Industry):
    """ Industries that produce cargo and (optionally) boost production if supplies are delivered """
    def __init__(self, **kwargs):
        super(IndustryPrimary, self).__init__(**kwargs)
        self.template = kwargs.get('template', 'industry_primary.pypnml')
        self.supply_requirements = None # default None, set appropriately by subclasses


class IndustryPrimaryExtractive(IndustryPrimary):
    """
        Industry that is extractive AND has production boosted by delivery of ENSP (mines and similar)
        Sparse subclass of IndustryPrimary, do not add much to this, it's subclassed once already
    """
    def __init__(self, **kwargs):
        kwargs['accept_cargo_types'] = ['ENSP']
        kwargs['life_type'] = 'IND_LIFE_TYPE_EXTRACTIVE'
        kwargs['extra_text_industry'] = True # slight hax, actual text string is determined by templated cb
        super(IndustryPrimaryExtractive, self).__init__(**kwargs)
        self.supply_requirements = [21, 84, 'PRIMARY'] # janky use of a un-named list for historical reasons (3rd item is string prefix)


class IndustryPrimaryOrganic(IndustryPrimary):
    """
        Industry that is organic AND has production boosted by delivery of FMSP (farms and similar)
        Sparse subclass of IndustryPrimary, do not add much to this, it's subclassed once already
    """
    def __init__(self, **kwargs):
        kwargs['accept_cargo_types'] = ['FMSP']
        kwargs['life_type'] = 'IND_LIFE_TYPE_BLACK_HOLE'
        kwargs['extra_text_industry'] = True # slight hax, actual text string is determined by templated cb
        super(IndustryPrimaryOrganic, self).__init__(**kwargs)
        self.supply_requirements = [14, 56, 'PRIMARY'] # janky use of a un-named list for historical reasons (3rd item is string prefix)


class IndustryPrimaryPort(IndustryPrimary):
    """
        Industry that is import-export AND has production boosted by delivery of arbitrary cargos (ports and similar)
        Sparse subclass of IndustryPrimary, do not add much to this, it's subclassed once already
    """
    def __init__(self, **kwargs):
        kwargs['life_type'] = 'IND_LIFE_TYPE_BLACK_HOLE'
        kwargs['extra_text_industry'] = True # slight hax, actual text string is determined by templated cb
        super(IndustryPrimaryPort, self).__init__(**kwargs)
        self.use_port_slope_switches = True # jank and hax for graphics switches, no 'proper' way yet for industries to set non-standard graphics via macros
        self.supply_requirements = [56, 224, 'PORT'] # janky use of a un-named list for historical reasons (3rd item is string prefix)


class IndustryPrimaryTownProducer(Industry):
    """ Industry that locates near towns, with production amount related to town population """
    def __init__(self, **kwargs):
        super(IndustryPrimaryTownProducer, self).__init__(**kwargs)
        self.template = kwargs.get('template', 'industry_primary_town_producer.pypnml')
        self.supply_requirements = None # supplies do not boost this type of primary

class IndustrySecondary(Industry):
    """ Processing industries: input cargo(s) -> output cargo(s) """
    def __init__(self, **kwargs):
        # !! this will need to handle economy variations also...might be non-viable in current form
        # - do that after snakebite, the CPP templating doesn't handle economy variations either
        self.processed_cargos_and_output_ratios = kwargs['processed_cargos_and_output_ratios'] # this kw is required, error if missing - no .get()
        kwargs['accept_cargo_types'] = [i[0] for i in self.processed_cargos_and_output_ratios]
        super(IndustrySecondary, self).__init__(**kwargs)
        self.template = kwargs.get('template', 'industry_secondary.pypnml')
        self.combined_cargos_boost_prod = kwargs.get('combined_cargos_boost_prod', False)
        self.mnsp_boosts_production_jank = kwargs.get('mnsp_boosts_production_jank', False) # jank jank jank

    def get_num_output_cargos(self):
        # !! no economy support currently, CPP templating doesn't handle it, but will be needed after snakebite
        return len(self.get_property('prod_cargo_types', None))

    def get_prod_ratio(self, cargo_num):
        if cargo_num > len(self.processed_cargos_and_output_ratios):
            return 0
        else:
            return self.processed_cargos_and_output_ratios[cargo_num - 1][1]

    def get_boost(self, supplied_cargo_num, boosted_cargo_num):
        # jank for MNSP first, this is due to design choices I now regret :|
        # some industries boost only in combination with MNSP, rather than any/all accepted cargos, ugh
        if self.mnsp_boosts_production_jank:
            if self.processed_cargos_and_output_ratios[supplied_cargo_num - 1][0] == 'MNSP':
                return self.get_prod_ratio(supplied_cargo_num)
            elif self.processed_cargos_and_output_ratios[boosted_cargo_num - 1][0] == 'MNSP':
                return self.get_prod_ratio(supplied_cargo_num)
            else:
                return 0
        # not jank, proper
        if self.combined_cargos_boost_prod:
            if boosted_cargo_num > len(self.processed_cargos_and_output_ratios):
                return 0
            else:
                return self.get_prod_ratio(supplied_cargo_num)
        return 0


class IndustryTertiary(Industry):
    """ Industries that consume cargo and don't produce much (or anything), typically black holes in or near towns """
    def __init__(self, **kwargs):
        super(IndustryTertiary, self).__init__(**kwargs)
        self.template = 'industry_tertiary.pypnml'

