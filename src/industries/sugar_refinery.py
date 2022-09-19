from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="sugar_refinery",
    accept_cargos_with_input_ratios=[
        ("MNSP", 3),
        ("SGBT", 5),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("FOOD", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="83",
    special_flags=["IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE"],
    name="string(STR_IND_SUGAR_REFINERY)",
    nearby_station_name="string(STR_STATION_SUGAR_COMPANY)",
    fund_cost_multiplier="140",
    provides_snow=True,
)

industry.add_tile(
    id="sugar_refinery_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="dirty_concrete")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 50, -31, -23)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 50, -31, -25)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 88, -31, -56)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 88, -31, -58)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 88, -31, -58)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 88, -31, -58)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 88, -31, -58)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 88, -31, -58)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=5,
    yoffset=8,
    zoffset=72,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=5,
    yoffset=12,
    zoffset=72,
    animation_frame_offset=1,
)

industry.add_spritelayout(
    id="sugar_refinery_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sugar_refinery_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sugar_refinery_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sugar_refinery_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sugar_refinery_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["se"],
)
industry.add_spritelayout(
    id="sugar_refinery_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sugar_refinery_spritelayout_7",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=[],
)
industry.add_spritelayout(
    id="sugar_refinery_spritelayout_8",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sugar_refinery_spritelayout_9",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="sugar_refinery_industry_layout_1",
    layout=[
        (0, 0, "sugar_refinery_tile_1", "sugar_refinery_spritelayout_4"),
        (0, 1, "sugar_refinery_tile_1", "sugar_refinery_spritelayout_4"),
        (0, 2, "sugar_refinery_tile_1", "sugar_refinery_spritelayout_4"),
        (1, 0, "sugar_refinery_tile_1", "sugar_refinery_spritelayout_8"),
        (1, 1, "sugar_refinery_tile_1", "sugar_refinery_spritelayout_3"),
        (1, 2, "sugar_refinery_tile_1", "sugar_refinery_spritelayout_1"),
        (2, 0, "sugar_refinery_tile_1", "sugar_refinery_spritelayout_6"),
        (2, 1, "sugar_refinery_tile_1", "sugar_refinery_spritelayout_9"),
        (2, 2, "sugar_refinery_tile_1", "sugar_refinery_spritelayout_2"),
        (3, 0, "sugar_refinery_tile_1", "sugar_refinery_spritelayout_7"),
        (3, 1, "sugar_refinery_tile_1", "sugar_refinery_spritelayout_7"),
        (3, 2, "sugar_refinery_tile_1", "sugar_refinery_spritelayout_5"),
    ],
)
