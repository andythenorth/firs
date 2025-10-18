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
        always_draw=False,
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
        self._always_draw = always_draw

    @property
    def always_draw(self):
        # handle converting bool to int for nml
        return int(self._always_draw)


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
        always_draw=False,
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
        self._always_draw = always_draw

    @property
    def always_draw(self):
        # handle converting bool to int for nml
        return int(self._always_draw)
