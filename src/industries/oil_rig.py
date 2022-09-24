from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="oil_rig",
    prod_cargo_types_with_multipliers=[
        ("OIL_", 29),
        ("PASS", 4),
    ],
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

industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
)

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
    tile="oil_rig_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[sprite_1],
)
industry.add_spritelayout(
    id="oil_rig_spritelayout_2",
    tile="oil_rig_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[sprite_2],
)
industry.add_spritelayout(
    id="oil_rig_spritelayout_3",
    tile="oil_rig_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[sprite_3],
)
industry.add_spritelayout(
    id="oil_rig_spritelayout_4",
    tile="oil_rig_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[sprite_4],
)

industry.add_industry_layout(
    id="oil_rig_layout_1",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "spritelayout_null_water"),
        (0, 2, "spritelayout_null_water"),
        (0, 3, "spritelayout_null_water"),
        (0, 4, "spritelayout_null_water"),
        (0, 5, "spritelayout_null_water"),
        (0, 6, "spritelayout_null_water"),
        (0, 7, "spritelayout_null_water"),
        (0, 8, "spritelayout_null_water"),
        (0, 9, "spritelayout_null_water"),
        (0, 10, "spritelayout_null_water"),
        (1, 0, "spritelayout_null_water"),
        (1, 10, "spritelayout_null_water"),
        (2, 0, "spritelayout_null_water"),
        (2, 10, "spritelayout_null_water"),
        (3, 0, "spritelayout_null_water"),
        (3, 10, "spritelayout_null_water"),
        (4, 0, "spritelayout_null_water"),
        (4, 3, "spritelayout_null_station"),
        (4, 4, "spritelayout_null_station"),
        (4, 5, "oil_rig_spritelayout_4"),
        (4, 10, "spritelayout_null_water"),
        (5, 0, "spritelayout_null_water"),
        (5, 5, "oil_rig_spritelayout_3"),
        (5, 4, "oil_rig_spritelayout_2"),
        (5, 3, "oil_rig_spritelayout_1"),
        (5, 10, "spritelayout_null_water"),
        (6, 0, "spritelayout_null_water"),
        (6, 10, "spritelayout_null_water"),
        (7, 0, "spritelayout_null_water"),
        (7, 10, "spritelayout_null_water"),
        (8, 0, "spritelayout_null_water"),
        (8, 10, "spritelayout_null_water"),
        (9, 0, "spritelayout_null_water"),
        (9, 10, "spritelayout_null_water"),
    ],
)
