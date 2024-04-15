"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from collections import deque
import copy
import os.path
import json

currentdir = os.curdir

import global_constants as global_constants
import utils as utils

from chameleon import PageTemplateLoader  # chameleon used in most template cases

# setup the places we look for templates
templates = PageTemplateLoader(
    os.path.join(currentdir, "src", "templates"), format="text"
)

from perm_storage_mappings import register_perm_storage_mapping, get_perm_num
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
    """Base class to hold industry tiles"""

    def __init__(self, industry_id, id, **kwargs):
        self.id = id
        self.numeric_id = global_constants.tile_numeric_ids[
            self.id
        ]  # don't fail this silently, tile id must be defined
        self.land_shape_flags = kwargs.get("land_shape_flags", "0")
        self.location_checks = kwargs.get("location_checks")
        # check for setting both land_shape_flags and location_checks
        # it's a cause of coder-error when I forget that land_shape_flags will be ignored when location_check is used
        if (
            self.land_shape_flags != "0"
            and len(self.location_checks.get_render_tree(self.id, industry_id)) > 0
        ):
            raise Exception(
                "Tile "
                + self.id
                + ": land_shape_flags are set but will be ignored because the tile also uses location_checks cb.  Only set one of these attributes."
            )
        self._special_flags = kwargs.get("special_flags", [])
        self.foundations = kwargs.get("foundations", None)
        self.autoslope = kwargs.get("autoslope", None)
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
        self.animation_length = kwargs.get(
            "animation_length", 1
        )  # allowed values 1-253
        self.animation_looping = kwargs.get("animation_looping", False)
        self.animation_speed = kwargs.get("animation_speed", 0)
        self.custom_animation_next_frame = kwargs.get(
            "custom_animation_next_frame", None
        )
        self.custom_animation_control = kwargs.get("custom_animation_control", None)
        self.random_trigger = kwargs.get("random_trigger", None)

    @property
    def special_flags(self):
        flags = ["INDTILE_FLAG_ACCEPT_ALL"]
        flags.extend(self._special_flags)
        return "bitmask(" + ",".join(flags) + ")"

    @property
    def animation_triggers(self):
        if self.custom_animation_control is None:
            return "bitmask()"
        else:
            return self.custom_animation_control["animation_triggers"]

    def animation_macros(self):
        template = templates["animation_macros.pynml"]
        return template.macros


class TileLocationChecks(object):
    """Class to hold location checks for a tile"""

    def __init__(self, **kwargs):
        self.always_allow_founder = kwargs.get(
            "always_allow_founder", True
        )  # occasionally this needs to be set False, e.g. for tiles that demand specific land shape
        self.disallow_slopes = kwargs.get("disallow_slopes", False)
        self.disallow_steep_slopes = kwargs.get("disallow_steep_slopes", False)
        self.disallow_industry_adjacent = kwargs.get(
            "disallow_industry_adjacent", False
        )
        self.require_effectively_flat = kwargs.get("require_effectively_flat", False)
        self.require_houses_nearby = kwargs.get("require_houses_nearby", False)
        self.require_road_adjacent = kwargs.get("require_road_adjacent", False)
        self.require_coast = kwargs.get("require_coast", False)
        self.disallow_above_snowline = kwargs.get("disallow_above_snowline", False)
        self.disallow_below_snowline = kwargs.get("disallow_below_snowline", False)
        self.disallow_desert = kwargs.get("disallow_desert", False)
        self.disallow_coast = kwargs.get("disallow_coast", False)

    def get_render_tree(self, tile_id, industry_id):
        switch_prefix = tile_id + "_lc_"
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
            for x in range(-1 * distance, distance + 1):
                for y in range(-1 * distance, distance + 1):
                    search_points.append((x, y))
            result.append(TileLocationCheckRequireHousesNearby(search_points))

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
    """Sparse class to base TileLocationCheck subclasses on"""

    @property
    def macro(self):
        return templates["location_check_macros_tile.pynml"].macros[self.macro_name]


class TileLocationCheckDisallowSlopes(TileLocationCheck):
    """
    Prevent building on all slopes
    Not to be confused with TileLocationCheckRequireEffectivelyFlat
    """

    def __init__(self):
        self.switch_result = None  # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.macro_name = "disallow_slopes"


class TileLocationCheckDisallowSteepSlopes(TileLocationCheck):
    """Prevent building on steep slopes (but not normal slopes)"""

    def __init__(self):
        self.switch_result = None  # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.macro_name = "disallow_steep_slopes"


class TileLocationCheckDisallowIndustryAdjacent(TileLocationCheck):
    """
    Prevent directly adjacent to another industry, used by most industries, but not all
    1. Makes it too hard for the game to find a location for some types (typically large flat industries)
    2. Not necessary for most town industries
    """

    def __init__(self):
        self.switch_result = "return CB_RESULT_LOCATION_ALLOW"  # default result, value may also be id for next switch
        self.switch_entry_point = None
        self.macro_name = "disallow_industry_adjacent"


class TileLocationCheckRequireEffectivelyFlat(TileLocationCheck):
    """
    Check that the highest corner of all tiles is equal to the highest corner of the north tile
    This permits building on slopes with foundations,
    but prevents industry graphics being 'broken' by being drawn at different height levels.
    Not to be confused with TileLocationCheckDisallowSlopes
    """

    def __init__(self):
        self.switch_result = None  # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.macro_name = "require_effectively_flat"


class TileLocationCheckRequireHousesNearby(TileLocationCheck):
    """Requires houses at offset x, y (to be fed by circular tile search)"""

    def __init__(self, search_points):
        self.switch_result = "return CB_RESULT_LOCATION_ALLOW"  # default result, value may also be id for next switch
        self.switch_entry_point = None
        self.macro_name = "require_houses_nearby"
        self.search_points = search_points


class TileLocationCheckRequireRoadAdjacent(TileLocationCheck):
    """Requires road on adjacent tile(s), with configurable directions"""

    def __init__(self):
        self.switch_result = "return CB_RESULT_LOCATION_ALLOW"  # default result, value may also be id for next switch
        self.switch_entry_point = None
        self.macro_name = "require_road_adjacent"


class TileLocationCheckRequireSea(TileLocationCheck):
    def __init__(self):
        self.switch_result = "return CB_RESULT_LOCATION_ALLOW"  # default result, value may also be id for next switch
        self.switch_entry_point = None
        self.macro_name = "require_sea_tile"


class TileLocationCheckRequireSlope(TileLocationCheck):
    def __init__(self):
        self.switch_result = "return CB_RESULT_LOCATION_ALLOW"  # default result, value may also be id for next switch
        self.switch_entry_point = None
        self.macro_name = "require_slope"


class TileLocationCheckDisallowDesert(TileLocationCheck):
    """Prevent building on desert tiles"""

    def __init__(self):
        self.switch_result = None  # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.macro_name = "disallow_desert"


class TileLocationCheckDisallowCoast(TileLocationCheck):
    """Prevent building on desert tiles"""

    def __init__(self):
        self.switch_result = None  # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.macro_name = "disallow_coast_or_water"


class TileLocationCheckDisallowAboveSnowline(TileLocationCheck):
    """Prevent building above snowline"""

    def __init__(self):
        self.switch_result = None  # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.minh = 0
        self.maxh = "snowline_height"
        self.outrange = "return string(STR_ERR_LOCATION_NOT_ABOVE_SNOWLINE)"
        self.macro_name = "require_height_range"


class TileLocationCheckDisallowBelowSnowline(TileLocationCheck):
    """Prevent building above snowline"""

    def __init__(self):
        self.switch_result = None  # no default value for this check, it may not be the last check in a chain
        self.switch_entry_point = None
        self.minh = "snowline_height"
        self.maxh = 255
        self.outrange = "return string(STR_ERR_LOCATION_NOT_BELOW_SNOWLINE)"
        self.macro_name = "require_height_range"


class TileLocationCheckFounder(TileLocationCheck):
    """
    Used to over-ride non-essential checks when player is building
    Some tile checks relating to landscape are essential and are placed before player check
    """

    def __init__(self):
        self.switch_result = "return CB_RESULT_LOCATION_ALLOW"  # default result, value may also be id for next switch
        self.switch_entry_point = None
        self.macro_name = "allow_player"


class Sprite(object):
    """Base class to hold simple sprites (using numbers from a base set)"""

    def __init__(
        self,
        sprite_number,
        sprite_number_snow="",
        xoffset=0,
        yoffset=0,
        zoffset=0,
        xextent=16,
        yextent=16,
        zextent=16,
        always_draw=0,
    ):
        # there are few shorthand constants for specific sprite numbers (legacy from CPP templating, kind of useful to keep)
        sprite_constants = {"GROUNDTILE_MUD_TRACKS": 2022, "GROUNDTILE_SLABS": 1420}
        if sprite_number in sprite_constants.keys():
            self.sprite_number = sprite_constants[sprite_number]
        else:
            self.sprite_number = sprite_number  # can also provide raw nml with the sprite number for things like controlling animation frame
        self.sprite_number_snow = (
            sprite_number_snow if sprite_number_snow != "" else self.sprite_number
        )  # set a snow sprite explicitly (optional).
        # optional parameters for offsets and extents for the *spritelayout* to use with this sprite (read nml spritelayout docs to see use)
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.zoffset = zoffset  # set extents to x/y/z sizes of largest sprite in spriteset, or omit for default (16)
        self.xextent = xextent
        self.yextent = yextent
        self.zextent = zextent
        self.always_draw = always_draw


class SmokeSprite(object):
    """Base class to handle smoke sprites (using smoke sprite numbers from a base set)"""

    def __init__(
        self,
        smoke_type,
        xoffset=0,
        yoffset=0,
        zoffset=0,
        hide_sprite=0,
        animation_frame_offset=0,
    ):
        # animation_frame_offset can be used (in some cases) to desynchronise animations in the same tile (or in some cases within the same industry as an alternative to animation triggers)
        # defaults
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.zoffset = zoffset
        self.xextent = 16
        self.yextent = 16
        self.zextent = 16
        self.hide_sprite = hide_sprite
        if smoke_type == "dark_smoke_small":
            self.sprite_number = "2040 + (animation_frame / 4)"
            self.zoffset = str(self.zoffset) + "+ animation_frame"
            self.xextent = 11
            self.zextent = 7
            self.hide_sprite = "animation_frame > 19"
        if smoke_type == "white_smoke_small":
            self.sprite_number = "3079 + (animation_frame / 4)"
            self.zoffset = str(self.zoffset) + "+ animation_frame"
            self.xextent = 11
            self.zextent = 7
            self.hide_sprite = "animation_frame > 19"
        if smoke_type == "white_smoke_big":
            self.sprite_number = (
                "3701 + ((animation_frame + " + str(animation_frame_offset) + ")%8)"
            )
            self.xextent = 15
            self.yextent = 7
            self.zextent = 7


