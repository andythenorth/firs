from industry import IndustrySecondary, TileLocationChecks

# !! layout names will need set correctly
industry = IndustrySecondary(
    id="factory_2",
    accept_cargos_with_input_ratios=[
        ("COPR", 2),
        ("STEL", 2),
        ("STWR", 2),
        ("PLAS", 2),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("POWR", 8)],
    prob_in_game="7",
    prob_map_gen="8",
    map_colour="166",
    name="string(STR_IND_SOAP_FACTORY)",
    nearby_station_name="string(STR_STATION_INDUSTRY_ESTATE_1)",
    fund_cost_multiplier="95",
)

industry.economy_variations['BETTER_LIVING_THROUGH_CHEMISTRY'].enabled = True

industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations["STEELTOWN"].accept_cargos_with_input_ratios = [
    ("LYE_", 2),
    ("SASH", 2),
    ("SALT", 2),
    ("NH3_", 2),
]
industry.economy_variations["STEELTOWN"].prod_cargo_types_with_output_ratios = [
    ("SOAP", 8),
]



# tile with animation for smoke
industry.add_tile(
    id="factory_2_tile_1",
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
    type="concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 94, -31, -63)],
)

spriteset_ground_anim = industry.add_spriteset(
    type="concrete",
)
spriteset_ground_overlay_anim = industry.add_spriteset(
    type="empty",
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 94, -31, -63)],
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
spriteset_9 = industry.add_spriteset(
    sprites=[(10, 120, 64, 64, -31, -33)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(80, 120, 64, 64, -31, -33)],
)

sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=12,
    zoffset=56,
)

industry.add_spritelayout(
    id="factory_2_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_2",
    ground_sprite=spriteset_ground_anim,
    ground_overlay=spriteset_ground_overlay_anim,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_7",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    smoke_sprites=[sprite_smoke],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_8",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_9",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
)
industry.add_spritelayout(
    id="factory_2_spritelayout_10",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
)

industry.add_industry_layout(
    id="factory_2_industry_layout_1",
    layout=[
        (0, 0, "factory_2_tile_1", "factory_2_spritelayout_7"),
        (0, 1, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (0, 2, "factory_2_tile_1", "factory_2_spritelayout_7"),
        (0, 3, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (1, 0, "factory_2_tile_1", "factory_2_spritelayout_6"),
        (1, 1, "factory_2_tile_1", "factory_2_spritelayout_4"),
        (1, 2, "factory_2_tile_1", "factory_2_spritelayout_6"),
        (1, 3, "factory_2_tile_1", "factory_2_spritelayout_4"),
        (2, 0, "factory_2_tile_1", "factory_2_spritelayout_8"),
        (2, 1, "factory_2_tile_1", "factory_2_spritelayout_3"),
        (2, 2, "factory_2_tile_1", "factory_2_spritelayout_9"),
        (2, 3, "factory_2_tile_1", "factory_2_spritelayout_10"),
        (3, 0, "factory_2_tile_1", "factory_2_spritelayout_1"),
        (3, 1, "factory_2_tile_1", "factory_2_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="factory_2_industry_layout_2",
    layout=[
        (0, 1, "factory_2_tile_1", "factory_2_spritelayout_7"),
        (0, 2, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (1, 1, "factory_2_tile_1", "factory_2_spritelayout_6"),
        (1, 2, "factory_2_tile_1", "factory_2_spritelayout_4"),
        (2, 0, "factory_2_tile_1", "factory_2_spritelayout_8"),
        (2, 1, "factory_2_tile_1", "factory_2_spritelayout_3"),
        (2, 2, "factory_2_tile_1", "factory_2_spritelayout_9"),
        (3, 0, "factory_2_tile_1", "factory_2_spritelayout_1"),
        (3, 1, "factory_2_tile_1", "factory_2_spritelayout_2"),
        (3, 2, "factory_2_tile_1", "factory_2_spritelayout_10"),
    ],
)
industry.add_industry_layout(
    id="factory_2_industry_layout_3",
    layout=[
        (0, 0, "factory_2_tile_1", "factory_2_spritelayout_7"),
        (0, 1, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (0, 2, "factory_2_tile_1", "factory_2_spritelayout_9"),
        (1, 0, "factory_2_tile_1", "factory_2_spritelayout_6"),
        (1, 1, "factory_2_tile_1", "factory_2_spritelayout_4"),
        (1, 2, "factory_2_tile_1", "factory_2_spritelayout_8"),
        (2, 0, "factory_2_tile_1", "factory_2_spritelayout_10"),
        (2, 1, "factory_2_tile_1", "factory_2_spritelayout_8"),
        (2, 2, "factory_2_tile_1", "factory_2_spritelayout_3"),
        (3, 1, "factory_2_tile_1", "factory_2_spritelayout_1"),
        (3, 2, "factory_2_tile_1", "factory_2_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="factory_2_industry_layout_4",
    layout=[
        (0, 0, "factory_2_tile_1", "factory_2_spritelayout_7"),
        (0, 1, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (0, 2, "factory_2_tile_1", "factory_2_spritelayout_7"),
        (0, 3, "factory_2_tile_1", "factory_2_spritelayout_5"),
        (1, 0, "factory_2_tile_1", "factory_2_spritelayout_6"),
        (1, 1, "factory_2_tile_1", "factory_2_spritelayout_4"),
        (1, 2, "factory_2_tile_1", "factory_2_spritelayout_6"),
        (1, 3, "factory_2_tile_1", "factory_2_spritelayout_4"),
        (2, 0, "factory_2_tile_1", "factory_2_spritelayout_9"),
        (2, 1, "factory_2_tile_1", "factory_2_spritelayout_8"),
        (2, 2, "factory_2_tile_1", "factory_2_spritelayout_3"),
        (2, 3, "factory_2_tile_1", "factory_2_spritelayout_10"),
        (3, 1, "factory_2_tile_1", "factory_2_spritelayout_1"),
        (3, 2, "factory_2_tile_1", "factory_2_spritelayout_2"),
    ],
)
