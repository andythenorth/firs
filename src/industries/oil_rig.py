from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="oil_rig",
    prod_cargo_types_with_multipliers=[("OIL_", 29), ("PASS", 4)],
    prob_in_game="6",
    prob_map_gen="6",
    substitute="5",
    map_colour="151",
    special_flags=[
        "IND_FLAG_BUILT_ON_WATER",
        "IND_FLAG_AI_CREATES_AIR_AND_SHIP_ROUTES",
    ],
    location_checks=dict(location_check_industry_disallow_too_far_from_coast=True),
    prospect_chance="0.75",
    name="TTD_STR_INDUSTRY_NAME_OIL_RIG",
    nearby_station_name="string(STR_STATION_OIL_RIG)",
    fund_cost_multiplier="255",
    override="5",
    intro_year=1967,
    pollution_and_squalor_factor=1,
)

industry.economy_variations["IN_A_HOT_COUNTRY"].enabled = True

industry.economy_variations["STEELTOWN"].enabled = True

industry.add_tile(
    id="oil_rig_tile_1",
    location_checks=TileLocationChecks(
        disallow_industry_adjacent=True, disallow_slopes=True
    ),
)

sprite_ground = industry.add_sprite(
    sprite_number="GROUNDSPRITE_WATER",
)
spriteset_ground_empty = industry.add_spriteset(type="empty")
sprite_1 = industry.add_sprite(sprite_number="2096")
sprite_2 = industry.add_sprite(sprite_number="2097")
sprite_3 = industry.add_sprite(sprite_number="2098")
sprite_4 = industry.add_sprite(sprite_number="2099")

industry.add_spritelayout(
    id="oil_rig_spritelayout_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[sprite_1],
)
industry.add_spritelayout(
    id="oil_rig_spritelayout_2",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[sprite_2],
)
industry.add_spritelayout(
    id="oil_rig_spritelayout_3",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[sprite_3],
)
industry.add_spritelayout(
    id="oil_rig_spritelayout_4",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[sprite_4],
)

industry.add_industry_layout(
    id="oil_rig_layout_1",
    layout=[
        (0, 0, "255", "spritelayout_null"),
        (0, 1, "255", "spritelayout_null"),
        (0, 2, "255", "spritelayout_null"),
        (0, 3, "255", "spritelayout_null"),
        (0, 4, "255", "spritelayout_null"),
        (0, 5, "255", "spritelayout_null"),
        (0, 6, "255", "spritelayout_null"),
        (0, 7, "255", "spritelayout_null"),
        (0, 8, "255", "spritelayout_null"),
        (0, 9, "255", "spritelayout_null"),
        (0, 10, "255", "spritelayout_null"),
        (1, 0, "255", "spritelayout_null"),
        (1, 10, "255", "spritelayout_null"),
        (2, 0, "255", "spritelayout_null"),
        (2, 10, "255", "spritelayout_null"),
        (3, 0, "255", "spritelayout_null"),
        (3, 10, "255", "spritelayout_null"),
        (4, 0, "255", "spritelayout_null"),
        (4, 3, "24", "spritelayout_null"),
        (4, 4, "24", "spritelayout_null"),
        (4, 5, "oil_rig_tile_1", "oil_rig_spritelayout_4"),
        (4, 10, "255", "spritelayout_null"),
        (5, 0, "255", "spritelayout_null"),
        (5, 5, "oil_rig_tile_1", "oil_rig_spritelayout_3"),
        (5, 4, "oil_rig_tile_1", "oil_rig_spritelayout_2"),
        (5, 3, "oil_rig_tile_1", "oil_rig_spritelayout_1"),
        (5, 10, "255", "spritelayout_null"),
        (6, 0, "255", "spritelayout_null"),
        (6, 10, "255", "spritelayout_null"),
        (7, 0, "255", "spritelayout_null"),
        (7, 10, "255", "spritelayout_null"),
        (8, 0, "255", "spritelayout_null"),
        (8, 10, "255", "spritelayout_null"),
        (9, 0, "255", "spritelayout_null"),
        (9, 10, "255", "spritelayout_null"),
    ],
)