class Spriteset(object):
    """Base class to hold industry spritesets"""

    # !! arguably this should be two different classes, one for building/feature spritesets, and one for ground spritesets
    def __init__(
        self,
        id,
        sprites=[],
        type="",
        xoffset=0,
        yoffset=0,
        zoffset=0,
        xextent=16,
        yextent=16,
        animation_rate=0,
        custom_sprite_selector=None,
        always_draw=0,
        num_sprites_to_autofill=1,
    ):
        self.id = id
        self.sprites = (
            sprites  # a list of sprites 6-tuples in format (x, y, w, h, xoffs, yoffs)
        )
        self.type = type  # set to ground or other special types, or omit for default (building, greeble, foundations etc - graphics from png named same as industry)
        self.animation_rate = animation_rate  # (must be int) optional multiplier to tile's animation rate, set to 1 for same as tile, >1 for faster; leave default (0) to disable animation; < 1 isn't valid and nml won't compile it
        self.custom_sprite_selector = custom_sprite_selector
        self.num_sprites_to_autofill = num_sprites_to_autofill  # create n sprites per sprite passed (optional convenience method for use where spriteset sizes must match; set value to same as size of largest spriteset)
        # optional parameters for offsets and extents for the *spritelayout* to use with this sprite (read nml spritelayout docs to see use)
        # (more convenient to store on the sprite, even though consumed by spritelayout, as they tend to be constant in most cases where the sprite is used)
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.zoffset = zoffset
        self.xextent = xextent  # set extents to x/y/z sizes of largest sprite in spriteset, or omit for default (16)
        self.yextent = yextent
        self.zextent = 32  # it's of limited use setting zextent, just make it 32 and be done with it
        self.always_draw = always_draw


class SpriteLayout(object):
    """Base class to hold spritelayouts for industry spritelayouts"""

    def __init__(
        self,
        id,
        ground_sprite,
        ground_overlay,
        building_sprites,
        smoke_sprites=[],
        fences=[],
        perma_fences=[],
        magic_trees=[],
        terrain_aware_ground=False,
        tile=None,
        add_to_object_num=None,
    ):
        self.id = id
        self.ground_sprite = ground_sprite
        self.ground_overlay = ground_overlay
        self.building_sprites = building_sprites
        self.smoke_sprites = smoke_sprites
        # Valid fence values: 'ne', 'se', 'sw', 'nw'.  Order is arbitrary.
        self.fences = fences
        # optionally prevent fences hiding when a station is adjacent.  Same string values as fences.
        self.perma_fences = perma_fences
        self.magic_trees = magic_trees
        self.terrain_aware_ground = terrain_aware_ground  # we don't draw terrain (and climate) aware ground unless explicitly required by the spritelayout, it makes nml compiles slower
        # as of September 2022, spritelayouts can define which tile they use
        # - this is optional as a migration strategy, but is intended to be the only supported approach in future
        self.tile = tile
        # optionally spritelayouts can cause objects to be defined
        self.add_to_object_num = add_to_object_num

    def resolve_tile(self, industry):
        for tile in industry.tiles:
            if tile.id == self.tile:
                return tile


class MagicSpritelayoutSlopeAwareTrees(object):
    """Occasionally we need magic.  If we're going magic, let's go full on magic.  This one makes 4 climate-aware trees on a slope-aware ground tile"""

    # Class attributes eh?  Might as well, these aren't supposed to be mutable

    # there are 19 slopes to handle, as per https://newgrf-specs.tt-wiki.net/wiki/NML:List_of_tile_slopes
    # format is slope_num: (tuples of x, y for 4 or 9 trees)

    slopes_4 = {
        0: ((2, 2), (2, 9), (9, 2), (9, 9)),  # done
        1: ((2, 2), (2, 9), (9, 2), (9, 9)),
        2: ((2, 2), (2, 9), (9, 2), (9, 9)),
        3: ((2, 0), (0, 6), (6, 0), (6, 6)),  # done
        4: ((2, 2), (2, 9), (9, 2), (9, 9)),
        5: ((2, 2), (2, 9), (9, 2), (9, 9)),
        6: ((2, 0), (0, 6), (8, 1), (6, 6)),  # done
        7: ((0, 0), (0, 5), (5, 0), (5, 5)),  # done
        8: ((2, 2), (2, 9), (9, 2), (9, 9)),
        9: ((1, 2), (2, 9), (8, 2), (9, 9)),  # done
        10: ((2, 2), (2, 9), (9, 2), (9, 9)),
        11: ((0, 0), (0, 8), (7, 0), (7, 7)),  # done
        12: ((2, 2), (2, 9), (9, 2), (9, 9)),
        13: ((2, 2), (2, 9), (9, 2), (9, 9)),
        14: ((1, 1), (-1, 6), (8, 2), (6, 6)),  # done
        23: ((0, 0), (0, 5), (5, -2), (4, 4)),  # done
        27: ((0, 0), (0, 7), (5, -2), (5, 5)),  # done
        29: ((0, 0), (0, 7), (7, 0), (7, 7)),  # done
        30: ((0, 0), (-1, 4), (7, 0), (6, 5)),
    }  # done

    slopes_9 = {
        0: (
            (0, 0),
            (0, 5),
            (0, 11),
            (5, 0),
            (5, 5),
            (5, 11),
            (11, 0),
            (11, 5),
            (11, 11),
        ),  # done
        1: (
            (0, 0),
            (0, 5),
            (0, 11),
            (5, -1),
            (4, 4),
            (5, 11),
            (9, -2),
            (10, 4),
            (11, 11),
        ),  # done
        2: (
            (0, 0),
            (0, 5),
            (0, 9),
            (5, 0),
            (4, 4),
            (4, 8),
            (10, 0),
            (9, 4),
            (7, 7),
        ),  # done
        3: (
            (-1, -3),
            (-1, 3),
            (-1, 9),
            (3, -3),
            (3, 2),
            (3, 8),
            (7, -3),
            (7, 2),
            (7, 7),
        ),  # done
        4: (
            (0, 0),
            (0, 4),
            (-2, 9),
            (5, 0),
            (5, 4),
            (5, 10),
            (11, 0),
            (11, 4),
            (11, 11),
        ),  # done
        5: (
            (0, 0),
            (-2, 3),
            (-4, 8),
            (5, 0),
            (3, 3),
            (3, 9),
            (10, 0),
            (8, 3),
            (11, 11),
        ),  # part done, hard to test
        6: (
            (0, 0),
            (-2, 3),
            (-4, 8),
            (5, 0),
            (3, 3),
            (1, 8),
            (10, 0),
            (8, 3),
            (6, 8),
        ),  # done
        7: (
            (-3, -3),
            (-3, 3),
            (-3, 7),
            (2, -3),
            (2, 2),
            (2, 7),
            (7, -3),
            (7, 2),
            (7, 7),
        ),  # done
        8: (
            (0, 0),
            (0, 5),
            (0, 11),
            (5, 0),
            (5, 5),
            (5, 11),
            (11, 0),
            (11, 5),
            (11, 11),
        ),
        9: (
            (-1, -1),
            (0, 5),
            (1, 10),
            (3, -1),
            (4, 5),
            (5, 10),
            (8, -1),
            (9, 5),
            (10, 10),
        ),  # done
        10: (
            (-3, -3),
            (-3, 3),
            (1, 10),
            (2, -3),
            (2, 2),
            (5, 9),
            (10, 1),
            (9, 5),
            (8, 8),
        ),  # part done, hard to test
        11: (
            (-3, -3),
            (-3, 3),
            (-1, 10),
            (2, -3),
            (2, 2),
            (3, 9),
            (7, -3),
            (7, 2),
            (7, 7),
        ),  # done
        12: (
            (0, 0),
            (-1, 4),
            (-3, 8),
            (5, 0),
            (5, 5),
            (4, 10),
            (11, 0),
            (11, 5),
            (11, 11),
        ),  # done
        13: (
            (0, 0),
            (0, 5),
            (-2, 9),
            (4, 0),
            (5, 5),
            (4, 10),
            (9, -2),
            (10, 5),
            (11, 11),
        ),  # done
        14: (
            (0, 0),
            (0, 5),
            (0, 10),
            (5, 0),
            (5, 5),
            (5, 10),
            (10, 0),
            (9, 4),
            (7, 7),
        ),  # done
        23: (
            (0, 0),
            (-2, 2),
            (-5, 7),
            (2, 0),
            (2, 2),
            (-1, 6),
            (8, -2),
            (5, 0),
            (4, 4),
        ),  # part done, hard to test
        27: (
            (0, 0),
            (0, 5),
            (-1, 11),
            (2, 0),
            (3, 5),
            (3, 10),
            (5, -5),
            (6, 2),
            (7, 8),
        ),  # done
        29: (
            (-3, 0),
            (-3, 4),
            (-3, 8),
            (3, 0),
            (1, 3),
            (4, 10),
            (8, -3),
            (10, 4),
            (11, 11),
        ),  # part done, hard to test
        30: (
            (-3, 0),
            (-5, 2),
            (-8, 4),
            (3, 0),
            (1, 3),
            (-1, 5),
            (10, -1),
            (9, 3),
            (7, 7),
        ),
    }  # done

    def __init__(self, industry, base_id, config):
        # !! ground sprites are slaved to sprite numbers currently, needs extending for spritesets
        ground_sprite = industry.add_sprite(
            sprite_number=str(config["ground_sprite"])
            + " + slope_to_sprite_offset(nearby_tile_slope(0,0))"
        )

        # tile has 4 or 9 tree positions, so 4 or 9 tree sprites/spritesets are required, just repeat as necessary if some positions use same sprite
        # trees can be ints (sprite numbers for baseset), or lists of tuples (for spritesets, with optional animation)
        trees_default = config["trees_default"]
        trees_snow = config.get(
            "trees_snow", trees_default
        )  # defining snow trees is optional
        trees_tropic = config.get(
            "trees_tropic", trees_default
        )  # defining tropic trees is optional
        if len(trees_snow) != len(trees_default):
            raise Exception(
                "Number of snow trees needs to match number of default trees for "
                + industry.id
            )
        if len(trees_tropic) != len(trees_default):
            raise Exception(
                "Number of tropic trees needs to match number of default trees for "
                + industry.id
            )

        num_trees = len(
            trees_default
        )  # whether 4 or 9 trees are used is determined by number of default trees passed
        slopes = {4: self.slopes_4, 9: self.slopes_9}[num_trees]

        trees = {}
        for terrain, tree_config in {
            "default": trees_default,
            "snow": trees_snow,
            "tropic": trees_tropic,
        }.items():
            trees[terrain] = []
            for index, tree in enumerate(tree_config):
                if isinstance(tree, int):  # we have a sprite, just store the number
                    trees[terrain].append(tree)
                if isinstance(tree, list):
                    print("tree is spriteset: not implemented yet")
                    # extend spriteset support here (noting that spritesets are lists of tuples as they can be animated also)
                    # my intent was simply to pass the offsets to this, as that should be all that is needed

        for slope, offsets in slopes.items():
            industry.add_spritelayout(
                id=base_id + str(slope),
                ground_sprite=ground_sprite,
                ground_overlay=ground_sprite,  # slight hax, assume we can just reuse ground for overlay
                magic_trees=[
                    MagicTree(trees, offsets, tree_num=tree_num)
                    for tree_num in range(num_trees)
                ],
                building_sprites=[],
            )

        id_slope_mapping = {
            base_id + str(slope): slope for slope in slopes
        }  # easier to match to format of slope switch in nml
        industry.add_slope_graphics_switch(
            base_id,
            default_result=base_id + "0",
            slope_spritelayout_mapping={
                slope: slope_id for slope_id, slope in id_slope_mapping.items()
            },
        )


