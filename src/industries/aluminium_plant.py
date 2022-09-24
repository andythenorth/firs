from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="aluminium_plant",
    accept_cargos_with_input_ratios=[
        ("ALO_", 8),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("ALUM", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="19",
    name="string(STR_IND_ALUMINIUM_PLANT)",
    nearby_station_name="string(STR_STATION_SMELTER)",
    fund_cost_multiplier="200",
    provides_snow=True,
)

# industry.enable_in_economy("MILD_MILD_WEST",)

industry.add_tile(
    id="aluminium_plant_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 57, -31, -26)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 66, -31, -26)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 92, -31, -61)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 90, -31, -61)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 100, -31, -61)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 100, -31, -61)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 56, -31, -26)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 56, -31, -26)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 110, -31, -61)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(640, 10, 64, 110, -31, -61)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(710, 10, 64, 110, -31, -61)],
)
sprite_transformer = industry.add_sprite(
    sprite_number=2054,
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=5,
    yoffset=0,
    zoffset=64,
)

industry.add_spritelayout(
    id="aluminium_plant_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="aluminium_plant_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="aluminium_plant_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="aluminium_plant_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="aluminium_plant_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="aluminium_plant_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="aluminium_plant_spritelayout_7",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="aluminium_plant_spritelayout_8",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="aluminium_plant_spritelayout_9",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="aluminium_plant_spritelayout_10",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="aluminium_plant_spritelayout_11",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_11],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="aluminium_plant_spritelayout_concrete",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="aluminium_plant_spritelayout_transformer",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_transformer],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="aluminium_plant_industry_layout_1",
    layout=[
        (0, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_transformer"),
        (0, 2, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_concrete"),
        (0, 3, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_11"),
        (1, 2, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_9"),
        (1, 3, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_10"),
        (2, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_3"),
        (2, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (2, 2, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_5"),
        (2, 3, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_6"),
        (3, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_4"),
        (3, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (3, 2, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_concrete"),
        (3, 3, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_8"),
        (4, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (4, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (4, 2, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (4, 3, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_2"),
        (5, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (5, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (5, 2, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (5, 3, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_7"),
    ],
)
industry.add_industry_layout(
    id="aluminium_plant_industry_layout_2",
    layout=[
        (0, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (0, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_concrete"),
        (0, 2, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (0, 3, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_concrete"),
        (0, 4, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_11"),
        (1, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (1, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_4"),
        (1, 2, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (1, 3, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_9"),
        (1, 4, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_10"),
        (2, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (2, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_3"),
        (2, 2, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (2, 3, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_5"),
        (2, 4, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_6"),
        (3, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (3, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_concrete"),
        (3, 2, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (3, 3, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_8"),
        (3, 4, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_concrete"),
        (4, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (4, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_transformer"),
        (4, 2, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (4, 3, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_2"),
        (4, 4, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_7"),
    ],
)
industry.add_industry_layout(
    id="aluminium_plant_industry_layout_3",
    layout=[
        (0, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_transformer"),
        (1, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_3"),
        (1, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_2"),
        (2, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_4"),
        (2, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_8"),
        (3, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (3, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (4, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (4, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (5, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (5, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_1"),
        (6, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_7"),
        (6, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_7"),
        (7, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_9"),
        (7, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_11"),
        (8, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_9"),
        (8, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_10"),
        (9, 0, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_5"),
        (9, 1, "aluminium_plant_tile_1", "aluminium_plant_spritelayout_6"),
    ],
)
