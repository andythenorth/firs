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
        self.numeric_id = global_constants.tile_numeric_ids[self.id] # don't fail this silently, tile id must be defined
        self.land_shape_flags = kwargs.get('land_shape_flags', '0')
        self.location_checks = kwargs.get('location_checks')
        # check for setting both land_shape_flags and location_checks
        # it's a cause of coder-error when I forget that land_shape_flags will be ignored when location_check is used
        # 'janky_industry_id_string' because an industry ID is needed, and I don't trivially have one here
        if self.land_shape_flags is not '0' and len(self.location_checks.get_render_tree(self.id, industry_id)) > 0:
            raise Exception("Tile " + self.id + ": land_shape_flags are set but will be ignored because the tile also uses location_checks cb.  Only set one of these attributes.")
        self.special_flags = kwargs.get('special_flags', None)
        self.foundations = kwargs.get('foundations', None)
        self.autoslope = kwargs.get('autoslope', None)
        # animation length (int), looping (bool), speed (int) should be set for all animations
        # basic tile animation plays consecutive-frames from the spriteset
        # spriteset can offset frames when multiple animations are used *on the same* tile (to avoid odd-looking sync effects)
        # spriteset can also be given custom rules to choose which sprite to show per animation_frame
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
        self.custom_animation_next_frame = kwargs.get('custom_animation_next_frame', None)
        self.custom_animation_control = kwargs.get('custom_animation_control', None)
        self.random_trigger = kwargs.get('random_trigger', None)

    def get_expression_for_tile_acceptance(self, industry, economy):
        result = []
        accept_cargo_types = industry.get_accept_cargo_types(economy)
        for cargo in accept_cargo_types:
            result.append('[cargotype("' + cargo + '"), 8]')
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
        self.require_effectively_flat = kwargs.get('require_effectively_flat', False)
        self.require_houses_nearby = kwargs.get('require_houses_nearby', False)
        self.require_road_adjacent = kwargs.get('require_road_adjacent', False)
        self.require_coast = kwargs.get('require_coast', False)
        self.disallow_above_snowline = kwargs.get('disallow_above_snowline', False)
        self.disallow_below_snowline = kwargs.get('disallow_below_snowline', False)
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

        if self.require_effectively_flat:
            result.appendleft(TileLocationCheckRequireEffectivelyFlat())

        if self.require_coast:
            result.append(TileLocationCheckRequireSea())
            result.append(TileLocationCheckRequireSlope())

        if self.require_houses_nearby:
            # generates circular tile search points automatically
            # possibly could be done simpler with a town zone check instead of a tile search, but eh, it's done and works
            # note that this automates the provision of tile locations for the search radius, no option to declare that per-industry
            distance = 7
            search_points = []
            for x in range(-1 * distance, distance+1):
                for y in range(-1 * distance, distance+1):
                    search_points.append((x, y))
            for search_offsets in search_points:
                result.append(TileLocationCheckRequireHousesNearby(search_offsets))

        if self.require_road_adjacent:
            result.append(TileLocationCheckRequireRoadAdjacent())

        if self.disallow_above_snowline:
            result.appendleft(TileLocationCheckDisallowAboveSnowline())

        if self.disallow_below_snowline:
            result.appendleft(TileLocationCheckDisallowBelowSnowline())

        if self.disallow_desert:
            result.appendleft(TileLocationCheckDisallowDesert())

        if self.disallow_coast:
            result.appendleft(TileLocationCheckDisallowCoast())

        # walk the tree, setting entry points and results (id of next switch) for each switch
        for count, lc in enumerate(result):
            lc.switch_entry_point = switch_prefix + str(count)
            # set result, except for the last check (last check uses the default allow/disallow value defined in the check)
            if count < len(result) - 1:
                lc.switch_result = switch_prefix + str(count + 1)

        return list(reversed(result))


class TileLocationCheck(object):
    """ Sparse class to base TileLocationCheck subclasses on """
    @property
    def macro(self):
        return templates["location_check_macros_tile.pynml"].macros[self.macro_name]


class TileLocationCheckDisallowSlopes(TileLocationCheck):
    """
        Prevent building on all slopes
        Not to be confused with TileLocationCheckRequireEffectivelyFlat
    """
    def __init__(self):
        self.switch_result = None # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.macro_name = 'disallow_slopes'


class TileLocationCheckDisallowSteepSlopes(TileLocationCheck):
    """ Prevent building on steep slopes (but not normal slopes) """
    def __init__(self):
        self.switch_result = None # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.macro_name = 'disallow_steep_slopes'


class TileLocationCheckDisallowIndustryAdjacent(TileLocationCheck):
    """
        Prevent directly adjacent to another industry, used by most industries, but not all
        1. Makes it too hard for the game to find a location for some types (typically large flat industries)
        2. Not necessary for most town industries
    """
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = None
        self.macro_name = 'disallow_industry_adjacent'


class TileLocationCheckRequireEffectivelyFlat(TileLocationCheck):
    """
        Check that the highest corner of all tiles is equal to the highest corner of the north tile
        This permits building on slopes with foundations,
        but prevents industry graphics being 'broken' by being drawn at different height levels.
        Not to be confused with TileLocationCheckDisallowSlopes
    """
    def __init__(self):
        self.switch_result = None # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.macro_name = 'require_effectively_flat'


class TileLocationCheckRequireHousesNearby(TileLocationCheck):
    """ Requires houses at offset x, y (to be fed by circular tile search) """
    def __init__(self, search_offsets):
        self.switch_result = 'return CB_RESULT_LOCATION_DISALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = None
        self.macro_name = 'require_houses_nearby'
        self.x = search_offsets[0]
        self.y = search_offsets[1]


class TileLocationCheckRequireRoadAdjacent(TileLocationCheck):
    """ Requires road on adjacent tile(s), with configurable directions """
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = None
        self.macro_name = 'require_road_adjacent'


class TileLocationCheckRequireSea(TileLocationCheck):
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = None
        self.macro_name = 'require_sea_tile'


class TileLocationCheckRequireSlope(TileLocationCheck):
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = None
        self.macro_name = 'require_slope'


