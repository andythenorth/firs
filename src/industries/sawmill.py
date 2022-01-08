from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="sawmill",
    accept_cargos_with_input_ratios=[
        ("WOOD", 6),
    ],
    prod_cargo_types_with_output_ratios=[
        ("WDPR", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="194",
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[["forest"], 72],
        same_type_distance=72,
    ),
    name="TTD_STR_INDUSTRY_NAME_SAWMILL",
    nearby_station_name="string(STR_STATION_MILL)",
    fund_cost_multiplier="97",
    pollution_and_squalor_factor=1,
)

industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
)
industry.enable_in_economy(
    "BASIC_ARCTIC",
)

industry.add_tile(
    id="sawmill_tile_1",
    location_checks=TileLocationChecks(disallow_industry_adjacent=True),
)

sprite_ground = industry.add_sprite(
    sprite_number="GROUNDTILE_MUD_TRACKS"  # ground tile same as overlay tile
)

spriteset_ground_overlay = industry.add_spriteset(type="empty")
sprite_hut_1 = industry.add_sprite(sprite_number="2069")
sprite_hut_2 = industry.add_sprite(sprite_number="2063")
sprite_logs_1 = industry.add_sprite(sprite_number="2066")
sprite_logs_2 = industry.add_sprite(sprite_number="2070")
sprite_logs_3 = industry.add_sprite(sprite_number="2071")

industry.add_spritelayout(
    id="sawmill_spritelayout_1",
    tile="sawmill_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_hut_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="sawmill_spritelayout_2",
    tile="sawmill_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_hut_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="sawmill_spritelayout_3",
    tile="sawmill_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_logs_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="sawmill_spritelayout_4",
    tile="sawmill_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_logs_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="sawmill_spritelayout_5",
    tile="sawmill_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_logs_3],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)

industry.add_industry_layout(
    id="sawmill_industry_layout_1",
    layout=[
        (0, 0, "sawmill_spritelayout_1"),
        (0, 1, "sawmill_spritelayout_2"),
        (0, 2, "sawmill_spritelayout_4"),
        (1, 0, "sawmill_spritelayout_1"),
        (1, 1, "sawmill_spritelayout_2"),
        (1, 2, "sawmill_spritelayout_3"),
        (2, 0, "sawmill_spritelayout_4"),
        (2, 1, "sawmill_spritelayout_5"),
    ],
)
