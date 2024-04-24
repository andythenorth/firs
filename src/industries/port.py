from industry import IndustryPrimaryPort, TileLocationChecks

industry = IndustryPrimaryPort(
    id="port",
    accept_cargo_types=[],
    prod_cargo_types_with_multipliers=[],
    prob_in_game="2",
    prob_map_gen="8",
    map_colour="186",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(same_type_distance=32),
    prospect_chance="0.75",
    name="string(STR_IND_PORT)",
    nearby_station_name="string(STR_STATION_INDUSTRY_HARBOUR_2)",
    fund_cost_multiplier="152",
    override_default_construction_states=True,
    primary_production_random_factor_set="wide_range",
    sprites_complete=True,
)

industry.enable_in_economy(
    "BASIC_TEMPERATE",
    accept_cargo_types=[
        "GOOD",
        "KAOL",
        "FOOD",
    ],
    prod_cargo_types_with_multipliers=[
        ("ENSP", 19),
        ("FMSP", 7),
        ("RFPR", 19),
    ],
    prob_map_gen="10",
)

industry.enable_in_economy(
    "BASIC_ARCTIC",
    accept_cargo_types=[
        "PAPR",
        "ZINC",
        "FERT",
    ],
    prod_cargo_types_with_multipliers=[
        ("KAOL", 16),
        ("NH3_", 17),
        ("ENSP", 9),
        ("FMSP", 9),
    ],
)

industry.enable_in_economy(
    "BASIC_TROPIC",
    accept_cargo_types=[
        "COPR",
        "JAVA",
        "WOOL",
        "BEER",
        "RFPR",
        "FOOD",
    ],
    prod_cargo_types_with_multipliers=[
        ("ENSP", 9),
        ("GOOD", 17),
        ("FMSP", 12),
    ],
)

industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
    accept_cargo_types=[
        "COPR",
        "FRUT",
        "WDPR",
    ],
    prod_cargo_types_with_multipliers=[
        ("GOOD", 14),
        ("ENSP", 17),
    ],
)
industry.enable_in_economy(
    "STEELTOWN",
    # quite a lot of accepted types, this is intentional to provide flexibility in obtaining boost
    accept_cargo_types=["FOOD", "POTA", "CHLO", "CMNT", "STIG", "STSE", "STSH"],
    prod_cargo_types_with_multipliers=[
        ("RUBR", 16),
        ("FEAL", 20),
        ("ALUM", 11),
        ("ZINC", 16),
    ],
)
# industry.economy_variations['IN_A_HOT_COUNTRY'].accept_cargo_types = ['DIAM', 'EOIL', 'JAVA', 'WDPR']
# industry.economy_variations['IN_A_HOT_COUNTRY'].prod_cargo_types_with_multipliers = [('GOOD', 14), ('SASH', 12)]

