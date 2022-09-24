from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="copper_concentrator",
    accept_cargos_with_input_ratios=[
        ("CORE", 4),
        ("SULP", 2),
        ("QLME", 2),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("COCO", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="64",
    name="string(STR_IND_COPPER_CONCENTRATOR)",
    nearby_station_name="string(STR_STATION_SMELTER)",
    fund_cost_multiplier="200",
)

# currently unused
# industry.economy_variations['BASIC_TROPIC'].enabled = True
# industry.economy_variations['BASIC_TROPIC'].accept_cargos_with_input_ratios = [('CORE', 5), ('RFPR', 3)]

# industry.economy_variations['IN_A_HOT_COUNTRY'].enabled = True

industry.add_tile(
    id="copper_concentrator_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

sprite_ground = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")
"""
spriteset_ground = industry.add_spriteset(
    type='mud',
)
"""
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
    id="copper_concentrator_spritelayout_tanks",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_concentrator_spritelayout_thickening_tank",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_concentrator_spritelayout_big_shed",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_concentrator_spritelayout_flue_stack",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    smoke_sprites=[sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_concentrator_spritelayout_ore_handling_front",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    smoke_sprites=[sprite_smoke_2, sprite_smoke_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_concentrator_spritelayout_ore_handling_rear",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_concentrator_spritelayout_copper_forklift",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_concentrator_spritelayout_small_shed",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_concentrator_spritelayout_stack_vent_thing",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_concentrator_spritelayout_ground",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_concentrator_spritelayout_transformer",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_transformer],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="copper_concentrator_industry_layout_1",
    layout=[
        (
            0,
            0,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_transformer",
        ),
        (
            0,
            1,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_big_shed",
        ),
        (
            0,
            2,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_big_shed",
        ),
        (
            0,
            3,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_small_shed",
        ),
        (
            1,
            0,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_ore_handling_rear",
        ),
        (1, 1, "copper_concentrator_tile_1", "copper_concentrator_spritelayout_tanks"),
        (
            1,
            2,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_stack_vent_thing",
        ),
        (
            1,
            3,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_copper_forklift",
        ),
        (
            2,
            0,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_ore_handling_front",
        ),
        (2, 1, "copper_concentrator_tile_1", "copper_concentrator_spritelayout_tanks"),
        (
            2,
            2,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_stack_vent_thing",
        ),
        (2, 3, "copper_concentrator_tile_1", "copper_concentrator_spritelayout_ground"),
        (
            3,
            0,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_flue_stack",
        ),
        (
            3,
            1,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_thickening_tank",
        ),
        (
            3,
            2,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_thickening_tank",
        ),
        (3, 3, "copper_concentrator_tile_1", "copper_concentrator_spritelayout_ground"),
    ],
)

industry.add_industry_layout(
    id="copper_concentrator_industry_layout_2",
    layout=[
        (
            0,
            0,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_ore_handling_rear",
        ),
        (
            0,
            1,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_stack_vent_thing",
        ),
        (0, 2, "copper_concentrator_tile_1", "copper_concentrator_spritelayout_tanks"),
        (
            0,
            3,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_flue_stack",
        ),
        (0, 4, "copper_concentrator_tile_1", "copper_concentrator_spritelayout_tanks"),
        (
            0,
            5,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_small_shed",
        ),
        (
            1,
            0,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_ore_handling_front",
        ),
        (
            1,
            1,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_stack_vent_thing",
        ),
        (
            1,
            2,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_big_shed",
        ),
        (
            1,
            3,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_big_shed",
        ),
        (
            1,
            4,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_big_shed",
        ),
        (
            1,
            5,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_copper_forklift",
        ),
        (
            2,
            0,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_transformer",
        ),
        (
            2,
            1,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_small_shed",
        ),
        (
            2,
            2,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_thickening_tank",
        ),
        (
            2,
            3,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_thickening_tank",
        ),
        (2, 4, "copper_concentrator_tile_1", "copper_concentrator_spritelayout_ground"),
        (2, 5, "copper_concentrator_tile_1", "copper_concentrator_spritelayout_ground"),
    ],
)

industry.add_industry_layout(
    id="copper_concentrator_industry_layout_3",
    layout=[
        (
            0,
            0,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_thickening_tank",
        ),
        (0, 1, "copper_concentrator_tile_1", "copper_concentrator_spritelayout_tanks"),
        (
            0,
            2,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_flue_stack",
        ),
        (0, 3, "copper_concentrator_tile_1", "copper_concentrator_spritelayout_tanks"),
        (
            0,
            4,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_ore_handling_rear",
        ),
        (
            1,
            0,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_thickening_tank",
        ),
        (
            1,
            1,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_big_shed",
        ),
        (
            1,
            2,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_big_shed",
        ),
        (
            1,
            3,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_big_shed",
        ),
        (
            1,
            4,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_ore_handling_front",
        ),
        (
            2,
            0,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_transformer",
        ),
        (
            2,
            1,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_big_shed",
        ),
        (
            2,
            2,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_big_shed",
        ),
        (
            2,
            3,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_big_shed",
        ),
        (
            2,
            4,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_stack_vent_thing",
        ),
        (
            3,
            1,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_copper_forklift",
        ),
        (
            3,
            2,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_small_shed",
        ),
        (3, 3, "copper_concentrator_tile_1", "copper_concentrator_spritelayout_ground"),
        (
            3,
            4,
            "copper_concentrator_tile_1",
            "copper_concentrator_spritelayout_stack_vent_thing",
        ),
    ],
)
