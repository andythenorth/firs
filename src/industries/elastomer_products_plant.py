from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="elastomer_products_plant",
    accept_cargos_with_input_ratios=[("RUBR", 6), ("CBLK", 1), ("SULP", 1)],
    prod_cargo_types_with_output_ratios=[
        ("SEAL", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="169",
    special_flags=["IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE"],
    name="string(STR_IND_ELASTOMER_PRODUCTS_PLANT)",
    nearby_station_name="string(STR_STATION_ELASTOMER_PLANT)",
    fund_cost_multiplier="45",
    sprites_complete=True,
)

industry.enable_in_economy(
    "STEELTOWN",
)

# tile with animation for flag
industry.add_tile(
    id="elastomer_products_plant_tile_1",
    animation_length=6,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
# tile with animation for smoke
industry.add_tile(
    id="elastomer_products_plant_tile_2",
    animation_length=7
    * 6,  # animation length should have a common factor for all tiles in industry
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

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 94, -31, -63)],
)
spriteset_flag_anim = industry.add_spriteset(
    sprites=[
        (220, 120, 64, 64, -31, -65),
        (10, 120, 64, 64, -31, -65),
        (80, 120, 64, 64, -31, -65),
        (150, 120, 64, 64, -31, -65),
        (80, 120, 64, 64, -31, -65),
        (10, 120, 64, 64, -31, -65),
    ],
    animation_rate=1,
)
spriteset_ground_anim = industry.add_spriteset(
    type="asphalt",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_flag_anim.sprites),
)
spriteset_ground_overlay_anim = industry.add_spriteset(
    type="empty",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_flag_anim.sprites),
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 94, -31, -63)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_flag_anim.sprites),
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 94, -31, -62)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 94, -31, -43)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 94, -31, -43)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 94, -31, -43)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 94, -31, -43)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 94, -31, -63)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=12,
    zoffset=56,
)

industry.add_spritelayout(
    id="elastomer_products_plant_spritelayout_1",
    tile="elastomer_products_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="elastomer_products_plant_spritelayout_2",
    tile="elastomer_products_plant_tile_1",
    ground_sprite=spriteset_ground_anim,
    ground_overlay=spriteset_ground_overlay_anim,
    building_sprites=[spriteset_2, spriteset_flag_anim],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="elastomer_products_plant_spritelayout_3",
    tile="elastomer_products_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="elastomer_products_plant_spritelayout_4",
    tile="elastomer_products_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="elastomer_products_plant_spritelayout_5",
    tile="elastomer_products_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="elastomer_products_plant_spritelayout_6",
    tile="elastomer_products_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="elastomer_products_plant_spritelayout_7",
    tile="elastomer_products_plant_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="elastomer_products_plant_spritelayout_8",
    tile="elastomer_products_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="elastomer_products_plant_industry_layout_1",
    layout=[
        (0, 0, "elastomer_products_plant_spritelayout_7"),
        (0, 1, "elastomer_products_plant_spritelayout_5"),
        (1, 0, "elastomer_products_plant_spritelayout_6"),
        (1, 1, "elastomer_products_plant_spritelayout_4"),
        (2, 0, "elastomer_products_plant_spritelayout_8"),
        (2, 1, "elastomer_products_plant_spritelayout_3"),
        (3, 0, "elastomer_products_plant_spritelayout_1"),
        (3, 1, "elastomer_products_plant_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="elastomer_products_plant_industry_layout_2",
    layout=[
        (0, 1, "elastomer_products_plant_spritelayout_7"),
        (0, 2, "elastomer_products_plant_spritelayout_5"),
        (1, 1, "elastomer_products_plant_spritelayout_6"),
        (1, 2, "elastomer_products_plant_spritelayout_4"),
        (2, 0, "elastomer_products_plant_spritelayout_8"),
        (2, 1, "elastomer_products_plant_spritelayout_3"),
        (2, 2, "elastomer_products_plant_spritelayout_8"),
        (3, 0, "elastomer_products_plant_spritelayout_1"),
        (3, 1, "elastomer_products_plant_spritelayout_2"),
        (3, 2, "elastomer_products_plant_spritelayout_8"),
    ],
)
industry.add_industry_layout(
    id="elastomer_products_plant_industry_layout_3",
    layout=[
        (0, 0, "elastomer_products_plant_spritelayout_7"),
        (0, 1, "elastomer_products_plant_spritelayout_5"),
        (0, 2, "elastomer_products_plant_spritelayout_8"),
        (1, 0, "elastomer_products_plant_spritelayout_6"),
        (1, 1, "elastomer_products_plant_spritelayout_4"),
        (1, 2, "elastomer_products_plant_spritelayout_8"),
        (2, 1, "elastomer_products_plant_spritelayout_8"),
        (2, 2, "elastomer_products_plant_spritelayout_3"),
        (3, 1, "elastomer_products_plant_spritelayout_1"),
        (3, 2, "elastomer_products_plant_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="elastomer_products_plant_industry_layout_4",
    layout=[
        (0, 0, "elastomer_products_plant_spritelayout_7"),
        (0, 1, "elastomer_products_plant_spritelayout_5"),
        (0, 2, "elastomer_products_plant_spritelayout_7"),
        (0, 3, "elastomer_products_plant_spritelayout_5"),
        (1, 0, "elastomer_products_plant_spritelayout_6"),
        (1, 1, "elastomer_products_plant_spritelayout_4"),
        (1, 2, "elastomer_products_plant_spritelayout_6"),
        (1, 3, "elastomer_products_plant_spritelayout_4"),
        (2, 0, "elastomer_products_plant_spritelayout_8"),
        (2, 1, "elastomer_products_plant_spritelayout_8"),
        (2, 2, "elastomer_products_plant_spritelayout_3"),
        (2, 3, "elastomer_products_plant_spritelayout_8"),
        (3, 1, "elastomer_products_plant_spritelayout_1"),
        (3, 2, "elastomer_products_plant_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="elastomer_products_plant_industry_layout_5",
    layout=[
        (0, 0, "elastomer_products_plant_spritelayout_8"),
        (0, 1, "elastomer_products_plant_spritelayout_3"),
        (0, 2, "elastomer_products_plant_spritelayout_7"),
        (0, 3, "elastomer_products_plant_spritelayout_5"),
        (1, 0, "elastomer_products_plant_spritelayout_1"),
        (1, 1, "elastomer_products_plant_spritelayout_2"),
        (1, 2, "elastomer_products_plant_spritelayout_6"),
        (1, 3, "elastomer_products_plant_spritelayout_4"),
    ],
)
industry.add_industry_layout(
    id="elastomer_products_plant_industry_layout_6",
    layout=[
        (0, 0, "elastomer_products_plant_spritelayout_7"),
        (0, 1, "elastomer_products_plant_spritelayout_5"),
        (0, 2, "elastomer_products_plant_spritelayout_7"),
        (0, 3, "elastomer_products_plant_spritelayout_5"),
        (1, 0, "elastomer_products_plant_spritelayout_6"),
        (1, 1, "elastomer_products_plant_spritelayout_4"),
        (1, 2, "elastomer_products_plant_spritelayout_6"),
        (1, 3, "elastomer_products_plant_spritelayout_4"),
        (2, 0, "elastomer_products_plant_spritelayout_8"),
        (2, 1, "elastomer_products_plant_spritelayout_3"),
        (2, 2, "elastomer_products_plant_spritelayout_8"),
        (2, 3, "elastomer_products_plant_spritelayout_8"),
        (3, 0, "elastomer_products_plant_spritelayout_1"),
        (3, 1, "elastomer_products_plant_spritelayout_2"),
    ],
)
