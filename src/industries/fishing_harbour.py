from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="fishing_harbour",
    accept_cargos_with_input_ratios=[
        ("FISH", 6),
    ],
    prod_cargo_types_with_output_ratios=[
        ("FOOD", 8),
    ],
    prob_in_game="10",
    prob_map_gen="10",
    map_colour="169",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[
            ["fishing_grounds", "fish_farm"],
            72,
        ]
    ),
    name="string(STR_IND_FISHING_HARBOUR)",
    nearby_station_name="string(STR_STATION_FISHMARKET)",
    fund_cost_multiplier="150",
    override_default_construction_states=True,
    pollution_and_squalor_factor=1,
    sprites_complete=True,
)

industry.enable_in_economy(
    "BASIC_TEMPERATE",
)
industry.enable_in_economy(
    "BASIC_TROPIC",
)
industry.enable_in_economy(
    "BASIC_ARCTIC",
)

# ['IN_A_HOT_COUNTRY'].enabled = True

industry.add_tile(
    id="fishing_harbour_tile_1",
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="fishing_harbour_tile_2",
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
spriteset_shed = industry.add_spriteset(sprites=[(80, 10, 64, 39, -31, 0)], zoffset=18)
spriteset_crane_1a = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, 0)],
    yoffset=4,
    zoffset=27,
    yextent=12,
)
spriteset_crane_1b = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, 0)],
    xoffset=5,
    zoffset=40,
    xextent=11,
)
spriteset_crane_2 = industry.add_spriteset(
    sprites=[(220, 10, 64, 39, -31, -7)],
    yoffset=4,
    zoffset=27,
    yextent=12,
)
spriteset_trawler_sw_ne = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -35, -15)],
)
spriteset_trawler_ne_sw = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -31, -14)],
)
spriteset_trawler_nw_se = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -31, -8)],
)
spriteset_trawler_nw_se = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -27, -12)],
)
spriteset_ship_ne_sw = industry.add_spriteset(
    sprites=[(290, 110, 64, 39, -15, -11)],
)
spriteset_ship_nw_se = industry.add_spriteset(
    sprites=[(360, 110, 64, 39, -45, -15)],
)
spriteset_ramp_rear = industry.add_spriteset(
    sprites=[(440, 110, 64, 74, -31, -26)], always_draw=1
)
spriteset_ramp_front = industry.add_spriteset(
    sprites=[(510, 110, 64, 74, -31, -42)], always_draw=1
)
spriteset_empty = industry.add_spriteset(
    sprites=[(360, 10, 64, 39, -31, 0)],
    zoffset=18,
)