class TileLocationCheckDisallowDesert(TileLocationCheck):
    """ Prevent building on desert tiles """
    def __init__(self):
        self.switch_result = None # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.macro_name = 'disallow_desert'


class TileLocationCheckDisallowCoast(TileLocationCheck):
    """ Prevent building on desert tiles """
    def __init__(self):
        self.switch_result = None # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.macro_name = 'disallow_coast_or_water'


class TileLocationCheckDisallowAboveSnowline(TileLocationCheck):
    """ Prevent building above snowline """
    def __init__(self):
        self.switch_result = None # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.minh = 0
        self.maxh = 'snowline_height'
        self.outrange = 'return string(STR_ERR_LOCATION_NOT_ABOVE_SNOWLINE)'
        self.macro_name = 'require_height_range'


class TileLocationCheckDisallowBelowSnowline(TileLocationCheck):
    """ Prevent building above snowline """
    def __init__(self):
        self.switch_result = None # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.minh = 'snowline_height'
        self.maxh = 255
        self.outrange = 'return string(STR_ERR_LOCATION_NOT_BELOW_SNOWLINE)'
        self.macro_name = 'require_height_range'


class TileLocationCheckFounder(TileLocationCheck):
    """
        Used to over-ride non-essential checks when player is building
        Some tile checks relating to landscape are essential and are placed before player check
    """
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = None
        self.macro_name = 'allow_player'


class Sprite(object):
    """Base class to hold simple sprites (using numbers from a base set)"""
    def __init__(self, sprite_number, sprite_number_snow='', xoffset=0, yoffset=0, zoffset=0, xextent=16, yextent=16, zextent=16, always_draw=0):
        # there are few shorthand constants for specific sprite numbers (legacy from CPP templating, kind of useful to keep)
        sprite_constants = {'GROUNDTILE_MUD_TRACKS': 2022, 'GROUNDTILE_SLABS': 1420}
        if sprite_number in sprite_constants.keys():
            self.sprite_number = sprite_constants[sprite_number]
        else:
            self.sprite_number = sprite_number # can also provide raw nml with the sprite number for things like controlling animation frame
        self.sprite_number_snow = sprite_number_snow if sprite_number_snow != '' else self.sprite_number  # set a snow sprite explicitly (optional).
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
        # animation_frame_offset can be used (in some cases) to desynchronise animations in the same tile (or in some cases within the same industry as an alternative to animation triggers)
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
                 animation_rate=0, custom_sprite_selector=None, always_draw=0, num_sprites_to_autofill=1):
        self.id = id
        self.sprites = sprites # a list of sprites 6-tuples in format (x, y, w, h, xoffs, yoffs)
        self.type = type # set to ground or other special types, or omit for default (building, greeble, foundations etc - graphics from png named same as industry)
        self.animation_rate = animation_rate # (must be int) optional multiplier to tile's animation rate, set to 1 for same as tile, >1 for faster; leave default (0) to disable animation; < 1 isn't valid and nml won't compile it
        self.custom_sprite_selector = custom_sprite_selector
        self.num_sprites_to_autofill = num_sprites_to_autofill # create n sprites per sprite passed (optional convenience method for use where spriteset sizes must match; set value to same as size of largest spriteset)
        # optional parameters for offsets and extents for the *spritelayout* to use with this sprite (read nml spritelayout docs to see use)
        # (more convenient to store on the sprite, even though consumed by spritelayout, as they tend to be constant in most cases where the sprite is used)
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.zoffset = zoffset
        self.xextent = xextent # set extents to x/y/z sizes of largest sprite in spriteset, or omit for default (16)
        self.yextent = yextent
        self.zextent = 32 # it's of limited use setting zextent, just make it 32 and be done with it
        self.always_draw = always_draw

    def get_ground_tile_x_start(self, type):
        return {'mud': 0, 'concrete': 80, 'cobble': 150, 'snow': 220, 'slab': 290, 'empty':360}[type]


class SpriteLayout(object):
    """ Base class to hold spritelayouts for industry spritelayouts """
    def __init__(self, id, ground_sprite, ground_overlay, building_sprites, smoke_sprites=[], fences=[], magic_trees=[], terrain_aware_ground=False):
        self.id = id
        self.ground_sprite = ground_sprite
        self.ground_overlay = ground_overlay
        self.building_sprites = building_sprites
        self.smoke_sprites = smoke_sprites
        self.fences = fences # a simple list of keywords.  Valid values: 'ne', 'se', 'sw', 'nw'.  Order is arbitrary.
        self.magic_trees = magic_trees
        self.terrain_aware_ground = terrain_aware_ground # we don't draw terrain (and climate) aware ground unless explicitly required by the spritelayout, it makes nml compiles slower


