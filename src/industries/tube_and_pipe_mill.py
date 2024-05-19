from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="tube_and_pipe_mill",
    accept_cargos_with_input_ratios=[
        ("STBL", 5),
        ("ACID", 1),
        ("SOAP", 1),
        ("COAT", 1),
    ],
    prod_cargo_types_with_output_ratios=[
        ("STTB", 3),
        ("STPP", 3),
        ("ENSP", 1),
    ],
    # do not build during gameplay
    prob_in_game="0",
    prob_map_gen="5",
    map_colour="70",
    name="string(STR_IND_TUBE_AND_PIPE_MILL)",
    nearby_station_name="string(STR_STATION_TUBE_MILL)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
    sprites_complete=True,
)


industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="tube_and_pipe_mill_tile_1",
    animation_length=71,
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


spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 64, -31, -34)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -33)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -33)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -33)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -33)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -33)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 64, -31, -33)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 64, -31, -33)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 64, -31, -33)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(360, 80, 64, 31, -31, 0)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(430, 80, 64, 31, -31, 0)],
)
spriteset_12 = industry.add_spriteset(
    sprites=[(500, 80, 64, 31, -31, -10)],
)
spriteset_13 = industry.add_spriteset(
    sprites=[(570, 80, 64, 31, -31, 0)],
)
spriteset_14 = industry.add_spriteset(
    sprites=[(640, 80, 64, 31, -31, 0)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-5,
    yoffset=0,
    zoffset=39,
)

industry.add_spritelayout(
    id="tube_and_pipe_mill_spritelayout_boilerhouse",
    tile="tube_and_pipe_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="tube_and_pipe_mill_spritelayout_shed_sw_ne_1",
    tile="tube_and_pipe_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=[],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="tube_and_pipe_mill_spritelayout_shed_sw_ne_2",
    tile="tube_and_pipe_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=[],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="tube_and_pipe_mill_spritelayout_shed_se_nw_1",
    tile="tube_and_pipe_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=[],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="tube_and_pipe_mill_spritelayout_shed_se_nw_2",
    tile="tube_and_pipe_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=[],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="tube_and_pipe_mill_spritelayout_open_shed_pipes",
    tile="tube_and_pipe_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=8,
)
industry.add_spritelayout(
    id="tube_and_pipe_mill_spritelayout_tanks",
    tile="tube_and_pipe_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="tube_and_pipe_mill_spritelayout_office",
    tile="tube_and_pipe_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "sw"],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="tube_and_pipe_mill_spritelayout_steel_pile_sw_ne",
    tile="tube_and_pipe_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tube_and_pipe_mill_spritelayout_steel_pile_se_nw",
    tile="tube_and_pipe_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_11],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tube_and_pipe_mill_spritelayout_pipe_stack_sw_ne",
    tile="tube_and_pipe_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_13],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=9,
)
industry.add_spritelayout(
    id="tube_and_pipe_mill_spritelayout_pipe_stack_se_nw",
    tile="tube_and_pipe_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_14],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=10,
)
industry.add_spritelayout(
    id="tube_and_pipe_mill_spritelayout_empty",
    tile="tube_and_pipe_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=[],
)

# this industry needs outpost layout as there are lots of cargos
# note there are two outposts, as this industry has sprites oriented sw_ne or se_nw, will select outpost to match main layout orientation
industry.add_industry_outpost_layout(
    id="tube_and_pipe_mill_industry_outpost_layout_sw_ne",
    layout=[
        (
            0,
            0,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            0,
            1,
            "tube_and_pipe_mill_spritelayout_boilerhouse",
        ),
        (
            1,
            1,
            "tube_and_pipe_mill_spritelayout_pipe_stack_sw_ne",
        ),
        (
            1,
            0,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            2,
            0,
            "tube_and_pipe_mill_spritelayout_open_shed_pipes",
        ),
        (
            2,
            1,
            "tube_and_pipe_mill_spritelayout_tanks",
        ),
    ],
)
industry.add_industry_outpost_layout(
    id="tube_and_pipe_mill_industry_outpost_layout_se_nw",
    layout=[
        (
            0,
            0,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_1",
        ),
        (
            0,
            1,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_2",
        ),
        (
            0,
            2,
            "tube_and_pipe_mill_spritelayout_open_shed_pipes",
        ),
        (
            1,
            0,
            "tube_and_pipe_mill_spritelayout_boilerhouse",
        ),
        (
            1,
            1,
            "tube_and_pipe_mill_spritelayout_pipe_stack_se_nw",
        ),
        (
            1,
            2,
            "tube_and_pipe_mill_spritelayout_tanks",
        ),
    ],
)
# core layouts are roughly 6x4 or 5x5
# long products mill uses non-standard layouts where some sprites only used for some orientiations (sw_ne or se_nw)
# this is to achieve the appearance of 'long'
industry.add_industry_layout(
    id="tube_and_pipe_mill_industry_layout_1",
    excluded_outpost_layouts=["tube_and_pipe_mill_industry_outpost_layout_se_nw"],
    layout=[
        (
            0,
            0,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            0,
            1,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            0,
            2,
            "tube_and_pipe_mill_spritelayout_boilerhouse",
        ),
        (
            1,
            0,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            1,
            1,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            1,
            2,
            "tube_and_pipe_mill_spritelayout_pipe_stack_sw_ne",
        ),
        (
            2,
            0,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            2,
            1,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            2,
            2,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            3,
            0,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            3,
            1,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            3,
            2,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            4,
            0,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            4,
            1,
            "tube_and_pipe_mill_spritelayout_open_shed_pipes",
        ),
        (
            4,
            2,
            "tube_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (5, 0, "tube_and_pipe_mill_spritelayout_tanks"),
        (
            5,
            1,
            "tube_and_pipe_mill_spritelayout_open_shed_pipes",
        ),
        (
            5,
            2,
            "tube_and_pipe_mill_spritelayout_pipe_stack_sw_ne",
        ),
    ],
)
industry.add_industry_layout(
    id="tube_and_pipe_mill_industry_layout_2",
    excluded_outpost_layouts=["tube_and_pipe_mill_industry_outpost_layout_sw_ne"],
    layout=[
        (
            0,
            0,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_1",
        ),
        (
            0,
            1,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_2",
        ),
        (
            0,
            2,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_2",
        ),
        (
            0,
            3,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_1",
        ),
        (
            0,
            4,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_1",
        ),
        (0, 5, "tube_and_pipe_mill_spritelayout_tanks"),
        (
            1,
            0,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_1",
        ),
        (
            1,
            1,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_2",
        ),
        (
            1,
            2,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_2",
        ),
        (
            1,
            3,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_1",
        ),
        (
            1,
            4,
            "tube_and_pipe_mill_spritelayout_open_shed_pipes",
        ),
        (
            1,
            5,
            "tube_and_pipe_mill_spritelayout_open_shed_pipes",
        ),
        (
            2,
            0,
            "tube_and_pipe_mill_spritelayout_boilerhouse",
        ),
        (
            2,
            1,
            "tube_and_pipe_mill_spritelayout_pipe_stack_se_nw",
        ),
        (
            2,
            2,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_2",
        ),
        (
            2,
            3,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_1",
        ),
        (
            2,
            4,
            "tube_and_pipe_mill_spritelayout_shed_se_nw_2",
        ),
        (
            2,
            5,
            "tube_and_pipe_mill_spritelayout_pipe_stack_se_nw",
        ),
    ],
)