class GRFObject(object):
    """Stubby class to hold objects - GRFObject to avoid conflating with built-in python classname"""

    def __init__(self, industry, add_to_object_num):
        # note spacing numeric part of id to add a leading 0 if needed, otherwise python lexical sort returns 'foo_1, foo_10, foo_2' etc
        self.id = f"{industry.id}_object_{add_to_object_num:02}"
        # we allocate up a range of up to 100 object numeric IDs per industry, using the industry numeric ID
        # this will keep object IDs relatively stable across releases unless the industry numeric ID changes or add_to_object_num changes
        if add_to_object_num > 99:
            raise BaseException(
                "Industry "
                + industry.id
                + " defines an object with numeric ID "
                + str(add_to_object_num)
                + " which exceeds the limit of 99"
            )
        self.numeric_id = (industry.numeric_id * 100) + add_to_object_num
        self.views = []
        self.industry = industry

    def add_view(self, spritelayout):
        self.views.append(spritelayout)
        # self.validate()

    def validate(self):
        # must be 1, 2, or 4 views https://newgrf-specs.tt-wiki.net/wiki/NML:Objects#Location_check_results
        if len(self.views) == 3:
            raise BaseException(
                self.id, "has 3 views defined, which is not permitted by spec"
            )
        # validation for case of too many views - shouldn't happen but eh
        if len(self.views) > 4:
            utils.echo_message(self.views)
            raise BaseException(
                self.id, "has too many views defined"
            )  # yair could do better?

    @property
    def tile(self):
        # all views in the object must resolve to one and only one industry tile
        # we use this for certain object properties / callbacks (such as animation, and possibly location checks)
        # check for mismatched tiles
        found_tiles = []
        for view in self.views:
            for x, y, spritelayout in view:
                found_tiles.append(spritelayout.resolve_tile(self.industry))
        if len(set(found_tiles)) != 1:
            raise BaseException(self.id, "tiles don't match:", found_tiles)
        else:
            # we have one and only one tile
            return found_tiles[0]

    @property
    def multi_tile_ground(self):
        result = []
        # only one view supported currently for multi_tile objects (could do more, but just 1 currently for basic simplicity)
        for x, y, spritelayout in self.views[0]:
            result.append([x, y, spritelayout.ground_sprite])
        return result

    @property
    def multi_tile_buildings(self):
        result = []
        # only one view supported currently for multi_tile objects (could do more, but just 1 currently for basic simplicity)
        for x, y, spritelayout in self.views[0]:
            for building_sprite in spritelayout.building_sprites:
                result.append([x, y, building_sprite])
        return result

    @property
    def animation_triggers(self):
        # object animation triggers don't match industry tile triggers, so remap
        result = []
        trigger_remap = {
            "ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE": "ANIM_TRIGGER_OBJ_BUILT",
            "ANIM_TRIGGER_INDTILE_TILE_LOOP": "ANIM_TRIGGER_OBJ_TILELOOP",
        }
        # split off some nml formatting to get the raw list
        triggers = (
            self.tile.animation_triggers.split("bitmask(")[1].split(")")[0].split(",")
        )
        # triggers from tile might be empty, strip those
        triggers = [i for i in triggers if i != ""]
        # this is expected to error if the trigger isn't found, it only mapped the triggers in use as of September 2022, not all possible triggers
        for trigger in triggers:
            result.append(trigger_remap[trigger])
        return "bitmask(" + ",".join(result) + ")"

    @property
    def size(self):
        view_sizes = []
        for view in self.views:
            x_values = [i[0] for i in view]
            y_values = [i[1] for i in view]
            view_size = (max(x_values), max(y_values))
            view_sizes.append(view_size)
        unique_sizes = list(set(view_sizes))
        if len(unique_sizes) > 1:
            raise BaseException(self.id, "views have different sizes / tile layouts")
        return [1 + unique_sizes[0][0], 1 + unique_sizes[0][1]]


class MagicTree(object):
    """Stubby class used in MagicSpriteLayoutSlopeAwareTrees; I just prefer object attribute access over an equivalent dict - Andy"""

    def __init__(self, trees, offsets, tree_num):
        self.default = trees["default"][tree_num]
        self.snow = trees["snow"][tree_num]
        self.tropic = trees["tropic"][tree_num]
        self.xoffset = offsets[tree_num][0]
        self.yoffset = offsets[tree_num][1]


class MagicSpritelayoutHarbourCoastFoundations(object):
    """
    Occasionally we need magic.  If we're going magic, let's go full on magic.
    This one provides the slope-aware foundations needed for coast tiles.
    Possibly could be used generically for all slopes, there's nothing specific to coasts in it, but other cases weren't needed when writing it.
    """

    # Class attributes eh?  Might as well, these aren't supposed to be mutable

    slope_spritelayout_nums = {
        0: "1",
        1: "4",
        2: "8",
        3: "2",
        4: "6",
        5: "5",
        6: "7",
        7: "1",
        8: "3",
        9: "4",
        10: "8",
        11: "2",
        12: "6",
        13: "5",
        14: "7",
    }

    spritelayout_foundations = {
        "1": [],
        "2": ["slope_sw_ne"],
        "3": ["se_nw", "ne_sw"],
        "4": ["ne_sw", "slope_nw_se"],
        "5": ["slope_ne_sw", "slope_nw_se"],
        "6": ["slope_ne_sw", "se_nw"],
        "7": ["slope_se_nw"],
        "8": ["slope_se_nw", "slope_sw_ne"],
    }

    def __init__(self, industry, base_id, config):
        for spritelayout_num, foundations in self.spritelayout_foundations.items():
            building_sprites = [
                config["foundation_sprites"][foundation_sprites]
                for foundation_sprites in foundations
            ]
            building_sprites.extend(config["building_sprites"])
            industry.add_spritelayout(
                id=base_id + str(spritelayout_num),
                ground_sprite=config[
                    "ground_sprite"
                ],  # should always be empty sprite for this magic layout
                ground_overlay=config[
                    "ground_sprite"
                ],  # should always be empty sprite for this magic layout
                building_sprites=building_sprites,
            )
        id_slope_mapping = {
            slope: base_id + str(spritelayout_num)
            for slope, spritelayout_num in self.slope_spritelayout_nums.items()
        }
        industry.add_slope_graphics_switch(
            base_id,
            default_result=base_id + "1",
            slope_spritelayout_mapping={
                slope_id: slope for slope_id, slope in id_slope_mapping.items()
            },
        )


class GraphicsSwitch(object):
    """base class for extra graphics switches"""

    def __init__(self, id, **kwargs):
        self.id = id


class GraphicsSwitchSlopes(GraphicsSwitch):
    """Class from which a slope-checking graphics switch can be generated, routing to appropriate spritelayout per slope type"""

    def __init__(self, id, slope_spritelayout_mapping, default_result):
        super().__init__(id)
        self.slope_spritelayout_mapping = slope_spritelayout_mapping
        self.default_result = default_result


class IndustryLayout(object):
    """Base class to hold industry layouts"""

    def __init__(
        self,
        industry,
        id,
        layout,
        excluded_outpost_layouts=[],
        validate_xy=True,
        validate_legacy_layout_defs=False,
    ):
        self.id = id
        self.industry = industry
        # as of September 2022 there are 2 formats accepted when defining layout
        #   -  a list of 4-tuples (SE offset from N tile, SW offset from N tile, tile identifier, identifier of spritelayout or next nml switch)
        #   -  a list of 3-tuples (SE offset from N tile, SW offset from N tile, identifier of spritelayout or next nml switch), where the spritelayout encapsulates the tile identifier
        # as of September 2022 these are stored in the ._layout private attr, then resolved by a .layout property method
        self._layout = layout
        self.excluded_outpost_layouts = excluded_outpost_layouts
        # validation can be optionally suppressed as combined layouts may be invalid until their xy offsets are shifted positive (for example)
        if validate_xy:
            self.validate_xy()
        # support whilst migrating layout_defs to remove tile ids
        if validate_legacy_layout_defs:
            self.validate_legacy_layout_defs()

    def validate_xy(self):
        # in-game industry layouts must not have negative xy offsets
        for x, y, tile_id, spritelayout_id in self.layout:
            for offset_dir in [x, y]:
                if offset_dir < 0:
                    raise BaseException(
                        "Negative values are invalid for x or y offsets: "
                        + self.id
                        + " ("
                        + str(x)
                        + ", "
                        + str(y)
                        + ")"
                    )
        # xy offset pairs must be unique per layout
        xy_offsets = [(i[0], i[1]) for i in self.layout]
        for x, y in xy_offsets:
            if xy_offsets.count((x, y)) > 1:
                raise BaseException(
                    "Repeated xy offset pair: " + self.id + " " + str((x, y))
                )

    def validate_legacy_layout_defs(self):
        # catch legacy layout_defs
        legacy_found = False
        for layout_def in self._layout:
            if len(layout_def) == 4:
                legacy_found = True
                for spritelayout in self.industry.spritelayouts:
                    if spritelayout.id == layout_def[3]:
                        if spritelayout.tile is not None:
                            utils.echo_message(
                                "tile defs migrated, but legacy layout def found for "
                                + self.industry.id
                                + " "
                                + str(layout_def)
                            )
                            break
        if legacy_found:
            utils.echo_message(
                "legacy layout def(s) found for " + self.industry.id + " " + self.id
            )

    @property
    def layout(self):
        result = []
        for layout_def in self._layout:
            if len(layout_def) == 3:
                tile = None
                if layout_def[2] == "spritelayout_null_water":
                    tile = "255"
                if layout_def[2] == "spritelayout_null_station":
                    tile = "24"
                #  resolve the spritelayout by ID
                for spritelayout in self.industry.spritelayouts:
                    if spritelayout.id == layout_def[2]:
                        if spritelayout.tile == None:
                            raise BaseException("No tile defined for", spritelayout.id)
                        else:
                            tile = spritelayout.tile
                        break
                # not found, look in other book-keeping lists of tile ids
                if tile == None:
                    tile = self.industry.magic_spritelayout_tile_ids[layout_def[2]]
                if tile == None:
                    raise BaseException(
                        self.id
                        + " - no spritelayout found matching id given by "
                        + str(layout_def)
                    )
                else:
                    # redefine the layout def
                    layout_def = (
                        layout_def[0],
                        layout_def[1],
                        tile,
                        layout_def[2],
                    )
            # write the original or modified layout def to result,
            result.append(layout_def)
        if len(result) == 0:
            # something went wrong, probably fancy conditions somewhere eh?
            raise BaseException("layout resolver failed for " + self.id)
        return result

    @property
    def layout_rotated_90(self):
        # Rotate 90 degrees clockwise
        rotated_layout = [
            (tile_def[1], self.max_x - tile_def[0], tile_def[2], tile_def[3])
            for tile_def in self.layout
        ]
        return rotated_layout

    @property
    def layout_rotated_180(self):
        # Rotate 180 degrees
        rotated_layout = [
            (
                self.max_x - tile_def[0],
                self.max_y - tile_def[1],
                tile_def[2],
                tile_def[3],
            )
            for tile_def in self.layout
        ]
        return rotated_layout

    @property
    def layout_rotated_270(self):
        # Rotate 270 degrees clockwise
        rotated_layout = [
            (self.max_y - tile_def[1], tile_def[0], tile_def[2], tile_def[3])
            for tile_def in self.layout
        ]
        return rotated_layout

    @property
    def min_x(self):
        return min([i[0] for i in self.layout])

    @property
    def min_y(self):
        return min([i[1] for i in self.layout])

    @property
    def max_x(self):
        return max([i[0] for i in self.layout])

    @property
    def max_y(self):
        return max([i[1] for i in self.layout])

    @property
    def xy_dimensions(self):
        # add 1 as the xy are zero based indexes, and we want total tiles
        return (1 + self.max_x - self.min_x, 1 + self.max_y - self.min_y)