industry.add_tile(
    id="port_tile_1",
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="port_tile_2",
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
spriteset_warehouse = industry.add_spriteset(
    sprites=[(440, 10, 64, 74, -31, -34)], zoffset=18
)
spriteset_9 = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, 0)],
    yoffset=4,
    zoffset=27,
    yextent=12,
)
spriteset_9b = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, 0)],
    xoffset=5,
    zoffset=40,
    xextent=11,
)
spriteset_10 = industry.add_spriteset(
    sprites=[(220, 10, 64, 39, -31, -7)],
    yoffset=4,
    zoffset=27,
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
spriteset_15 = industry.add_spriteset(
    sprites=[(290, 110, 64, 39, -15, -11)],
)
spriteset_16 = industry.add_spriteset(
    sprites=[(360, 110, 64, 39, -45, -15)],
)
spriteset_truck = industry.add_spriteset(
    sprites=[(360, 10, 64, 39, -31, 0)],
    zoffset=18,
)
# spritelayout numbers have gaps for historical reasons
industry.add_spritelayout(
    id="port_spritelayout_2",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_truck,
    ],
)
industry.add_spritelayout(
    id="port_spritelayout_11",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_concrete, spriteset_warehouse],
)
industry.add_spritelayout(
    id="port_spritelayout_12",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_ne_sw, spriteset_concrete, spriteset_warehouse],
)
industry.add_spritelayout(
    id="port_spritelayout_13",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_warehouse,
    ],
)
industry.add_spritelayout(
    id="port_spritelayout_21",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_11],
)
industry.add_spritelayout(
    id="port_spritelayout_22",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_12],
)
industry.add_spritelayout(
    id="port_spritelayout_23",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_13],
)
industry.add_spritelayout(
    id="port_spritelayout_24",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_14],
)
industry.add_spritelayout(
    id="port_spritelayout_25",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_14],
)
industry.add_spritelayout(
    id="port_spritelayout_26",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_15],
)
industry.add_spritelayout(
    id="port_spritelayout_27",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_16],
)
industry.add_spritelayout(
    id="port_spritelayout_28",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_9,
    ],
)
industry.add_spritelayout(
    id="port_spritelayout_29",
    tile="port_tile_1",
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
    id="port_spritelayout_30",
    tile="port_tile_1",
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
    base_id="port_spritelayout_coast_warehouse",
    tile="port_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_warehouse],
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
    base_id="port_spritelayout_coast_truck",
    tile="port_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_truck],
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
    id="port_industry_layout_1",
    layout=[
        (0, 3, "port_spritelayout_27"),
        (0, 4, "port_spritelayout_coast_truck"),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "port_spritelayout_11"),
        (1, 2, "port_spritelayout_29"),
        (1, 3, "port_spritelayout_11"),
        (1, 4, "port_spritelayout_coast_warehouse"),
        (2, 1, "port_spritelayout_24"),
        (2, 2, "port_spritelayout_24"),
    ],
)
industry.add_industry_layout(
    id="port_industry_layout_2",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "spritelayout_null_water"),
        (0, 2, "spritelayout_null_water"),
        (1, 0, "port_spritelayout_23"),
        (1, 1, "port_spritelayout_23"),
        (1, 255, "spritelayout_null_water"),
        (2, 0, "port_spritelayout_30"),
        (2, 1, "port_spritelayout_12"),
        (2, 2, "port_spritelayout_21"),
        (2, 255, "spritelayout_null_water"),
        (3, 1, "port_spritelayout_coast_warehouse"),
        (3, 2, "port_spritelayout_coast_truck"),
    ],
)
industry.add_industry_layout(
    id="port_industry_layout_3",
    layout=[
        (0, 0, "port_spritelayout_coast_warehouse"),
        (0, 1, "port_spritelayout_coast_warehouse"),
        (0, 2, "port_spritelayout_coast_warehouse"),
        (1, 0, "port_spritelayout_24"),
        (1, 2, "port_spritelayout_2"),
        (2, 1, "port_spritelayout_26"),
        (2, 2, "port_spritelayout_28"),
        (2, 3, "port_spritelayout_22"),
        (2, 4, "spritelayout_null_water"),
        (3, 2, "spritelayout_null_water"),
        (3, 3, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="port_industry_layout_4",
    layout=[
        (0, 0, "port_spritelayout_coast_warehouse"),
        (0, 1, "port_spritelayout_2"),
        (0, 2, "port_spritelayout_29"),
        (0, 3, "port_spritelayout_11"),
        (0, 4, "port_spritelayout_28"),
        (0, 5, "spritelayout_null_water"),
        (1, 0, "port_spritelayout_coast_warehouse"),
        (1, 1, "port_spritelayout_28"),
        (1, 2, "port_spritelayout_25"),
        (1, 4, "port_spritelayout_25"),
        (1, 5, "spritelayout_null_water"),
        (2, 3, "spritelayout_null_water"),
        (2, 4, "spritelayout_null_water"),
        (2, 5, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="port_industry_layout_5",
    layout=[
        (0, 0, "port_spritelayout_coast_warehouse"),
        (1, 0, "port_spritelayout_12"),
        (1, 2, "spritelayout_null_water"),
        (2, 0, "port_spritelayout_12"),
        (2, 1, "port_spritelayout_29"),
        (2, 2, "port_spritelayout_28"),
        (2, 3, "spritelayout_null_water"),
        (3, 0, "port_spritelayout_12"),
        (3, 1, "port_spritelayout_2"),
        (3, 2, "port_spritelayout_28"),
        (3, 3, "spritelayout_null_water"),
        (4, 255, "spritelayout_null_water"),
        (4, 0, "port_spritelayout_13"),
        (4, 1, "port_spritelayout_24"),
        (4, 2, "port_spritelayout_24"),
        (4, 3, "spritelayout_null_water"),
        (5, 255, "spritelayout_null_water"),
        (5, 0, "spritelayout_null_water"),
        (5, 1, "spritelayout_null_water"),
        (5, 2, "spritelayout_null_water"),
        (5, 3, "spritelayout_null_water"),
    ],
)
