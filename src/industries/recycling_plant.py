from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="recycling_plant",
    accept_cargos_with_input_ratios=[
        ("RCYC", 6),
    ],
    prod_cargo_types_with_output_ratios=[
        ("SCMT", 4),
        ("MNSP", 4),
    ],
    prob_in_game="7",
    prob_map_gen="7",
    map_colour="164",
    name="string(STR_IND_RECYCLING_PLANT)",
    nearby_station_name="string(STR_STATION_INDUSTRY_ESTATE_1)",
    fund_cost_multiplier="118",
    intro_year=1978,
    provides_snow=True,
)


industry.add_tile(
    id="recycling_plant_tile_1",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="dirty_concrete")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 76, -31, -45)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 76, -31, -45)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 63, -31, -32)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 63, -31, -32)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 63, -31, -32)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 63, -31, -32)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-5,
    yoffset=0,
    zoffset=40,
    animation_frame_offset=8,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-5,
    yoffset=5,
    zoffset=40,
)

industry.add_spritelayout(
    id="recycling_plant_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="recycling_plant_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="recycling_plant_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="recycling_plant_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="recycling_plant_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="recycling_plant_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="recycling_plant_industry_layout_1",
    layout=[
        (0, 0, "recycling_plant_tile_1", "recycling_plant_spritelayout_2"),
        (0, 1, "recycling_plant_tile_1", "recycling_plant_spritelayout_3"),
        (1, 0, "recycling_plant_tile_1", "recycling_plant_spritelayout_1"),
        (1, 1, "recycling_plant_tile_1", "recycling_plant_spritelayout_4"),
        (2, 0, "recycling_plant_tile_1", "recycling_plant_spritelayout_5"),
        (2, 1, "recycling_plant_tile_1", "recycling_plant_spritelayout_6"),
    ],
)

industry.add_industry_layout(
    id="recycling_plant_industry_layout_2",
    layout=[
        (0, 0, "recycling_plant_tile_1", "recycling_plant_spritelayout_2"),
        (0, 1, "recycling_plant_tile_1", "recycling_plant_spritelayout_3"),
        (0, 2, "recycling_plant_tile_1", "recycling_plant_spritelayout_5"),
        (1, 0, "recycling_plant_tile_1", "recycling_plant_spritelayout_1"),
        (1, 1, "recycling_plant_tile_1", "recycling_plant_spritelayout_4"),
        (1, 2, "recycling_plant_tile_1", "recycling_plant_spritelayout_6"),
    ],
)

industry.add_industry_layout(
    id="recycling_plant_industry_layout_3",
    layout=[
        (0, 0, "recycling_plant_tile_1", "recycling_plant_spritelayout_5"),
        (0, 1, "recycling_plant_tile_1", "recycling_plant_spritelayout_3"),
        (0, 2, "recycling_plant_tile_1", "recycling_plant_spritelayout_2"),
        (1, 0, "recycling_plant_tile_1", "recycling_plant_spritelayout_6"),
        (1, 1, "recycling_plant_tile_1", "recycling_plant_spritelayout_4"),
        (1, 2, "recycling_plant_tile_1", "recycling_plant_spritelayout_1"),
    ],
)