class IndustryLocationChecks(object):
    """Class to hold location checks for an industry"""

    def __init__(self, industry, location_args={}):
        self.industry = industry
        self.same_type_distance = location_args.get("same_type_distance", None)
        self.near_at_least_one_of_these_keystone_industries = location_args.get(
            "near_at_least_one_of_these_keystone_industries", None
        )
        if self.near_at_least_one_of_these_keystone_industries is not None:
            utils.echo_message(
                "near_at_least_one_of_these_keystone_industries set by",
                industry.id,
                "- should be in economy location checks only",
                "(is this supported yet?)",
                message_type="info",
            )
        self.require_cluster = location_args.get("require_cluster", None)
        self.require_town_industry_count = location_args.get(
            "require_town_industry_count", None
        )
        self.require_town_min_population = location_args.get(
            "require_town_min_population", None
        )
        self.location_check_industry_disallow_too_far_from_coast = location_args.get(
            "location_check_industry_disallow_too_far_from_coast", None
        )
        # this is custom to grain mill, can be made generic if needed
        self.flour_mill_layouts_by_date = location_args.get(
            "flour_mill_layouts_by_date", None
        )
        # economies may optionally define specific biomes which industries must locate in for that economy
        self.economy_biome_checks = {}

    def get_pre_player_founding_checks(self, incompatible_industries):
        result = []

        if self.flour_mill_layouts_by_date:
            result.append(IndustryLocationCheckGrainMillLayoutsByDate())

        return result

    def get_post_player_founding_checks_AND(self, incompatible_industries):
        # checks where all conditions must be satisfied
        result = []

        if self.require_cluster:
            # special case if clustering is used, require_cluster check handles max distance and cluster counts...
            # ...and min distance is set to 20 for all types (as all clustered industries were using this value at time of writing)
            result.append(
                IndustryLocationCheckCluster(self.industry.id, self.require_cluster)
            )
            result.append(
                IndustryLocationCheckIndustryMinDistance(self.industry.id, 20)
            )
        elif self.same_type_distance:
            # industries can over-ride the default min distance to others of same type
            result.append(
                IndustryLocationCheckIndustryMinDistance(
                    self.industry.id, self.same_type_distance
                )
            )
        else:
            # enforce a default min distance to other industries of same type
            result.append(
                IndustryLocationCheckIndustryMinDistance(self.industry.id, 56)
            )

        if self.require_town_industry_count:
            result.append(
                IndustryLocationCheckTownIndustryCount(self.require_town_industry_count)
            )

        if self.require_town_min_population:
            result.append(
                IndustryLocationCheckTownMinPopulation(self.require_town_min_population)
            )

        if self.location_check_industry_disallow_too_far_from_coast:
            result.append(IndustryLocationCheckCoastDistance())

        # prevent locating very near industries in the same accept / produce chain
        for industry in set(incompatible_industries[self.industry]):
            # don't check for self type, we have other ways to do that (occasionally economy cargo variations trigger this)
            if industry.id != self.industry.id:
                result.append(IndustryLocationCheckIndustryMinDistance(industry.id, 16))

        return result

    def get_post_player_founding_checks_OR(self, incompatible_industries):
        # checks structured in OR groups
        # within each OR group, satisyfing any one of the conditions is enough
        result = []

        keystone_industries = {
            "OR_group_name": "keystone_industries",
            "location_checks": [],
            "next_switch_name": "",
        }
        if self.near_at_least_one_of_these_keystone_industries:
            for industry_type in self.near_at_least_one_of_these_keystone_industries[0]:
                # if the ID of the keystone type is higher than the current industry, the current industry won't be built on smaller maps or low industry settings
                # this is because OpenTTD places first round of industries sequentially by ID (lowest first) at map gen time
                if self.industry.numeric_id < (
                    get_another_industry(industry_type).numeric_id
                ):
                    utils.echo_message(
                        self.industry.id
                        + " declares a keystone with higher ID ("
                        + industry_type
                        + ") - keystones must have lower ID than declaring industry, as industries are placed sequentially by ID (lowest first) when generating map.  Move "
                        + self.industry.id
                        + " to a higher ID (probably breaks savegames)."
                    )
                    permissive_flag = 1
                else:
                    permissive_flag = 0
                keystone_industries["location_checks"].append(
                    IndustryLocationCheckIndustryMaxDistance(
                        industry_type,
                        self.near_at_least_one_of_these_keystone_industries[1],
                        permissive_flag,
                    )
                )
        result.append(keystone_industries)

        economy_specific_biomes = {
            "OR_group_name": "economy_specific_biomes",
            "location_checks": [],
            "next_switch_name": "",
        }
        for economy_id, biome_list in self.economy_biome_checks.items():
            for biome_id in biome_list:
                economy_specific_biomes["location_checks"].append(
                    IndustryLocationCheckEconomySpecificBiome(economy_id, biome_id)
                )
        result.append(economy_specific_biomes)

        for counter, group in enumerate(result):
            if counter == 0:
                # last result (switches tree is reversed list order), so branch to AND checks
                group["next_switch_name"] = "AND"
            else:
                group["next_switch_name"] = "OR_" + result[counter - 1]["OR_group_name"]

        return result


class IndustryLocationCheck(object):
    """sparse base class for industry location checks"""

    @property
    def procedure_name_and_params_as_nml_string(self):
        params_as_nml_string = ",".join([str(param) for param in self.params])
        return (
            "location_check_industry_"
            + self.procedure_name
            + "("
            + params_as_nml_string
            + ")"
        )


class IndustryLocationCheckTownIndustryCount(IndustryLocationCheck):
    """Require specific count of industry type in a town"""

    def __init__(self, require_town_industry_count):
        # use the numeric_id so that we can do single-industry compiles without nml barfing on missing identifiers
        self.industry_type_numeric_id = get_another_industry(
            require_town_industry_count[0]
        ).numeric_id
        self.min_count = require_town_industry_count[1]
        self.max_count = require_town_industry_count[2]
        if self.min_count != 0 or self.max_count != 0:
            utils.echo_message(
                "IndustryLocationCheckTownIndustryCount uses a hardcoded error string limiting to 1 instance per town, add more strings to handle higher limits"
            )
        self.procedure_name = "require_town_industry_count"
        self.params = [self.industry_type_numeric_id, self.min_count, self.max_count]


class IndustryLocationCheckTownMinPopulation(IndustryLocationCheck):
    """Require the nearest town to have a minimum population"""

    def __init__(self, require_town_min_population):
        self.min_population = require_town_min_population
        self.procedure_name = "require_town_min_population"
        self.params = [self.min_population]


class IndustryLocationCheckCluster(IndustryLocationCheck):
    """Require industries to locate in n clusters"""

    def __init__(self, industry_type, require_cluster):
        # use the numeric_id so that we can do single-industry compiles without nml barfing on missing identifiers
        self.industry_type_numeric_id = industry_type
        self.max_distance = require_cluster[0]
        # cluster factor is a fudge, theoretically determines number of clusters per 256x256 section of map, but often irrelevant due to industry counts in any given combination of map/setting/economy/randomisation
        self.cluster_factor = require_cluster[1]
        self.procedure_name = "require_cluster"
        self.params = [
            self.industry_type_numeric_id,
            self.cluster_factor,
            self.max_distance,
        ]


class IndustryLocationCheckIndustryMinDistance(IndustryLocationCheck):
    """Prevent locating near incompatible industry types"""

    def __init__(self, industry_type, distance):
        self.industry_type = industry_type
        # use the numeric_id so that we can do single-industry compiles without nml barfing on missing identifiers
        self.industry_type_numeric_id = get_another_industry(industry_type).numeric_id
        self.distance = distance
        self.procedure_name = "require_min_distance_to_another_industry_type"
        self.params = [self.industry_type_numeric_id, self.distance]


class IndustryLocationCheckIndustryMaxDistance(IndustryLocationCheck):
    """Check distance to another industry type"""

    def __init__(self, industry_type, distance, permissive_flag):
        # use the numeric_id so that we can do single-industry compiles without nml barfing on missing identifiers
        self.industry_type_numeric_id = get_another_industry(industry_type).numeric_id
        self.distance = distance
        self.permissive_flag = permissive_flag
        self.procedure_name = "require_max_distance_to_another_industry_type"
        self.params = [
            self.industry_type_numeric_id,
            self.distance,
            self.permissive_flag,
        ]


class IndustryLocationCheckCoastDistance(IndustryLocationCheck):
    """Maximum distance to coast (player can vary this with parameter)"""

    def __init__(self):
        self.procedure_name = "disallow_too_far_from_coast"
        self.params = []


class IndustryLocationCheckEconomySpecificBiome(IndustryLocationCheck):
    """Check for a biome specific to the economy"""

    def __init__(self, economy_id, biome_id):
        self.procedure_name = "economy_biome_test_" + economy_id + "_" + biome_id
        self.params = []


class IndustryLocationCheckGrainMillLayoutsByDate(IndustryLocationCheck):
    """Custom check for Grain mill, layouts are restricted by date; this is a one-off, but could be made generic if needed"""

    def __init__(self):
        self.procedure_name = "flour_mill_layouts_by_date"
        self.params = []


class IndustryProperties(object):
    """Base class to hold industry item properties, as the instance for defaults, or for economy variations"""

    def __init__(self, **kwargs):
        # nml item properties, most of these should be provided as strings for insertion into nml.  See nml docs for meaning + acceptable values.
        self.substitute = kwargs.get(
            "substitute", "0"
        )  # '0' is safe default, most industries don't need to set this prop explicitly, but the prop must have *a* value or industry won't appear in game
        self.override = kwargs.get(
            "override", "0"
        )  # industries should only set this explicitly when re-using a default industry, otherwise '0' is a safe default
        self.name = kwargs.get("name", None)
        self.nearby_station_name = kwargs.get("nearby_station_name", None)
        self.intro_year = kwargs.get("intro_year", None)
        self.expiry_year = kwargs.get("expiry_year", None)
        self.min_cargo_distr = "1"  # just use the most common value from default OTTD industries, this property needs set but has little use
        #  input multipliers must be explicitly 0 unless set, don't rely on sensible defaults
        self.input_multiplier_1 = kwargs.get("input_multiplier_1", "[0, 0]")
        self.input_multiplier_2 = kwargs.get("input_multiplier_2", "[0, 0]")
        self.input_multiplier_3 = kwargs.get("input_multiplier_3", "[0, 0]")
        self.prod_increase_msg = kwargs.get("prod_increase_msg", None)
        self.prod_decrease_msg = kwargs.get("prod_decrease_msg", None)
        self.new_ind_msg = kwargs.get("new_ind_msg", None)
        self.closure_msg = kwargs.get("closure_msg", None)
        self.prob_in_game = kwargs.get("prob_in_game", None)
        self.prob_map_gen = kwargs.get("prob_map_gen", None)
        self.prospect_chance = kwargs.get("prospect_chance", None)
        self.map_colour = kwargs.get("map_colour", None)
        self.life_type = kwargs.get("life_type", None)
        self.fund_cost_multiplier = kwargs.get("fund_cost_multiplier", None)
        self.remove_cost_multiplier = kwargs.get("remove_cost_multiplier", "0")
        self._special_flags = kwargs.get("special_flags", [])
        # not nml properties
        self.enabled = kwargs.get("enabled", False)
        self.accept_cargo_types = kwargs.get("accept_cargo_types", None)
        self.accept_cargos_with_input_ratios = kwargs.get(
            "accept_cargos_with_input_ratios", None
        )
        self.prod_cargo_types_with_multipliers = kwargs.get(
            "prod_cargo_types_with_multipliers", None
        )
        self.prod_cargo_types_with_output_ratios = kwargs.get(
            "prod_cargo_types_with_output_ratios", None
        )
        self.prod_multiplier = kwargs.get("prod_multiplier", None)
        self.override_default_construction_states = kwargs.get(
            "override_default_construction_states", False
        )
        self.extra_text_fund = kwargs.get("extra_text_fund", None)
        # used by primaries only as of August 2023
        self.primary_production_random_factor_set = kwargs.get(
            "primary_production_random_factor_set", None
        )
        # default and/or economy-specific configuration for FIRS GS at compile time
        self.vulcan_config = kwargs.get("vulcan_config", {})
        # nml properties we want to prevent being set for one reason or another
        if "conflicting_ind_types" in kwargs:
            raise Exception(
                "Don't set conflicting_ind_types property; use the FIRS location checks for conflicting industry (these are more flexible)."
            )
        self.basic_needs_and_luxuries_factor = kwargs.get(
            "basic_needs_and_luxuries_factor", 0
        )
        self.pollution_and_squalor_factor = kwargs.get(
            "pollution_and_squalor_factor", 0
        )


