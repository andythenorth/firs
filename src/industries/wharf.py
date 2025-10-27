from industry import IndustryPrimaryPort, TileLocationChecks

industry = IndustryPrimaryPort(
    id="wharf",
    accept_cargo_types=[],
    prod_cargo_types_with_multipliers=[],
    prob_in_game="2",
    prob_map_gen="6",
    map_colour="37",
    colour_scheme_name="scheme_2_dylan",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(same_type_distance=32),
    prospect_chance="0.75",
    name="string(STR_IND_WHARF)",
    nearby_station_name="string(STR_STATION_INDUSTRY_HARBOUR_4)",
    fund_cost_multiplier="152",
    override_default_construction_states=True,
    primary_production_random_factor_set="medium_range",
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "BASIC_ARCTIC",
    accept_cargo_types=[
        "BOOM",
        "PEAT",
        "WDPR",
    ],
    prod_cargo_types_with_multipliers=[
        ("POTA", 19),
        ("ENSP", 9),
        ("FMSP", 9),
    ],
)

industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
    accept_cargo_types=[
        "MNO2",
        "PHOS",
        "BDMT",
    ],
    prod_cargo_types_with_multipliers=[
        ("RFPR", 12),
        ("FMSP", 12),
    ],
)

industry.enable_in_economy(
    "STEELTOWN",
    # quite a lot of accepted types, this is intentional to provide flexibility in obtaining boost
    # NO steel strip, no structural steel, not fitting
    accept_cargo_types=["FOOD", "POTA", "CHLO", "CMNT", "PLNT", "STIG", "STPL"],
    prod_cargo_types_with_multipliers=[
        ("RUBR", 16),
        ("FEAL", 20),
        ("ALUM", 14),
        ("ZINC", 16),
    ],
    vulcan_config={
        "map_curator": {
            "curation_function": "MinimumRatioToCompanionIndustryTypes",
            "companion_industries": ["basic_oxygen_furnace", "electric_arc_furnace"],
            "companion_industries_ratio": 1,
        }
    },
)

