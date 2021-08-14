from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="brewery",
    accept_cargos_with_input_ratios=[("FRUT", 6)],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("BEER", 8)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="191",
    # no industry location checks for brewery, by design
    name="string(STR_IND_BREWERY)",
    nearby_station_name="string(STR_STATION_BARREL_AND_KEG)",
    fund_cost_multiplier="50",
    pollution_and_squalor_factor=1,
)

###industry.economy_variations['BETTER_LIVING_THROUGH_CHEMISTRY'].enabled = True
###industry.economy_variations['BETTER_LIVING_THROUGH_CHEMISTRY'].accept_cargos_with_input_ratios = [('GRAI', 4), ('MNSP', 4)]

industry.economy_variations["IN_A_HOT_COUNTRY"].enabled = True
industry.economy_variations["IN_A_HOT_COUNTRY"].accept_cargos_with_input_ratios = [
    ("FRUT", 4),
    ("MAIZ", 4),
]

industry.add_tile(
    id="brewery_tile_1",
    animation_length=6,
    animation_looping=True,
    animation_speed=3,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True,
        require_houses_nearby=True,
        disallow_industry_adjacent=True,
    ),
)
industry.add_tile(
    id="brewery_tile_2",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="cobble",
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
    type="cobble",
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
    id="brewery_spritelayout_1_anim",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="brewery_spritelayout_2",
    ground_sprite=spriteset_ground_anim,
    ground_overlay=spriteset_ground_overlay_anim,
    building_sprites=[spriteset_2_anim],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="brewery_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="brewery_industry_layout_1",
    layout=[
        (0, 2, "brewery_tile_1", "brewery_spritelayout_3"),
        (1, 0, "brewery_tile_2", "brewery_spritelayout_1_anim"),
        (1, 2, "brewery_tile_1", "brewery_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="brewery_industry_layout_2",
    layout=[
        (0, 0, "brewery_tile_1", "brewery_spritelayout_3"),
        (1, 0, "brewery_tile_1", "brewery_spritelayout_2"),
        (2, 0, "brewery_tile_2", "brewery_spritelayout_1_anim"),
    ],
)
industry.add_industry_layout(
    id="brewery_industry_layout_3",
    layout=[
        (0, 1, "brewery_tile_1", "brewery_spritelayout_3"),
        (1, 0, "brewery_tile_2", "brewery_spritelayout_1_anim"),
        (1, 1, "brewery_tile_1", "brewery_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="brewery_industry_layout_4",
    layout=[
        (0, 0, "brewery_tile_2", "brewery_spritelayout_1_anim"),
        (1, 0, "brewery_tile_1", "brewery_spritelayout_3"),
        (2, 0, "brewery_tile_1", "brewery_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="brewery_industry_layout_5",
    layout=[
        (0, 0, "brewery_tile_1", "brewery_spritelayout_3"),
        (0, 1, "brewery_tile_1", "brewery_spritelayout_3"),
        (1, 0, "brewery_tile_1", "brewery_spritelayout_2"),
        (1, 1, "brewery_tile_1", "brewery_spritelayout_2"),
        (2, 0, "brewery_tile_2", "brewery_spritelayout_1_anim"),
    ],
)