class MagicSpritelayoutSlopeAwareTrees(object):
    """ Occasionally we need magic.  If we're going magic, let's go full on magic.  This one makes 4 climate-aware trees on a slope-aware ground tile """

    # Class attributes eh?  Might as well, these aren't supposed to be mutable

    # there are 19 slopes to handle, as per https://newgrf-specs.tt-wiki.net/wiki/NML:List_of_tile_slopes
    # format is slope_num: (tuples of x, y for 4 or 9 trees)

    slopes_4 = {0: ((2, 2), (2, 9), (9, 2), (9, 9)), # done
                1: ((2, 2), (2, 9), (9, 2), (9, 9)),
                2: ((2, 2), (2, 9), (9, 2), (9, 9)),
                3: ((2, 0), (0, 6), (6, 0), (6, 6)), # done
                4: ((2, 2), (2, 9), (9, 2), (9, 9)),
                5: ((2, 2), (2, 9), (9, 2), (9, 9)),
                6: ((2, 0), (0, 6), (8, 1), (6, 6)), # done
                7: ((0, 0), (0, 5), (5, 0), (5, 5)), # done
                8: ((2, 2), (2, 9), (9, 2), (9, 9)),
                9: ((1, 2), (2, 9), (8, 2), (9, 9)), # done
                10: ((2, 2), (2, 9), (9, 2), (9, 9)),
                11: ((0, 0), (0, 8), (7, 0), (7, 7)), # done
                12: ((2, 2), (2, 9), (9, 2), (9, 9)),
                13: ((2, 2), (2, 9), (9, 2), (9, 9)),
                14: ((1, 1), (-1, 6), (8, 2), (6, 6)), # done
                23: ((0, 0), (0, 5), (5, -2), (4, 4)), # done
                27: ((0, 0), (0, 7), (5, -2), (5, 5)), # done
                29: ((0, 0), (0, 7), (7, 0), (7, 7)), # done
                30: ((0, 0), (-1, 4), (7, 0), (6, 5))} # done

    slopes_9 = {0: ((0, 0), (0, 5), (0, 11), (5, 0), (5, 5), (5, 11), (11, 0), (11, 5), (11, 11)), # done
                1: ((0, 0), (0, 5), (0, 11), (5, -1), (4, 4), (5, 11), (9, -2), (10, 4), (11, 11)), # done
                2: ((0, 0), (0, 5), (0, 9), (5, 0), (4, 4), (4, 8), (10, 0), (9, 4), (7, 7)), # done
                3: ((-1, -3), (-1, 3), (-1, 9), (3, -3), (3, 2), (3, 8), (7, -3), (7, 2), (7, 7)), # done
                4: ((0, 0), (0, 4), (-2, 9), (5, 0), (5, 4), (5, 10), (11, 0), (11, 4), (11, 11)), # done
                5: ((0, 0), (-2, 3), (-4, 8), (5, 0), (3, 3), (3, 9), (10, 0), (8, 3), (11, 11)), # part done, hard to test
                6: ((0, 0), (-2, 3), (-4, 8), (5, 0), (3, 3), (1, 8), (10, 0), (8, 3), (6, 8)), # done
                7: ((-3, -3), (-3, 3), (-3, 7), (2, -3), (2, 2), (2, 7), (7, -3), (7, 2), (7, 7)), # done
                8: ((0, 0), (0, 5), (0, 11), (5, 0), (5, 5), (5, 11), (11, 0), (11, 5), (11, 11)),
                9: ((-1, -1), (0, 5), (1, 10), (3, -1), (4, 5), (5, 10), (8, -1), (9, 5), (10, 10)), # done
                10: ((-3, -3), (-3, 3), (1, 10), (2, -3), (2, 2), (5, 9), (10, 1), (9, 5), (8, 8)), # part done, hard to test
                11: ((-3, -3), (-3, 3), (-1, 10), (2, -3), (2, 2), (3, 9), (7, -3), (7, 2), (7, 7)), # done
                12: ((0, 0), (-1, 4), (-3, 8), (5, 0), (5, 5), (4, 10), (11, 0), (11, 5), (11, 11)), # done
                13: ((0, 0), (0, 5), (-2, 9), (4, 0), (5, 5), (4, 10), (9, -2), (10, 5), (11, 11)), # done
                14: ((0, 0), (0, 5), (0, 10), (5, 0), (5, 5), (5, 10), (10, 0), (9, 4), (7, 7)), # done
                23: ((0, 0), (-2, 2), (-5, 7), (2, 0), (2, 2), (-1, 6), (8, -2), (5, 0), (4, 4)), # part done, hard to test
                27: ((0, 0), (0, 5), (-1, 11), (2, 0), (3, 5), (3, 10), (5, -5), (6, 2), (7, 8)), # done
                29: ((-3, 0), (-3, 4), (-3, 8), (3, 0), (1, 3), (4, 10), (8, -3), (10, 4), (11, 11)), # part done, hard to test
                30: ((-3, 0), (-5, 2), (-8, 4), (3, 0), (1, 3), (-1, 5), (10, -1), (9, 3), (7, 7))} # done

    def __init__(self, industry, base_id, config):
        # !! ground sprites are slaved to sprite numbers currently, needs extending for spritesets
        ground_sprite = industry.add_sprite(sprite_number=str(config['ground_sprite']) + ' + slope_to_sprite_offset(nearby_tile_slope(0,0))')

        # tile has 4 or 9 tree positions, so 4 or 9 tree sprites/spritesets are required, just repeat as necessary if some positions use same sprite
        # trees can be ints (sprite numbers for baseset), or lists of tuples (for spritesets, with optional animation)
        trees_default = config['trees_default']
        trees_snow = config.get('trees_snow', trees_default) # defining snow trees is optional
        trees_tropic = config.get('trees_tropic', trees_default) # defining tropic trees is optional
        if len(trees_snow) != len(trees_default):
            raise Exception("Number of snow trees needs to match number of default trees for " + industry.id)
        if len(trees_tropic) != len(trees_default):
            raise Exception("Number of tropic trees needs to match number of default trees for " + industry.id)

        num_trees = len(trees_default) # whether 4 or 9 trees are used is determined by number of default trees passed
        slopes = {4: self.slopes_4, 9: self.slopes_9}[num_trees]

        trees = {}
        for terrain, tree_config in {'default': trees_default, 'snow': trees_snow, 'tropic': trees_tropic}.items():
            trees[terrain] = []
            for index, tree in enumerate(tree_config):
                if isinstance(tree, int): # we have a sprite, just store the number
                    trees[terrain].append(tree)
                if isinstance(tree, list):
                    print('tree is spriteset: not implemented yet')
                    # extend spriteset support here (noting that spritesets are lists of tuples as they can be animated also)
                    # my intent was simply to pass the offsets to this, as that should be all that is needed

        for slope, offsets in slopes.items():
            industry.add_spritelayout(id = base_id + str(slope),
                                  ground_sprite = ground_sprite,
                                  ground_overlay = ground_sprite, # slight hax, assume we can just reuse ground for overlay
                                  magic_trees = [MagicTree(trees, offsets, tree_num=tree_num) for tree_num in range(num_trees)],
                                  building_sprites = [])

        id_slope_mapping = {base_id + str(slope): slope for slope in slopes} # easier to match to format of slope switch in nml
        industry.add_slope_graphics_switch(base_id,
                                       default_result = base_id + '0',
                                       slope_spritelayout_mapping = {slope: slope_id for slope_id, slope in id_slope_mapping.items()})


