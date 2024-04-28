from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="metal_workshop",
    accept_cargos_with_input_ratios=[
        ("STEL", 6),
        ("RFPR", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("GOOD", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="164",
    name="string(STR_IND_METAL_WORKSHOP)",
    nearby_station_name="string(STR_STATION_STAMP_AND_PLATE)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
    provides_snow=True,
    sprites_complete=True,
)

industry.enable_in_economy(
    "BASIC_TEMPERATE",
)

industry.add_tile(
    id="metal_workshop_tile_1",
    animation_length=47,
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
    sprites=[(10, 60, 64, 70, -31, -39)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 70, -31, -39)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 51, -31, -20)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 51, -31, -20)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 60, 64, 51, -31, -20)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 60, 64, 31, -31, 0)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 60, 64, 31, -31, 0)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=0,
    yoffset=8,
    zoffset=53,
)

industry.add_spritelayout(
    id="metal_workshop_spritelayout_1",
    tile="metal_workshop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="metal_workshop_spritelayout_2",
    tile="metal_workshop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="metal_workshop_spritelayout_3",
    tile="metal_workshop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="metal_workshop_spritelayout_4",
    tile="metal_workshop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="metal_workshop_spritelayout_5",
    tile="metal_workshop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="metal_workshop_spritelayout_6",
    tile="metal_workshop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="metal_workshop_spritelayout_7",
    tile="metal_workshop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)

industry.add_multi_tile_object(
    add_to_object_num=4,
    view_layout=[
        (0, 0, "metal_workshop_spritelayout_1"),
        (0, 1, "metal_workshop_spritelayout_2"),
    ],
)

industry.add_industry_layout(
    id="metal_workshop_industry_layout_1",
    layout=[
        (0, 0, "metal_workshop_spritelayout_3"),
        (0, 1, "metal_workshop_spritelayout_3"),
        (0, 2, "metal_workshop_spritelayout_5"),
        (0, 3, "metal_workshop_spritelayout_4"),
        (0, 4, "metal_workshop_spritelayout_5"),
        (1, 0, "metal_workshop_spritelayout_3"),
        (1, 1, "metal_workshop_spritelayout_3"),
        (1, 2, "metal_workshop_spritelayout_5"),
        (1, 3, "metal_workshop_spritelayout_4"),
        (1, 4, "metal_workshop_spritelayout_6"),
        (2, 0, "metal_workshop_spritelayout_3"),
        (2, 1, "metal_workshop_spritelayout_1"),
        (2, 2, "metal_workshop_spritelayout_2"),
        (2, 3, "metal_workshop_spritelayout_7"),
        (2, 4, "metal_workshop_spritelayout_7"),
    ],
)
industry.add_industry_layout(
    id="metal_workshop_industry_layout_2",
    layout=[
        (0, 2, "metal_workshop_spritelayout_3"),
        (0, 3, "metal_workshop_spritelayout_3"),
        (1, 0, "metal_workshop_spritelayout_1"),
        (1, 1, "metal_workshop_spritelayout_2"),
        (1, 2, "metal_workshop_spritelayout_3"),
        (1, 3, "metal_workshop_spritelayout_3"),
        (2, 0, "metal_workshop_spritelayout_4"),
        (2, 1, "metal_workshop_spritelayout_7"),
        (2, 2, "metal_workshop_spritelayout_6"),
        (2, 3, "metal_workshop_spritelayout_6"),
        (3, 0, "metal_workshop_spritelayout_4"),
        (3, 1, "metal_workshop_spritelayout_5"),
        (3, 2, "metal_workshop_spritelayout_4"),
        (3, 3, "metal_workshop_spritelayout_3"),
    ],
)
