from industry import IndustryPrimaryPort, TileLocationChecks

industry = IndustryPrimaryPort(
    id="trading_post",
    accept_cargo_types=[
        "DIAM",
        "JAVA",
        "RUBR",
    ],
    prod_cargo_types_with_multipliers=[
        ("ENSP", 7),
        ("FMSP", 6),
    ],
    prob_in_game="2",
    prob_map_gen="6",
    map_colour="177",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_TRADING_POST)",
    nearby_station_name="string(STR_STATION_INDUSTRY_HARBOUR_3)",
    fund_cost_multiplier="152",
    override_default_construction_states=True,
    primary_production_random_factor_set="wide_range",
    sprites_complete=True,
)

industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
)

industry.add_tile(
    id="trading_post_tile_1",
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="trading_post_tile_2",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)
sprite_ground = industry.add_sprite(sprite_number="GROUNDSPRITE_WATER")
spriteset_ground_empty = industry.add_spriteset(type="empty")
spriteset_concrete = industry.add_spriteset(
    sprites=[(10, 10, 64, 39, -31, -8)],
    always_draw=1,
)
spriteset_jetty_se_nw = industry.add_spriteset(
    sprites=[(10, 60, 64, 39, -31, -7)],
    always_draw=1,
)
spriteset_jetty_ne_sw = industry.add_spriteset(
    sprites=[(80, 60, 64, 39, -31, -7)], always_draw=1
)
spriteset_jetty_slope_nw_se = industry.add_spriteset(
    sprites=[(150, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_ne_sw = industry.add_spriteset(
    sprites=[(220, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_se_nw = industry.add_spriteset(
    sprites=[(290, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_sw_ne = industry.add_spriteset(
    sprites=[(360, 60, 64, 39, -31, -7)],
)
spriteset_large_warehouse = industry.add_spriteset(
    sprites=[(80, 10, 64, 39, -31, 0)], zoffset=18
)
spriteset_9 = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, 0)],
    yoffset=4,
    zoffset=27,
    yextent=12,
)
spriteset_9b = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, -7)],
    xoffset=0,
    zoffset=12,
    xextent=11,
)
spriteset_10 = industry.add_spriteset(
    sprites=[(220, 10, 64, 39, -31, -7)],
    yoffset=0,
    zoffset=12,
    yextent=12,
)
spriteset_11 = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -35, -15)],
)
spriteset_12 = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -31, -14)],
)
spriteset_13 = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -31, -8)],
)
spriteset_14 = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -27, -12)],
)
spriteset_small_warehouse = industry.add_spriteset(
    sprites=[(360, 10, 64, 39, -31, 0)],
    zoffset=18,
)

