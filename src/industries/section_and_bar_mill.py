from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="section_and_bar_mill",
    # this one is supposed to be an easy dump, so doesn't require ACID or SOAP: products can be mechanically de-scaled and / or assume recycled pickling acid etc
    accept_cargos_with_input_ratios=[
        ("STBL", 8),
    ],
    prod_cargo_types_with_output_ratios=[
        ("STSW", 3),
        ("STBR", 2),
        ("RBAR", 2),
        ("ENSP", 1),
    ],
    prob_in_game="0",  # do not build during gameplay
    prob_map_gen="5",
    map_colour="190",
    colour_scheme_name="scheme_8_bono",
    name="string(STR_IND_SECTION_AND_BAR_MILL)",
    nearby_station_name="string(STR_STATION_BAR_AND_SECTION_MILL)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
    sprites_complete=True,
)


industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="section_and_bar_mill_tile_1",
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
    id="section_and_bar_mill_tile_2",
    animation_length=10,
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
    sprites=[(10, 10, 64, 84, -31, -53)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 84, -31, -53)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 84, -31, -53)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 84, -31, -53)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 84, -31, -53)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 84, -31, -53)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 31, -31, 0)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(430, 43, 64, 51, -31, -21)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(500, 43, 64, 51, -31, -21)],
)
spriteset_gantry_non_animated = industry.add_spriteset(
    sprites=[(570, 30, 64, 64, -31, -33)],
)
spriteset_shed_large_extra = industry.add_spriteset(
    sprites=[(640, 10, 64, 84, -31, -53)],
)
spriteset_nearly_empty = industry.add_spriteset(
    sprites=[(500, 10, 64, 31, -31, 0)],
)
spriteset_rolling_line_metal_animated = industry.add_spriteset(
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
    ],
    animation_rate=1,
)
spriteset_rolling_line_stand_animated = industry.add_spriteset(
    sprites=[(10, 160, 64, 64, -31, -33)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_rolling_line_metal_animated.sprites),
)
spriteset_rolling_line_roof_animated = industry.add_spriteset(
    sprites=[(80, 160, 64, 64, -31, -33)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_rolling_line_metal_animated.sprites),
)
spriteset_ground_tile_animated_rolling_line = industry.add_spriteset(
    type="asphalt",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_rolling_line_metal_animated.sprites),
)
sprite_smoke_1 = industry.add_smoke_sprite(
    # smoke position has to be faffed with to prevent spritesorter issues on adjacent rolling line tile
    smoke_type="white_smoke_big",
    xoffset=4,
    yoffset=-10,
    zoffset=45,
)

industry.add_spritelayout(
    id="section_and_bar_mill_spritelayout_shed_sw_ne_small_doors",
    tile="section_and_bar_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=[],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="section_and_bar_mill_spritelayout_shed_sw_ne_large_door",
    tile="section_and_bar_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=[],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="section_and_bar_mill_spritelayout_shed_sw_ne_tall_1",
    tile="section_and_bar_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=[],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="section_and_bar_mill_spritelayout_shed_sw_ne_tall_2",
    tile="section_and_bar_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    smoke_sprites=[sprite_smoke_1],
    fences=[],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="section_and_bar_mill_spritelayout_shed_sw_ne_tall_3",
    tile="section_and_bar_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="section_and_bar_mill_spritelayout_offices",
    tile="section_and_bar_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="section_and_bar_mill_spritelayout_steel_1",
    tile="section_and_bar_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "sw", "se"],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="section_and_bar_mill_spritelayout_steel_2",
    tile="section_and_bar_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=8,
)
industry.add_spritelayout(
    id="section_and_bar_mill_spritelayout_nearly_empty",
    tile="section_and_bar_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_nearly_empty],
    fences=["nw", "ne"],
    add_to_object_num=9,
)
industry.add_spritelayout(
    id="section_and_bar_mill_spritelayout_gantry_non_animated_1",
    tile="section_and_bar_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9, spriteset_gantry_non_animated],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=10,
)
industry.add_spritelayout(
    id="section_and_bar_mill_spritelayout_sw_ne_rolling_line",
    tile="section_and_bar_mill_tile_2",
    ground_sprite=spriteset_ground_tile_animated_rolling_line,
    ground_overlay=spriteset_ground_tile_animated_rolling_line,
    building_sprites=[
        spriteset_rolling_line_stand_animated,
        spriteset_rolling_line_metal_animated,
        spriteset_rolling_line_roof_animated,
    ],
    fences=[],
    # no animated object; fails on mismatched spritesets, TMWFTLB as of August 2023
    # add_to_object_num=10,
)
industry.add_spritelayout(
    id="section_and_bar_mill_spritelayout_shed_large_extra",
    tile="section_and_bar_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_large_extra],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=11,
)
industry.add_spritelayout(
    id="section_and_bar_mill_spritelayout_empty",
    tile="section_and_bar_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=12,
)