class MagicTree(object):
    """ Stubby class used in MagicSpriteLayoutSlopeAwareTrees; I just prefer object attribute access over an equivalent dict - Andy"""
    def __init__(self, trees, offsets, tree_num):
        self.default = trees['default'][tree_num]
        self.snow = trees['snow'][tree_num]
        self.tropic = trees['tropic'][tree_num]
        self.xoffset = offsets[tree_num][0]
        self.yoffset = offsets[tree_num][1]


class MagicSpritelayoutHarbourCoastFoundations(object):
    """
        Occasionally we need magic.  If we're going magic, let's go full on magic.
        This one makes provides the slope-aware foundations needed for coast tiles.
        Possibly could be used generically for all slopes, there's nothing specific to coasts in it, but other cases weren't needed when writing it.
    """
    # Class attributes eh?  Might as well, these aren't supposed to be mutable

    slope_spritelayout_nums = {0: '1', 1: '4', 2: '8', 3: '2', 4: '6', 5: '5', 6: '7', 7: '1',
                               8: '3', 9: '4', 10: '8', 11: '2', 12: '6', 13: '5', 14: '7'}

    spritelayout_foundations = {'1': [],
                                '2': ['slope_sw_ne'],
                                '3': ['se_nw', 'ne_sw'],
                                '4': ['ne_sw', 'slope_nw_se'],
                                '5': ['slope_ne_sw', 'slope_nw_se'],
                                '6': ['slope_ne_sw', 'se_nw'],
                                '7': ['slope_se_nw'],
                                '8': ['slope_se_nw', 'slope_sw_ne']}

    def __init__(self, industry, base_id, config):
        for spritelayout_num, foundations in self.spritelayout_foundations.items():
            building_sprites = [config['foundation_sprites'][foundation_sprites] for foundation_sprites in foundations]
            building_sprites.extend(config['building_sprites'])
            industry.add_spritelayout(id = base_id + str(spritelayout_num),
                                  ground_sprite = config['ground_sprite'], # should always be empty sprite for this magic layout
                                  ground_overlay = config['ground_sprite'], # should always be empty sprite for this magic layout
                                  building_sprites = building_sprites)
        id_slope_mapping = {slope: base_id + str(spritelayout_num) for slope, spritelayout_num in self.slope_spritelayout_nums.items()}
        industry.add_slope_graphics_switch(base_id,
                                       default_result = base_id + '1',
                                       slope_spritelayout_mapping = {slope_id: slope for slope_id, slope in id_slope_mapping.items()})


class GraphicsSwitch(object):
    """ base class for extra graphics switches """
    def __init__(self, id, **kwargs):
        self.id = id


class GraphicsSwitchSlopes(GraphicsSwitch):
    """ Class from which a slope-checking graphics switch can be generated, routing to appropriate spritelayout per slope type """
    def __init__(self, id, slope_spritelayout_mapping, default_result):
        super().__init__(id)
        self.slope_spritelayout_mapping = slope_spritelayout_mapping
        self.default_result = default_result


class IndustryLayout(object):
    """ Base class to hold industry layouts """
    def __init__(self, id, layout):
        self.id = id
        self.layout = layout # a list of 4-tuples (SE offset from N tile, SW offset from N tile, tile identifier, identifier of spriteset or next nml switch)


class IndustryLocationChecks(object):
    """ Class to hold location checks for an industry """
    def __init__(self, industry, location_args={}):
        self.industry = industry
        self.prevent_player_founding = location_args.get('prevent_player_founding', False)
        self.same_type_distance = location_args.get('same_type_distance', None)
        self.industry_max_distance = location_args.get('industry_max_distance', None)
        self.cluster = location_args.get('cluster', None)
        self.town_industry_count = location_args.get('town_industry_count', None)
        self.coast_distance = location_args.get('coast_distance', None)
        # this is custom to grain mill, can be made generic if needed
        self.flour_mill_layouts_by_date = location_args.get('flour_mill_layouts_by_date', None)

    def get_render_tree(self, incompatible_industries):
        switch_prefix = self.industry.id + '_'
        # this could be reimplemented to just use numeric switch suffixes, as per tile location check tree
        result = deque([])

        # usually industry location checks *alway* allow player to found industries (tile location checks still apply)
        # *very rarely* we need to prevent player founding (e.g. recycling depot, where production depends on town population)
        if not self.prevent_player_founding:
            result.append(IndustryLocationCheckFounder())

        if self.cluster:
            # special case if clustering is used, cluster check handles max distance and cluster counts...
            # ...and min distance is set to 20 for all types (as all clustered industries were using this value at time of writing)
            result.append(IndustryLocationCheckCluster(self.industry.id, self.cluster))
            result.append(IndustryLocationCheckIndustryMinDistance(self.industry.id, 20))
        elif self.same_type_distance:
            # industries can over-ride the default min distance to others of same type
            result.append(IndustryLocationCheckIndustryMinDistance(self.industry.id, self.same_type_distance))
        else:
            # enforce a default min distance to other industries of same type
            result.append(IndustryLocationCheckIndustryMinDistance(self.industry.id, 56))

        if self.industry_max_distance:
            result.append(IndustryLocationCheckIndustryMaxDistance(self.industry_max_distance))

        if self.town_industry_count:
            result.append(IndustryLocationCheckTownIndustryCount(self.town_industry_count))

        if self.coast_distance:
            result.append(IndustryLocationCheckCoastDistance())

        if self.flour_mill_layouts_by_date:
            result.appendleft(IndustryLocationCheckGrainMillLayoutsByDate())

        # prevent locating very near industries in the same accept / produce chain
        for industry in set(incompatible_industries[self.industry]):
            # don't check for self type, we have other ways to do that (occasionally economy cargo variations trigger this)
            if industry.id != self.industry.id:
                result.append(IndustryLocationCheckIndustryMinDistance(industry.id, 16))

        prev = None
        for lc in reversed(result):
            lc.switch_entry_point = switch_prefix + lc.switch_entry_point
            if prev is not None:
                lc.switch_result = prev.switch_entry_point
            prev = lc
        result[0].switch_entry_point = switch_prefix + 'check_location'
        return list(reversed(result))


