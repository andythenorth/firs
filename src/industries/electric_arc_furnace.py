from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="electric_arc_furnace",
    accept_cargos_with_input_ratios=[
        ("SCMT", 4),
        ("FECR", 2),
        ("QLME", 1),
        ("O2__", 1),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("STCB", 4),
        ("STST", 2),
        ("SLAG", 2),
    ],
    prob_in_game="1",  # low chance of build during gameplay
    prob_map_gen="5",
    map_colour="186",
    name="string(STR_IND_ELECTRIC_ARC_FURNACE)",
    nearby_station_name="string(STR_STATION_FURNACE)",
    fund_cost_multiplier="160",
    pollution_and_squalor_factor=2,
)

industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="electric_arc_furnace_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="electric_arc_furnace_tile_2",
    animation_length=10,
    animation_looping=True,
    animation_speed=4,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="hard_standing_dirt",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)
spriteset_large_shed_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -90)],
)
spriteset_large_shed_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -90)],
)
spriteset_large_shed_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_tanks = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
)
spriteset_air_plant = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
)
spriteset_metal_1 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -33)],
)
spriteset_extra_shed_1 = industry.add_spriteset(
    sprites=[(430, 10, 64, 64, -31, -33)],
)
spriteset_casting_shed_1 = industry.add_spriteset(
    sprites=[(10, 160, 64, 64, -31, -33)],
)
spriteset_casting_shed_2 = industry.add_spriteset(
    sprites=[(80, 160, 64, 64, -31, -33)],
)
spriteset_casting_shed_3 = industry.add_spriteset(
    sprites=[(150, 160, 64, 64, -31, -33)],
)
spriteset_caster_line_metal_animated = industry.add_spriteset(
    sprites=[
        (10, 340, 64, 64, -31, -33),
        (80, 340, 64, 64, -31, -33),
        (150, 340, 64, 64, -31, -33),
        (220, 340, 64, 64, -31, -33),
        (290, 340, 64, 64, -31, -33),
        (360, 340, 64, 64, -31, -33),
        (430, 340, 64, 64, -31, -33),
        (500, 340, 64, 64, -31, -33),
        (570, 340, 64, 64, -31, -33),
        (640, 340, 64, 64, -31, -33),
    ],
    animation_rate=1,
)
spriteset_caster_line_1_animated = industry.add_spriteset(
    sprites=[(10, 250, 64, 64, -31, -33)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_caster_line_metal_animated.sprites),
)
spriteset_ground_tile_animated_caster_line = industry.add_spriteset(
    type="hard_standing_dirt",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_caster_line_metal_animated.sprites),
)

sprite_smoke_main_stack_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=2,
    yoffset=0,
    zoffset=56,
)
sprite_smoke_main_stack_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=2,
    yoffset=1,
    zoffset=59,
)
sprite_smoke_coolers_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=5,
    yoffset=-2,
    zoffset=13,
)
sprite_smoke_coolers_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=5,
    yoffset=0,
    zoffset=14,
)
sprite_smoke_coolers_3 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=5,
    yoffset=2,
    zoffset=12,
)
sprite_smoke_coolers_4 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=5,
    yoffset=4,
    zoffset=13,
)
sprite_smoke_coolers_5 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=5,
    yoffset=7,
    zoffset=13,
)
sprite_smoke_coolers_6 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=5,
    yoffset=9,
    zoffset=14,
)

industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_empty",
    tile="electric_arc_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_large_furnace_shed_1",
    tile="electric_arc_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_shed_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_large_furnace_shed_2",
    tile="electric_arc_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_shed_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_large_furnace_shed_3",
    tile="electric_arc_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_shed_3],
    fences=["nw", "ne", "se", "sw"],
    smoke_sprites=[
        sprite_smoke_coolers_1,
        sprite_smoke_coolers_2,
        sprite_smoke_coolers_3,
        sprite_smoke_coolers_4,
        sprite_smoke_coolers_5,
        sprite_smoke_coolers_6,
    ],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_casting_shed_1",
    tile="electric_arc_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_casting_shed_1],
    fences=["nw", "ne", "se"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_casting_shed_2",
    tile="electric_arc_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_casting_shed_2],
    fences=["nw", "ne", "sw"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_casting_shed_3",
    tile="electric_arc_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_casting_shed_3],
    fences=["nw", "ne"],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_caster_line_animated",
    tile="electric_arc_furnace_tile_2",
    ground_sprite=spriteset_ground_tile_animated_caster_line,
    ground_overlay=spriteset_ground_tile_animated_caster_line,
    building_sprites=[
        spriteset_caster_line_1_animated,
        spriteset_caster_line_metal_animated,
    ],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_tanks",
    tile="electric_arc_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_tanks],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=9,
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_air_plant",
    tile="electric_arc_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_air_plant],
    fences=["nw", "ne", "se", "sw"],
    smoke_sprites=[
        sprite_smoke_main_stack_1,
        sprite_smoke_main_stack_2,
    ],
    add_to_object_num=8,
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_metal_1",
    tile="electric_arc_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=10,
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_extra_shed_1",
    tile="electric_arc_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_extra_shed_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=7,
)
# this industry needs outpost layout as there are lots of cargos
industry.add_industry_outpost_layout(
    id="electric_arc_furnace_industry_outpost_layout_1",
    layout=[
        # test outpost layout
        (
            0,
            0,
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            0,
            1,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            0,
            2,
            "electric_arc_furnace_spritelayout_casting_shed_3",
        ),
        (
            1,
            0,
            "electric_arc_furnace_spritelayout_air_plant",
        ),
        (
            1,
            1,
            "electric_arc_furnace_spritelayout_tanks",
        ),
        (
            1,
            2,
            "electric_arc_furnace_spritelayout_metal_1",
        ),
    ],
)
industry.add_industry_outpost_layout(
    id="electric_arc_furnace_industry_outpost_layout_2",
    layout=[
        # test outpost layout
        (
            0,
            0,
            "electric_arc_furnace_spritelayout_tanks",
        ),
        (
            0,
            1,
            "electric_arc_furnace_spritelayout_air_plant",
        ),
        (
            1,
            0,
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            1,
            1,
            "electric_arc_furnace_spritelayout_casting_shed_3",
        ),
        (
            2,
            0,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            2,
            1,
            "electric_arc_furnace_spritelayout_metal_1",
        ),
    ],
)
# core layouts are roughly 5x4 or 4x4
industry.add_industry_layout(
    id="electric_arc_furnace_industry_layout_1",
    layout=[
        (
            0,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            1,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            2,
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            0,
            3,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            0,
            4,
            "electric_arc_furnace_spritelayout_casting_shed_3",
        ),
        (
            1,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_3",
        ),
        (
            1,
            1,
            "electric_arc_furnace_spritelayout_large_furnace_shed_1",
        ),
        (
            1,
            2,
            "electric_arc_furnace_spritelayout_caster_line_animated",
        ),
        (
            1,
            3,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            1,
            4,
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            2,
            0,
            "electric_arc_furnace_spritelayout_tanks",
        ),
        (
            2,
            1,
            "electric_arc_furnace_spritelayout_air_plant",
        ),
        (
            2,
            2,
            "electric_arc_furnace_spritelayout_extra_shed_1",
        ),
        (
            2,
            3,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            2,
            4,
            "electric_arc_furnace_spritelayout_casting_shed_3",
        ),
    ],
)
industry.add_industry_layout(
    id="electric_arc_furnace_industry_layout_2",
    layout=[
        (
            0,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            1,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            2,
            "electric_arc_furnace_spritelayout_air_plant",
        ),
        (
            1,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            1,
            1,
            "electric_arc_furnace_spritelayout_large_furnace_shed_3",
        ),
        (
            1,
            2,
            "electric_arc_furnace_spritelayout_tanks",
        ),
        (
            2,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_1",
        ),
        (
            2,
            1,
            "electric_arc_furnace_spritelayout_caster_line_animated",
        ),
        (
            2,
            2,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            3,
            0,
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            3,
            1,
            "electric_arc_furnace_spritelayout_extra_shed_1",
        ),
        (
            3,
            2,
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            4,
            0,
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            4,
            1,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            4,
            2,
            "electric_arc_furnace_spritelayout_casting_shed_3",
        ),
    ],
)
industry.add_industry_layout(
    id="electric_arc_furnace_industry_layout_3",
    layout=[
        (
            0,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            1,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            2,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            0,
            3,
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            1,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            1,
            1,
            "electric_arc_furnace_spritelayout_large_furnace_shed_3",
        ),
        (
            1,
            2,
            "electric_arc_furnace_spritelayout_tanks",
        ),
        (
            1,
            3,
            "electric_arc_furnace_spritelayout_air_plant",
        ),
        (
            2,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_1",
        ),
        (
            2,
            1,
            "electric_arc_furnace_spritelayout_caster_line_animated",
        ),
        (
            2,
            2,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            2,
            3,
            "electric_arc_furnace_spritelayout_casting_shed_3",
        ),
        (
            3,
            0,
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            3,
            1,
            "electric_arc_furnace_spritelayout_extra_shed_1",
        ),
        (
            3,
            2,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            3,
            3,
            "electric_arc_furnace_spritelayout_casting_shed_3",
        ),
    ],
)
industry.add_industry_layout(
    id="electric_arc_furnace_industry_layout_4",
    layout=[
        (
            0,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            1,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            2,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            3,
            "electric_arc_furnace_spritelayout_tanks",
        ),
        (
            0,
            4,
            "electric_arc_furnace_spritelayout_air_plant",
        ),
        (
            1,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            1,
            1,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            1,
            2,
            "electric_arc_furnace_spritelayout_large_furnace_shed_1",
        ),
        (
            1,
            3,
            "electric_arc_furnace_spritelayout_caster_line_animated",
        ),
        (
            1,
            4,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            2,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_3",
        ),
        (
            2,
            1,
            "electric_arc_furnace_spritelayout_large_furnace_shed_1",
        ),
        (
            2,
            2,
            "electric_arc_furnace_spritelayout_caster_line_animated",
        ),
        (
            2,
            3,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            2,
            4,
            "electric_arc_furnace_spritelayout_casting_shed_3",
        ),
        (
            3,
            0,
            "electric_arc_furnace_spritelayout_tanks",
        ),
        (
            3,
            1,
            "electric_arc_furnace_spritelayout_air_plant",
        ),
        (
            3,
            2,
            "electric_arc_furnace_spritelayout_extra_shed_1",
        ),
        (
            3,
            3,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            3,
            4,
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
    ],
)
industry.add_industry_layout(
    id="electric_arc_furnace_industry_layout_5",
    layout=[
        (
            0,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            1,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            2,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            3,
            "electric_arc_furnace_spritelayout_air_plant",
        ),
        (
            1,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            1,
            1,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            1,
            2,
            "electric_arc_furnace_spritelayout_large_furnace_shed_3",
        ),
        (
            1,
            3,
            "electric_arc_furnace_spritelayout_tanks",
        ),
        (
            2,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            2,
            1,
            "electric_arc_furnace_spritelayout_large_furnace_shed_1",
        ),
        (
            2,
            2,
            "electric_arc_furnace_spritelayout_caster_line_animated",
        ),
        (
            2,
            3,
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            3,
            0,
            "electric_arc_furnace_spritelayout_large_furnace_shed_1",
        ),
        (
            3,
            1,
            "electric_arc_furnace_spritelayout_caster_line_animated",
        ),
        (
            3,
            2,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            3,
            3,
            "electric_arc_furnace_spritelayout_casting_shed_3",
        ),
        (
            4,
            0,
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            4,
            1,
            "electric_arc_furnace_spritelayout_extra_shed_1",
        ),
        (
            4,
            2,
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            4,
            3,
            "electric_arc_furnace_spritelayout_casting_shed_3",
        ),
    ],
)