# this industry needs outpost layout as there are lots of cargos
industry.add_industry_outpost_layout(
    id="section_and_bar_mill_industry_outpost_layout_1",
    layout=[
        (
            0,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_large_door",
        ),
        (
            0,
            1,
            "section_and_bar_mill_spritelayout_shed_sw_ne_large_door",
        ),
        (
            1,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_large_door",
        ),
        (
            1,
            1,
            "section_and_bar_mill_spritelayout_steel_1",
        ),  # shed 2 used as it has smoke
        (
            2,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_small_doors",
        ),
        (
            2,
            1,
            "section_and_bar_mill_spritelayout_offices",
        ),
    ],
)
industry.add_industry_outpost_layout(
    id="section_and_bar_mill_industry_outpost_layout_2",
    layout=[
        (
            0,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_large_door",
        ),
        (
            0,
            1,
            "section_and_bar_mill_spritelayout_shed_sw_ne_large_door",
        ),
        (
            0,
            2,
            "section_and_bar_mill_spritelayout_shed_sw_ne_large_door",
        ),
        (
            1,
            0,
            "section_and_bar_mill_spritelayout_steel_1",
        ),  # shed 2 used as it has smoke
        (
            1,
            1,
            "section_and_bar_mill_spritelayout_shed_sw_ne_small_doors",
        ),
        (
            1,
            2,
            "section_and_bar_mill_spritelayout_offices",
        ),
    ],
)
# core layouts are roughly 6x4 or 5x5
# only one orientation sw_ne, couldn't be faffed changing angles for all sprites to do a se_nw
industry.add_industry_layout(
    id="section_and_bar_mill_industry_layout_1",
    layout=[
        (
            0,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_1",
        ),
        (
            0,
            1,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_2",
        ),
        (
            0,
            2,
            "section_and_bar_mill_spritelayout_shed_sw_ne_large_door",
        ),
        (
            1,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_1",
        ),
        (
            1,
            1,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_2",
        ),
        (
            1,
            2,
            "section_and_bar_mill_spritelayout_shed_sw_ne_small_doors",
        ),
        (
            2,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_1",
        ),
        (
            2,
            1,
            "section_and_bar_mill_spritelayout_sw_ne_rolling_line",
        ),
        (
            2,
            2,
            "section_and_bar_mill_spritelayout_steel_2",
        ),
        (
            3,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_1",
        ),
        (
            3,
            1,
            "section_and_bar_mill_spritelayout_sw_ne_rolling_line",
        ),
        (
            3,
            2,
            "section_and_bar_mill_spritelayout_steel_2",
        ),
        (
            4,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_1",
        ),
        (
            4,
            1,
            "section_and_bar_mill_spritelayout_shed_sw_ne_large_door",
        ),
        (
            4,
            2,
            "section_and_bar_mill_spritelayout_steel_1",
        ),
        (
            5,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_3",
        ),
        (
            5,
            1,
            "section_and_bar_mill_spritelayout_shed_sw_ne_small_doors",
        ),
        (
            5,
            2,
            "section_and_bar_mill_spritelayout_offices",
        ),
    ],
)
industry.add_industry_layout(
    id="section_and_bar_mill_industry_layout_2",
    layout=[
        (
            0,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_1",
        ),
        (
            0,
            1,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_2",
        ),
        (
            0,
            2,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_2",
        ),
        (
            0,
            3,
            "section_and_bar_mill_spritelayout_offices",
        ),
        (
            1,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_1",
        ),
        (
            1,
            1,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_1",
        ),
        (
            1,
            2,
            "section_and_bar_mill_spritelayout_sw_ne_rolling_line",
        ),
        (
            1,
            3,
            "section_and_bar_mill_spritelayout_steel_2",
        ),
        (
            2,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_1",
        ),
        (
            2,
            1,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_1",
        ),
        (
            2,
            2,
            "section_and_bar_mill_spritelayout_sw_ne_rolling_line",
        ),
        (
            2,
            3,
            "section_and_bar_mill_spritelayout_steel_2",
        ),
        (
            3,
            0,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_2",
        ),
        (
            3,
            1,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_1",
        ),
        (
            3,
            2,
            "section_and_bar_mill_spritelayout_shed_sw_ne_large_door",
        ),
        (
            3,
            3,
            "section_and_bar_mill_spritelayout_shed_sw_ne_large_door",
        ),
        (
            4,
            0,
            "section_and_bar_mill_spritelayout_steel_1",
        ),
        (
            4,
            1,
            "section_and_bar_mill_spritelayout_shed_sw_ne_tall_3",
        ),
        (
            4,
            2,
            "section_and_bar_mill_spritelayout_shed_sw_ne_small_doors",
        ),
        (
            4,
            3,
            "section_and_bar_mill_spritelayout_shed_sw_ne_small_doors",
        ),
    ],
)
