from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="plate_mill",
    accept_cargos_with_input_ratios=[
        # this is a Quarto type plate mill
        # water-jet descaling, no pickling, https://spartan.metinvestholding.com/en/activities/manufacturing
        # uses gas for plate cutting / heat treatment, might be weird, but eh we'll see
        ("STSL", 6),
        ("WELD", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        # high plate mill output production is unwanted
        ("STSE", 6),
    ],
    # do not build during gameplay
    prob_in_game="0",
    prob_map_gen="5",
    map_colour="64",
    name="string(STR_IND_PLATE_MILL)",
    nearby_station_name="string(STR_STATION_MILL)",
    fund_cost_multiplier="200",
    pollution_and_squalor_factor=2,
    sprites_complete=False,
)

industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="plate_mill_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="gravel",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 64, -31, -31)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -26)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -31)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 128, -31, -95)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 128, -31, -95)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 128, -31, -95)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 56, -31, -26)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 56, -31, -26)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 64, -31, -31)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(640, 10, 64, 64, -31, -31)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(710, 10, 64, 110, -31, -61)],
)
sprite_transformer = industry.add_sprite(
    sprite_number=2054,
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=1,
    yoffset=0,
    zoffset=72,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=-12,
    yoffset=0,
    zoffset=56,
    animation_frame_offset=1,
)
sprite_smoke_3 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=0,
    zoffset=56,
    animation_frame_offset=2,
)

industry.add_spritelayout(
    id="plate_mill_spritelayout_tanks",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_thickening_tank",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_big_shed",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_flue_stack",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    smoke_sprites=[sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_ore_handling_front",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    smoke_sprites=[sprite_smoke_2, sprite_smoke_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_ore_handling_rear",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_copper_forklift",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_small_shed",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_stack_vent_thing",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_ground",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_transformer",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_transformer],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="plate_mill_industry_layout_1",
    layout=[
        (0, 0, "plate_mill_spritelayout_transformer"),
        (0, 1, "plate_mill_spritelayout_big_shed"),
        (0, 2, "plate_mill_spritelayout_big_shed"),
        (0, 3, "plate_mill_spritelayout_small_shed"),
        (
            1,
            0,
            "plate_mill_spritelayout_ore_handling_rear",
        ),
        (1, 1, "plate_mill_spritelayout_tanks"),
        (
            1,
            2,
            "plate_mill_spritelayout_stack_vent_thing",
        ),
        (
            1,
            3,
            "plate_mill_spritelayout_copper_forklift",
        ),
        (
            2,
            0,
            "plate_mill_spritelayout_ore_handling_front",
        ),
        (2, 1, "plate_mill_spritelayout_tanks"),
        (
            2,
            2,
            "plate_mill_spritelayout_stack_vent_thing",
        ),
        (2, 3, "plate_mill_spritelayout_ground"),
        (3, 0, "plate_mill_spritelayout_flue_stack"),
        (
            3,
            1,
            "plate_mill_spritelayout_thickening_tank",
        ),
        (
            3,
            2,
            "plate_mill_spritelayout_thickening_tank",
        ),
        (3, 3, "plate_mill_spritelayout_ground"),
    ],
)

industry.add_industry_layout(
    id="plate_mill_industry_layout_2",
    layout=[
        (
            0,
            0,
            "plate_mill_spritelayout_ore_handling_rear",
        ),
        (
            0,
            1,
            "plate_mill_spritelayout_stack_vent_thing",
        ),
        (0, 2, "plate_mill_spritelayout_tanks"),
        (0, 3, "plate_mill_spritelayout_flue_stack"),
        (0, 4, "plate_mill_spritelayout_tanks"),
        (0, 5, "plate_mill_spritelayout_small_shed"),
        (
            1,
            0,
            "plate_mill_spritelayout_ore_handling_front",
        ),
        (
            1,
            1,
            "plate_mill_spritelayout_stack_vent_thing",
        ),
        (1, 2, "plate_mill_spritelayout_big_shed"),
        (1, 3, "plate_mill_spritelayout_big_shed"),
        (1, 4, "plate_mill_spritelayout_big_shed"),
        (
            1,
            5,
            "plate_mill_spritelayout_copper_forklift",
        ),
        (2, 0, "plate_mill_spritelayout_transformer"),
        (2, 1, "plate_mill_spritelayout_small_shed"),
        (
            2,
            2,
            "plate_mill_spritelayout_thickening_tank",
        ),
        (
            2,
            3,
            "plate_mill_spritelayout_thickening_tank",
        ),
        (2, 4, "plate_mill_spritelayout_ground"),
        (2, 5, "plate_mill_spritelayout_ground"),
    ],
)

industry.add_industry_layout(
    id="plate_mill_industry_layout_3",
    layout=[
        (
            0,
            0,
            "plate_mill_spritelayout_thickening_tank",
        ),
        (0, 1, "plate_mill_spritelayout_tanks"),
        (0, 2, "plate_mill_spritelayout_flue_stack"),
        (0, 3, "plate_mill_spritelayout_tanks"),
        (
            0,
            4,
            "plate_mill_spritelayout_ore_handling_rear",
        ),
        (
            1,
            0,
            "plate_mill_spritelayout_thickening_tank",
        ),
        (1, 1, "plate_mill_spritelayout_big_shed"),
        (1, 2, "plate_mill_spritelayout_big_shed"),
        (1, 3, "plate_mill_spritelayout_big_shed"),
        (
            1,
            4,
            "plate_mill_spritelayout_ore_handling_front",
        ),
        (2, 0, "plate_mill_spritelayout_transformer"),
        (2, 1, "plate_mill_spritelayout_big_shed"),
        (2, 2, "plate_mill_spritelayout_big_shed"),
        (2, 3, "plate_mill_spritelayout_big_shed"),
        (
            2,
            4,
            "plate_mill_spritelayout_stack_vent_thing",
        ),
        (
            3,
            1,
            "plate_mill_spritelayout_copper_forklift",
        ),
        (3, 2, "plate_mill_spritelayout_small_shed"),
        (3, 3, "plate_mill_spritelayout_ground"),
        (
            3,
            4,
            "plate_mill_spritelayout_stack_vent_thing",
        ),
    ],
)
