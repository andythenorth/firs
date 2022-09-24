from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="power_plant",
    accept_cargo_types=[],
    prod_cargo_types=[],
    prob_in_game="3",
    prob_map_gen="5",
    prod_multiplier="[0, 0]",
    map_colour="168",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    town_industry_for_cargoflow=False,
    prospect_chance="0.75",
    name="string(STR_IND_POWER_PLANT)",
    nearby_station_name="string(STR_STATION_POWERHUNGRY)",
    fund_cost_multiplier="15",
)


industry.enable_in_economy(
    "BASIC_ARCTIC",
    accept_cargo_types=["PEAT"],
)

industry.add_tile(
    id="power_plant_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
sprite_ground = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")
sprite_ground_overlay = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")
sprite_1 = industry.add_sprite(sprite_number="2047")
sprite_2 = industry.add_sprite(sprite_number="2050")
sprite_3 = industry.add_sprite(sprite_number="2053")
sprite_4 = industry.add_sprite(sprite_number="2054")
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big", xoffset=3, yoffset=0, zoffset=36
)

industry.add_spritelayout(
    id="power_plant_spritelayout_cooling_tower",
    tile="power_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[sprite_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="power_plant_spritelayout_large_building",
    tile="power_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[sprite_2],
    smoke_sprites=[sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="power_plant_spritelayout_small_building",
    tile="power_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[sprite_3],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="power_plant_spritelayout_substation",
    tile="power_plant_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[sprite_4],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)

industry.add_industry_layout(
    id="power_plant_industry_layout_1",
    layout=[
        (0, 0, "power_plant_spritelayout_cooling_tower"),
        (0, 1, "power_plant_spritelayout_small_building"),
        (1, 0, "power_plant_spritelayout_cooling_tower"),
        (1, 1, "power_plant_spritelayout_large_building"),
        (2, 0, "power_plant_spritelayout_cooling_tower"),
        (2, 1, "power_plant_spritelayout_large_building"),
        (3, 0, "power_plant_spritelayout_substation"),
        (3, 1, "power_plant_spritelayout_substation"),
    ],
)
industry.add_industry_layout(
    id="power_plant_industry_layout_2",
    layout=[
        (0, 1, "power_plant_spritelayout_cooling_tower"),
        (0, 2, "power_plant_spritelayout_cooling_tower"),
        (1, 0, "power_plant_spritelayout_large_building"),
        (1, 1, "power_plant_spritelayout_large_building"),
        (1, 2, "power_plant_spritelayout_cooling_tower"),
        (2, 0, "power_plant_spritelayout_small_building"),
        (2, 1, "power_plant_spritelayout_substation"),
        (2, 2, "power_plant_spritelayout_small_building"),
    ],
)
industry.add_industry_layout(
    id="power_plant_industry_layout_3",
    layout=[
        (0, 0, "power_plant_spritelayout_cooling_tower"),
        (0, 1, "power_plant_spritelayout_cooling_tower"),
        (1, 0, "power_plant_spritelayout_small_building"),
        (1, 1, "power_plant_spritelayout_large_building"),
        (2, 0, "power_plant_spritelayout_substation"),
        (2, 1, "power_plant_spritelayout_small_building"),
    ],
)