class Industry(object):
    """Base class for all types of industry"""

    def __init__(self, id, **kwargs):
        self.id = id
        self.tiles = []
        self.sprites = []
        self.smoke_sprites = []
        self.spritesets = []
        # by convention spritelayout is one word :P
        self.spritelayouts = []
        # magic has a cost - we can't look up tiles in magic spritelayouts using the standard (non-magic) methods, so we have to do book-keeping
        self.magic_spritelayout_tile_ids = {}
        # objects dict keyed on the object num local to the industry, for convenience of access creating/appending - isn't significant for rendering
        self.objects = {}
        self.extra_graphics_switches = []
        self._industry_layouts = {"core": [], "outposts": [], "jetties": []}
        self.default_industry_properties = IndustryProperties(**kwargs)
        # economy variation structure is provisioned containing all economies, but with empty industry config, industry is then enabled for economies later
        # this could be changed so that economies are only provisioned by enable_in_economy(), but it's easy to ensure economy looks up don't fail this way
        self.economy_variations = {}
        for economy in registered_economies:
            self.add_economy_variation(economy)
        # Vulcan is used to configure FIRS GS compile-time properties, and holds Vulcan-specific properties and methods
        self.vulcan = Vulcan(self)
        # template will be set by subcass, and/or by individual industry instances
        self.template = kwargs.get("template", None)
        self.location_checks = IndustryLocationChecks(
            self, kwargs.get("location_checks", {})
        )
        self.provides_snow = kwargs.get("provides_snow", False)
        self.sprites_complete = kwargs["sprites_complete"]

    def register(self):
        if (
            len(
                [
                    i
                    for i in self.economy_variations
                    if self.economy_variations[i].enabled is True
                ]
            )
            == 0
        ):
            utils.echo_message(self.id + " is not used in any economy")
        registered_industries.append(self)

    def enable_in_economy(self, economy_id, **kwargs):
        self.economy_variations[economy_id].enabled = True
        for kwarg_name, kwarg_value in kwargs.items():
            # special case for location checks, which must be appended to the dedicated IndustryLocationChecks instance holding the standard checks for the industry
            if kwarg_name == "locate_in_specific_biomes":
                self.location_checks.economy_biome_checks[economy_id] = kwarg_value
            else:
                if hasattr(self.economy_variations[economy_id], kwarg_name):
                    setattr(
                        self.economy_variations[economy_id], kwarg_name, kwarg_value
                    )
                else:
                    raise NameError(
                        "unknown economy variation kwarg '"
                        + kwarg_name
                        + "' declared by "
                        + self.id
                    )

    def add_tile(self, *args, **kwargs):
        new_tile = Tile(self.id, *args, **kwargs)
        self.tiles.append(new_tile)
        return new_tile

    def add_sprite(self, *args, **kwargs):
        new_sprite = Sprite(*args, **kwargs)
        self.sprites.append(new_sprite)
        # returning the new sprite isn't essential, but permits the caller giving it a reference for use elsewhere
        return new_sprite

    def add_smoke_sprite(self, *args, **kwargs):
        new_smoke_sprite = SmokeSprite(*args, **kwargs)
        self.smoke_sprites.append(new_smoke_sprite)
        # returning the new smokesprite isn't essential, but permits the caller giving it a reference for use elsewhere
        return new_smoke_sprite

    def add_spriteset(self, *args, **kwargs):
        id = self.id + "_spriteset_" + str(len(self.spritesets))
        new_spriteset = Spriteset(id=id, *args, **kwargs)
        self.spritesets.append(new_spriteset)
        # returning the new spriteset isn't essential, but permits the caller giving it a reference for use elsewhere
        return new_spriteset

    def add_spritelayout(self, *args, **kwargs):
        new_spritelayout = SpriteLayout(*args, **kwargs)
        self.spritelayouts.append(new_spritelayout)
        if kwargs.get("add_to_object_num", None) is not None:
            # when adding spritelayouts this way, all views will be single tile, 0-indexed
            view = [(0, 0, new_spritelayout)]
            self.add_view_for_object(view, **kwargs)
        # returning the new spritelayout isn't essential, but permits the caller giving it a reference for use elsewhere
        return new_spritelayout

    def add_magic_spritelayout(self, type, base_id, tile, config):
        # sometimes magic is the only way
        # this is for very specific spritelayout patterns that repeat across multiple industries and require long declarations and extra switches
        if type == "slope_aware_trees":
            # the Magic is so magic that we don't have any further assignment, instantiating the class does all the registration etc (ugh)
            MagicSpritelayoutSlopeAwareTrees(self, base_id, config)
        if type == "jetty_coast_foundations":
            # the Magic is so magic that we don't have any further assignment, instantiating the class does all the registration etc (ugh)
            MagicSpritelayoutHarbourCoastFoundations(self, base_id, config)
        # we do have to book-keep the magic, as there are Magic taxes that must be paid
        self.magic_spritelayout_tile_ids[base_id] = tile

    def add_slope_graphics_switch(self, *args, **kwargs):
        new_graphics_switch = GraphicsSwitchSlopes(*args, **kwargs)
        self.extra_graphics_switches.append(new_graphics_switch)
        # returning the new switch isn't essential, but permits the caller giving it a reference for use elsewhere
        return new_graphics_switch

    def add_industry_layout(self, layout_type="core", *args, **kwargs):
        new_industry_layout = IndustryLayout(
            self, *args, **kwargs, validate_legacy_layout_defs=True
        )
        self._industry_layouts[layout_type].append(new_industry_layout)
        # returning the new layout isn't essential, but permits the caller giving it a reference for use elsewhere
        return new_industry_layout

    def add_industry_outpost_layout(self, *args, **kwargs):
        return self.add_industry_layout("outposts", *args, **kwargs)

    def add_industry_jetty_layout(self, *args, **kwargs):
        return self.add_industry_layout("jetties", *args, **kwargs)

    def add_economy_variation(self, economy):
        self.economy_variations[economy.id] = IndustryProperties()

    def add_view_for_object(self, view, **kwargs):
        # view is a list of tuples as [(x, y, spritelayout)], similar to industry layouts, but there's no need for a stubby class for view
        add_to_object_num = kwargs["add_to_object_num"]
        # create object with this num if it doesn't exist
        if add_to_object_num not in self.objects.keys():
            self.objects[add_to_object_num] = GRFObject(self, add_to_object_num)
        self.objects[add_to_object_num].add_view(view)

    def add_multi_tile_object(self, **kwargs):
        view = []
        for x_y_spritelayout in kwargs["view_layout"]:
            # does not handle case of invalid spritelayout id currently, so...don't do that :)
            for spritelayout in self.spritelayouts:
                if spritelayout.id == x_y_spritelayout[2]:
                    view.append(
                        (x_y_spritelayout[0], x_y_spritelayout[1], spritelayout)
                    )
        self.add_view_for_object(view, **kwargs)

    @property
    def numeric_id(self):
        return global_constants.industry_numeric_ids[self.id]

    @property
    def economies_enabled_for_industry(self):
        result = []
        for economy in registered_economies:
            if self.get_property("enabled", economy):
                result.append(economy)
        return result

    def get_graphics_file_path(self, terrain=None, construction_state_num=None):
        if terrain == "snow" and self.provides_snow:
            terrain_suffix = "_snow"
        else:
            terrain_suffix = ""
        # don't use os.path.join here, this returns a string for use by nml
        if construction_state_num != None:
            return (
                '"src/graphics/industries/'
                + self.id
                + "_construction_"
                + str(construction_state_num + 1)
                + '.png"'
            )
        else:
            return '"src/graphics/industries/' + self.id + terrain_suffix + '.png"'

    @property
    def switch_name_for_construction_states(self):
        # industries use the default construction sprites (shared), or their own handled by automagic spritesets / spritelayouts (graphics in spritesheets with same layout as industry)
        if (
            self.default_industry_properties.override_default_construction_states
            == True
        ):
            return self.id + "_industry_graphics_switch_layouts"
        else:
            return "spritelayout_default_construction_states"

    @property
    def industry_layouts(self):
        # JFDI switching, it's either default layouts or jetties (for port-type and harbour industries)
        # jetties can't be combined with other industry layout approaches, it's XOR
        if len(self._industry_layouts["jetties"]) > 0:
            # precisely 2 jetty layouts must be provided
            if len(self._industry_layouts["jetties"]) != 2:
                raise BaseException(
                    "For industry using jetty layouts, precisely 2 layouts must be provided; industry "
                    + self.id
                    + " provides "
                    + str(len(self._industry_layouts["jetties"]))
                )
            return self.industry_layouts_jetties
        else:
            return self.industry_layouts_default

    @property
    def industry_layouts_default(self):
        # industry layouts are composed from
        # - main layouts in _industry_layouts
        # - optional outpost layouts
        # the outpost layouts increase total catchment area for station building, whilst leaving plenty of room to actually build the stations
        # when outposts are used, 8 layouts are created, distributing outpusts at compass points around the core layout
        # outposts are intended for industries with many pickup cargos, where multiple stations are required, outposts are not otherwise advised
        result = []
        composite_layout_counter = 0
        for core_layout in self._industry_layouts["core"]:
            if len(self._industry_layouts["outposts"]) == 0:
                result.append(core_layout)
            else:
                for outpost_layout in self._industry_layouts["outposts"]:
                    if outpost_layout.id not in core_layout.excluded_outpost_layouts:
                        # NOTE the required xy offset depends on size of outpost layout as it reflects how far 0,0 tile is shifted - this is handled by checking outpost dimensions
                        # 8 outpost placements, 2 for each compass point, leaving a sufficient 2 tile gap to fit a double track / platform in straight, or diagonal double track
                        # I tested NE, SW etc, but didn't like it - seems to look better at N, S etc diagonal offsets from core layout
                        outpost_xy_offsets = [
                            # north
                            (
                                0 - (outpost_layout.xy_dimensions[0] + 2),
                                0 - (outpost_layout.xy_dimensions[1] + 1),
                            ),
                            # south
                            (
                                core_layout.xy_dimensions[0] + 1,
                                core_layout.xy_dimensions[1] + 2,
                            ),
                            # east
                            (
                                0,
                                core_layout.xy_dimensions[1] + 2,
                            ),
                            # this offset removed because it creates a layout with no tiles on N tile
                            # (
                            # 0 - (outpost_layout.xy_dimensions[0] + 2),
                            # core_layout.xy_dimensions[1],
                            # ),
                            # this offset removed because it creates a layout with no tiles on N tile
                            # (
                            # 0 - (outpost_layout.xy_dimensions[0]),
                            # core_layout.xy_dimensions[1] + 2,
                            # ),
                            # west
                            (
                                core_layout.xy_dimensions[0] + 2,
                                0,
                            ),
                            # this offset removed because it creates a layout with no tiles on N tile
                            # (
                            # core_layout.xy_dimensions[0] + 2,
                            # 0 - (outpost_layout.xy_dimensions[1]),
                            # ),
                            # this offset removed because it creates a layout with no tiles on N tile
                            # (
                            # core_layout.xy_dimensions[0],
                            # 0 - (outpost_layout.xy_dimensions[1] + 2),
                            # ),
                        ]
                        for outpost_direction_counter, xy_offset in enumerate(
                            outpost_xy_offsets
                        ):
                            composite_layout_counter += 1
                            new_id = (
                                core_layout.id
                                + "_"
                                + outpost_layout.id
                                + "_"
                                + str(outpost_direction_counter)
                                + "_composite_layout_num_"
                                + str(composite_layout_counter)
                            )
                            result.append(
                                IndustryLayout(
                                    industry=self,
                                    id=new_id,
                                    layout=self.composite_two_industry_layouts(
                                        core_layout.layout,
                                        outpost_layout.layout,
                                        xy_offset,
                                    ),
                                )
                            )
        return result

    @property
    def industry_layouts_jetties(self):
        # non-standard case, used for port-type industries and harbours
        result = []
        composite_layout_counter = 0
        jetty_layout_1 = self._industry_layouts["jetties"][0]
        jetty_layout_2 = self._industry_layouts["jetties"][1]
        coast_configurations = [
            (
                "se",
                [
                    (jetty_layout_1.xy_dimensions[0] + 3, 0),
                    (jetty_layout_1.xy_dimensions[0] + 3, 1),
                    (jetty_layout_1.xy_dimensions[0] + 3, 2),
                    (jetty_layout_1.xy_dimensions[0] + 3, -1),
                    (jetty_layout_1.xy_dimensions[0] + 3, -2),
                ],
                # note the transposition of the two layouts, to get the desired effect
                jetty_layout_2.layout,
                jetty_layout_1.layout,
            ),
            (
                "ne",
                [
                    (jetty_layout_1.xy_dimensions[0] + 3, 0),
                    (jetty_layout_1.xy_dimensions[0] + 3, 1),
                    (jetty_layout_1.xy_dimensions[0] + 3, 2),
                    (jetty_layout_1.xy_dimensions[0] + 3, -1),
                    (jetty_layout_1.xy_dimensions[0] + 3, -2),
                ],
                jetty_layout_1.layout_rotated_180,
                jetty_layout_2.layout_rotated_180,
            ),
            (
                "sw",
                [
                    # note that we have to use the x dimensions to calculate y offset as we are rotating this one 90 degrees
                    (0, jetty_layout_1.xy_dimensions[0] + 3),
                    (1, jetty_layout_1.xy_dimensions[0] + 3),
                    (2, jetty_layout_1.xy_dimensions[0] + 3),
                    (-1, jetty_layout_1.xy_dimensions[0] + 3),
                    (-2, jetty_layout_1.xy_dimensions[0] + 3),
                ],
                jetty_layout_1.layout_rotated_90,
                jetty_layout_2.layout_rotated_90,
            ),
            (
                "ne",
                [
                    # note that we have to use the x dimensions to calculate y offset as we are rotating this one 270 degrees
                    (0, jetty_layout_1.xy_dimensions[0] + 3),
                    (1, jetty_layout_1.xy_dimensions[0] + 3),
                    (2, jetty_layout_1.xy_dimensions[0] + 3),
                    (-1, jetty_layout_1.xy_dimensions[0] + 3),
                    (-2, jetty_layout_1.xy_dimensions[0] + 3),
                ],
                # note the transposition of the two layouts, to get the desired effect
                jetty_layout_2.layout_rotated_270,
                jetty_layout_1.layout_rotated_270,
            ),
        ]
        for orientation_label, xy_offsets, layout_1, layout_2 in coast_configurations:
            for xy_offset in xy_offsets:
                composite_layout_counter += 1
                new_id = (
                    jetty_layout_1.id
                    + "_"
                    + jetty_layout_2.id
                    + "_composite_layout_num_"
                    + str(composite_layout_counter)
                    + "_orientation_"
                    + orientation_label
                )
                layout = []
                for tiledef in self.composite_two_industry_layouts(
                    layout_1,
                    layout_2,
                    xy_offset,
                ):
                    spritelayout_id = tiledef[3]
                    if orientation_label in ["ne", "sw"]:
                        if spritelayout_id.find("nw_se_auto_orient") != -1:
                            spritelayout_id = spritelayout_id.replace("nw_se_auto_orient", "ne_sw_auto_orient")
                            print("CABBAGE 9222", spritelayout_id)
                        # *must* be elif or we'll replace what we already just replaced
                        elif spritelayout_id.find("ne_sw_auto_orient") != -1:
                            spritelayout_id = spritelayout_id.replace("ne_sw_auto_orient", "nw_se_auto_orient")
                            print("CABBAGE 7777", spritelayout_id)
                    tiledef = (tiledef[0], tiledef[1], tiledef[2], spritelayout_id)
                    layout.append(tiledef)
                    print(layout)
                result.append(
                    IndustryLayout(
                        industry=self,
                        id=new_id,
                        layout=layout,
                    )
                )
        return result

    def composite_two_industry_layouts(self, layout_1, layout_2, xy_offset):
        # for simplicity, this assumes we only ever want to composite 2 layouts
        # more than 2 layouts could be supported easily enough, but there was no case so far
        composite_layout = layout_1.copy()
        for tile_def in layout_2:
            new_tile_def = (
                xy_offset[0] + tile_def[0],
                xy_offset[1] + tile_def[1],
                tile_def[2],
                tile_def[3],
            )
            composite_layout.append(new_tile_def)

        composite_layout = self.transpose_industry_layout_to_set_n_tile_as_origin(
            composite_layout
        )
        return composite_layout

    def transpose_industry_layout_to_set_n_tile_as_origin(self, layout):
        transposed_layout = []
        # layouts can't use -ve xy values,
        # ensure that the layout is valid by transposing it to put north tile on 0,0
        # temp IndustryLayout objs created here just to use their min_x, min_y methods for convenience
        transpose_x = (
            -1
            * IndustryLayout(
                industry=self,
                id="temp",
                layout=layout,
                validate_xy=False,
            ).min_x
        )
        transpose_y = (
            -1
            * IndustryLayout(
                industry=self,
                id="temp",
                layout=layout,
                validate_xy=False,
            ).min_y
        )
        for tile_def in layout:
            transposed_tile_def = (
                tile_def[0] + transpose_x,
                tile_def[1] + transpose_y,
                tile_def[2],
                tile_def[3],
            )
            transposed_layout.append(transposed_tile_def)
        return transposed_layout

    @property
    def industry_layouts_as_nml_property(self):
        result = [
            industry_layout.id + "_tilelayout"
            for industry_layout in self.industry_layouts
        ]
        return "layouts: [" + ",".join(result) + "];"

    def randomise_primary_production_on_build_as_nml_property(self, economy):
        if self.get_property("prod_cargo_types_with_multipliers", economy) in [
            None,
            [],
        ]:
            # if there's no production, there's no point setting this prop (this mostly handles case of IndustryTertiary where hotel produces and others do not)
            return ""
        else:
            # don't otherwise bother handling errors, just fail if this is missing
            primary_production_random_factor_set = self.get_property(
                "primary_production_random_factor_set", economy
            )
            params = [
                self.get_perm_num("base_prod_factor"),
                # we want the index of the primary_production_random_factor_set so we can switch on it in nml
                global_constants.primary_production_random_factor_sets.index(
                    primary_production_random_factor_set
                ),
            ]
            return (
                "build_prod_change: randomise_primary_production_on_build("
                + ",".join([str(i) for i in params])
                + ");"
            )

    def get_extra_text_fund(self, economy):
        # some fund text options are orthogonal, there is no support for combining them currently
        # support for combined fund text could be added, it's just a substr tree eh?
        result = (
            []
        )  # use a list, because I want to warn if industry tries to set more than one result
        if self.get_intro_year(economy) != 0:
            result.append(
                "string(STR_FUND_AVAILABLE_FROM, "
                + str(self.get_intro_year(economy))
                + ")"
            )
        if self.get_expiry_year(economy) != global_constants.max_game_date:
            result.append(
                "string(STR_FUND_AVAILABLE_UNTIL, "
                + str(self.get_expiry_year(economy))
                + ")"
            )

        if self.get_property("extra_text_fund", economy) is not None:
            result.append(self.get_property("extra_text_fund", economy))

        # integrity check, no handling of multiple results currently so alert on that at compile time
        if len(result) > 1:
            utils.echo_message(
                "Industry "
                + self.id
                + " wants more than one string for extra_text_fund, only one is supported currently"
            )
            utils.echo_message(
                str(self.get_intro_year(economy))
                + " "
                + str(self.get_expiry_year(economy))
            )

        # if no text is needed...
        if len(result) == 0:
            result.append("CB_RESULT_NO_TEXT")

        return "return " + result[0]

    def get_extra_text_string(self, economy):
        accept_cargos_with_ratios = self.get_property(
            "accept_cargos_with_input_ratios", economy
        )
        if len(accept_cargos_with_ratios) == 1:
            extra_text_string = "STR_EMPTY"  # nothing useful to show where just one cargo is accepted eh
        elif len(accept_cargos_with_ratios) == 2:
            extra_text_string = "STR_EXTRA_TEXT_SECONDARY_COMBINATORY_BOTH"
        else:
            # below here is increasingly JFDI and may well go wrong if industries are inappropriately configured
            max_ratio = sum(
                [cargo_with_ratio[1] for cargo_with_ratio in accept_cargos_with_ratios]
            )
            if max_ratio == 8:
                # common case, industry is configured so that ratios sum to 8
                extra_text_string = "STR_EXTRA_TEXT_SECONDARY_COMBINATORY_ALL"
            elif int(max_ratio / len(accept_cargos_with_ratios)) == 8:
                # less common case: all ratios are 8, so there is no combination
                # to prevent surprises we guard on known industry ids
                if self.id not in ["supply_yard", "food_processor"]:
                    raise Exception(
                        "get_extra_text_string: "
                        + self.id
                        + " needs combinatorial production values checked, they may be incorrect?"
                    )
                extra_text_string = "STR_EXTRA_TEXT_SECONDARY_NON_COMBINATORY"
            elif int(max_ratio / len(accept_cargos_with_ratios)) == 3:
                # rare case of 3 out of n cargos being required
                # to prevent surprises we guard on known industry ids
                if self.id not in ["precision_parts_plant", "appliance_factory"]:
                    raise Exception(
                        "get_extra_text_string: "
                        + self.id
                        + " needs combinatorial production values checked, they may be incorrect?"
                    )
                extra_text_string = "STR_EXTRA_TEXT_SECONDARY_COMBINATORY_ANY_THREE"
            else:
                # as of April 2023, we just assume that any 2 will give a max ratio
                # to prevent surprises we guard on known industry ids
                if self.id not in ["hardware_factory"]:
                    raise Exception(
                        "get_extra_text_string: "
                        + self.id
                        + " needs combinatorial production values checked, they may be incorrect?"
                    )
                extra_text_string = "STR_EXTRA_TEXT_SECONDARY_COMBINATORY_ANY_TWO"
        return "string(" + extra_text_string + ")"

    def get_intro_year(self, economy):
        # simple wrapper to get_property(), which sanitises intro_year from None to 0 if unspecified by economy
        result = self.get_property("intro_year", economy)
        if result == None:
            return 0
        else:
            return result

    def get_expiry_year(self, economy):
        # simple wrapper to get_property(), which sanitises expiry from None to max game date if unspecified by economy
        result = self.get_property("expiry_year", economy)
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
        if property_name == "map_colour":
            self.validate_map_colour(value)

        return value

    def get_property_declaration(self, property_name, economy=None):
        value = self.get_property(property_name, economy)
        # we don't want to render empty properties for nml
        if value == None or value == "":
            return
        else:
            return property_name + ": " + value + ";"

    @property
    def nearby_station_name_as_nml_property(self):
        return (
            "nearby_station_name: string(STR_STATION, string(STR_TOWN),"
            + self.get_property("nearby_station_name", None)
            + ");"
        )

    def get_cargo_types_declaration(self, economy):
        """
        *Output Format*
        accept_cargo("COAL", produce_cargo("MAIL", 1), produce_cargo("GOOD", 1), produce_cargo("STEL", 1), produce_cargo("VALU", 1)),
        accept_cargo("OIL_"),
        accept_cargo("IORE", produce_cargo("STEL", 4)),
        produce_cargo("VALU", 0.5)
        Just use 0 in produce_cargo("STEL", 0) if prod. cb is in use (i.e. secondaries).
        """
        cargo_types = []
        cargo_types.extend(
            [
                'accept_cargo("' + label + '")'
                for label in self.get_accept_cargo_types(economy)
            ]
        )
        zero_output = "0"  # *all* industry production is via production cb, so force output to 0 in the action 0 prop
        cargo_types.extend(
            [
                'produce_cargo("' + label + '",' + zero_output + ")"
                for label, output_ratio in self.get_prod_cargo_types(economy)
            ]
        )
        result = "cargo_types: [" + ",".join(cargo_types) + "];"
        return result

    def get_accept_cargo_types(self, economy):
        # method used here for (1) guarding against invalid values (2) so that it can be over-ridden by industry subclasses as needed
        accept_cargo_types = self.get_property("accept_cargo_types", economy)
        if accept_cargo_types is None:
            # returning None causes some things to explode in docs, which I should fix, but haven't, this patches it with jank
            result = []
        else:
            result = accept_cargo_types
            # although OpenTTD 1.9.0+ supports up to 16 accepted cargos, FIRS caps to 8
            # - for gameplay reasons (too many cargos in one industry isn't fun)
            # - because of long-established production rules that calculate cargo output using ratios of n/8
            assert (
                len(result) <= 8
            ), "More than 8 accepted cargos defined for %s in economy %s" % (
                self.id,
                economy.id,
            )
        return result

    def get_prod_cargo_types(self, economy):
        # stub, this should be handled in Industry subclasses
        raise Exception("get_prod_cargo_types called", self.id)
        return []

    def get_animation_macro_config(self, animation_context):
        if animation_context == "industry":
            tiles = self.tiles
            feature = "FEAT_INDUSTRYTILES"
        elif animation_context == "object":
            all_tiles = []
            for grf_object in self.objects.values():
                all_tiles.append(grf_object.tile)
            tiles = list(set(all_tiles))
            feature = "FEAT_OBJECTS"
        else:
            raise BaseException("Unknown animation_context ", animation_context)
        return {"tiles": tiles, "feature": feature}

    def get_another_industry(self, id):
        return get_another_industry(id)

    @property
    def uses_magic_trees(self):
        for spritelayout in self.spritelayouts:
            if len(spritelayout.magic_trees) > 0:
                return True
        return False

    @property
    def incompatible_industries(self):
        # there's no sensible way to get incompatible_industries from here, it has to be passed in when rendering templates
        # there are genuine performance reasons to have incompatibility calculated once and only once by firs.py
        utils.echo_message(
            "Incompatible industries not implemented in industry.py, must be passed from firs.py at render time"
        )

    @property
    def special_flags(self):
        flags = ["IND_FLAG_LONG_CARGO_TYPE_LISTS"]
        flags.extend(self.get_property("_special_flags", None))
        return "bitmask(" + ",".join(flags) + ")"

    @property
    def basic_needs_and_luxuries_score(self):
        # handled via a method so that multipliers can be applied to adjust scoring, this might not be necessary
        return 0

    @property
    def pollution_and_squalor_score(self):
        # handled via a method so that multipliers can be applied to adjust scoring, this might not be necessary
        return self.get_property("pollution_and_squalor_factor", None)

    def validate_map_colour(self, value):
        # we need to guard against map colours that have poor contrast with the green, dark green and purple maps
        # see the list of valid colours in global_constants
        # !! this might need special case handling for water industries (list.extend() in global constants?)
        if int(value) not in global_constants.valid_industry_map_colours:
            utils.echo_message(
                "Industry "
                + self.id
                + " uses map Colour "
                + value
                + " which is invalid (lacks contrast)"
            )

    def unpack_sprite_or_spriteset(
        self,
        sprite_or_spriteset,
        construction_state_num=3,
        snow_overlay=False,
    ):
        # note the annoying edge case where 'empty' should not have a snow overlay
        if (
            snow_overlay == True
            and getattr(sprite_or_spriteset, "type", None) != "empty"
        ):
            suffix = "_snow"
        else:
            suffix = ""
        if isinstance(sprite_or_spriteset, Spriteset):
            # tiny optimisation, don't use an animation sprite selector if there is no animation
            if sprite_or_spriteset.animation_rate > 0:
                if sprite_or_spriteset.custom_sprite_selector:
                    sprite_selector = (
                        str(sprite_or_spriteset.animation_rate)
                        + "*"
                        + sprite_or_spriteset.custom_sprite_selector
                    )
                else:
                    sprite_selector = (
                        str(sprite_or_spriteset.animation_rate) + "* (animation_frame)"
                    )
            else:
                sprite_selector = "0"
            if sprite_or_spriteset.type != "":
                # ground tile assumes sprite_or_spriteset.type will always map to a ground_tile type
                # have to accomodate number of frames needed (num_sprites_to_autofill) for animated spritelayouts
                # !! if this is failing, look if the required number of frames is provided in ground.pynml
                if (
                    sprite_or_spriteset.num_sprites_to_autofill
                    not in global_constants.animated_ground_tile_frame_counts
                ):
                    raise BaseException(
                        self.id
                        + " needs global_constants.animated_ground_tile_frame_counts extended to add a frame count of "
                        + str(sprite_or_spriteset.num_sprites_to_autofill)
                    )
                return (
                    "spriteset_ground_tile_"
                    + sprite_or_spriteset.type
                    + "_"
                    + str(sprite_or_spriteset.num_sprites_to_autofill)
                )
            elif (
                construction_state_num != 3
                and self.default_industry_properties.override_default_construction_states
                == False
            ):
                # default construction state (no custom construction sprites)
                return (
                    sprite_or_spriteset.id
                    + "_spriteset_default_construction_state_"
                    + str(construction_state_num)
                    + "("
                    + sprite_selector
                    + ")"
                )
            else:
                # default result is a spriteset name and optional frame number
                return sprite_or_spriteset.id + suffix + "(" + sprite_selector + ")"
        if isinstance(sprite_or_spriteset, Sprite):
            return getattr(sprite_or_spriteset, "sprite_number" + suffix)

    def get_perm_num(self, identifier):
        # just a silly pass-through to perm_storage_mappings.get_perm_num
        return get_perm_num(identifier, industry_type=self.__class__.__name__)

    def render_nml(self, incompatible_industries):
        # incompatible industries isn't known at init time, only at compile time, so it has to be passed in
        industry_template = templates[self.template]
        templated_nml = utils.unescape_chameleon_output(
            industry_template(
                industry=self,
                get_perm_num=self.get_perm_num,
                global_constants=global_constants,
                graphics_temp_storage=global_constants.graphics_temp_storage,  # convenience measure
                registered_industries=registered_industries,
                incompatible_industries=incompatible_industries,
                economies=registered_economies,
                utils=utils,
            )
        )
        return templated_nml