class IndustryLocationCheck(object):
    """ sparse base class for industry location checks """
    @property
    def macro(self):
        return templates["location_check_macros_industry.pynml"].macros[self.macro_name]


class IndustryLocationCheckTownIndustryCount(IndustryLocationCheck):
    """ Require specific count of industry type in a town """
    def __init__(self, town_industry_count):
        # use the numeric_id so that we can do single-industry compiles without nml barfing on missing identifiers
        self.industry_type_numeric_id = get_another_industry(town_industry_count[0]).numeric_id
        self.min_count = town_industry_count[1]
        self.max_count = town_industry_count[2]
        if self.min_count != 0 or self.max_count != 0:
            utils.echo_message('IndustryLocationCheckTownIndustryCount uses a hardcoded error string limint to 1 instance per town, add more strings to handle higher limits')
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = 'town_industry_count'
        self.macro_name = 'town_industry_count'


class IndustryLocationCheckCluster(IndustryLocationCheck):
    """ Require industries to locate in n clusters """
    def __init__(self, industry_type, cluster):
        # use the numeric_id so that we can do single-industry compiles without nml barfing on missing identifiers
        self.industry_type_numeric_id = industry_type
        self.max_distance = cluster[0]
        # cluster factor is a fudge, theoretically determines number of clusters per 256x256 section of map, but often irrelevant due to industry counts in any given combination of map/setting/economy/randomisation
        self.cluster_factor = cluster[1]
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = 'cluster_' + str(self.industry_type_numeric_id)
        self.macro_name = 'cluster'


class IndustryLocationCheckIndustryMinDistance(IndustryLocationCheck):
    """ Prevent locating near incompatible industry types """
    def __init__(self, industry_type, distance):
        self.industry_type = industry_type
        # use the numeric_id so that we can do single-industry compiles without nml barfing on missing identifiers
        self.industry_type_numeric_id = get_another_industry(industry_type).numeric_id
        self.distance = distance
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = 'min_distance_' + str(self.industry_type_numeric_id)
        self.macro_name = 'check_industry_min_distance'


class IndustryLocationCheckIndustryMaxDistance(IndustryLocationCheck):
    """ Prevent locating near incompatible industry types """
    def __init__(self, industry_max_distance):
        self.industry_type = industry_max_distance[0]
        # use the numeric_id so that we can do single-industry compiles without nml barfing on missing identifiers
        self.industry_type_numeric_id = get_another_industry(self.industry_type).numeric_id
        self.distance = industry_max_distance[1]
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = 'max_distance_' + str(self.industry_type_numeric_id)
        self.macro_name = 'check_industry_max_distance'


class IndustryLocationCheckFounder(IndustryLocationCheck):
    """ Ensures player can build irrespective of _industry_ location checks (tile checks still apply) """
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = 'check_founder'
        self.macro_name = 'check_founder'


class IndustryLocationCheckCoastDistance(IndustryLocationCheck):
    """ Maximum distance to coast (player can vary this with parameter) """
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = 'coast_distance'
        self.macro_name = 'coast_distance'


class IndustryLocationCheckGrainMillLayoutsByDate(IndustryLocationCheck):
    """ Custom check for Grain mill, layouts are restricted by date; this is a one-off, but could be made generic if needed """
    def __init__(self):
        self.switch_result = 'return CB_RESULT_LOCATION_ALLOW' # default result, value may also be id for next switch
        self.switch_entry_point = 'check_date'
        self.macro_name = 'flour_mill_layouts_by_date'


class IndustryPermStorage(object):
    """ sparse class mapping properties names to int numbers 1-16, used to aid readability when using STORE_PERM and LOAD_PERM"""
    def __init__(self, identifiers):
        # should be passed a list of length 16, with 'unused' string in empty slots
        # doesn't need any numbers, just don't mess with positions of identifiers (or bump savegame version if you do)
        if len(identifiers) is not 16:
            utils.echo_message("IndustryPermStorageNums must be passed a list of 16 registers containing var names as strings, or 'unused'")
        self.unused = []
        for register_num, identifier in enumerate(identifiers):
            if identifier is 'unused':
                self.unused.append(register_num)
            else:
                setattr(self, identifier, register_num)


