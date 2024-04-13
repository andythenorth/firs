from industry import IndustryPrimaryPort, TileLocationChecks

industry = IndustryPrimaryPort(
    id="liquids_terminal",
    accept_cargo_types=[],
    prod_cargo_types_with_multipliers=[],
    prob_in_game="2",
    prob_map_gen="6",
    map_colour="164",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_LIQUIDS_TERMINAL)",
    nearby_station_name="string(STR_STATION_TANK_FARM)",
    fund_cost_multiplier="152",
    override_default_construction_states=True,
    primary_production_random_factor_set="wide_range",
    sprites_complete=True,
)

industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
    accept_cargo_types=["EOIL", "OIL_"],
    prod_cargo_types_with_multipliers=[
        ("RFPR", 11),
        ("PETR", 7),
    ],
)
# industry.economy_variations['IN_A_HOT_COUNTRY'].prod_cargo_types_with_multipliers = [('NH3_', 16)]

industry.add_tile(
    id="liquids_terminal_tile_1",
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="liquids_terminal_tile_2",
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
spriteset_small_tanks = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_office = industry.add_spriteset(
    sprites=[(440, 10, 64, 84, -31, -43)], zoffset=18
)
spriteset_spherical_tank = industry.add_spriteset(
    sprites=[(510, 10, 64, 84, -35, -61)],
)
spriteset_large_cylinder_tank = industry.add_spriteset(
    sprites=[(510, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_boat_1 = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -35, -15)],
)
spriteset_boat_2 = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -40, -12)],
)
spriteset_boat_3 = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -13, -19)],
)
spriteset_boat_4 = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -27, -12)],
)
industry.add_spritelayout(
    id="liquids_terminal_spritelayout_small_tanks",
    tile="liquids_terminal_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_small_tanks,
    ],
)
industry.add_magic_spritelayout(
    type="jetty_coast_foundations",
    base_id="liquids_terminal_spritelayout_coast_large_cylinder_tank",
    tile="liquids_terminal_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_large_cylinder_tank],
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
    base_id="liquids_terminal_spritelayout_coast_office",
    tile="liquids_terminal_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_office],
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
    base_id="liquids_terminal_spritelayout_coast_spherical_tank",
    tile="liquids_terminal_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_spherical_tank],
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

industry.add_spritelayout(
    id="liquids_terminal_spritelayout_water_barge_sw_ne",
    tile="liquids_terminal_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_1],
)
industry.add_spritelayout(
    id="liquids_terminal_spritelayout_water_barge_ne_sw",
    tile="liquids_terminal_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_2],
)
industry.add_spritelayout(
    id="liquids_terminal_spritelayout_water_barge_se_nw",
    tile="liquids_terminal_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_3],
)
industry.add_spritelayout(
    id="liquids_terminal_spritelayout_water_barge_nw_se",
    tile="liquids_terminal_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_4],
)
industry.add_spritelayout(
    id="liquids_terminal_spritelayout_water_empty",
    tile="liquids_terminal_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[],
)
industry.add_spritelayout(
    id="liquids_terminal_spritelayout_office",
    tile="liquids_terminal_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_office,
    ],
)
industry.add_spritelayout(
    id="liquids_terminal_spritelayout_large_cylinder_tank",
    tile="liquids_terminal_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_large_cylinder_tank,
    ],
)
industry.add_spritelayout(
    id="liquids_terminal_spritelayout_crane_ne_sw",
    tile="liquids_terminal_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_small_tanks,
    ],
)
industry.add_spritelayout(
    id="liquids_terminal_spritelayout_jetty_empty",
    tile="liquids_terminal_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete],
)

