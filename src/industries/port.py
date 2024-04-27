from industry import IndustryPrimaryPort, TileLocationChecks

industry = IndustryPrimaryPort(
    id="port",
    accept_cargo_types=[],
    prod_cargo_types_with_multipliers=[],
    prob_in_game="2",
    prob_map_gen="8",
    # map_colour="186", # former orange before v5?
    # map_colour="177",  # former Bulk Terminal colour?
    map_colour="45",
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
spriteset_warehouse_half_nw_se = industry.add_spriteset(
    sprites=[(440, 10, 64, 84, -31, -61)],
)
spriteset_warehouse_half_ne_sw = industry.add_spriteset(
    sprites=[(510, 10, 64, 84, -31, -61)],
)
spriteset_warehouse_half_se_nw = industry.add_spriteset(
    sprites=[(580, 10, 64, 84, -31, -61)],
)
spriteset_warehouse_half_sw_ne = industry.add_spriteset(
    sprites=[(650, 10, 64, 84, -31, -61)],
)
spriteset_warehouse_nw_se = industry.add_spriteset(
    sprites=[(720, 10, 64, 84, -31, -61)],
)
spriteset_warehouse_ne_sw = industry.add_spriteset(
    sprites=[(790, 10, 64, 84, -31, -61)],
)
spriteset_shed_nw_se = industry.add_spriteset(
    sprites=[(440, 210, 64, 84, -31, -61)],
)
spriteset_tanks_small = industry.add_spriteset(
    sprites=[(720, 110, 64, 84, -31, -61)],
)
spriteset_tanks_sphere = industry.add_spriteset(
    sprites=[(790, 110, 64, 84, -31, -61)],
)
spriteset_silos_1 = industry.add_spriteset(
    sprites=[(720, 210, 64, 84, -31, -61)],
)
spriteset_crawler_crane_ne_sw = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_crawler_crane_nw_se = industry.add_spriteset(
    sprites=[(510, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_crawler_crane_se_nw = industry.add_spriteset(
    sprites=[(580, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_crawler_crane_sw_ne = industry.add_spriteset(
    sprites=[(650, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_ship_ne_sw = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -15, -11)],
)
spriteset_ship_nw_se = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -20, -15)],
)
spriteset_ship_sw_ne = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -15, -11)],
)
spriteset_ship_se_nw = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -25, -20)],
)
industry.add_spritelayout(
    id="port_spritelayout_water_empty",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[],
)
industry.add_spritelayout(
    id="port_spritelayout_jetty_empty",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete],
)
industry.add_magic_spritelayout(
    type="jetty_coast_foundations",
    base_id="port_spritelayout_coast_shed",
    tile="port_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_shed_nw_se],
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
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_crane_parallel_auto_orient",
    tile="port_tile_1",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "foundation_sprites": [spriteset_jetty_ne_sw, spriteset_jetty_se_nw],
        "jetty_top_sprites": [spriteset_concrete],
        "building_sprites": {
            "se": [
                spriteset_crawler_crane_se_nw,
            ],
            "sw": [
                spriteset_crawler_crane_ne_sw,
            ],
            "nw": [
                spriteset_crawler_crane_se_nw,
            ],
            "ne": [
                spriteset_crawler_crane_ne_sw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_crane_orthogonal_auto_orient",
    tile="port_tile_1",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "foundation_sprites": [spriteset_jetty_ne_sw, spriteset_jetty_se_nw],
        "jetty_top_sprites": [spriteset_concrete],
        "building_sprites": {
            "se": [
                spriteset_crawler_crane_ne_sw,
            ],
            "sw": [
                spriteset_crawler_crane_nw_se,
            ],
            "nw": [
                spriteset_crawler_crane_sw_ne,
            ],
            "ne": [
                spriteset_crawler_crane_se_nw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_tanks_small_auto_orient",
    tile="port_tile_1",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "foundation_sprites": [spriteset_jetty_ne_sw, spriteset_jetty_se_nw],
        "jetty_top_sprites": [spriteset_concrete],
        "building_sprites": {
            "se": [
                spriteset_tanks_small,
            ],
            "sw": [
                spriteset_tanks_small,
            ],
            "nw": [
                spriteset_tanks_small,
            ],
            "ne": [
                spriteset_tanks_small,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_tanks_sphere_auto_orient",
    tile="port_tile_1",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "foundation_sprites": [spriteset_jetty_ne_sw, spriteset_jetty_se_nw],
        "jetty_top_sprites": [spriteset_concrete],
        "building_sprites": {
            "se": [
                spriteset_tanks_sphere,
            ],
            "sw": [
                spriteset_tanks_sphere,
            ],
            "nw": [
                spriteset_tanks_sphere,
            ],
            "ne": [
                spriteset_tanks_sphere,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_silos_1_auto_orient",
    tile="port_tile_1",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "foundation_sprites": [spriteset_jetty_ne_sw, spriteset_jetty_se_nw],
        "jetty_top_sprites": [spriteset_concrete],
        "building_sprites": {
            "se": [
                spriteset_silos_1,
            ],
            "sw": [
                spriteset_silos_1,
            ],
            "nw": [
                spriteset_silos_1,
            ],
            "ne": [
                spriteset_silos_1,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_warehouse_half_auto_orient",
    tile="port_tile_1",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "foundation_sprites": [spriteset_jetty_ne_sw, spriteset_jetty_se_nw],
        "jetty_top_sprites": [spriteset_concrete],
        "building_sprites": {
            "se": [
                spriteset_warehouse_half_nw_se,
            ],
            "sw": [
                spriteset_warehouse_half_sw_ne,
            ],
            "nw": [
                spriteset_warehouse_half_se_nw,
            ],
            "ne": [
                spriteset_warehouse_half_ne_sw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_warehouse_full_auto_orient",
    tile="port_tile_1",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "foundation_sprites": [spriteset_jetty_ne_sw, spriteset_jetty_se_nw],
        "jetty_top_sprites": [spriteset_concrete],
        "building_sprites": {
            "se": [
                spriteset_warehouse_nw_se,
            ],
            "sw": [
                spriteset_warehouse_ne_sw,
            ],
            "nw": [
                spriteset_warehouse_nw_se,
            ],
            "ne": [
                spriteset_warehouse_ne_sw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_shed_auto_orient",
    tile="port_tile_1",
    config={
        "ground_sprite": spriteset_ground_empty,  # should always be empty for this magic spritelayout
        "foundation_sprites": [spriteset_jetty_ne_sw, spriteset_jetty_se_nw],
        "jetty_top_sprites": [spriteset_concrete],
        "building_sprites": {
            "se": [
                spriteset_shed_nw_se,
                spriteset_crawler_crane_nw_se,
            ],
            "sw": [
                spriteset_shed_nw_se,
                spriteset_crawler_crane_nw_se,
            ],
            "nw": [
                spriteset_shed_nw_se,
                spriteset_crawler_crane_nw_se,
            ],
            "ne": [
                spriteset_shed_nw_se,
                spriteset_crawler_crane_nw_se,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_water_ship_auto_orient",
    tile="port_tile_1",
    config={
        "ground_sprite": sprite_ground,
        "foundation_sprites": [],
        "jetty_top_sprites": [],
        "building_sprites": {
            "se": [
                spriteset_ship_nw_se,  # wrong? or needs offsets adjusted?
            ],
            "sw": [
                spriteset_ship_ne_sw,  # wrong? or needs offsets adjusted?
            ],
            "nw": [
                spriteset_ship_se_nw,  # wrong? or needs offsets adjusted?
            ],
            "ne": [
                spriteset_ship_sw_ne,  # wrong? or needs offsets adjusted?
            ],
        },
    },
)
industry.add_industry_jetty_layout(
    id="port_industry_jetty_layout_1",
    layout=[
        # ensure spacing from coast, to improve map-gen buildabilty
        (0, 2, "port_spritelayout_warehouse_full_auto_orient"),
        (0, 3, "port_spritelayout_warehouse_half_auto_orient"),
        (0, 4, "port_spritelayout_silos_1_auto_orient"),
        (0, 5, "port_spritelayout_silos_1_auto_orient"),
        (0, 6, "port_spritelayout_warehouse_half_auto_orient"),
        (0, 7, "spritelayout_null_water"),
        (1, 0, "port_spritelayout_coast_shed"),
        (1, 1, "port_spritelayout_warehouse_full_auto_orient"),
        (1, 2, "port_spritelayout_warehouse_half_auto_orient"),
        (1, 3, "port_spritelayout_warehouse_full_auto_orient"),
        (1, 4, "port_spritelayout_warehouse_half_auto_orient"),
        (1, 5, "port_spritelayout_water_ship_auto_orient"),
        (1, 6, "spritelayout_null_water"),
        (1, 7, "spritelayout_null_water"),
        # ensure spacing from coast, to improve map-gen buildabilty
        (2, 2, "port_spritelayout_shed_auto_orient"),
        (2, 3, "port_spritelayout_shed_auto_orient"),
        (2, 4, "port_spritelayout_warehouse_half_auto_orient"),
        (2, 5, "port_spritelayout_tanks_small_auto_orient"),
        (2, 6, "port_spritelayout_tanks_sphere_auto_orient"),
        (2, 7, "spritelayout_null_water"),
        (3, 3, "spritelayout_null_water"),
        (3, 4, "spritelayout_null_water"),
        (3, 5, "spritelayout_null_water"),
        (3, 6, "spritelayout_null_water"),
        (3, 7, "spritelayout_null_water"),
    ],
)
industry.add_industry_jetty_layout(
    id="port_industry_jetty_layout_2",
    layout=[
        (0, 4, "spritelayout_null_water"),
        (0, 5, "spritelayout_null_water"),
        (0, 6, "spritelayout_null_water"),
        (0, 7, "spritelayout_null_water"),
        # ensure spacing from coast, to improve map-gen buildabilty
        (1, 2, "port_spritelayout_silos_1_auto_orient"),
        (1, 3, "port_spritelayout_silos_1_auto_orient"),
        (1, 4, "port_spritelayout_warehouse_half_auto_orient"),
        (1, 5, "port_spritelayout_shed_auto_orient"),
        (1, 6, "port_spritelayout_shed_auto_orient"),
        (1, 7, "spritelayout_null_water"),
        (2, 0, "port_spritelayout_coast_shed"),
        (2, 1, "port_spritelayout_warehouse_full_auto_orient"),
        (2, 2, "port_spritelayout_warehouse_half_auto_orient"),
        (2, 3, "port_spritelayout_warehouse_full_auto_orient"),
        (2, 4, "port_spritelayout_warehouse_half_auto_orient"),
        (2, 5, "port_spritelayout_water_ship_auto_orient"),
        (2, 6, "spritelayout_null_water"),
        (2, 7, "spritelayout_null_water"),
        # ensure spacing from coast, to improve map-gen buildabilty
        (3, 2, "port_spritelayout_tanks_small_auto_orient"),
        (3, 3, "port_spritelayout_tanks_sphere_auto_orient"),
        (3, 4, "port_spritelayout_warehouse_half_auto_orient"),
        (3, 5, "port_spritelayout_warehouse_full_auto_orient"),
        (3, 6, "port_spritelayout_warehouse_half_auto_orient"),
        (3, 7, "spritelayout_null_water"),
    ],
)
