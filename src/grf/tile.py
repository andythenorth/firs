from collections import deque
import os.path

currentdir = os.curdir

import global_constants as global_constants

from chameleon import PageTemplateLoader  # chameleon used in most template cases

# setup the places we look for templates
templates = PageTemplateLoader(
    os.path.join(currentdir, "src", "grf", "templates"), format="text"
)

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


