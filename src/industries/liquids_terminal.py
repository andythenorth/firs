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
    # we'll draw our own foundations as needed - this also conveniently adjusts the y offsets on the tile to where we want them
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    # supporting autoslope for the water tiles produces too many edge cases which are difficult to handle, so ban it
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="liquids_terminal_tile_2",
    # we'll draw our own foundations as needed - this also conveniently adjusts the y offsets on the tile to where we want them
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    # supporting autoslope for water tiles produces too many edge cases which are difficult to handle, so ban it
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)
industry.add_tile(
    id="liquids_terminal_tile_3",
    # this is a totally flat tile for ships or other pure water features, so do not allow on coast slopes
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    # we'll draw our own foundations as needed - this also conveniently adjusts the y offsets on the tile to where we want them
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    # supporting autoslope for water tiles produces too many edge cases which are difficult to handle, so ban it
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(always_allow_founder=False),
)

sprite_ground = industry.add_sprite(sprite_number="GROUNDSPRITE_WATER")
spriteset_ground_empty = industry.add_spriteset(type="empty")
spriteset_small_tanks = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_office = industry.add_spriteset(
    sprites=[(440, 10, 64, 84, -31, -43)], zoffset=18
)
spriteset_sphere_tank = industry.add_spriteset(
    sprites=[(510, 10, 64, 84, -31, -60)],
)
spriteset_large_cylinder_tank = industry.add_spriteset(
    sprites=[(510, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_barge_1_ne_sw = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -22, 0)],
)
spriteset_barge_1_nw_se = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -23, -13)],
)
spriteset_barge_1_sw_ne = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -38, -13)],
)
spriteset_barge_1_se_nw = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -47, -1)],
)
spriteset_barge_2_ne_sw = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -22, 0)],
)
spriteset_barge_2_nw_se = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -23, -13)],
)
spriteset_barge_2_sw_ne = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -38, -13)],
)
spriteset_barge_2_se_nw = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -47, -1)],
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="liquids_terminal_spritelayout_coast_office",
    tile="liquids_terminal_tile_2",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_office,
            ],
            "sw": [
                spriteset_office,
            ],
            "nw": [
                spriteset_office,
            ],
            "ne": [
                spriteset_office,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="liquids_terminal_spritelayout_sphere_tank",
    tile="liquids_terminal_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_sphere_tank,
            ],
            "sw": [
                spriteset_sphere_tank,
            ],
            "nw": [
                spriteset_sphere_tank,
            ],
            "ne": [
                spriteset_sphere_tank,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="liquids_terminal_spritelayout_small_tanks",
    tile="liquids_terminal_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_small_tanks,
            ],
            "sw": [
                spriteset_small_tanks,
            ],
            "nw": [
                spriteset_small_tanks,
            ],
            "ne": [
                spriteset_small_tanks,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="liquids_terminal_spritelayout_large_tank",
    tile="liquids_terminal_tile_1",
    config={
        "jetty_foundations": True,
        "building_sprites": {
            "se": [
                spriteset_large_cylinder_tank,
            ],
            "sw": [
                spriteset_large_cylinder_tank,
            ],
            "nw": [
                spriteset_large_cylinder_tank,
            ],
            "ne": [
                spriteset_large_cylinder_tank,
            ],
        },
    },
)

industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="liquids_terminal_spritelayout_water_barge_1",
    tile="liquids_terminal_tile_3",
    config={
        "jetty_foundations": False,
        "building_sprites": {
            "se": [
                spriteset_barge_1_nw_se,
            ],
            "sw": [
                spriteset_barge_1_ne_sw,
            ],
            "nw": [
                spriteset_barge_1_se_nw,
            ],
            "ne": [
                spriteset_barge_1_sw_ne,
            ],
        },
    },
)
industry.add_magic_spritelayout(
    type="jetty_auto_orient_to_coast_direction",
    base_id="liquids_terminal_spritelayout_water_barge_2",
    tile="liquids_terminal_tile_3",
    config={
        "jetty_foundations": False,
        "building_sprites": {
            "se": [
                spriteset_barge_2_nw_se,
            ],
            "sw": [
                spriteset_barge_2_ne_sw,
            ],
            "nw": [
                spriteset_barge_2_se_nw,
            ],
            "ne": [
                spriteset_barge_2_sw_ne,
            ],
        },
    },
)

# 2 jetty layouts which will be combined for different coast angles
# by convention, the jetty layout definitions are aligned to the SE coast
industry.add_industry_jetty_layout(
    id="liquids_terminal_industry_layout_1",
    layout=[
        (0, 0, "liquids_terminal_spritelayout_coast_office"),
        (0, 1, "liquids_terminal_spritelayout_large_tank"),
        (0, 2, "liquids_terminal_spritelayout_large_tank"),
        (0, 3, "liquids_terminal_spritelayout_small_tanks"),
        (0, 4, "spritelayout_null_water"),
        (1, 0, "liquids_terminal_spritelayout_sphere_tank"),
        (1, 1, "liquids_terminal_spritelayout_sphere_tank"),
        (1, 2, "liquids_terminal_spritelayout_water_barge_2"),
        (1, 3, "spritelayout_null_water"),
        (1, 4, "spritelayout_null_water"),
        (2, 0, "liquids_terminal_spritelayout_large_tank"),
        (2, 1, "liquids_terminal_spritelayout_large_tank"),
        (2, 2, "liquids_terminal_spritelayout_small_tanks"),
        (2, 3, "liquids_terminal_spritelayout_small_tanks"),
        (2, 4, "spritelayout_null_water"),
        # additional spacing at end of jetty (for better clearance in map edge context), only one tile needed for this
        (2, 5, "spritelayout_null_water"),
        (3, 0, "liquids_terminal_spritelayout_large_tank"),
        (3, 1, "liquids_terminal_spritelayout_large_tank"),
        (3, 2, "liquids_terminal_spritelayout_water_barge_1"),
        (3, 3, "spritelayout_null_water"),
    ],
)

industry.add_industry_jetty_layout(
    id="liquids_terminal_industry_layout_2",
    layout=[
        (0, 0, "liquids_terminal_spritelayout_large_tank"),
        (0, 1, "liquids_terminal_spritelayout_large_tank"),
        (1, 0, "liquids_terminal_spritelayout_large_tank"),
        (1, 1, "liquids_terminal_spritelayout_large_tank"),
        (1, 2, "liquids_terminal_spritelayout_small_tanks"),
        (1, 3, "liquids_terminal_spritelayout_small_tanks"),
        (1, 4, "spritelayout_null_water"),
        # additional spacing at end of jetty (for better clearance in map edge context), only one tile needed for this
        (1, 5, "spritelayout_null_water"),
        (2, 0, "liquids_terminal_spritelayout_coast_office"),
        (2, 1, "liquids_terminal_spritelayout_sphere_tank"),
        (2, 2, "liquids_terminal_spritelayout_water_barge_1"),
        (2, 3, "spritelayout_null_water"),
        (2, 4, "spritelayout_null_water"),
    ],
)
