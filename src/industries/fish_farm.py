from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(
    id="fish_farm",
    accept_cargo_types=[],
    prod_cargo_types_with_multipliers=[("FISH", 8)],
    prob_in_game="14",
    prob_map_gen="14",
    substitute="5",
    map_colour="160",
    life_type="IND_LIFE_TYPE_EXTRACTIVE",
    special_flags=[
        "IND_FLAG_BUILT_ON_WATER",
        "IND_FLAG_NO_PRODUCTION_INCREASE",
        "IND_FLAG_AI_CREATES_AIR_AND_SHIP_ROUTES",
    ],
    location_checks=dict(
        cluster=[60, 5], location_check_industry_disallow_too_far_from_coast=True
    ),
    prospect_chance="0.75",
    name="string(STR_IND_FISH_FARM)",
    nearby_station_name="string(STR_STATION_SEAFOOD)",  # appears to not work - maybe water industries don't accept station names?
    fund_cost_multiplier="88",
)

industry.economy_variations["BASIC_ARCTIC"].enabled = True

industry.add_tile(
    id="fish_farm_tile_1",
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="fish_farm_tile_2",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)

sprite_ground = industry.add_sprite(
    sprite_number="GROUNDSPRITE_WATER",
)
spriteset_ground_empty = industry.add_spriteset(type="empty")
spriteset_concrete = industry.add_spriteset(
    sprites=[(10, 10, 64, 39, -31, -8)],
    always_draw=1,
)
spriteset_warehouse = industry.add_spriteset(
    sprites=[(80, 10, 64, 39, -31, -16)],
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
spriteset_tank_1 = industry.add_spriteset(
    sprites=[(10, 110, 64, 31, -31, 0)],
)
spriteset_tank_2 = industry.add_spriteset(
    sprites=[(80, 110, 64, 31, -31, 0)],
)
spriteset_tank_3 = industry.add_spriteset(
    sprites=[(150, 110, 64, 31, -31, 0)],
)
spriteset_tank_4 = industry.add_spriteset(
    sprites=[(220, 110, 64, 31, -31, 0)],
)
spriteset_station_bouy = industry.add_spriteset(
    sprites=[(290, 110, 64, 31, -31, -32)],
)

industry.add_spritelayout(
    id="fish_farm_spritelayout_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_tank_1],
)
industry.add_spritelayout(
    id="fish_farm_spritelayout_2",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_tank_2],
)
industry.add_spritelayout(
    id="fish_farm_spritelayout_3",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_tank_3],
)
industry.add_spritelayout(
    id="fish_farm_spritelayout_4",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_station_bouy,
    building_sprites=[spriteset_tank_4],
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="fish_farm_spritelayout_coast_warehouse",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
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

industry.add_industry_layout(
    id="fish_farm_industry_layout_1",
    layout=[
        (0, 0, "fish_farm_tile_2", "fish_farm_spritelayout_coast_warehouse"),
        (0, 1, "255", "spritelayout_null"),
        (0, 2, "255", "spritelayout_null"),
        (0, 3, "255", "spritelayout_null"),
        (0, 4, "255", "spritelayout_null"),
        (0, 5, "255", "spritelayout_null"),
        (0, 6, "255", "spritelayout_null"),
        (1, 0, "255", "spritelayout_null"),
        (1, 1, "255", "spritelayout_null"),
        (1, 2, "255", "spritelayout_null"),
        (1, 3, "255", "spritelayout_null"),
        (1, 4, "255", "spritelayout_null"),
        (1, 5, "255", "spritelayout_null"),
        (1, 6, "255", "spritelayout_null"),
        (2, 0, "255", "spritelayout_null"),
        (2, 1, "255", "spritelayout_null"),
        (2, 2, "24", "spritelayout_null"),
        (2, 3, "24", "spritelayout_null"),
        (2, 4, "255", "spritelayout_null"),
        (2, 5, "255", "spritelayout_null"),
        (2, 6, "255", "spritelayout_null"),
        (3, 0, "255", "spritelayout_null"),
        (3, 1, "255", "spritelayout_null"),
        (3, 2, "fish_farm_tile_1", "fish_farm_spritelayout_1"),
        (3, 3, "fish_farm_tile_1", "fish_farm_spritelayout_4"),
        (3, 4, "fish_farm_tile_1", "fish_farm_spritelayout_2"),
        (3, 5, "255", "spritelayout_null"),
        (3, 6, "255", "spritelayout_null"),
        (4, 0, "255", "spritelayout_null"),
        (4, 1, "255", "spritelayout_null"),
        (4, 2, "255", "spritelayout_null"),
        (4, 3, "fish_farm_tile_1", "fish_farm_spritelayout_3"),
        (4, 4, "255", "spritelayout_null"),
        (4, 5, "255", "spritelayout_null"),
        (4, 6, "255", "spritelayout_null"),
        (5, 0, "255", "spritelayout_null"),
        (5, 1, "255", "spritelayout_null"),
        (5, 2, "255", "spritelayout_null"),
        (5, 3, "255", "spritelayout_null"),
        (5, 4, "255", "spritelayout_null"),
        (5, 5, "255", "spritelayout_null"),
        (5, 6, "255", "spritelayout_null"),
        (6, 0, "255", "spritelayout_null"),
        (6, 1, "255", "spritelayout_null"),
        (6, 2, "255", "spritelayout_null"),
        (6, 3, "255", "spritelayout_null"),
        (6, 4, "255", "spritelayout_null"),
        (6, 5, "255", "spritelayout_null"),
        (6, 6, "255", "spritelayout_null"),
    ],
)
industry.add_industry_layout(
    id="fish_farm_industry_layout_2",
    layout=[
        (0, 0, "fish_farm_tile_2", "fish_farm_spritelayout_coast_warehouse"),
        (0, 1, "255", "spritelayout_null"),
        (0, 2, "255", "spritelayout_null"),
        (0, 3, "255", "spritelayout_null"),
        (0, 4, "255", "spritelayout_null"),
        (0, 5, "255", "spritelayout_null"),
        (0, 6, "255", "spritelayout_null"),
        (1, 0, "255", "spritelayout_null"),
        (1, 1, "255", "spritelayout_null"),
        (1, 2, "255", "spritelayout_null"),
        (1, 3, "255", "spritelayout_null"),
        (1, 4, "255", "spritelayout_null"),
        (1, 5, "255", "spritelayout_null"),
        (1, 6, "255", "spritelayout_null"),
        (2, 0, "255", "spritelayout_null"),
        (2, 1, "255", "spritelayout_null"),
        (2, 2, "255", "spritelayout_null"),
        (2, 3, "24", "spritelayout_null"),
        (2, 4, "24", "spritelayout_null"),
        (2, 5, "255", "spritelayout_null"),
        (2, 6, "255", "spritelayout_null"),
        (3, 0, "255", "spritelayout_null"),
        (3, 1, "255", "spritelayout_null"),
        (3, 2, "fish_farm_tile_1", "fish_farm_spritelayout_1"),
        (3, 3, "fish_farm_tile_1", "fish_farm_spritelayout_2"),
        (3, 4, "fish_farm_tile_1", "fish_farm_spritelayout_4"),
        (3, 5, "255", "spritelayout_null"),
        (3, 6, "255", "spritelayout_null"),
        (4, 0, "255", "spritelayout_null"),
        (4, 1, "255", "spritelayout_null"),
        (4, 2, "255", "spritelayout_null"),
        (4, 3, "255", "spritelayout_null"),
        (4, 4, "fish_farm_tile_1", "fish_farm_spritelayout_3"),
        (4, 5, "255", "spritelayout_null"),
        (4, 6, "255", "spritelayout_null"),
        (5, 0, "255", "spritelayout_null"),
        (5, 1, "255", "spritelayout_null"),
        (5, 2, "255", "spritelayout_null"),
        (5, 3, "255", "spritelayout_null"),
        (5, 4, "fish_farm_tile_1", "fish_farm_spritelayout_3"),
        (5, 5, "255", "spritelayout_null"),
        (5, 6, "255", "spritelayout_null"),
        (6, 0, "255", "spritelayout_null"),
        (6, 1, "255", "spritelayout_null"),
        (6, 2, "255", "spritelayout_null"),
        (6, 3, "255", "spritelayout_null"),
        (6, 4, "255", "spritelayout_null"),
        (6, 5, "255", "spritelayout_null"),
        (6, 6, "255", "spritelayout_null"),
        (7, 0, "255", "spritelayout_null"),
        (7, 1, "255", "spritelayout_null"),
        (7, 2, "255", "spritelayout_null"),
        (7, 3, "255", "spritelayout_null"),
        (7, 4, "255", "spritelayout_null"),
        (7, 5, "255", "spritelayout_null"),
        (7, 6, "255", "spritelayout_null"),
    ],
)
industry.add_industry_layout(
    id="fish_farm_industry_layout_3",
    layout=[
        (0, 0, "fish_farm_tile_2", "fish_farm_spritelayout_coast_warehouse"),
        (0, 1, "255", "spritelayout_null"),
        (0, 2, "255", "spritelayout_null"),
        (0, 3, "255", "spritelayout_null"),
        (0, 4, "255", "spritelayout_null"),
        (0, 5, "255", "spritelayout_null"),
        (0, 6, "255", "spritelayout_null"),
        (1, 0, "255", "spritelayout_null"),
        (1, 1, "255", "spritelayout_null"),
        (1, 2, "255", "spritelayout_null"),
        (1, 3, "255", "spritelayout_null"),
        (1, 4, "255", "spritelayout_null"),
        (1, 5, "255", "spritelayout_null"),
        (1, 6, "255", "spritelayout_null"),
        (2, 0, "255", "spritelayout_null"),
        (2, 1, "255", "spritelayout_null"),
        (2, 2, "255", "spritelayout_null"),
        (2, 3, "fish_farm_tile_1", "fish_farm_spritelayout_3"),
        (2, 4, "255", "spritelayout_null"),
        (2, 5, "255", "spritelayout_null"),
        (2, 6, "255", "spritelayout_null"),
        (3, 0, "255", "spritelayout_null"),
        (3, 1, "255", "spritelayout_null"),
        (3, 2, "255", "spritelayout_null"),
        (3, 3, "255", "spritelayout_null"),
        (3, 4, "255", "spritelayout_null"),
        (3, 5, "255", "spritelayout_null"),
        (3, 6, "255", "spritelayout_null"),
        (4, 0, "255", "spritelayout_null"),
        (4, 1, "255", "spritelayout_null"),
        (4, 2, "24", "spritelayout_null"),
        (4, 3, "24", "spritelayout_null"),
        (4, 4, "255", "spritelayout_null"),
        (4, 5, "255", "spritelayout_null"),
        (4, 6, "255", "spritelayout_null"),
        (5, 0, "255", "spritelayout_null"),
        (5, 1, "255", "spritelayout_null"),
        (5, 2, "fish_farm_tile_1", "fish_farm_spritelayout_2"),
        (5, 3, "fish_farm_tile_1", "fish_farm_spritelayout_4"),
        (5, 4, "fish_farm_tile_1", "fish_farm_spritelayout_2"),
        (5, 5, "255", "spritelayout_null"),
        (5, 6, "255", "spritelayout_null"),
        (6, 0, "255", "spritelayout_null"),
        (6, 1, "255", "spritelayout_null"),
        (6, 2, "255", "spritelayout_null"),
        (6, 3, "255", "spritelayout_null"),
        (6, 4, "255", "spritelayout_null"),
        (6, 5, "255", "spritelayout_null"),
        (6, 6, "255", "spritelayout_null"),
        (7, 0, "255", "spritelayout_null"),
        (7, 1, "255", "spritelayout_null"),
        (7, 2, "255", "spritelayout_null"),
        (7, 3, "255", "spritelayout_null"),
        (7, 4, "255", "spritelayout_null"),
        (7, 5, "255", "spritelayout_null"),
        (7, 6, "255", "spritelayout_null"),
    ],
)
industry.add_industry_layout(
    id="fish_farm_industry_layout_4",
    layout=[
        (0, 0, "fish_farm_tile_2", "fish_farm_spritelayout_coast_warehouse"),
        (0, 1, "255", "spritelayout_null"),
        (0, 2, "255", "spritelayout_null"),
        (0, 3, "255", "spritelayout_null"),
        (0, 4, "255", "spritelayout_null"),
        (0, 5, "255", "spritelayout_null"),
        (0, 6, "255", "spritelayout_null"),
        (1, 0, "255", "spritelayout_null"),
        (1, 1, "255", "spritelayout_null"),
        (1, 2, "255", "spritelayout_null"),
        (1, 3, "255", "spritelayout_null"),
        (1, 4, "255", "spritelayout_null"),
        (1, 5, "255", "spritelayout_null"),
        (1, 6, "255", "spritelayout_null"),
        (2, 0, "255", "spritelayout_null"),
        (2, 1, "255", "spritelayout_null"),
        (2, 2, "24", "spritelayout_null"),
        (2, 3, "24", "spritelayout_null"),
        (2, 4, "255", "spritelayout_null"),
        (2, 5, "fish_farm_tile_1", "fish_farm_spritelayout_3"),
        (2, 6, "255", "spritelayout_null"),
        (3, 0, "255", "spritelayout_null"),
        (3, 1, "255", "spritelayout_null"),
        (3, 2, "fish_farm_tile_1", "fish_farm_spritelayout_2"),
        (3, 3, "fish_farm_tile_1", "fish_farm_spritelayout_4"),
        (3, 4, "fish_farm_tile_1", "fish_farm_spritelayout_3"),
        (3, 5, "fish_farm_tile_1", "fish_farm_spritelayout_1"),
        (3, 6, "255", "spritelayout_null"),
        (4, 0, "255", "spritelayout_null"),
        (4, 1, "255", "spritelayout_null"),
        (4, 2, "255", "spritelayout_null"),
        (4, 3, "255", "spritelayout_null"),
        (4, 4, "255", "spritelayout_null"),
        (4, 5, "255", "spritelayout_null"),
        (4, 6, "255", "spritelayout_null"),
        (5, 0, "255", "spritelayout_null"),
        (5, 1, "255", "spritelayout_null"),
        (5, 2, "255", "spritelayout_null"),
        (5, 3, "255", "spritelayout_null"),
        (5, 4, "255", "spritelayout_null"),
        (5, 5, "255", "spritelayout_null"),
        (5, 6, "255", "spritelayout_null"),
    ],
)