industry.add_industry_layout(
    id="liquids_terminal_industry_layout_1",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "liquids_terminal_spritelayout_water_empty"),
        (0, 2, "liquids_terminal_spritelayout_water_empty"),
        (0, 3, "liquids_terminal_spritelayout_office"),
        (
            0,
            4,
            "liquids_terminal_spritelayout_coast_spherical_tank",
        ),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "liquids_terminal_spritelayout_small_tanks"),
        (1, 2, "liquids_terminal_spritelayout_small_tanks"),
        (1, 3, "liquids_terminal_spritelayout_jetty_empty"),
        (1, 4, "liquids_terminal_spritelayout_coast_office"),
        (2, 0, "spritelayout_null_water"),
        (
            2,
            1,
            "liquids_terminal_spritelayout_water_barge_se_nw",
        ),
        (2, 2, "liquids_terminal_spritelayout_water_empty"),
        (
            2,
            3,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (
            2,
            4,
            "liquids_terminal_spritelayout_coast_large_cylinder_tank",
        ),
        (3, 0, "spritelayout_null_water"),
        (
            3,
            1,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (
            3,
            2,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (
            3,
            3,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (
            3,
            4,
            "liquids_terminal_spritelayout_coast_large_cylinder_tank",
        ),
        (4, 0, "spritelayout_null_water"),
        (4, 1, "liquids_terminal_spritelayout_water_empty"),
        (
            4,
            2,
            "liquids_terminal_spritelayout_water_barge_nw_se",
        ),
        (
            4,
            3,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (
            4,
            4,
            "liquids_terminal_spritelayout_coast_large_cylinder_tank",
        ),
        (5, 0, "spritelayout_null_water"),
        (5, 1, "spritelayout_null_water"),
        (5, 2, "spritelayout_null_water"),
        (5, 3, "spritelayout_null_water"),
        (5, 4, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="liquids_terminal_industry_layout_2",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "spritelayout_null_water"),
        (0, 2, "spritelayout_null_water"),
        (0, 3, "spritelayout_null_water"),
        (0, 4, "spritelayout_null_water"),
        (0, 5, "spritelayout_null_water"),
        (1, 0, "liquids_terminal_spritelayout_water_empty"),
        (
            1,
            1,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (
            1,
            2,
            "liquids_terminal_spritelayout_water_barge_sw_ne",
        ),
        (1, 3, "liquids_terminal_spritelayout_small_tanks"),
        (1, 4, "liquids_terminal_spritelayout_water_empty"),
        (1, 5, "spritelayout_null_water"),
        (2, 0, "liquids_terminal_spritelayout_water_empty"),
        (
            2,
            1,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (2, 2, "liquids_terminal_spritelayout_water_empty"),
        (2, 3, "liquids_terminal_spritelayout_small_tanks"),
        (
            2,
            4,
            "liquids_terminal_spritelayout_water_barge_ne_sw",
        ),
        (2, 5, "spritelayout_null_water"),
        (
            3,
            0,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (
            3,
            1,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (
            3,
            2,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (3, 3, "liquids_terminal_spritelayout_jetty_empty"),
        (3, 4, "liquids_terminal_spritelayout_office"),
        (3, 5, "spritelayout_null_water"),
        (
            4,
            0,
            "liquids_terminal_spritelayout_coast_large_cylinder_tank",
        ),
        (
            4,
            1,
            "liquids_terminal_spritelayout_coast_large_cylinder_tank",
        ),
        (
            4,
            2,
            "liquids_terminal_spritelayout_coast_large_cylinder_tank",
        ),
        (4, 3, "liquids_terminal_spritelayout_coast_office"),
        (
            4,
            4,
            "liquids_terminal_spritelayout_coast_spherical_tank",
        ),
    ],
)
industry.add_industry_layout(
    id="liquids_terminal_industry_layout_3",
    layout=[
        (
            0,
            1,
            "liquids_terminal_spritelayout_coast_spherical_tank",
        ),
        (0, 2, "liquids_terminal_spritelayout_coast_office"),
        (
            0,
            3,
            "liquids_terminal_spritelayout_coast_large_cylinder_tank",
        ),
        (
            0,
            4,
            "liquids_terminal_spritelayout_coast_large_cylinder_tank",
        ),
        (
            0,
            5,
            "liquids_terminal_spritelayout_coast_large_cylinder_tank",
        ),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "liquids_terminal_spritelayout_office"),
        (1, 2, "liquids_terminal_spritelayout_jetty_empty"),
        (
            1,
            3,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (
            1,
            4,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (
            1,
            5,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (2, 0, "spritelayout_null_water"),
        (2, 1, "liquids_terminal_spritelayout_water_empty"),
        (2, 2, "liquids_terminal_spritelayout_small_tanks"),
        (2, 3, "liquids_terminal_spritelayout_water_empty"),
        (
            2,
            4,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (
            2,
            5,
            "liquids_terminal_spritelayout_water_barge_se_nw",
        ),
        (3, 0, "spritelayout_null_water"),
        (3, 1, "liquids_terminal_spritelayout_water_empty"),
        (3, 2, "liquids_terminal_spritelayout_crane_ne_sw"),
        (
            3,
            3,
            "liquids_terminal_spritelayout_water_barge_ne_sw",
        ),
        (
            3,
            4,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (3, 5, "liquids_terminal_spritelayout_water_empty"),
        (4, 0, "spritelayout_null_water"),
        (4, 1, "spritelayout_null_water"),
        (4, 2, "spritelayout_null_water"),
        (4, 3, "spritelayout_null_water"),
        (4, 4, "spritelayout_null_water"),
        (4, 5, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="liquids_terminal_industry_layout_4",
    layout=[
        (
            0,
            0,
            "liquids_terminal_spritelayout_coast_large_cylinder_tank",
        ),
        (
            0,
            1,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (0, 2, "liquids_terminal_spritelayout_water_empty"),
        (0, 3, "liquids_terminal_spritelayout_water_empty"),
        (0, 4, "spritelayout_null_water"),
        (
            1,
            0,
            "liquids_terminal_spritelayout_coast_large_cylinder_tank",
        ),
        (
            1,
            1,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (
            1,
            2,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (
            1,
            3,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (1, 4, "spritelayout_null_water"),
        (
            2,
            0,
            "liquids_terminal_spritelayout_coast_large_cylinder_tank",
        ),
        (
            2,
            1,
            "liquids_terminal_spritelayout_large_cylinder_tank",
        ),
        (2, 2, "liquids_terminal_spritelayout_water_empty"),
        (
            2,
            3,
            "liquids_terminal_spritelayout_water_barge_nw_se",
        ),
        (2, 4, "spritelayout_null_water"),
        (3, 0, "liquids_terminal_spritelayout_coast_office"),
        (3, 1, "liquids_terminal_spritelayout_jetty_empty"),
        (3, 2, "liquids_terminal_spritelayout_small_tanks"),
        (3, 3, "liquids_terminal_spritelayout_small_tanks"),
        (3, 4, "spritelayout_null_water"),
        (
            4,
            0,
            "liquids_terminal_spritelayout_coast_spherical_tank",
        ),
        (4, 1, "liquids_terminal_spritelayout_office"),
        (
            4,
            2,
            "liquids_terminal_spritelayout_water_barge_ne_sw",
        ),
        (4, 3, "liquids_terminal_spritelayout_water_empty"),
        (4, 4, "spritelayout_null_water"),
        (5, 2, "spritelayout_null_water"),
        (5, 3, "spritelayout_null_water"),
        (5, 4, "spritelayout_null_water"),
    ],
)