class IndustryProperties(object):
    """ Base class to hold properties corresponding to nml industry item properties """
    def __init__(self, **kwargs):
        # nml item properties, most of these should be provided as strings for insertion into nml.  See nml docs for meaning + acceptable values.
        self.substitute = kwargs.get('substitute', '0') # '0' is safe default, most industries don't need to set this prop explicitly, but the prop must have *a* value or industry won't appear in game
        self.override = kwargs.get('override', '0') # industries should only set this explicitly when re-using a default industry, otherwise '0' is a safe default
        self.name = kwargs.get('name', None)
        self.nearby_station_name = kwargs.get('nearby_station_name', None)
        self.intro_year = kwargs.get('intro_year', None)
        self.expiry_year = kwargs.get('expiry_year', None)
        self.accept_cargo_types = kwargs.get('accept_cargo_types', None)
        self.prod_cargo_types = kwargs.get('prod_cargo_types', None)
        self.prod_multiplier = kwargs.get('prod_multiplier', None)
        self.min_cargo_distr = '5' # just use the most common value from default OTTD industries, this property needs set but has little use
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
        self.remove_cost_multiplier = kwargs.get('remove_cost_multiplier', '0')
        # not nml properties
        self.enabled = kwargs.get('enabled', False)
        self.processed_cargos_and_output_ratios = kwargs.get('processed_cargos_and_output_ratios', None)
        self.override_default_construction_states = kwargs.get('override_default_construction_states', False)
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
        self.extra_graphics_switches = []
        self.industry_layouts = []
        self.default_industry_properties = IndustryProperties(**kwargs)
        self.economy_variations = {}
        for economy in registered_economies:
            self.add_economy_variation(economy)
        self.template = kwargs.get('template', None) # template will be set by subcass, and/or by individual industry instances
        self.location_checks = IndustryLocationChecks(self, kwargs.get('location_checks', {}))

    def register(self):
        if len([i for i in self.economy_variations if self.economy_variations[i].enabled is True]) == 0:
            utils.echo_message(self.id + ' is not used in any economy')
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
        id = self.id + '_spriteset_' + str(len(self.spritesets))
        new_spriteset = Spriteset(id=id, *args, **kwargs)
        self.spritesets.append(new_spriteset)
        return new_spriteset # returning the new obj isn't essential, but permits the caller giving it a reference for use elsewhere

    def add_spritelayout(self, *args, **kwargs):
        new_spritelayout = SpriteLayout(*args, **kwargs)
        self.spritelayouts.append(new_spritelayout)
        return new_spritelayout # returning the new obj isn't essential, but permits the caller giving it a reference for use elsewhere

    def add_magic_spritelayout(self, type, base_id, config):
        # sometimes magic is the only way
        # this is for very specific spritelayout patterns that repeat across multiple industries and require long declarations and extra switches
        if type == 'slope_aware_trees':
            MagicSpritelayoutSlopeAwareTrees(self, base_id, config)
        if type == 'harbour_coast_foundations':
            MagicSpritelayoutHarbourCoastFoundations(self, base_id, config)


    def add_slope_graphics_switch(self, *args, **kwargs):
        new_graphics_switch = GraphicsSwitchSlopes(*args, **kwargs)
        self.extra_graphics_switches.append(new_graphics_switch)
        return new_graphics_switch # returning the new obj isn't essential, but permits the caller giving it a reference for use elsewhere

    def add_industry_layout(self, *args, **kwargs):
        new_industry_layout = IndustryLayout(*args, **kwargs)
        self.industry_layouts.append(new_industry_layout)
        return new_industry_layout # returning the new obj isn't essential, but permits the caller giving it a reference for use elsewhere

    def add_economy_variation(self, economy):
        self.economy_variations[economy.id] = IndustryProperties()

    @property
    def numeric_id(self):
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
        temp_store_random_bits = global_constants.temp_storage_graphics_chain['var_random_bits']
        random_offset = "5 * LOAD_TEMP(" + str(temp_store_random_bits) + ") / 0x10000" # random is in nml at run-time, not compile-time python, so this is a string
        if len(self.graphics_change_dates) == 0:
            return "0" # no date variations, just one set of graphics, never hide
        elif date_variation_index == 0:
            return "(current_year + " + random_offset + ") >= " + str(self.graphics_change_dates[date_variation_index]) # first set of graphics, hide after first change date
        elif date_variation_index == len(self.graphics_change_dates):
            return "(current_year + " + random_offset + ") < " + str(self.graphics_change_dates[date_variation_index - 1]) # last set of graphics, hide before last change date
        else:
            return "(current_year + " + random_offset + ") < " + str(self.graphics_change_dates[date_variation_index - 1]) + " || (current_year + " + random_offset + ") >= " + str(self.graphics_change_dates[date_variation_index])

    def get_industry_layouts_as_property(self):
        result = [industry_layout.id + '_tilelayout' for industry_layout in self.industry_layouts]
        return 'layouts: [' + ','.join(result) + '];'

    def get_extra_text_fund(self, economy):
        # some fund text options are orthogonal, there is no support for combining them currently
        # support for combined fund text could be added, it's just a substr tree eh?
        result = [] # use a list, because I want to warn if industry tries to set more than one result
        if self.get_intro_year(economy) != 0:
            result.append('string(STR_FUND_AVAILABLE_FROM, ' + str(self.get_intro_year(economy)) + ')')
        if self.get_expiry_year(economy) != global_constants.max_game_date:
            result.append('string(STR_FUND_AVAILABLE_UNTIL, ' + str(self.get_expiry_year(economy)) + ')')

        if self.get_property('extra_text_fund', economy) is not None:
            result.append(self.get_property('extra_text_fund', economy))

        # integrity check, no handling of multiple results currently so alert on that at compile time
        if len(result) > 1:
            utils.echo_message('Industry ' + self.id + ' wants more than one string for extra_text_fund, only one is supported currently')
            utils.echo_message(str(self.get_intro_year(economy)) + ' ' + str(self.get_expiry_year(economy)))

        # if no text is needed...
        if len(result) == 0:
            result.append('CB_RESULT_NO_TEXT')

        return 'return ' + result[0]

    def get_extra_text_string(self, economy):
        accept_cargos_with_ratios = self.get_property('processed_cargos_and_output_ratios', economy)
        if len(accept_cargos_with_ratios) == 1:
            extra_text_string = 'STR_EMPTY' # nothing useful to show where just one cargo is accepted eh
        else:
            if self.combined_cargos_boost_prod:
                extra_text_string = 'STR_EXTRA_TEXT_SECONDARY_COMBINATORY'
            else:
                extra_text_string = 'STR_EXTRA_TEXT_SECONDARY_NON_COMBINATORY'
        return 'string(' + extra_text_string + ')'

    def get_intro_year(self, economy):
        # simple wrapper to get_property(), which sanitises intro_year from None to 0 if unspecified by economy
        result = self.get_property('intro_year', economy)
        if result == None:
            return 0
        else:
            return result

    def get_expiry_year(self, economy):
        # simple wrapper to get_property(), which sanitises expiry from None to max game date if unspecified by economy
        result = self.get_property('expiry_year', economy)
        if result == None:
            return global_constants.max_game_date
        else:
            return result

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

        # map colour uses a guarding function
        if property_name is 'map_colour':
            self.validate_map_colour(value)

        return value

    def get_property_declaration(self, property_name, economy=None):
        value = self.get_property(property_name, economy)
        # we don't want to render empty properties for nml
        if value == None or value == '':
            return
        else:
            return property_name + ': ' + value + ';'

    def get_nearby_station_name_declaration(self):
        return 'nearby_station_name: string(STR_STATION, string(STR_TOWN),' + self.get_property('nearby_station_name', None) + ');'

    def get_accept_cargo_types_declaration(self, economy):
        # special handling to reformat python list as nml property declaration
        result = ','.join(['cargotype("' + label + '")' for label in self.get_accept_cargo_types(economy)])
        return 'accept_cargo_types: [' + result + '];'

    def get_prod_cargo_types_declaration(self, economy):
        # special handling to reformat python list as nml property declaration
        result = ','.join(['cargotype("' + label + '")' for label, output_ratio in self.get_prod_cargo_types(economy)])
        return 'prod_cargo_types: [' + result + '];'

    def get_accept_cargo_types(self, economy):
        # method used here for (1) guarding against invalid values (2) so that it can be over-ridden by industry subclasses as needed
        result = self.get_property('accept_cargo_types', economy)
        if result is None:
            # returning None causes some things to explode in docs, which I should fix, but haven't, this patches it with jank
            return []
        else:
            # guard against too many cargos being defined
            if len(result) > 3:
                utils.echo_message("Too many accepted cargos defined for " + self.id + ' in economy ' + economy.id)
            return result

    def get_prod_cargo_types(self, economy):
        # method used here for (1) unfortunate magic (2) guarding against invalid values
        # the magic is applied to prod_cargo_types, which industries can define as
        # (a) list of 1 or 2 labels ['GOOD', 'ENSP'] etc, in which case output is split 4:4 (evenly)
        # (b) list of 1 or 2 2-tuples [('GOOD', 6), ('ENSP', 2)], in which case output is split 6:2 unevenly)
        # the uneven case is much rarer, and should only be used for balancing industries where one cargo is strictly a by-product
        prod_cargo_types = self.get_property('prod_cargo_types', economy)
        if prod_cargo_types is None:
            # returning None causes some things to explode in docs, which I should fix, but haven't, this patches it with jank
            return []
        else:
            # guard against too many cargos being defined
            if len(prod_cargo_types) > 2:
                utils.echo_message("Too many produced cargos defined for " + self.id + ' in economy ' + economy.id)
            # now do some magic to support occasionally using output ratios other than 50:50;
            # magic is bad, but so is manually adjusting more than 80 industries :|
            result = []
            for i in prod_cargo_types:
                if isinstance(i, str):
                    if len(prod_cargo_types) == 2:
                        result.append((i, 4))
                    else:
                        result.append((i, 8))
                else:
                    # assume it's a two tuple (no guards against other types here right now)
                    result.append(i)
                    # do guard against explicitly defining 4:4 splits (e.g. copy-paste-adjust mistakes), because that's pointless and makes any future migration harder
                    if i[1] == 4:
                        utils.echo_message("Explictly defining output ratio of 4 is pointless for industry " + self.id + ' in economy ' + economy.id + ".  4 is the default if no value is defined.")
            # guard against ratios that don't add up to 8 (values other than 8 make no sense)
            if len(prod_cargo_types) > 0:
                sum_of_output_ratios = 0
                for label, output_ratio in result:
                    sum_of_output_ratios += output_ratio
                if sum_of_output_ratios != 8:
                    utils.echo_message("Sum of output ratios must be 8: sum is " + str(sum_of_output_ratios) + " for industry " + self.id + ' in economy ' + economy.id)
            return result

    def get_another_industry(self, id):
        return get_another_industry(id)

    @property
    def incompatible_industries(self):
        # there's no sensible way to get incompatible_industries from here, it has to be passed in when rendering templates
        # there are genuine performance reasons to have incompatibility calculated once and only once by firs.py
        utils.echo_message('Incompatible industries not implemented in industry.py, must be passed from firs.py at render time')

    def validate_map_colour(self, value):
        # we need to guard against map colours that have poor contrast with the green, dark green and purple maps
        # see the list of valid colours in global_constants
        # !! this might need special case handling for water industries (list.extend() in global constants?)
        if int(value) not in global_constants.valid_industry_map_colours:
            utils.echo_message("Industry " + self.id +  " uses map Colour " + value + " which is invalid (lacks contrast)")


    def get_output_ratio(self, cargo_num, economy):
        prod_cargo_types = self.get_prod_cargo_types(economy)
        if cargo_num > len(prod_cargo_types):
            # cargo isn't defined, just return 8, does no harm and prevents upstream code choking (returning 0 might lead to a divide-by-zero)
            return 8
        else:
            return prod_cargo_types[cargo_num - 1][1]

    def unpack_sprite_or_spriteset(self, sprite_or_spriteset, construction_state_num=3, terrain_type='', date_variation_num='0'):
        date_variation_suffix = '_' + str(date_variation_num)
        if terrain_type != '':
            suffix = '_' + terrain_type
        else:
            suffix = ''
        if isinstance(sprite_or_spriteset, Spriteset):
            # tiny optimisation, don't use an animation sprite selector if there is no animation
            if sprite_or_spriteset.animation_rate > 0:
                if sprite_or_spriteset.custom_sprite_selector:
                    sprite_selector = str(sprite_or_spriteset.animation_rate) + '*' + sprite_or_spriteset.custom_sprite_selector
                else:
                     sprite_selector = str(sprite_or_spriteset.animation_rate) + '* (animation_frame)'
            else:
                sprite_selector = '0'
            if construction_state_num == 3 or self.default_industry_properties.override_default_construction_states == False:
                return sprite_or_spriteset.id + date_variation_suffix + suffix  + '(' + sprite_selector + ')'
            else:
                return sprite_or_spriteset.id + '_spriteset_default_construction_state_' + str(construction_state_num) + '(' + sprite_selector + ')'
        if isinstance(sprite_or_spriteset, Sprite):
            return getattr(sprite_or_spriteset, 'sprite_number' + suffix)

    def render_nml(self, incompatible_industries):
        # incompatible industries isn't known at init time, only at compile time, so it has to be passed in
        industry_template = templates[self.template]
        templated_nml = utils.unescape_chameleon_output(industry_template(industry=self,
                                                                          global_constants=global_constants,
                                                                          incompatible_industries=incompatible_industries,
                                                                          economies=registered_economies,
                                                                          utils=utils))
        return templated_nml


