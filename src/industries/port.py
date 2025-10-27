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
    colour_scheme_name="scheme_9_shania",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(same_type_distance=32),
    prospect_chance="0.75",
    name="string(STR_IND_PORT)",
    nearby_station_name="string(STR_STATION_INDUSTRY_HARBOUR_2)",
    fund_cost_multiplier="152",
    override_default_construction_states=True,
    primary_production_random_factor_set="medium_range",
    sprites_complete=True,
    animated_tiles_fixed=True,
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
    accept_cargo_types=[
        "FOOD",
        "LYE_",
        "CMNT",
        "HWAR",
        "PPWK",
        "VEHI",
        "GOOD",
    ],
    prod_cargo_types_with_multipliers=[
        ("ENSP", 12),
        ("POWR", 14),
        ("COAT", 18),
        ("SOAP", 18),
    ],
    vulcan_config={
        "map_curator": {
            "curation_function": "MinimumRatioToCompanionIndustryTypes",
            "companion_industries": [
                "appliance_factory",
                "body_plant",
                "steel_forge_and_foundry",
                "precision_parts_plant",
                "tube_and_pipe_mill",
                "wire_rod_mill",
            ],
            "companion_industries_ratio": 0.33,
        }
    },
)
# industry.economy_variations['IN_A_HOT_COUNTRY'].accept_cargo_types = ['DIAM', 'EOIL', 'JAVA', 'WDPR']
# industry.economy_variations['IN_A_HOT_COUNTRY'].prod_cargo_types_with_multipliers = [('GOOD', 14), ('SASH', 12)]

industry.add_tile(
    id="port_tile_1",
    # we'll draw our own foundations as needed - this also conveniently adjusts the y offsets on the tile to where we want them
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    # supporting autoslope for the water tiles produces too many edge cases which are difficult to handle, so ban it
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="port_tile_2",
    # we'll draw our own foundations as needed - this also conveniently adjusts the y offsets on the tile to where we want them
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    # supporting autoslope for water tiles produces too many edge cases which are difficult to handle, so ban it
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)
industry.add_tile(
    id="port_tile_3",
    # this is a totally flat tile for ships or other pure water features, so do not allow on coast slopes
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    # we'll draw our own foundations as needed - this also conveniently adjusts the y offsets on the tile to where we want them
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    # supporting autoslope for water tiles produces too many edge cases which are difficult to handle, so ban it
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False),
)

spriteset_crane_rails_nw_se = industry.add_spriteset(
    sprites=[(80, 10, 64, 39, -31, -8)],
    always_draw=1,
)
spriteset_crane_rails_ne_sw = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, -8)],
    always_draw=1,
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
spriteset_warehouse_full_nw_se = industry.add_spriteset(
    sprites=[(720, 10, 64, 84, -31, -61)],
)
spriteset_warehouse_full_ne_sw = industry.add_spriteset(
    sprites=[(790, 10, 64, 84, -31, -61)],
)
spriteset_shed_half_nw_se = industry.add_spriteset(
    sprites=[(440, 210, 64, 84, -31, -61)],
)
spriteset_shed_half_ne_sw = industry.add_spriteset(
    sprites=[(510, 210, 64, 84, -31, -61)],
)
spriteset_shed_half_se_nw = industry.add_spriteset(
    sprites=[(580, 210, 64, 84, -31, -61)],
)
spriteset_shed_half_sw_ne = industry.add_spriteset(
    sprites=[(650, 210, 64, 84, -31, -61)],
)
spriteset_shed_full_nw_se = industry.add_spriteset(
    sprites=[(720, 210, 64, 84, -31, -61)],
)
spriteset_shed_full_ne_sw = industry.add_spriteset(
    sprites=[(790, 210, 64, 84, -31, -61)],
)
spriteset_tanks_sphere = industry.add_spriteset(
    sprites=[(510, 310, 64, 84, -31, -61)],
)
# silos use the same sprite, but adjusted offsets for each coast
spriteset_silos_nw_se = industry.add_spriteset(
    sprites=[(720, 110, 64, 84, -33, -60)],
)
spriteset_silos_ne_sw = industry.add_spriteset(
    sprites=[(720, 110, 64, 84, -31, -61)],
)
spriteset_silos_se_nw = industry.add_spriteset(
    sprites=[(720, 110, 64, 84, -33, -60)],
)
spriteset_silos_sw_ne = industry.add_spriteset(
    sprites=[(720, 110, 64, 84, -33, -60)],
)
spriteset_bulk_handling_nw_se = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -61)],
)
spriteset_bulk_handling_ne_sw = industry.add_spriteset(
    sprites=[(510, 110, 64, 84, -31, -61)],
)
spriteset_bulk_handling_se_nw = industry.add_spriteset(
    sprites=[(580, 110, 64, 84, -31, -61)],
)
spriteset_bulk_handling_sw_ne = industry.add_spriteset(
    sprites=[(650, 110, 64, 84, -31, -61)],
)
# only 2 angles for crawler crane, to keep things visually simple
spriteset_crawler_crane_ne_sw = industry.add_spriteset(
    sprites=[(580, 310, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_crawler_crane_nw_se = industry.add_spriteset(
    sprites=[(650, 310, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_ne_sw = industry.add_spriteset(
    sprites=[(440, 410, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_nw_se = industry.add_spriteset(
    sprites=[(510, 410, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_se_nw = industry.add_spriteset(
    sprites=[(580, 410, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_sw_ne = industry.add_spriteset(
    sprites=[(650, 410, 64, 84, -31, -43)],
    zoffset=18,
)
# there are 2 variations of the ship, (reversed, unreversed) with coast appropriate offsets for each
spriteset_ship_1_ne_sw = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -40, -18)],
)
spriteset_ship_1_nw_se = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -22, -18)],
)
spriteset_ship_1_sw_ne = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -30, -22)],
)
spriteset_ship_1_se_nw = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -27, -20)],
)
spriteset_ship_2_ne_sw = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -40, -18)],
)
spriteset_ship_2_nw_se = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -22, -18)],
)
spriteset_ship_2_sw_ne = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -30, -22)],
)
spriteset_ship_2_se_nw = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -27, -20)],
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_gate_shed_coast_part",
    tile="port_tile_2",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_shed_half_se_nw,
            ],
            "sw": [
                spriteset_shed_half_sw_ne,
            ],
            "nw": [
                spriteset_shed_half_nw_se,
            ],
            "ne": [
                spriteset_shed_half_ne_sw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_gate_shed_sea_part",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_shed_full_nw_se,
            ],
            "sw": [
                spriteset_shed_full_ne_sw,
            ],
            "nw": [
                spriteset_shed_full_nw_se,
            ],
            "ne": [
                spriteset_shed_full_ne_sw,
            ],
        },
    },
)

industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_crane_rails_parallel",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_crane_rails_nw_se,
            ],
            "sw": [
                spriteset_crane_rails_ne_sw,
            ],
            "nw": [
                spriteset_crane_rails_nw_se,
            ],
            "ne": [
                spriteset_crane_rails_ne_sw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_crane_rails_orthogonal",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_crane_rails_ne_sw,
            ],
            "sw": [
                spriteset_crane_rails_nw_se,
            ],
            "nw": [
                spriteset_crane_rails_ne_sw,
            ],
            "ne": [
                spriteset_crane_rails_nw_se,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_crane_parallel",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_crane_rails_nw_se,
                spriteset_large_crane_nw_se,
            ],
            "sw": [
                spriteset_crane_rails_ne_sw,
                spriteset_large_crane_sw_ne,
            ],
            "nw": [
                spriteset_crane_rails_nw_se,
                spriteset_large_crane_se_nw,
            ],
            "ne": [
                spriteset_crane_rails_ne_sw,
                spriteset_large_crane_ne_sw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_crane_orthogonal",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_crane_rails_ne_sw,
                spriteset_large_crane_sw_ne,
            ],
            "sw": [
                spriteset_crane_rails_nw_se,
                spriteset_large_crane_se_nw,
            ],
            "nw": [
                spriteset_crane_rails_ne_sw,
                spriteset_large_crane_sw_ne,
            ],
            "ne": [
                spriteset_crane_rails_nw_se,
                spriteset_large_crane_se_nw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_crawler_crane_orthogonal",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_crawler_crane_ne_sw,
            ],
            "sw": [
                spriteset_crawler_crane_nw_se,
            ],
            "nw": [
                spriteset_crawler_crane_ne_sw,
            ],
            "ne": [
                spriteset_crawler_crane_nw_se,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_tanks_sphere",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
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
    base_id="port_spritelayout_silos",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_silos_nw_se,
            ],
            "sw": [
                spriteset_silos_ne_sw,
            ],
            "nw": [
                spriteset_silos_se_nw,
            ],
            "ne": [
                spriteset_silos_sw_ne,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_bulk_handling",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_bulk_handling_nw_se,
            ],
            "sw": [
                spriteset_bulk_handling_ne_sw,
            ],
            "nw": [
                spriteset_bulk_handling_se_nw,
            ],
            "ne": [
                spriteset_bulk_handling_sw_ne,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_warehouse_half_1",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_warehouse_half_nw_se,
            ],
            "sw": [
                spriteset_warehouse_half_ne_sw,
            ],
            "nw": [
                spriteset_warehouse_half_se_nw,
            ],
            "ne": [
                spriteset_warehouse_half_sw_ne,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_warehouse_half_2",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_warehouse_half_se_nw,
            ],
            "sw": [
                spriteset_warehouse_half_sw_ne,
            ],
            "nw": [
                spriteset_warehouse_half_nw_se,
            ],
            "ne": [
                spriteset_warehouse_half_ne_sw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_warehouse_full",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_warehouse_full_nw_se,
            ],
            "sw": [
                spriteset_warehouse_full_ne_sw,
            ],
            "nw": [
                spriteset_warehouse_full_nw_se,
            ],
            "ne": [
                spriteset_warehouse_full_ne_sw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_shed_half_1",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_shed_half_nw_se,
            ],
            "sw": [
                spriteset_shed_half_ne_sw,
            ],
            "nw": [
                spriteset_shed_half_se_nw,
            ],
            "ne": [
                spriteset_shed_half_sw_ne,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_shed_half_2",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        # reversed variant of the half-shed for alternate end of the shed
        "building_sprites": {
            "se": [
                spriteset_shed_half_se_nw,
            ],
            "sw": [
                spriteset_shed_half_sw_ne,
            ],
            "nw": [
                spriteset_shed_half_nw_se,
            ],
            "ne": [
                spriteset_shed_half_ne_sw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_shed_full",
    tile="port_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_shed_full_nw_se,
            ],
            "sw": [
                spriteset_shed_full_ne_sw,
            ],
            "nw": [
                spriteset_shed_full_nw_se,
            ],
            "ne": [
                spriteset_shed_full_ne_sw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_water_ship_1",
    tile="port_tile_3",
    config={
        "jetty_foundations": False,
        "building_sprites": {
            "se": [
                spriteset_ship_1_nw_se,
            ],
            "sw": [
                spriteset_ship_1_ne_sw,
            ],
            "nw": [
                spriteset_ship_1_se_nw,
            ],
            "ne": [
                spriteset_ship_1_sw_ne,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="port_spritelayout_water_ship_2",
    tile="port_tile_3",
    config={
        "jetty_foundations": False,
        "building_sprites": {
            "se": [
                spriteset_ship_2_nw_se,
            ],
            "sw": [
                spriteset_ship_2_ne_sw,
            ],
            "nw": [
                spriteset_ship_2_se_nw,
            ],
            "ne": [
                spriteset_ship_2_sw_ne,
            ],
        },
    },
)

# 2 jetty layouts which will be combined for different coast angles
# by convention, the jetty layout definitions are aligned to the SE coast
industry.add_industry_jetty_layout(
    id="port_industry_jetty_layout_1",
    layout=[
        (0, 0, "port_spritelayout_gate_shed_coast_part"),
        (0, 1, "port_spritelayout_gate_shed_sea_part"),
        (0, 2, "port_spritelayout_warehouse_full"),
        (0, 3, "port_spritelayout_warehouse_full"),
        (0, 4, "port_spritelayout_warehouse_half_1"),
        (0, 5, "spritelayout_null_water"),
        # ensure spacing from coast, to improve map-gen buildabilty
        (1, 1, "port_spritelayout_tanks_sphere"),
        (1, 2, "port_spritelayout_tanks_sphere"),
        (1, 3, "port_spritelayout_crane_rails_parallel"),
        (1, 4, "port_spritelayout_crane_parallel"),
        # additional spacing at end of jetty (for better clearance in map edge context), only one tile needed for this
        (1, 5, "spritelayout_null_water"),
        # ensure spacing from coast, to improve map-gen buildabilty
        (2, 1, "port_spritelayout_shed_full"),
        (2, 2, "port_spritelayout_shed_half_1"),
        (2, 3, "port_spritelayout_water_ship_1"),
        (2, 4, "spritelayout_null_water"),
        (2, 5, "spritelayout_null_water"),
        (3, 1, "port_spritelayout_silos"),
        (3, 2, "port_spritelayout_silos"),
        (3, 3, "port_spritelayout_bulk_handling"),
        (3, 4, "spritelayout_null_water"),
    ],
)
industry.add_industry_jetty_layout(
    id="port_industry_jetty_layout_2",
    layout=[
        # ensure spacing from coast, to improve map-gen buildabilty
        (0, 1, "port_spritelayout_warehouse_full"),
        (0, 2, "port_spritelayout_warehouse_full"),
        (0, 3, "port_spritelayout_warehouse_half_1"),
        (0, 4, "spritelayout_null_water"),
        (1, 1, "port_spritelayout_silos"),
        (1, 2, "port_spritelayout_crane_rails_parallel"),
        (1, 3, "port_spritelayout_crane_parallel"),
        (2, 1, "port_spritelayout_silos"),
        (2, 2, "port_spritelayout_water_ship_2"),
        (2, 3, "spritelayout_null_water"),
        (2, 4, "spritelayout_null_water"),
        (3, 0, "port_spritelayout_gate_shed_coast_part"),
        (3, 1, "port_spritelayout_gate_shed_sea_part"),
        (3, 2, "port_spritelayout_bulk_handling"),
        (3, 3, "port_spritelayout_tanks_sphere"),
        (3, 4, "port_spritelayout_tanks_sphere"),
        (3, 5, "spritelayout_null_water"),
        # additional spacing at end of jetty (for better clearance in map edge context), only one tile needed for this
        (3, 7, "spritelayout_null_water"),
    ],
)