class IndustryPrimary(Industry):
    """Industries that produce cargo and (optionally) boost production if supplies are delivered"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = kwargs.get("template", "industry_primary.pynml")
        self.supply_requirements = None  # default None, set appropriately by subclasses
        register_perm_storage_mapping(
            self.__class__.__name__,
            [
                "unused",
                "unused",
                # base prod factor is randomised when industry is constructed, to give production variation between instances of this type
                # used in the production calculation as n/16
                # this is NOT built-in production_level which is used, but will always be 16 by default, and can be adjusted by cheats and monthly/random prod change cbs
                "base_prod_factor",
                "current_supplies_prod_factor",
                # used by industry text window to display 'supplied' or not
                # usually will just be supplies in slot 1 for primaries, except for port-type industries
                "supplied_cycles_remaining_cargo_1",
                "supplied_cycles_remaining_cargo_2",
                "supplied_cycles_remaining_cargo_3",
                "supplied_cycles_remaining_cargo_4",
                "supplied_cycles_remaining_cargo_5",
                "supplied_cycles_remaining_cargo_6",
                "supplied_cycles_remaining_cargo_7",
                "supplied_cycles_remaining_cargo_8",
                # amount of supplies delivered in each of 27 recent production cycles (27 is nice approximation to 3 months, in player's favour given varying month lengths)
                "num_supplies_delivered_1",
                "num_supplies_delivered_2",
                "num_supplies_delivered_3",
                "num_supplies_delivered_4",
                "num_supplies_delivered_5",
                "num_supplies_delivered_6",
                "num_supplies_delivered_7",
                "num_supplies_delivered_8",
                "num_supplies_delivered_9",
                "num_supplies_delivered_10",
                "num_supplies_delivered_11",
                "num_supplies_delivered_12",
                "num_supplies_delivered_13",
                "num_supplies_delivered_14",
                "num_supplies_delivered_15",
                "num_supplies_delivered_16",
                "num_supplies_delivered_17",
                "num_supplies_delivered_18",
                "num_supplies_delivered_19",
                "num_supplies_delivered_20",
                "num_supplies_delivered_21",
                "num_supplies_delivered_22",
                "num_supplies_delivered_23",
                "num_supplies_delivered_24",
                "num_supplies_delivered_25",
                "num_supplies_delivered_26",
                "num_supplies_delivered_27",
            ],
        )

    def get_prod_cargo_types(self, economy):
        # primary industry prod cargo provides multipliers for the produced amounts (8 or 9 times per month)
        prod_cargo_types = self.get_property(
            "prod_cargo_types_with_multipliers", economy
        )
        # prod_cargo_types cannot be None for primary industries
        assert prod_cargo_types is not None, (
            "prod_cargo_types_with_multipliers cannot be None for %s - property should be set in industry definition "
            % (self.id)
        )
        # guard against too many cargos being defined
        # although OpenTTD 1.9.0+ supports up to 16 produced cargos, FIRS caps to 8
        # - for gameplay reasons (too many cargos in one industry isn't fun)
        # - because of long-established production rules that calculate cargo output using ratios of n/8
        assert (
            len(prod_cargo_types) <= 8
        ), "More than 8 produced cargos defined for %s in economy %s" % (
            self.id,
            economy.id,
        )
        # guard against multipliers being 0
        for label, prod_multiplier in prod_cargo_types:
            assert (
                prod_multiplier != 0
            ), "Prod multiplier cannot be 0 for %s industry %s in economy %s" % (
                label,
                self.id,
                economy.id,
            )
        return prod_cargo_types


class IndustryPrimaryExtractive(IndustryPrimary):
    """
    Industry that is extractive AND has production boosted by delivery of ENSP (mines and similar)
    Sparse subclass of IndustryPrimary, do not add much to this, it's subclassed once already
    """

    def __init__(self, **kwargs):
        kwargs["accept_cargo_types"] = ["ENSP"]
        kwargs["life_type"] = "IND_LIFE_TYPE_EXTRACTIVE"
        super().__init__(**kwargs)
        # janky use of a un-named list for historical reasons (2nd item is string prefix, 3rd is multiplier of requirements parameters)
        self.supply_requirements = [
            0,
            "PRIMARY",
            1,
        ]
        self.allow_production_change_from_gs = True


class IndustryPrimaryOrganic(IndustryPrimary):
    """
    Industry that is organic AND has production boosted by delivery of FMSP (farms and similar)
    Sparse subclass of IndustryPrimary, do not add much to this, it's subclassed once already
    """

    def __init__(self, **kwargs):
        kwargs["accept_cargo_types"] = ["FMSP"]
        kwargs["life_type"] = "IND_LIFE_TYPE_ORGANIC"
        super().__init__(**kwargs)
        # janky use of a un-named list for historical reasons (2nd item is string prefix, 3rd is multiplier of requirements parameters)
        self.supply_requirements = [
            0,
            "PRIMARY",
            1,
        ]
        self.allow_production_change_from_gs = True


class IndustryPrimaryPort(IndustryPrimary):
    """
    Industry that is import-export AND has production boosted by delivery of arbitrary cargos (ports and similar)
    Sparse subclass of IndustryPrimary, do not add much to this, it's subclassed once already
    """

    def __init__(self, **kwargs):
        kwargs["life_type"] = "IND_LIFE_TYPE_BLACK_HOLE"
        super().__init__(**kwargs)
        # janky use of a un-named list for historical reasons (2nd item is string prefix, 3rd is multiplier of requirements parameters)
        self.supply_requirements = [
            0,
            "PORT",
            8,
        ]
        self.allow_production_change_from_gs = True


class IndustryPrimaryNoSupplies(IndustryPrimary):
    """Industry that does not accept supplies"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = kwargs.get("template", "industry_primary_no_supplies.pynml")
        self.supply_requirements = None  # supplies do not boost this type of primary
        self.allow_production_change_from_gs = kwargs.get(
            "allow_production_change_from_gs", False
        )


