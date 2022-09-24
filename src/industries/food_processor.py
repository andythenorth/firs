from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="food_processor",
    accept_cargos_with_input_ratios=[],
    prod_cargo_types_with_output_ratios=[
        ("FOOD", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="181",
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[
            ["arable_farm", "fruit_plantation", "coffee_estate", "vineyard"],
            72,
        ]
    ),
    name="TTD_STR_INDUSTRY_NAME_FOOD_PROCESSING_PLANT",
    nearby_station_name="string(STR_STATION_FOOD_CORPORATION)",
    fund_cost_multiplier="65",
)

industry.enable_in_economy(
    "BASIC_TROPIC",
    accept_cargos_with_input_ratios=[
        ("BEAN", 6),
        ("FRUT", 6),
    ],
)

industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
    accept_cargos_with_input_ratios=[
        ("NUTS", 6),
        ("FRUT", 6),
    ],
    prod_cargo_types_with_output_ratios=[
        ("EOIL", 4),
        ("FOOD", 4),
    ],
)

industry.add_tile(
    id="food_processor_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="dirty_concrete")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 87, -31, -56)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 87, -31, -56)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 87, -31, -56)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 87, -31, -56)],
)

industry.add_spritelayout(
    id="food_processor_spritelayout_1",
    tile="food_processor_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="food_processor_spritelayout_2",
    tile="food_processor_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="food_processor_spritelayout_3",
    tile="food_processor_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="food_processor_spritelayout_4",
    tile="food_processor_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)

industry.add_industry_layout(
    id="food_processor_industry_layout_1",
    layout=[
        (0, 0, "food_processor_spritelayout_1"),
        (0, 1, "food_processor_spritelayout_1"),
        (0, 2, "food_processor_spritelayout_3"),
        (1, 0, "food_processor_spritelayout_1"),
        (1, 1, "food_processor_spritelayout_1"),
        (1, 2, "food_processor_spritelayout_3"),
        (2, 0, "food_processor_spritelayout_2"),
        (2, 1, "food_processor_spritelayout_2"),
        (2, 2, "food_processor_spritelayout_4"),
        (3, 0, "food_processor_spritelayout_4"),
        (3, 1, "food_processor_spritelayout_4"),
        (3, 2, "food_processor_spritelayout_4"),
    ],
)
industry.add_industry_layout(
    id="food_processor_industry_layout_2",
    layout=[
        (0, 0, "food_processor_spritelayout_2"),
        (0, 1, "food_processor_spritelayout_3"),
        (0, 2, "food_processor_spritelayout_1"),
        (0, 3, "food_processor_spritelayout_3"),
        (1, 0, "food_processor_spritelayout_1"),
        (1, 1, "food_processor_spritelayout_4"),
        (1, 2, "food_processor_spritelayout_1"),
        (1, 3, "food_processor_spritelayout_3"),
        (2, 0, "food_processor_spritelayout_2"),
        (2, 1, "food_processor_spritelayout_4"),
        (2, 2, "food_processor_spritelayout_1"),
        (3, 0, "food_processor_spritelayout_2"),
        (3, 1, "food_processor_spritelayout_4"),
        (3, 2, "food_processor_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="food_processor_industry_layout_3",
    layout=[
        (0, 0, "food_processor_spritelayout_1"),
        (0, 1, "food_processor_spritelayout_1"),
        (0, 2, "food_processor_spritelayout_2"),
        (0, 3, "food_processor_spritelayout_3"),
        (1, 0, "food_processor_spritelayout_1"),
        (1, 1, "food_processor_spritelayout_1"),
        (1, 2, "food_processor_spritelayout_2"),
        (1, 3, "food_processor_spritelayout_3"),
        (2, 0, "food_processor_spritelayout_1"),
        (2, 1, "food_processor_spritelayout_1"),
        (2, 2, "food_processor_spritelayout_4"),
        (2, 3, "food_processor_spritelayout_4"),
    ],
)
