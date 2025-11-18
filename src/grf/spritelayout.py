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
        jetty_foundations=False,
        jetty_surface_overlay=None,
        terrain_aware_ground=False,
        land_object_zoffset=0,
        water_object_zoffset=8,
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
        self.jetty_foundations = jetty_foundations
        if jetty_surface_overlay is None:
            self.jetty_surface_overlay = self.ground_sprite
        else:
            self.jetty_surface_overlay = jetty_surface_overlay
        self.terrain_aware_ground = terrain_aware_ground  # we don't draw terrain (and climate) aware ground unless explicitly required by the spritelayout, it makes nml compiles slower
        if self.terrain_aware_ground:
            assert (
                self.ground_sprite == None
            ), f"{self.id} sets both ground_sprite and terrain_aware_ground - can't set both"
        self.land_object_zoffset = land_object_zoffset
        self.water_object_zoffset = water_object_zoffset
        # as of September 2022, spritelayouts can define which tile they use
        # - this is optional as a migration strategy, but is intended to be the only supported approach in future
        self.tile = tile
        assert self.tile != None, f"{self.id} {self.tile}"
        # optionally spritelayouts can cause objects to be defined
        self.add_to_object_num = add_to_object_num
        if self.ground_overlay is not None:
            if hasattr(self.ground_overlay, "type"):
                print("'empty' in spritelayout:", self.id, self.ground_overlay.type)

    def resolve_tile(self, industry):
        for tile in industry.tiles:
            if tile.id == self.tile:
                return tile


class MagicSpritelayoutJettyFoundations(object):
    """
    Occasionally we need magic.  If we're going magic, let's go full on magic.
    This one provides the slope-aware foundations needed for jetty tiles (either coast, or flat water).
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

    def __init__(self, industry, base_id, tile, config, **kwargs):
        self.tile = tile
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
                tile=self.tile,
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


class MagicSpritelayoutJettyAutoOrientToCoastDirection(object):
    """
    Occasionally we need magic.  If we're going magic, let's go full on magic.
    This one provides tiles for jetties that automatically orient to the coast direction, fine-grained configurable per spritelayout.
    """

    def __init__(self, industry, base_id, tile, config, **kwargs):
        self.tile = tile
        self.auto_orient = True
        jetty_surface_overlay = industry.add_spriteset(
            type="asphalt",
        )
        for coast_direction in ["se", "sw", "nw", "ne"]:
            building_sprites = []
            building_sprites.extend(config["building_sprites"][coast_direction])
            industry.add_spritelayout(
                id=base_id + "_" + coast_direction,
                ground_sprite=None,
                ground_overlay=None,
                building_sprites=building_sprites,
                jetty_foundations=config["jetty_foundations"],
                jetty_surface_overlay=jetty_surface_overlay,
                terrain_aware_ground=True,
                # to avoid overcomplicating industry spritelayout, we make adjustments to object spritelayout
                land_object_zoffset=-8,
                water_object_zoffset=0,
                tile=self.tile,
            )

        # handle addition of objects separately, don't interleave with industry handling
        # we infer the need to add objects from 'can build on' for land and/or water
        if len(config.get("objects_can_build_on", [])) > 0:
            for spritelayout in self.get_unique_spritelayouts_for_objects(industry):
                # when adding spritelayouts this way, all views will be single tile, 0-indexed
                view = [(0, 0, spritelayout)]
                new_object_num = len(industry.objects) + 1
                allow_on_land = "land" in config["objects_can_build_on"]
                allow_on_water = "water" in config["objects_can_build_on"]
                industry.add_view_for_object(
                    view,
                    add_to_object_num=new_object_num,
                    allow_on_land=allow_on_land,
                    allow_on_water=allow_on_water,
                )

    def get_unique_spritelayouts_for_objects(self, industry):
        # spritelayouts for ne, sw, nw, ne orientations may or may not be unique, depending on whether spritesets are unique per direction, or reused
        result = []
        # unique *lists* of spritesets as this is significant
        seen_building_sprite_lists = []
        # take the last 4 spritelayouts added, correspondign to 4 coast directions
        for spritelayout in industry.spritelayouts[-4:]:
            if spritelayout.building_sprites not in seen_building_sprite_lists:
                result.append(spritelayout)
                seen_building_sprite_lists.append(spritelayout.building_sprites)
        return result


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

    def __init__(self, industry, base_id, tile, config, **kwargs):
        self.tile = tile
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
                tile=self.tile,
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


class MagicTree(object):
    """Stubby class used in MagicSpriteLayoutSlopeAwareTrees; I just prefer object attribute access over an equivalent dict - Andy"""

    def __init__(self, trees, offsets, tree_num):
        self.default = trees["default"][tree_num]
        self.snow = trees["snow"][tree_num]
        self.tropic = trees["tropic"][tree_num]
        self.xoffset = offsets[tree_num][0]
        self.yoffset = offsets[tree_num][1]


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