industry.add_spritelayout(
    id="fishing_harbour_spritelayout_1",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_jetty_se_nw, spriteset_concrete, spriteset_empty],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_2",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_jetty_ne_sw, spriteset_concrete, spriteset_empty],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_11",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_jetty_se_nw, spriteset_concrete, spriteset_shed],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_12",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_jetty_ne_sw, spriteset_concrete, spriteset_shed],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_13",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_shed,
    ],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_21",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_trawler_sw_ne],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_22",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_trawler_ne_sw],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_23",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_trawler_nw_se],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_24",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_trawler_nw_se],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_25",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_trawler_nw_se],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_26",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_ship_ne_sw],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_27",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_ship_nw_se],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_28",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_crane_1a,
    ],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_29",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_crane_2,
    ],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_30",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_crane_1b,
    ],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_31",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_ramp_rear],
)
industry.add_spritelayout(
    id="fishing_harbour_spritelayout_32",
    tile="fishing_harbour_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_ramp_front],
)
industry.add_magic_spritelayout(
    type="jetty_coast_foundations",
    base_id="fishing_harbour_spritelayout_coast_empty",
    tile="fishing_harbour_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_empty],
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
    base_id="fishing_harbour_spritelayout_coast_shed",
    tile="fishing_harbour_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_shed],
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
    id="fishing_harbour_industry_layout_1",
    layout=[
        (0, 3, "fishing_harbour_spritelayout_27"),
        (0, 4, "fishing_harbour_spritelayout_coast_empty"),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "fishing_harbour_spritelayout_11"),
        (1, 2, "fishing_harbour_spritelayout_29"),
        (1, 3, "fishing_harbour_spritelayout_11"),
        (1, 4, "fishing_harbour_spritelayout_coast_shed"),
        (2, 1, "fishing_harbour_spritelayout_24"),
        (2, 2, "fishing_harbour_spritelayout_24"),
    ],
)
industry.add_industry_layout(
    id="fishing_harbour_industry_layout_2",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "spritelayout_null_water"),
        (0, 2, "spritelayout_null_water"),
        (1, 0, "fishing_harbour_spritelayout_23"),
        (1, 1, "fishing_harbour_spritelayout_23"),
        (1, 2, "spritelayout_null_water"),
        (2, 0, "fishing_harbour_spritelayout_30"),
        (2, 1, "fishing_harbour_spritelayout_12"),
        (2, 2, "fishing_harbour_spritelayout_21"),
        (2, 3, "spritelayout_null_water"),
        (3, 1, "fishing_harbour_spritelayout_coast_shed"),
        (3, 2, "fishing_harbour_spritelayout_coast_empty"),
    ],
)
industry.add_industry_layout(
    id="fishing_harbour_industry_layout_3",
    layout=[
        (0, 0, "fishing_harbour_spritelayout_coast_shed"),
        (0, 1, "fishing_harbour_spritelayout_coast_shed"),
        (0, 2, "fishing_harbour_spritelayout_coast_shed"),
        (1, 0, "fishing_harbour_spritelayout_24"),
        (1, 2, "fishing_harbour_spritelayout_2"),
        (2, 1, "fishing_harbour_spritelayout_26"),
        (2, 2, "fishing_harbour_spritelayout_28"),
        (2, 3, "fishing_harbour_spritelayout_22"),
        (2, 4, "spritelayout_null_water"),
        (3, 2, "spritelayout_null_water"),
        (3, 3, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="fishing_harbour_industry_layout_4",
    layout=[
        (0, 0, "fishing_harbour_spritelayout_coast_shed"),
        (0, 1, "fishing_harbour_spritelayout_11"),
        (0, 2, "fishing_harbour_spritelayout_1"),
        (0, 3, "fishing_harbour_spritelayout_1"),
        (0, 4, "fishing_harbour_spritelayout_28"),
        (0, 5, "spritelayout_null_water"),
        (1, 0, "fishing_harbour_spritelayout_coast_empty"),
        (1, 1, "fishing_harbour_spritelayout_31"),
        (1, 2, "fishing_harbour_spritelayout_32"),
        (1, 4, "fishing_harbour_spritelayout_25"),
        (1, 5, "spritelayout_null_water"),
        (2, 3, "spritelayout_null_water"),
        (2, 4, "spritelayout_null_water"),
        (2, 5, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="fishing_harbour_industry_layout_5",
    layout=[
        (0, 0, "fishing_harbour_spritelayout_coast_empty"),
        (1, 0, "fishing_harbour_spritelayout_28"),
        (1, 2, "spritelayout_null_water"),
        (2, 0, "fishing_harbour_spritelayout_2"),
        (2, 1, "fishing_harbour_spritelayout_31"),
        (2, 2, "fishing_harbour_spritelayout_32"),
        (2, 3, "spritelayout_null_water"),
        (3, 0, "fishing_harbour_spritelayout_30"),
        (3, 1, "fishing_harbour_spritelayout_13"),
        (3, 2, "fishing_harbour_spritelayout_13"),
        (3, 3, "spritelayout_null_water"),
        (3, 4, "spritelayout_null_water"),
        (4, 0, "fishing_harbour_spritelayout_24"),
        (4, 1, "fishing_harbour_spritelayout_24"),
        (4, 2, "fishing_harbour_spritelayout_24"),
        (4, 3, "spritelayout_null_water"),
        (4, 4, "spritelayout_null_water"),
        (5, 0, "spritelayout_null_water"),
        (5, 1, "spritelayout_null_water"),
        (5, 2, "spritelayout_null_water"),
        (5, 3, "spritelayout_null_water"),
    ],
)
