from industry import IndustrySecondary, TileLocationChecks

# fabricator of pressure-grade, assembled liquid-handling systems

industry = IndustrySecondary(
    id="pipe_shop",
    accept_cargos_with_input_ratios=[("STPP", 2), ("STPL", 2), ("PUMP", 2), ("COAT", 1), ("WELD", 1)],
    prod_cargo_types_with_output_ratios=[
        # high output production is unwanted
        ("PPWK", 4),
        ("ENSP", 2),
        ("FMSP", 1),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="160",
    colour_scheme_name="scheme_10_wyclef",
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[
            ["tube_and_pipe_mill", "precision_parts_plant", "plate_mill"],
            84,
        ],
    ),
    name="string(STR_IND_PIPEWORK_FABRICATOR)",
    nearby_station_name="string(STR_STATION_PIPEWORK_FABRICATOR)",
    fund_cost_multiplier="145",
    intro_year=1790,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="pipe_shop_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="pipe_shop_tile_2",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
    always_draw=True,
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 31, -31, 0)],
    always_draw=True,
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
    always_draw=True,
)
spriteset_12 = industry.add_spriteset(
    sprites=[(850, 10, 64, 31, -35, 2)],
    always_draw=True,
)
spriteset_13 = industry.add_spriteset(
    sprites=[(920, 10, 64, 49, -39, -15)],
)
# out of sequence for historical reasons
spriteset_14 = industry.add_spriteset(
    sprites=[(710, 10, 64, 31, -28, -1)],
    always_draw=True,
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=13,
    yoffset=0,
    zoffset=73,
)

industry.add_spritelayout(
    id="pipe_shop_spritelayout_1",
    tile="pipe_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="pipe_shop_spritelayout_2",
    tile="pipe_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="pipe_shop_spritelayout_3",
    tile="pipe_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="pipe_shop_spritelayout_4",
    tile="pipe_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="pipe_shop_spritelayout_5",
    tile="pipe_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="pipe_shop_spritelayout_6",
    tile="pipe_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    # building_sprites = [spriteset_6, spriteset_14], # commented due to spritesorter issues obscuring spriteset_14
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="pipe_shop_spritelayout_7",
    tile="pipe_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="pipe_shop_spritelayout_8",
    tile="pipe_shop_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_8],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="pipe_shop_spritelayout_9",
    tile="pipe_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="pipe_shop_spritelayout_10",
    tile="pipe_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="pipe_shop_spritelayout_11",
    tile="pipe_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_11],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="pipe_shop_spritelayout_12",
    tile="pipe_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_12],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="pipe_shop_spritelayout_13",
    tile="pipe_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_13],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="pipe_shop_spritelayout_14",
    tile="pipe_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=[],
)

# this industry needs outpost layout as there are lots of cargos
industry.add_industry_outpost_layout(
    id="pipe_shop_industry_outpost_layout_1",
    layout=[
        # test outpost layout
        (
            0,
            0,
            "pipe_shop_spritelayout_1",
        ),
        (
            0,
            1,
            "pipe_shop_spritelayout_10",
        ),
        (
            0,
            2,
            "pipe_shop_spritelayout_12",
        ),
        (
            1,
            0,
            "pipe_shop_spritelayout_9",
        ),
        (
            1,
            1,
            "pipe_shop_spritelayout_8",
        ),
        (
            1,
            2,
            "pipe_shop_spritelayout_13",
        ),
    ],
)

industry.add_industry_layout(
    id="pipe_shop_industry_layout_1",
    layout=[
        (0, 0, "pipe_shop_spritelayout_3"),
        (0, 1, "pipe_shop_spritelayout_4"),
        (0, 2, "pipe_shop_spritelayout_1"),
        (0, 3, "pipe_shop_spritelayout_10"),
        (0, 4, "pipe_shop_spritelayout_1"),
        (0, 5, "pipe_shop_spritelayout_10"),
        (1, 0, "pipe_shop_spritelayout_12"),
        (1, 1, "pipe_shop_spritelayout_11"),
        (1, 2, "pipe_shop_spritelayout_9"),
        (1, 3, "pipe_shop_spritelayout_8"),
        (1, 4, "pipe_shop_spritelayout_9"),
        (1, 5, "pipe_shop_spritelayout_8"),
        (2, 0, "pipe_shop_spritelayout_13"),
        (2, 1, "pipe_shop_spritelayout_13"),
        (2, 2, "pipe_shop_spritelayout_14"),
        (2, 3, "pipe_shop_spritelayout_2"),
        (2, 4, "pipe_shop_spritelayout_1"),
        (2, 5, "pipe_shop_spritelayout_1"),
    ],
)
