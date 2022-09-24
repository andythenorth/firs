from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="basic_oxygen_furnace",
    accept_cargos_with_input_ratios=[
        ("IRON", 4),
        ("MNO2", 2),
        ("QLME", 1),
        ("O2__", 1),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("STCB", 4),
        ("STAL", 2),
        ("SLAG", 2),
    ],
    prob_in_game="0",  # do not build during gameplay
    prob_map_gen="5",
    map_colour="49",
    special_flags=["IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE"],
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[["blast_furnace"], 72],
        same_type_distance=72,
    ),
    name="string(STR_IND_BASIC_OXYGEN_FURNACE)",
    nearby_station_name="string(STR_STATION_FURNACE)",
    fund_cost_multiplier="160",
    pollution_and_squalor_factor=2,
)

industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="basic_oxygen_furnace_tile_1",
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
industry.add_tile(
    id="basic_oxygen_furnace_tile_2",
    animation_length=36,
    animation_looping=True,
    animation_speed=4,  # 4 is intended, use 5 for slower frame testing when drawing sprites
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
spriteset_tanks = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -90)],
)
spriteset_tanks_ground_shading = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_furnace = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
)
spriteset_air_plant = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
)
spriteset_caster = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -90)],
)
spriteset_metal_1 = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -90)],
)
spriteset_shed = industry.add_spriteset(
    sprites=[(710, 10, 64, 122, -31, -90)],
)
spriteset_caster_crane_animated = industry.add_spriteset(
    sprites=[
        (10, 250, 64, 64, -31, -33),
        (80, 250, 64, 64, -31, -33),
        (150, 250, 64, 64, -31, -33),
        (220, 250, 64, 64, -31, -33),
        (290, 250, 64, 64, -31, -33),
        (360, 250, 64, 64, -31, -33),
        (430, 250, 64, 64, -31, -33),
        (500, 250, 64, 64, -31, -33),
        (570, 250, 64, 64, -31, -33),
        (640, 250, 64, 64, -31, -33),
        # repeat the pour for 9 frames
        (710, 250, 64, 64, -31, -33),
        (710, 250, 64, 64, -31, -33),
        (710, 250, 64, 64, -31, -33),
        (710, 250, 64, 64, -31, -33),
        (710, 250, 64, 64, -31, -33),
        (710, 250, 64, 64, -31, -33),
        (710, 250, 64, 64, -31, -33),
        (710, 250, 64, 64, -31, -33),
        (710, 250, 64, 64, -31, -33),
        # repeat the end of the pour for 2 frames
        (780, 250, 64, 64, -31, -33),
        (780, 250, 64, 64, -31, -33),
        (850, 250, 64, 64, -31, -33),
        (920, 250, 64, 64, -31, -33),
        (990, 250, 64, 64, -31, -33),
        (1060, 250, 64, 64, -31, -33),
        (1130, 250, 64, 64, -31, -33),
        (1200, 250, 64, 64, -31, -33),
        (1270, 250, 64, 64, -31, -33),
        (1340, 250, 64, 64, -31, -33),
        (1410, 250, 64, 64, -31, -33),
        (1480, 250, 64, 64, -31, -33),
    ],
    animation_rate=1,
    # the offset here acts to extend the animation, and for this case should be the total number of animation frames provided in the spriteset
    custom_sprite_selector="(animation_frame < 31) ? (animation_frame % 31) : 0",
)
spriteset_caster_gantry_animated = industry.add_spriteset(
    sprites=[
        (10, 160, 64, 64, -31, -33),
    ],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_caster_crane_animated.sprites),
)
# needed to overlay the ladle
spriteset_caster_gantry_overlay_animated = industry.add_spriteset(
    sprites=[
        (80, 160, 64, 64, -31, -33),
    ],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_caster_crane_animated.sprites),
)
spriteset_ground_tile_animated_crane = industry.add_spriteset(
    type="hard_standing_dirt",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_caster_crane_animated.sprites),
)
spriteset_caster_metal_run_animated = industry.add_spriteset(
    sprites=[
        # repeat the empty frame until the 1 frame after the crane pour starts
        (10, 430, 64, 64, -31, -33),
        (10, 430, 64, 64, -31, -33),
        (10, 430, 64, 64, -31, -33),
        (10, 430, 64, 64, -31, -33),
        (10, 430, 64, 64, -31, -33),
        (10, 430, 64, 64, -31, -33),
        (10, 430, 64, 64, -31, -33),
        (10, 430, 64, 64, -31, -33),
        (10, 430, 64, 64, -31, -33),
        (10, 430, 64, 64, -31, -33),
        (10, 430, 64, 64, -31, -33),
        (10, 430, 64, 64, -31, -33),
        (80, 430, 64, 64, -31, -33),
        (150, 430, 64, 64, -31, -33),
        (220, 430, 64, 64, -31, -33),
        (290, 430, 64, 64, -31, -33),
        (360, 430, 64, 64, -31, -33),
        (430, 430, 64, 64, -31, -33),
        (500, 430, 64, 64, -31, -33),
        (570, 430, 64, 64, -31, -33),
        (640, 430, 64, 64, -31, -33),
        # continuous casting frame, tried repeating, but looks odd with the pour
        (710, 430, 64, 64, -31, -33),
        (780, 430, 64, 64, -31, -33),
        (850, 430, 64, 64, -31, -33),
        (920, 430, 64, 64, -31, -33),
        (990, 430, 64, 64, -31, -33),
        (1060, 430, 64, 64, -31, -33),
        (1130, 430, 64, 64, -31, -33),
        (1200, 430, 64, 64, -31, -33),
        (1270, 430, 64, 64, -31, -33),
        (1340, 430, 64, 64, -31, -33),
        (1410, 430, 64, 64, -31, -33),
    ],
    animation_rate=1,
    # the offset here acts to extend the animation, and for this case should be the total number of animation frames provided in the spriteset
    custom_sprite_selector="(animation_frame < 32) ? (animation_frame % 32) : 0",
)
spriteset_caster_machinery_animated = industry.add_spriteset(
    sprites=[
        (10, 340, 64, 64, -31, -33),
    ],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_caster_metal_run_animated.sprites),
)
spriteset_ground_tile_animated_metal_run = industry.add_spriteset(
    type="hard_standing_dirt",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_caster_metal_run_animated.sprites),
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=1,
    yoffset=0,
    zoffset=61,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=4,
    yoffset=1,
    zoffset=93,
)

industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_empty",
    tile="basic_oxygen_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_tanks",
    tile="basic_oxygen_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_tanks_ground_shading,
    building_sprites=[spriteset_tanks],
    fences=[],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_air_plant",
    tile="basic_oxygen_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_air_plant],
    smoke_sprites=[sprite_smoke_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_furnace",
    tile="basic_oxygen_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_furnace],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_casting_shed",
    tile="basic_oxygen_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_caster],
    smoke_sprites=[sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_metal_1",
    tile="basic_oxygen_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_small_shed",
    tile="basic_oxygen_furnace_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed],
    fences=["nw", "se"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_animated_casting_front_part",
    tile="basic_oxygen_furnace_tile_2",
    ground_sprite=spriteset_ground_tile_animated_crane,
    ground_overlay=spriteset_ground_tile_animated_crane,
    building_sprites=[
        spriteset_caster_gantry_animated,
        spriteset_caster_crane_animated,
        spriteset_caster_gantry_overlay_animated,
    ],
    fences=["nw", "ne", "se", "sw"],
    perma_fences=["sw"],
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_animated_casting_rear_part",
    tile="basic_oxygen_furnace_tile_2",
    ground_sprite=spriteset_ground_tile_animated_metal_run,
    ground_overlay=spriteset_ground_tile_animated_metal_run,
    building_sprites=[
        spriteset_caster_machinery_animated,
        spriteset_caster_metal_run_animated,
    ],
    fences=["nw", "ne", "se", "sw"],
    perma_fences=["sw"],
)

# this industry needs outpost layout as there are lots of cargos
industry.add_industry_outpost_layout(
    id="basic_oxygen_furnace_industry_outpost_layout_1",
    layout=[
        # test outpost layout
        (
            0,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_spritelayout_metal_1",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_spritelayout_small_shed",
        ),
    ],
)
# core layouts are roughly 4x4 or 3x5
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_1",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            3,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            4,
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            3,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            4,
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_spritelayout_animated_casting_rear_part",
        ),
        (
            2,
            3,
            "basic_oxygen_furnace_spritelayout_animated_casting_front_part",
        ),
        (
            2,
            4,
            "basic_oxygen_furnace_spritelayout_small_shed",
        ),
    ],
)
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_2",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            0,
            3,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            3,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            3,
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            3,
            0,
            "basic_oxygen_furnace_spritelayout_small_shed",
        ),
        (
            3,
            1,
            "basic_oxygen_furnace_spritelayout_animated_casting_rear_part",
        ),
        (
            3,
            2,
            "basic_oxygen_furnace_spritelayout_animated_casting_front_part",
        ),
        (
            3,
            3,
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
    ],
)
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_3",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            0,
            3,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            3,
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            3,
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            3,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            3,
            1,
            "basic_oxygen_furnace_spritelayout_animated_casting_rear_part",
        ),
        (
            3,
            2,
            "basic_oxygen_furnace_spritelayout_animated_casting_front_part",
        ),
        (
            3,
            3,
            "basic_oxygen_furnace_spritelayout_small_shed",
        ),
    ],
)
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_4",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            3,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            3,
            1,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            3,
            2,
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            4,
            0,
            "basic_oxygen_furnace_spritelayout_animated_casting_rear_part",
        ),
        (
            4,
            1,
            "basic_oxygen_furnace_spritelayout_animated_casting_front_part",
        ),
        (
            4,
            2,
            "basic_oxygen_furnace_spritelayout_small_shed",
        ),
    ],
)
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_5",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            3,
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            3,
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            3,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            3,
            0,
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            3,
            1,
            "basic_oxygen_furnace_spritelayout_animated_casting_rear_part",
        ),
        (
            3,
            2,
            "basic_oxygen_furnace_spritelayout_animated_casting_front_part",
        ),
        (
            3,
            3,
            "basic_oxygen_furnace_spritelayout_small_shed",
        ),
    ],
)
