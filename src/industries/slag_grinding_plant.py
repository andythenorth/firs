from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="slag_grinding_plant",
    accept_cargos_with_input_ratios=[
        ("SLAG", 8),
    ],
    prod_cargo_types_with_output_ratios=[
        ("CMNT", 5),
        ("FMSP", 3),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="19",
    special_flags=["IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE"],
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[
            ["blast_furnace", "basic_oxygen_furnace", "electric_arc_furnace"],
            56,
        ],
        same_type_distance=72,
    ),
    name="string(STR_IND_SLAG_GRINDING_PLANT)",
    nearby_station_name="string(STR_STATION_SILO)",
    fund_cost_multiplier="100 ",
    pollution_and_squalor_factor=2,
)

industry.enable_in_economy(
    "STEELTOWN",
    prob_in_game="0",  # do not build during gameplay
)

industry.add_tile(
    id="slag_grinding_plant_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

industry.add_tile(
    id="slag_grinding_plant_tile_2",
    animation_length=56,
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
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_silos = industry.add_spriteset(
    sprites=[(10, 10, 64, 120, -31, -89)],
)
spriteset_large_shed = industry.add_spriteset(
    sprites=[(80, 10, 64, 120, -31, -89)],
)
spriteset_grinding_tower = industry.add_spriteset(
    sprites=[(150, 10, 64, 120, -31, -89)],
)
spriteset_conveyors_1 = industry.add_spriteset(
    sprites=[(220, 10, 64, 120, -31, -89)],
)
spriteset_conveyors_2 = industry.add_spriteset(
    sprites=[(290, 10, 64, 120, -31, -89)],
)
spriteset_slag_dump_1 = industry.add_spriteset(
    sprites=[(360, 10, 64, 120, -31, -89)],
)
spriteset_slag_dump_2 = industry.add_spriteset(
    sprites=[(430, 10, 64, 120, -31, -89)],
)
# non-standard offsets to position crane over slag pit, may be regrettable
spriteset_crane = industry.add_spriteset(
    sprites=[(500, 10, 64, 120, -6, -89)],
)
spriteset_office = industry.add_spriteset(
    sprites=[(570, 10, 64, 120, -31, -89)],
)
spriteset_animated_dozer = industry.add_spriteset(
    sprites=[
        (10, 140, 64, 64, -31, -31),
        (80, 140, 64, 64, -31, -31),
        (150, 140, 64, 64, -31, -31),
        (220, 140, 64, 64, -31, -31),
        (290, 140, 64, 64, -31, -31),
        (360, 140, 64, 64, -31, -31),
        (360, 140, 64, 64, -31, -31),
        (290, 140, 64, 64, -31, -31),
        (220, 140, 64, 64, -31, -31),
        (150, 140, 64, 64, -31, -31),
        (80, 140, 64, 64, -31, -31),
        (10, 140, 64, 64, -31, -31),
    ],
    animation_rate=1,
    custom_sprite_selector="(animation_frame < 36) ? (animation_frame % 12) : 0",
)
# filled out version of ground for slag pit with animation frames
spriteset_animated_ground = industry.add_spriteset(
    type="dirty_concrete",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_animated_ground_overlay = industry.add_spriteset(
    type="empty",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)
spriteset_animated_slag_dump_1 = industry.add_spriteset(
    sprites=[(360, 10, 64, 120, -31, -89)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_animated_dozer.sprites),
)

sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=2,
    zoffset=76,
    animation_frame_offset=1,
)

industry.add_spritelayout(
    id="slag_grinding_plant_spritelayout_tile_empty",
    tile="slag_grinding_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
)
industry.add_spritelayout(
    id="slag_grinding_plant_spritelayout_large_silo",
    tile="slag_grinding_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_silos],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="slag_grinding_plant_spritelayout_large_shed",
    tile="slag_grinding_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_shed],
    smoke_sprites=[sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="slag_grinding_plant_spritelayout_grinding_tower",
    tile="slag_grinding_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_grinding_tower],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="slag_grinding_plant_spritelayout_conveyors_1",
    tile="slag_grinding_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_conveyors_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="slag_grinding_plant_spritelayout_conveyors_2",
    tile="slag_grinding_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_conveyors_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="slag_grinding_plant_spritelayout_slag_dump_1",
    tile="slag_grinding_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_slag_dump_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="slag_grinding_plant_spritelayout_slag_dump_2",
    tile="slag_grinding_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_slag_dump_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="slag_grinding_plant_spritelayout_slag_dump_dozer",
    tile="slag_grinding_plant_tile_2",
    ground_sprite=spriteset_animated_ground,
    ground_overlay=spriteset_animated_ground_overlay,
    building_sprites=[spriteset_animated_slag_dump_1, spriteset_animated_dozer],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="slag_grinding_plant_spritelayout_office",
    tile="slag_grinding_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_office],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)

industry.add_multi_tile_object(
    add_to_object_num=4,
    view_layout=[
        (0, 0, "slag_grinding_plant_spritelayout_grinding_tower"),
        (0, 1, "slag_grinding_plant_spritelayout_conveyors_1"),
    ],
)
industry.add_multi_tile_object(
    add_to_object_num=6,
    view_layout=[
        (0, 1, "slag_grinding_plant_spritelayout_slag_dump_2"),
        (0, 0, "slag_grinding_plant_spritelayout_slag_dump_1"),
    ],
)

industry.add_industry_layout(
    id="slag_grinding_plant_industry_layout_1",
    layout=[
        (
            0,
            0,
            "slag_grinding_plant_spritelayout_large_silo",
        ),
        (
            0,
            1,
            "slag_grinding_plant_spritelayout_large_silo",
        ),
        (
            0,
            2,
            "slag_grinding_plant_spritelayout_slag_dump_dozer",
        ),
        (
            0,
            3,
            "slag_grinding_plant_spritelayout_slag_dump_2",
        ),
        (
            1,
            0,
            "slag_grinding_plant_spritelayout_large_shed",
        ),
        (
            1,
            1,
            "slag_grinding_plant_spritelayout_grinding_tower",
        ),
        (
            1,
            2,
            "slag_grinding_plant_spritelayout_conveyors_1",
        ),
        (
            1,
            3,
            "slag_grinding_plant_spritelayout_conveyors_2",
        ),
        (
            2,
            0,
            "slag_grinding_plant_spritelayout_large_shed",
        ),
        (
            2,
            1,
            "slag_grinding_plant_spritelayout_grinding_tower",
        ),
        (
            2,
            2,
            "slag_grinding_plant_spritelayout_conveyors_1",
        ),
        (
            2,
            3,
            "slag_grinding_plant_spritelayout_conveyors_2",
        ),
        (
            3,
            0,
            "slag_grinding_plant_spritelayout_large_silo",
        ),
        (
            3,
            1,
            "slag_grinding_plant_spritelayout_slag_dump_dozer",
        ),
        (
            3,
            2,
            "slag_grinding_plant_spritelayout_slag_dump_2",
        ),
        (3, 3, "slag_grinding_plant_spritelayout_office"),
    ],
)
industry.add_industry_layout(
    id="slag_grinding_plant_industry_layout_2",
    layout=[
        (
            0,
            0,
            "slag_grinding_plant_spritelayout_large_silo",
        ),
        (
            0,
            1,
            "slag_grinding_plant_spritelayout_large_shed",
        ),
        (
            0,
            2,
            "slag_grinding_plant_spritelayout_slag_dump_dozer",
        ),
        (
            0,
            3,
            "slag_grinding_plant_spritelayout_slag_dump_2",
        ),
        (
            1,
            0,
            "slag_grinding_plant_spritelayout_large_shed",
        ),
        (
            1,
            1,
            "slag_grinding_plant_spritelayout_grinding_tower",
        ),
        (
            1,
            2,
            "slag_grinding_plant_spritelayout_conveyors_1",
        ),
        (
            1,
            3,
            "slag_grinding_plant_spritelayout_conveyors_2",
        ),
        (
            2,
            0,
            "slag_grinding_plant_spritelayout_slag_dump_dozer",
        ),
        (
            2,
            1,
            "slag_grinding_plant_spritelayout_slag_dump_2",
        ),
        (
            2,
            2,
            "slag_grinding_plant_spritelayout_large_silo",
        ),
        (
            2,
            3,
            "slag_grinding_plant_spritelayout_large_silo",
        ),
        (
            3,
            0,
            "slag_grinding_plant_spritelayout_grinding_tower",
        ),
        (
            3,
            1,
            "slag_grinding_plant_spritelayout_conveyors_1",
        ),
        (
            3,
            2,
            "slag_grinding_plant_spritelayout_conveyors_2",
        ),
        (
            3,
            3,
            "slag_grinding_plant_spritelayout_office",
        ),
    ],
)
industry.add_industry_layout(
    id="slag_grinding_plant_industry_layout_3",
    layout=[
        (
            0,
            0,
            "slag_grinding_plant_spritelayout_large_silo",
        ),
        (
            0,
            1,
            "slag_grinding_plant_spritelayout_slag_dump_dozer",
        ),
        (
            0,
            2,
            "slag_grinding_plant_spritelayout_slag_dump_2",
        ),
        (
            1,
            0,
            "slag_grinding_plant_spritelayout_grinding_tower",
        ),
        (
            1,
            1,
            "slag_grinding_plant_spritelayout_conveyors_1",
        ),
        (
            1,
            2,
            "slag_grinding_plant_spritelayout_conveyors_2",
        ),
        (
            2,
            0,
            "slag_grinding_plant_spritelayout_large_shed",
        ),
        (
            2,
            1,
            "slag_grinding_plant_spritelayout_large_silo",
        ),
        (
            2,
            2,
            "slag_grinding_plant_spritelayout_large_silo",
        ),
        (
            3,
            0,
            "slag_grinding_plant_spritelayout_slag_dump_dozer",
        ),
        (
            3,
            1,
            "slag_grinding_plant_spritelayout_slag_dump_2",
        ),
        (
            3,
            2,
            "slag_grinding_plant_spritelayout_office",
        ),
        (
            4,
            0,
            "slag_grinding_plant_spritelayout_grinding_tower",
        ),
        (
            4,
            1,
            "slag_grinding_plant_spritelayout_conveyors_1",
        ),
        (
            4,
            2,
            "slag_grinding_plant_spritelayout_conveyors_2",
        ),
    ],
)
industry.add_industry_layout(
    id="slag_grinding_plant_industry_layout_4",
    layout=[
        (
            0,
            0,
            "slag_grinding_plant_spritelayout_large_silo",
        ),
        (
            0,
            1,
            "slag_grinding_plant_spritelayout_slag_dump_dozer",
        ),
        (
            0,
            2,
            "slag_grinding_plant_spritelayout_slag_dump_2",
        ),
        (
            0,
            3,
            "slag_grinding_plant_spritelayout_large_silo",
        ),
        (
            0,
            4,
            "slag_grinding_plant_spritelayout_large_silo",
        ),
        (
            1,
            0,
            "slag_grinding_plant_spritelayout_grinding_tower",
        ),
        (
            1,
            1,
            "slag_grinding_plant_spritelayout_conveyors_1",
        ),
        (
            1,
            2,
            "slag_grinding_plant_spritelayout_conveyors_2",
        ),
        (
            1,
            3,
            "slag_grinding_plant_spritelayout_slag_dump_dozer",
        ),
        (
            1,
            4,
            "slag_grinding_plant_spritelayout_slag_dump_2",
        ),
        (
            2,
            0,
            "slag_grinding_plant_spritelayout_large_shed",
        ),
        (
            2,
            1,
            "slag_grinding_plant_spritelayout_grinding_tower",
        ),
        (
            2,
            2,
            "slag_grinding_plant_spritelayout_conveyors_1",
        ),
        (
            2,
            3,
            "slag_grinding_plant_spritelayout_conveyors_2",
        ),
        (
            2,
            4,
            "slag_grinding_plant_spritelayout_office",
        ),
    ],
)