industry.add_spritelayout(
    id="trading_post_spritelayout_11",
    tile="trading_post_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_concrete,
        spriteset_large_warehouse,
    ],
)
industry.add_spritelayout(
    id="trading_post_spritelayout_12",
    tile="trading_post_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_large_warehouse,
    ],
)
industry.add_spritelayout(
    id="trading_post_spritelayout_13",
    tile="trading_post_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_large_warehouse,
    ],
)
industry.add_spritelayout(
    id="trading_post_spritelayout_21",
    tile="trading_post_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_11],
)
industry.add_spritelayout(
    id="trading_post_spritelayout_22",
    tile="trading_post_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_12],
)
industry.add_spritelayout(
    id="trading_post_spritelayout_23",
    tile="trading_post_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_13],
)
industry.add_spritelayout(
    id="trading_post_spritelayout_24",
    tile="trading_post_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_14],
)
industry.add_spritelayout(
    id="trading_post_spritelayout_25",
    tile="trading_post_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_14],
)
industry.add_spritelayout(
    id="trading_post_spritelayout_26",
    tile="trading_post_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[],
)
industry.add_spritelayout(
    id="trading_post_spritelayout_27",
    tile="trading_post_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[],
)
# trading_post_spritelayout_28 fell out of use and was removed
industry.add_spritelayout(
    id="trading_post_spritelayout_29",
    tile="trading_post_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_10,
    ],
)
industry.add_spritelayout(
    id="trading_post_spritelayout_30",
    tile="trading_post_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_9b,
    ],
)
industry.add_magic_spritelayout(
    type="jetty_coast_foundations",
    base_id="trading_post_spritelayout_coast_small_warehouse",
    tile="trading_post_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_small_warehouse],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_coast_foundations",
    base_id="trading_post_spritelayout_coast_large_warehouse",
    tile="trading_post_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_large_warehouse],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)

industry.add_industry_layout(
    id="trading_post_industry_layout_1",
    layout=[
        (0, 2, "trading_post_spritelayout_27"),
        (
            0,
            3,
            "trading_post_spritelayout_coast_small_warehouse",
        ),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "trading_post_spritelayout_11"),
        (1, 2, "trading_post_spritelayout_29"),
        (
            1,
            3,
            "trading_post_spritelayout_coast_large_warehouse",
        ),
        (2, 1, "trading_post_spritelayout_24"),
        (2, 2, "trading_post_spritelayout_24"),
    ],
)
industry.add_industry_layout(
    id="trading_post_industry_layout_2",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "spritelayout_null_water"),
        (0, 2, "spritelayout_null_water"),
        (1, 0, "trading_post_spritelayout_23"),
        (1, 1, "trading_post_spritelayout_23"),
        (1, 255, "spritelayout_null_water"),
        (2, 0, "trading_post_spritelayout_30"),
        (2, 1, "trading_post_spritelayout_12"),
        (2, 2, "trading_post_spritelayout_21"),
        (2, 255, "spritelayout_null_water"),
        (
            3,
            1,
            "trading_post_spritelayout_coast_large_warehouse",
        ),
        (
            3,
            2,
            "trading_post_spritelayout_coast_small_warehouse",
        ),
    ],
)
industry.add_industry_layout(
    id="trading_post_industry_layout_3",
    layout=[
        (
            0,
            0,
            "trading_post_spritelayout_coast_large_warehouse",
        ),
        (
            0,
            1,
            "trading_post_spritelayout_coast_large_warehouse",
        ),
        (
            0,
            2,
            "trading_post_spritelayout_coast_small_warehouse",
        ),
        (1, 0, "trading_post_spritelayout_24"),
        (1, 2, "trading_post_spritelayout_30"),
        (2, 1, "trading_post_spritelayout_26"),
        (2, 2, "trading_post_spritelayout_29"),
        (2, 3, "trading_post_spritelayout_22"),
        (2, 4, "spritelayout_null_water"),
        (3, 2, "spritelayout_null_water"),
        (3, 3, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="trading_post_industry_layout_4",
    layout=[
        (
            0,
            0,
            "trading_post_spritelayout_coast_large_warehouse",
        ),
        (0, 1, "spritelayout_null_water"),
        (
            1,
            0,
            "trading_post_spritelayout_coast_large_warehouse",
        ),
        (1, 1, "trading_post_spritelayout_29"),
        (1, 2, "trading_post_spritelayout_30"),
        (1, 3, "spritelayout_null_water"),
        (
            2,
            0,
            "trading_post_spritelayout_coast_small_warehouse",
        ),
        (2, 1, "trading_post_spritelayout_25"),
        (2, 2, "spritelayout_null_water"),
        (3, 2, "spritelayout_null_water"),
        (3, 3, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="trading_post_industry_layout_5",
    layout=[
        (
            0,
            0,
            "trading_post_spritelayout_coast_small_warehouse",
        ),
        (
            1,
            0,
            "trading_post_spritelayout_coast_large_warehouse",
        ),
        (1, 2, "spritelayout_null_water"),
        (2, 0, "trading_post_spritelayout_13"),
        (2, 1, "trading_post_spritelayout_29"),
        (2, 2, "trading_post_spritelayout_30"),
        (2, 3, "spritelayout_null_water"),
        (3, 255, "spritelayout_null_water"),
        (3, 0, "trading_post_spritelayout_24"),
        (3, 1, "trading_post_spritelayout_24"),
        (3, 2, "trading_post_spritelayout_24"),
        (3, 3, "spritelayout_null_water"),
        (4, 255, "spritelayout_null_water"),
        (4, 0, "spritelayout_null_water"),
        (4, 1, "spritelayout_null_water"),
        (4, 2, "spritelayout_null_water"),
        (4, 3, "spritelayout_null_water"),
    ],
)
