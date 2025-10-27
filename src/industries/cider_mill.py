from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="cider_mill",
    accept_cargos_with_input_ratios=[],
    prod_cargo_types_with_output_ratios=[
        ("BEER", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="191",
    colour_scheme_name="scheme_3_hendrix",
    location_checks=dict(
        same_type_distance=72,
    ),
    name="string(STR_IND_CIDER_MILL)",
    nearby_station_name="string(STR_STATION_BARREL_AND_KEG)",
    fund_cost_multiplier="50",
    pollution_and_squalor_factor=1,
    provides_snow=True,
    sprites_complete=True,
    animated_tiles_fixed=False,
)

industry.enable_in_economy(
    "BASIC_TEMPERATE",
    accept_cargos_with_input_ratios=[
        ("FRUT", 6),
    ],
)

industry.add_tile(
    id="cider_mill_tile_1",
    animation_length=6,
    animation_looping=True,
    animation_speed=3,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True,
        disallow_industry_adjacent=True,
    ),
)
industry.add_tile(
    id="cider_mill_tile_2",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 91, -31, -60)],
)
# building with animated flags
spriteset_2_anim = industry.add_spriteset(
    sprites=[
        (80, 390, 64, 91, -31, -60),
        (80, 60, 64, 91, -31, -60),
        (80, 170, 64, 91, -31, -60),
        (80, 280, 64, 91, -31, -60),
        (80, 170, 64, 91, -31, -60),
        (80, 60, 64, 91, -31, -60),
    ],
    animation_rate=1,
)
spriteset_ground_anim = industry.add_spriteset(
    type="asphalt",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_2_anim.sprites),
)
spriteset_ground_overlay_anim = industry.add_spriteset(
    type="empty",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_2_anim.sprites),
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 91, -31, -60)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=8,
    yoffset=0,
    zoffset=55,
)

industry.add_spritelayout(
    id="cider_mill_spritelayout_1_anim",
    tile="cider_mill_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="cider_mill_spritelayout_2",
    tile="cider_mill_tile_1",
    ground_sprite=spriteset_ground_anim,
    ground_overlay=spriteset_ground_overlay_anim,
    building_sprites=[spriteset_2_anim],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="cider_mill_spritelayout_3",
    tile="cider_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="cider_mill_industry_layout_1",
    layout=[
        (0, 2, "cider_mill_spritelayout_3"),
        (1, 0, "cider_mill_spritelayout_1_anim"),
        (1, 2, "cider_mill_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="cider_mill_industry_layout_2",
    layout=[
        (0, 0, "cider_mill_spritelayout_3"),
        (1, 0, "cider_mill_spritelayout_2"),
        (2, 0, "cider_mill_spritelayout_1_anim"),
    ],
)
industry.add_industry_layout(
    id="cider_mill_industry_layout_3",
    layout=[
        (0, 1, "cider_mill_spritelayout_3"),
        (1, 0, "cider_mill_spritelayout_1_anim"),
        (1, 1, "cider_mill_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="cider_mill_industry_layout_4",
    layout=[
        (0, 0, "cider_mill_spritelayout_1_anim"),
        (1, 0, "cider_mill_spritelayout_3"),
        (2, 0, "cider_mill_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="cider_mill_industry_layout_5",
    layout=[
        (0, 0, "cider_mill_spritelayout_3"),
        (0, 1, "cider_mill_spritelayout_3"),
        (1, 0, "cider_mill_spritelayout_2"),
        (1, 1, "cider_mill_spritelayout_2"),
        (2, 0, "cider_mill_spritelayout_1_anim"),
    ],
)