class IndustryPrimary(Industry):
    """ Industries that produce cargo and (optionally) boost production if supplies are delivered """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = kwargs.get('template', 'industry_primary.pynml')
        self.supply_requirements = None # default None, set appropriately by subclasses
        self.perm_storage = IndustryPermStorage(['var_num_supplies_delivered', # amount of supplies delivered this month
                                                 'var_num_supplies_delivered_last',
                                                 'var_num_supplies_delivered_bef_last',
                                                 'var_current_supplies_prod_factor',
                                                 'unused',
                                                 'unused',
                                                 'unused',
                                                 'unused',
                                                 'unused',
                                                 'unused',
                                                 'unused',
                                                 'unused',
                                                 'unused',
                                                 'unused',
                                                 'unused',
                                                 'unused'])


class IndustryPrimaryExtractive(IndustryPrimary):
    """
        Industry that is extractive AND has production boosted by delivery of ENSP (mines and similar)
        Sparse subclass of IndustryPrimary, do not add much to this, it's subclassed once already
    """
    def __init__(self, **kwargs):
        kwargs['accept_cargo_types'] = ['ENSP']
        kwargs['life_type'] = 'IND_LIFE_TYPE_EXTRACTIVE'
        super().__init__(**kwargs)
        self.supply_requirements = [0, 'PRIMARY', 1] # janky use of a un-named list for historical reasons (2nd item is string prefix, 3rd is multiplier of requirements parameters)


