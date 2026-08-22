from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="frozen_food_plant",
    accept_cargos_with_input_ratios=[
        ("VEG_", 3),
        ("MEAT", 3),
        ("FISH", 3),
        ("ENUM", 3),
        ("PACK", 3),
    ],
    prod_cargo_types_with_output_ratios=[
        ("FRZN", 8),
    ],
    # do not build during gameplay
    prob_in_game="0",
    prob_map_gen="5",
    map_colour="177",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    name="string(STR_IND_FROZEN_FOOD_PLANT)",
    nearby_station_name="string(STR_STATION_FREEZERS)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
    sprites_complete=False,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "MILD_MILD_WEST",
)

industry.add_tile(
    id="frozen_food_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 70, -31, -39)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 70, -31, -39)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 70, -31, -39)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 51, -31, -20)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 60, 64, 51, -31, -20)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 60, 64, 31, -31, 0)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 60, 64, 31, -31, 0)],
)

industry.add_spritelayout(
    id="frozen_food_plant_spritelayout_1",
    tile="frozen_food_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="frozen_food_plant_spritelayout_2",
    tile="frozen_food_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="frozen_food_plant_spritelayout_3",
    tile="frozen_food_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="frozen_food_plant_spritelayout_4",
    tile="frozen_food_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="frozen_food_plant_spritelayout_5",
    tile="frozen_food_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="frozen_food_plant_spritelayout_6",
    tile="frozen_food_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="frozen_food_plant_spritelayout_7",
    tile="frozen_food_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="frozen_food_plant_spritelayout_empty",
    tile="frozen_food_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)

industry.add_industry_layout(
    id="frozen_food_plant_industry_layout_1",
    layout=[
        (0, 0, "frozen_food_plant_spritelayout_3"),
        (0, 1, "frozen_food_plant_spritelayout_3"),
        (0, 2, "frozen_food_plant_spritelayout_5"),
        (0, 3, "frozen_food_plant_spritelayout_4"),
        (0, 4, "frozen_food_plant_spritelayout_5"),
        (1, 0, "frozen_food_plant_spritelayout_3"),
        (1, 1, "frozen_food_plant_spritelayout_3"),
        (1, 2, "frozen_food_plant_spritelayout_5"),
        (1, 3, "frozen_food_plant_spritelayout_4"),
        (1, 4, "frozen_food_plant_spritelayout_6"),
        (2, 0, "frozen_food_plant_spritelayout_3"),
        (2, 1, "frozen_food_plant_spritelayout_1"),
        (2, 2, "frozen_food_plant_spritelayout_2"),
        (2, 3, "frozen_food_plant_spritelayout_7"),
        (2, 4, "frozen_food_plant_spritelayout_7"),
    ],
)
industry.add_industry_layout(
    id="frozen_food_plant_industry_layout_2",
    layout=[
        (0, 2, "frozen_food_plant_spritelayout_3"),
        (0, 3, "frozen_food_plant_spritelayout_3"),
        (1, 0, "frozen_food_plant_spritelayout_1"),
        (1, 1, "frozen_food_plant_spritelayout_2"),
        (1, 2, "frozen_food_plant_spritelayout_3"),
        (1, 3, "frozen_food_plant_spritelayout_3"),
        (2, 0, "frozen_food_plant_spritelayout_4"),
        (2, 1, "frozen_food_plant_spritelayout_7"),
        (2, 2, "frozen_food_plant_spritelayout_6"),
        (2, 3, "frozen_food_plant_spritelayout_6"),
        (3, 0, "frozen_food_plant_spritelayout_4"),
        (3, 1, "frozen_food_plant_spritelayout_5"),
        (3, 2, "frozen_food_plant_spritelayout_4"),
        (3, 3, "frozen_food_plant_spritelayout_3"),
    ],
)