class IndustryTownProducerPopulationDependent(IndustryPrimary):
    """Industry that locates near towns, with production amount related to town population"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = kwargs.get("template", "industry_primary_town_producer.pynml")
        self.supply_requirements = None  # supplies do not boost this type of primary
        # town producer industries have lower and upper production caps
        self.min_production = 64
        self.max_production = 2048

    def get_prod_cargo_types(self, economy):
        # town-population-dependent industries provide multipliers which are used as n/16 - set 16 for default
        prod_cargo_types = self.get_property(
            "prod_cargo_types_with_multipliers", economy
        )
        # prod_cargo_types cannot be None for town-population-dependent industries
        assert prod_cargo_types is not None, (
            "prod_cargo_types_with_multipliers cannot be None for %s - property should be set in industry definition "
            % (self.id)
        )
        # guard against too many cargos being defined
        # although OpenTTD 1.9.0+ supports up to 16 produced cargos, FIRS caps to 8
        # - for gameplay reasons (too many cargos in one industry isn't fun)
        # - because of long-established production rules that calculate cargo output using ratios of n/8
        assert (
            len(prod_cargo_types) <= 8
        ), "More than 8 produced cargos defined for %s in economy %s" % (
            self.id,
            economy.id,
        )
        # guard against multipliers being 0
        for label, prod_multiplier in prod_cargo_types:
            assert (
                prod_multiplier != 0
            ), "Prod multiplier cannot be 0 for %s industry %s in economy %s" % (
                label,
                self.id,
                economy.id,
            )
        return prod_cargo_types


class IndustrySecondary(Industry):
    """Processing industries: input cargo(s) -> output cargo(s)"""

    def __init__(self, **kwargs):
        kwargs["life_type"] = "IND_LIFE_TYPE_PROCESSING"
        super().__init__(**kwargs)
        self.template = kwargs.get("template", "industry_secondary.pynml")
        register_perm_storage_mapping(
            self.__class__.__name__,
            [
                "closure_counter",  # months without delivery, same as primary industries
                "current_production_ratio",  # in format n/8, calculated during prod cycle, permanent register used for ease of debugging
                "total_cargo_produced_this_cycle",  # calculated during prod cycle, permanent register used for ease of debugging
                # used by industry text window to display 'supplied' or not
                "supplied_cycles_remaining_cargo_1",
                "supplied_cycles_remaining_cargo_2",
                "supplied_cycles_remaining_cargo_3",
                "supplied_cycles_remaining_cargo_4",
                "supplied_cycles_remaining_cargo_5",
                "supplied_cycles_remaining_cargo_6",
                "supplied_cycles_remaining_cargo_7",
                "supplied_cycles_remaining_cargo_8",
                "total_cargo_to_distribute_this_cycle",
                "total_produced_cargo_available",
                "unused",
                "unused",
                "unused",
            ],
        )
        # guard against prospect chance kword being set, it's pure cruft for secondary industry (harmless, but needless)
        if "prospect_chance" in kwargs:
            utils.echo_message(
                "prospect_chance passed in kwargs for "
                + self.id
                + "; secondary industries should not set prospect_chance"
            )

    def get_prod_ratio(self, cargo_num, economy):
        if cargo_num > len(
            self.get_property("accept_cargos_with_input_ratios", economy)
        ):
            return 0
        else:
            return self.get_property("accept_cargos_with_input_ratios", economy)[
                cargo_num - 1
            ][1]

    def get_accept_cargo_types(self, economy):
        # method used here for (1) guarding against invalid values (2) so that it can be over-ridden by industry subclasses as needed
        accept_cargo_types = [
            i[0] for i in self.get_property("accept_cargos_with_input_ratios", economy)
        ]
        # guard against too many cargos being defined
        if len(accept_cargo_types) > 8:
            utils.echo_message(
                "Too many accepted cargos defined for "
                + self.id
                + " in economy "
                + economy.id
                + " (max 8)"
            )
        return accept_cargo_types

    def get_prod_cargo_types(self, economy):
        # secondary industry prod cargo uses output ratios of n/8 per cargo, which must sum to 8 for all cargos
        prod_cargo_types = self.get_property(
            "prod_cargo_types_with_output_ratios", economy
        )
        # prod_cargo_types cannot be None for secondary industries
        assert prod_cargo_types is not None, (
            "prod_cargo_types_with_output_ratios cannot be None for %s - property should be set in industry definition "
            % (self.id)
        )
        # guard against too many cargos being defined
        # although OpenTTD 1.9.0+ supports up to 16 produced cargos, FIRS caps to 8
        # - for gameplay reasons (too many cargos in one industry isn't fun)
        # - because of long-established production rules that calculate cargo output using ratios of n/8
        assert (
            len(prod_cargo_types) <= 8
        ), "More than 8 produced cargos defined for %s in economy %s" % (
            self.id,
            economy.id,
        )
        return prod_cargo_types


class IndustryTertiary(Industry):
    """Industries that are typically black holes in or near towns. Consume cargo, may also produce town-type cargos (e.g. pax) at a constant rate unrelated to delivery."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = "industry_tertiary.pynml"
        # common case is that tertiary should be treated as town industry when drawing docs cargoflow, but over-ride for cases where that's not wanted
        self.town_industry_for_cargoflow = kwargs.get(
            "town_industry_for_cargoflow", True
        )
        register_perm_storage_mapping(
            self.__class__.__name__,
            [
                # base prod factor is randomised when industry is constructed, to give production variation between instances of this type
                # used in the production calculation as n/16
                # this is NOT built-in production_level which is used, but will always be 16 by default, and can be adjusted by cheats and monthly/random prod change cbs
                "base_prod_factor",
                # used by industry text window to display 'supplied' or not
                # usually will just be supplies in slot 1 for primaries, except for port-type industries
                "supplied_cycles_remaining_cargo_1",
                "supplied_cycles_remaining_cargo_2",
                "supplied_cycles_remaining_cargo_3",
                "supplied_cycles_remaining_cargo_4",
                "supplied_cycles_remaining_cargo_5",
                "supplied_cycles_remaining_cargo_6",
                "supplied_cycles_remaining_cargo_7",
                "supplied_cycles_remaining_cargo_8",
                # amount of supplies delivered in each of 27 recent production cycles (27 is nice approximation to 3 months, in player's favour given varying month lengths)
                "input_cargo_delivered_1",
                "input_cargo_delivered_2",
                "input_cargo_delivered_3",
                "input_cargo_delivered_4",
                "input_cargo_delivered_5",
                "input_cargo_delivered_6",
                "input_cargo_delivered_7",
                "input_cargo_delivered_8",
                "input_cargo_delivered_9",
                "input_cargo_delivered_10",
                "input_cargo_delivered_11",
                "input_cargo_delivered_12",
                "input_cargo_delivered_13",
                "input_cargo_delivered_14",
                "input_cargo_delivered_15",
                "input_cargo_delivered_16",
                "input_cargo_delivered_17",
                "input_cargo_delivered_18",
                "input_cargo_delivered_19",
                "input_cargo_delivered_20",
                "input_cargo_delivered_21",
                "input_cargo_delivered_22",
                "input_cargo_delivered_23",
                "input_cargo_delivered_24",
                "input_cargo_delivered_25",
                "input_cargo_delivered_26",
                "input_cargo_delivered_27",
            ],
        )

    @property
    def has_production(self):
        # bool, used to micro-optimise compile
        result = False
        for economy in registered_economies:
            if (
                self.get_property("prod_cargo_types_with_multipliers", economy)
                is not None
            ):
                if (
                    len(self.get_property("prod_cargo_types_with_multipliers", economy))
                    > 0
                ):
                    result = True
        return result

    def get_prod_cargo_types(self, economy):
        # primary industry prod cargo provides multipliers for the produced amounts (8 or 9 times per month)
        prod_cargo_types = self.get_property(
            "prod_cargo_types_with_multipliers", economy
        )
        if prod_cargo_types is None:
            return []
        # guard against too many cargos being defined
        # although OpenTTD 1.9.0+ supports up to 16 produced cargos, FIRS caps to 8
        # - for gameplay reasons (too many cargos in one industry isn't fun)
        # - because of long-established production rules that calculate cargo output using ratios of n/8
        assert (
            len(prod_cargo_types) <= 8
        ), "More than 8 produced cargos defined for %s in economy %s" % (
            self.id,
            economy.id,
        )
        # guard against prod multipliers that are 0, they're not wanted
        for label, prod_multiplier in prod_cargo_types:
            assert (
                prod_multiplier != 0
            ), "Prod multiplier cannot be 0 for %s industry %s in economy %s" % (
                label,
                self.id,
                economy.id,
            )
        return prod_cargo_types


class Vulcan(object):
    """Used for GS configuration at compile time, which influences GS at run time"""

    def __init__(self, industry):
        self.industry = industry

    def get_default_vulcan_config_as_gs_table(self):
        vulcan_config = self.industry.get_property("vulcan_config", None)
        result = {}
        result["allow_production_change_from_gs"] = getattr(
            self.industry, "allow_production_change_from_gs", False
        )
        # append some additional derived properties to Vulcan config
        result["town_cargo_sink_industry"] = (
            True
            if self.industry.id in ["builders_yard", "hardware_store", "general_store"]
            else False
        )
        return utils.gs_table_repr(result)

    def get_economy_variations_as_gs_table(self):
        result = {}
        for economy in self.industry.economies_enabled_for_industry:
            economy_config = {}
            economy_config["accept_cargo_types"] = self.industry.get_accept_cargo_types(
                economy
            )
            economy_config["vulcan_config"] = self.industry.get_property(
                "vulcan_config", economy
            )
            result[economy.id] = economy_config
        return utils.gs_table_repr(result)
