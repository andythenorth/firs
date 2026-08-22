from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="engineering_works",

    accept_cargos_with_input_ratios=[
        ("STEL", 3),
        ("ALUM", 3),
        ("PCMP", 3),
        ("PRCH", 3),
        ("INGA", 3),
    ],
    prod_cargo_types_with_output_ratios=[
        ("ENSP", 2),
        ("FMSP", 2),
        ("PLNT", 2),
        ("GOOD", 2),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="49",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    name="string(STR_IND_ENGINEERING_WORKS)",
    nearby_station_name="string(STR_STATION_WORKS)",
    fund_cost_multiplier="145",
    sprites_complete=False,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "MILD_MILD_WEST",
)

industry.add_tile(
    id="engineering_works_factory_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 31, -31, 0)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 78, -25, -12)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 78, -48, -28)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 78, -31, -47)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 78, -31, -47)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 78, -31, -47)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 85, -31, -54)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 85, -31, -54)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(640, 10, 64, 85, -31, -54)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(780, 10, 64, 31, -35, 2)],
)
spriteset_12 = industry.add_spriteset(
    sprites=[(850, 10, 64, 31, -35, 2)],
)
spriteset_13 = industry.add_spriteset(
    sprites=[(920, 10, 64, 49, -39, -15)],
)
# out of sequence for historical reasons
spriteset_14 = industry.add_spriteset(
    sprites=[(710, 10, 64, 31, -28, -1)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=13,
    yoffset=0,
    zoffset=73,
)

industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_1",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_2",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_3",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_4",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_5",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_6",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    # building_sprites = [spriteset_6, spriteset_14], # commented due to spritesorter issues obscuring spriteset_14
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_7",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_8",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_8],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_9",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_10",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_11",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_11],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_12",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_12],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_13",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_13],
    fences=[],
)
industry.add_spritelayout(
    id="engineering_works_factory_spritelayout_14",
    tile="engineering_works_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=[],
)


# this industry needs outpost layout as there are lots of cargos
industry.add_industry_outpost_layout(
    id="engineering_works_factory_industry_outpost_layout_1",
    layout=[
        # test outpost layout
        (
            0,
            0,
            "engineering_works_factory_spritelayout_1",
        ),
        (
            0,
            1,
            "engineering_works_factory_spritelayout_7",
        ),
        (
            0,
            2,
            "engineering_works_factory_spritelayout_12",
        ),
        (
            1,
            0,
            "engineering_works_factory_spritelayout_6",
        ),
        (
            1,
            1,
            "engineering_works_factory_spritelayout_5",
        ),
        (
            1,
            2,
            "engineering_works_factory_spritelayout_11",
        ),
    ],
)

industry.add_industry_layout(
    id="engineering_works_factory_industry_layout_1",
    layout=[
        (0, 0, "engineering_works_factory_spritelayout_1"),
        (0, 1, "engineering_works_factory_spritelayout_7"),
        (0, 2, "engineering_works_factory_spritelayout_1"),
        (0, 3, "engineering_works_factory_spritelayout_7"),
        (0, 4, "engineering_works_factory_spritelayout_12"),
        (1, 0, "engineering_works_factory_spritelayout_6"),
        (1, 1, "engineering_works_factory_spritelayout_5"),
        (1, 2, "engineering_works_factory_spritelayout_6"),
        (1, 3, "engineering_works_factory_spritelayout_5"),
        (1, 4, "engineering_works_factory_spritelayout_11"),
        (2, 0, "engineering_works_factory_spritelayout_1"),
        (2, 1, "engineering_works_factory_spritelayout_7"),
        (2, 2, "engineering_works_factory_spritelayout_13"),
        (2, 3, "engineering_works_factory_spritelayout_3"),
        (2, 4, "engineering_works_factory_spritelayout_4"),
        (3, 0, "engineering_works_factory_spritelayout_6"),
        (3, 1, "engineering_works_factory_spritelayout_5"),
        (3, 2, "engineering_works_factory_spritelayout_14"),
        (3, 3, "engineering_works_factory_spritelayout_2"),
        (3, 4, "engineering_works_factory_spritelayout_1"),
    ],
)