class IndustryPrimaryOrganic(IndustryPrimary):
    """
        Industry that is organic AND has production boosted by delivery of FMSP (farms and similar)
        Sparse subclass of IndustryPrimary, do not add much to this, it's subclassed once already
    """
    def __init__(self, **kwargs):
        kwargs['accept_cargo_types'] = ['FMSP']
        kwargs['life_type'] = 'IND_LIFE_TYPE_ORGANIC'
        super().__init__(**kwargs)
        self.supply_requirements = [0, 'PRIMARY', 1] # janky use of a un-named list for historical reasons (2nd item is string prefix, 3rd is multiplier of requirements parameters)


class IndustryPrimaryPort(IndustryPrimary):
    """
        Industry that is import-export AND has production boosted by delivery of arbitrary cargos (ports and similar)
        Sparse subclass of IndustryPrimary, do not add much to this, it's subclassed once already
    """
    def __init__(self, **kwargs):
        kwargs['life_type'] = 'IND_LIFE_TYPE_BLACK_HOLE'
        super().__init__(**kwargs)
        self.supply_requirements = [0, 'PORT', 8] # janky use of a un-named list for historical reasons (2nd item is string prefix, 3rd is multiplier of requirements parameters)


class IndustryPrimaryNoSupplies(Industry):
    """ Industry that does not accept supplies and does not change production amounts during game """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = kwargs.get('template', 'industry_primary_no_supplies.pynml')


class IndustryPrimaryTownProducer(Industry):
    """ Industry that locates near towns, with production amount related to town population """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = kwargs.get('template', 'industry_primary_town_producer.pynml')
        self.supply_requirements = None # supplies do not boost this type of primary

class IndustrySecondary(Industry):
    """ Processing industries: input cargo(s) -> output cargo(s) """
    def __init__(self, **kwargs):
        kwargs['life_type'] = 'IND_LIFE_TYPE_PROCESSING'
        super().__init__(**kwargs)
        self.template = kwargs.get('template', 'industry_secondary.pynml')
        self.combined_cargos_boost_prod = kwargs.get('combined_cargos_boost_prod', False)
        self.perm_storage = IndustryPermStorage(['unused',
                                                 'ratio_input_1', # output per 8 units input of cargo 1; can be made temporary
                                                 'ratio_input_2', # output per 8 units input of cargo 2; can be made temporary
                                                 'ratio_input_3', # output per 8 units input of cargo 3; can be made temporary
                                                 'leftover_cargo_1', # non-processed cargo 1
                                                 'leftover_cargo_2', # non-processed cargo 2
                                                 'leftover_cargo_3', # non-processed cargo 3
                                                 'unused',
                                                 'unused',
                                                 'unused',
                                                 'date_received_1', # date of last cargo 1 delivery
                                                 'date_received_2', # date of last cargo 2 delivery
                                                 'date_received_3', # date of last cargo 2 delivery
                                                 'unused',
                                                 'unused',
                                                 'closure_counter' # months without delivery, same as primary industries
                                                 ])
        # guard against prospect chance kword being set, it's pure cruft for secondary industry (harmless, but needless)
        if 'prospect_chance' in kwargs:
            utils.echo_message("prospect_chance passed in kwargs for " + self.id + "; secondary industries should not set prospect_chance")

    def get_prod_ratio(self, cargo_num, economy):
        if cargo_num > len(self.get_property('processed_cargos_and_output_ratios', economy)):
            return 0
        else:
            return self.get_property('processed_cargos_and_output_ratios', economy)[cargo_num - 1][1]

    def get_accept_cargo_types(self, economy):
        # method used here for (1) guarding against invalid values (2) so that it can be over-ridden by industry subclasses as needed
        accept_cargo_types = [i[0] for i in self.get_property('processed_cargos_and_output_ratios', economy)]
        # guard against too many cargos being defined
        if len(accept_cargo_types) > 3:
            utils.echo_message("Too many accepted cargos defined for " + self.id + ' in economy ' + economy.id)
        return accept_cargo_types

    def get_boost(self, supplied_cargo_num, boosted_cargo_num, economy):
        if self.combined_cargos_boost_prod:
            if boosted_cargo_num > len(self.get_property('processed_cargos_and_output_ratios', economy)):
                return 0
            else:
                return self.get_prod_ratio(supplied_cargo_num, economy)
        return 0


class IndustryTertiary(Industry):
    """ Industries that consume cargo and don't produce much (or anything), typically black holes in or near towns """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = 'industry_tertiary.pynml'
        # no perm_storage needed currently