industry.add_tile(
    id="wharf_tile_1",
    # we'll draw our own foundations as needed - this also conveniently adjusts the y offsets on the tile to where we want them
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    # supporting autoslope for the water tiles produces too many edge cases which are difficult to handle, so ban it
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="wharf_tile_2",
    # we'll draw our own foundations as needed - this also conveniently adjusts the y offsets on the tile to where we want them
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    # supporting autoslope for water tiles produces too many edge cases which are difficult to handle, so ban it
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)
industry.add_tile(
    id="wharf_tile_3",
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
spriteset_warehouse_full_nw_se = industry.add_spriteset(
    sprites=[(580, 10, 64, 84, -31, -61)],
)
spriteset_warehouse_full_ne_sw = industry.add_spriteset(
    sprites=[(650, 10, 64, 84, -31, -61)],
)
spriteset_shed_nw_se = industry.add_spriteset(
    sprites=[(440, 310, 64, 84, -31, -61)],
)
spriteset_shed_ne_sw = industry.add_spriteset(
    sprites=[(510, 310, 64, 84, -31, -61)],
)
spriteset_tanks_medium = industry.add_spriteset(
    sprites=[(720, 210, 64, 84, -31, -61)],
)
spriteset_tanks_sphere = industry.add_spriteset(
    sprites=[(790, 210, 64, 84, -31, -61)],
)
spriteset_gatehouse = industry.add_spriteset(
    sprites=[(580, 310, 64, 84, -31, -61)],
)
spriteset_silo_1_nw_se = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -61)],
)
spriteset_silo_1_ne_sw = industry.add_spriteset(
    sprites=[(580, 110, 64, 84, -31, -61)],
)
spriteset_silo_1_se_nw = industry.add_spriteset(
    sprites=[(510, 110, 64, 84, -31, -61)],
)
spriteset_silo_1_sw_ne = industry.add_spriteset(
    sprites=[(650, 110, 64, 84, -31, -61)],
)
spriteset_silo_2_nw_se = industry.add_spriteset(
    sprites=[(510, 110, 64, 84, -31, -61)],
)
spriteset_silo_2_ne_sw = industry.add_spriteset(
    sprites=[(650, 110, 64, 84, -31, -61)],
)
spriteset_silo_2_se_nw = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -61)],
)
spriteset_silo_2_sw_ne = industry.add_spriteset(
    sprites=[(580, 110, 64, 84, -31, -61)],
)
spriteset_large_crane_ne_sw = industry.add_spriteset(
    sprites=[(440, 210, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_nw_se = industry.add_spriteset(
    sprites=[(510, 210, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_se_nw = industry.add_spriteset(
    sprites=[(580, 210, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_sw_ne = industry.add_spriteset(
    sprites=[(650, 210, 64, 84, -31, -43)],
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
    base_id="wharf_spritelayout_coast_building",
    tile="wharf_tile_2",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_gatehouse,
            ],
            "sw": [
                spriteset_gatehouse,
            ],
            "nw": [
                spriteset_gatehouse,
            ],
            "ne": [
                spriteset_gatehouse,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="wharf_spritelayout_crane_rails_parallel",
    tile="wharf_tile_1",
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
    base_id="wharf_spritelayout_crane_rails_orthogonal",
    tile="wharf_tile_1",
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
    base_id="wharf_spritelayout_crane_parallel",
    tile="wharf_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_crane_rails_nw_se,
                spriteset_large_crane_se_nw,
            ],
            "sw": [
                spriteset_crane_rails_ne_sw,
                spriteset_large_crane_ne_sw,
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
    base_id="wharf_spritelayout_crane_orthogonal",
    tile="wharf_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_crane_rails_ne_sw,
                spriteset_large_crane_ne_sw,
            ],
            "sw": [
                spriteset_crane_rails_nw_se,
                spriteset_large_crane_nw_se,
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
    base_id="wharf_spritelayout_tanks_1",
    tile="wharf_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_tanks_medium,
            ],
            "sw": [
                spriteset_tanks_medium,
            ],
            "nw": [
                spriteset_tanks_medium,
            ],
            "ne": [
                spriteset_tanks_medium,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="wharf_spritelayout_tanks_2",
    tile="wharf_tile_1",
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
    base_id="wharf_spritelayout_silo_1",
    tile="wharf_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_silo_1_nw_se,
            ],
            "sw": [
                spriteset_silo_1_ne_sw,
            ],
            "nw": [
                spriteset_silo_1_se_nw,
            ],
            "ne": [
                spriteset_silo_1_sw_ne,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="wharf_spritelayout_silo_2",
    tile="wharf_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_silo_2_nw_se,
            ],
            "sw": [
                spriteset_silo_2_ne_sw,
            ],
            "nw": [
                spriteset_silo_2_se_nw,
            ],
            "ne": [
                spriteset_silo_2_sw_ne,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="wharf_spritelayout_warehouse_1",
    tile="wharf_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_warehouse_half_ne_sw,
            ],
            "sw": [
                spriteset_warehouse_full_nw_se,
            ],
            "nw": [
                spriteset_warehouse_full_ne_sw,
            ],
            "ne": [
                spriteset_warehouse_half_nw_se,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="wharf_spritelayout_warehouse_2",
    tile="wharf_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_warehouse_full_ne_sw,
            ],
            "sw": [
                spriteset_warehouse_half_nw_se,
            ],
            "nw": [
                spriteset_warehouse_half_ne_sw,
            ],
            "ne": [
                spriteset_warehouse_full_nw_se,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="wharf_spritelayout_shed_1",
    tile="wharf_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_shed_nw_se,
            ],
            "sw": [
                spriteset_shed_ne_sw,
            ],
            "nw": [
                spriteset_shed_nw_se,
            ],
            "ne": [
                spriteset_shed_ne_sw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="wharf_spritelayout_water_ship_1",
    tile="wharf_tile_3",
    config={
        "jetty_foundations": False,
        "building_sprites": {
            "se": [
                spriteset_ship_1_ne_sw,
            ],
            "sw": [
                spriteset_ship_1_nw_se,
            ],
            "nw": [
                spriteset_ship_1_sw_ne,
            ],
            "ne": [
                spriteset_ship_1_se_nw,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="wharf_spritelayout_water_ship_2",
    tile="wharf_tile_3",
    config={
        "jetty_foundations": False,
        "building_sprites": {
            "se": [
                spriteset_ship_2_ne_sw,
            ],
            "sw": [
                spriteset_ship_2_nw_se,
            ],
            "nw": [
                spriteset_ship_2_sw_ne,
            ],
            "ne": [
                spriteset_ship_2_se_nw,
            ],
        },
    },
)

# 2 jetty layouts which will be combined for different coast angles
# by convention, the jetty layout definitions are aligned to the SE coast
industry.add_industry_jetty_layout(
    id="wharf_industry_jetty_layout_1",
    layout=[
        (0, 0, "wharf_spritelayout_coast_building"),
        (0, 1, "wharf_spritelayout_shed_1"),
        (0, 2, "wharf_spritelayout_silo_1"),
        (0, 3, "wharf_spritelayout_silo_2"),
        (0, 4, "wharf_spritelayout_warehouse_2"),
        (0, 5, "spritelayout_null_water"),
        # additional spacing at end of jetty (for better clearance in map edge context), only one tile needed for this
        (0, 6, "spritelayout_null_water"),
        (1, 1, "wharf_spritelayout_tanks_1"),
        (1, 2, "wharf_spritelayout_tanks_2"),
        (1, 3, "wharf_spritelayout_shed_1"),
        (1, 4, "wharf_spritelayout_warehouse_1"),
        (1, 5, "spritelayout_null_water"),
        (2, 2, "wharf_spritelayout_warehouse_2"),
        (2, 3, "wharf_spritelayout_crane_orthogonal"),
        (2, 4, "wharf_spritelayout_water_ship_1"),
        (3, 2, "wharf_spritelayout_warehouse_1"),
        (3, 3, "wharf_spritelayout_crane_rails_orthogonal"),
        (3, 4, "spritelayout_null_water"),
        (3, 5, "spritelayout_null_water"),
    ],
)
industry.add_industry_jetty_layout(
    id="wharf_industry_jetty_layout_2",
    layout=[
        (0, 2, "wharf_spritelayout_warehouse_2"),
        (0, 3, "wharf_spritelayout_crane_rails_orthogonal"),
        (0, 4, "spritelayout_null_water"),
        (0, 5, "spritelayout_null_water"),
        (0, 6, "spritelayout_null_water"),
        (1, 2, "wharf_spritelayout_warehouse_1"),
        (1, 3, "wharf_spritelayout_crane_orthogonal"),
        (1, 4, "wharf_spritelayout_water_ship_2"),
        (1, 5, "wharf_spritelayout_tanks_1"),
        (1, 6, "spritelayout_null_water"),
        (2, 0, "wharf_spritelayout_coast_building"),
        (2, 1, "wharf_spritelayout_shed_1"),
        (2, 2, "wharf_spritelayout_silo_1"),
        (2, 3, "wharf_spritelayout_silo_2"),
        (2, 4, "wharf_spritelayout_shed_1"),
        (2, 5, "wharf_spritelayout_tanks_2"),
        (2, 6, "spritelayout_null_water"),
        # additional spacing at end of jetty (for better clearance in map edge context), only one tile needed for this
        (2, 7, "spritelayout_null_water"),
    ],
)
