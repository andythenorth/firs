from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="body_plant",
    accept_cargos_with_input_ratios=[
        ("STSH", 4),
        ("COAT", 2),
        ("GLAS", 2),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("VBOD", 8),
    ],
    prob_in_game="0",  # do not build during gameplay
    prob_map_gen="5",
    map_colour="194",
    name="string(STR_IND_BODY_PLANT)",
    nearby_station_name="string(STR_STATION_HEAVY_INDUSTRY_2)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
    provides_snow=True,
)


industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="body_plant_tile_1",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)


spriteset_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 70, -31, -35)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 70, -31, -35)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 51, -31, -20)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 51, -31, -23)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 60, 64, 51, -31, -20)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 60, 64, 31, -31, 0)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-5,
    yoffset=0,
    zoffset=26,
)

industry.add_spritelayout(
    id="body_plant_spritelayout_1",
    tile="body_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="body_plant_spritelayout_2",
    tile="body_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="body_plant_spritelayout_3",
    tile="body_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="body_plant_spritelayout_4",
    tile="body_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="body_plant_spritelayout_5",
    tile="body_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="body_plant_spritelayout_6",
    tile="body_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)

industry.add_multi_tile_object(
    add_to_object_num=1,
    view_layout=[
        (0, 0, "body_plant_spritelayout_1"),
        (0, 1, "body_plant_spritelayout_2"),
    ],
)

industry.add_industry_layout(
    id="body_plant_industry_layout_1",
    layout=[
        (0, 0, "body_plant_spritelayout_3"),
        (0, 1, "body_plant_spritelayout_3"),
        (0, 2, "body_plant_spritelayout_3"),
        (0, 3, "body_plant_spritelayout_3"),
        (0, 4, "body_plant_spritelayout_6"),
        (0, 5, "body_plant_spritelayout_4"),
        (1, 0, "body_plant_spritelayout_3"),
        (1, 1, "body_plant_spritelayout_3"),
        (1, 2, "body_plant_spritelayout_3"),
        (1, 3, "body_plant_spritelayout_3"),
        (1, 4, "body_plant_spritelayout_6"),
        (1, 5, "body_plant_spritelayout_5"),
        (2, 0, "body_plant_spritelayout_3"),
        (2, 1, "body_plant_spritelayout_1"),
        (2, 2, "body_plant_spritelayout_2"),
        (2, 3, "body_plant_spritelayout_1"),
        (2, 4, "body_plant_spritelayout_2"),
        (2, 5, "body_plant_spritelayout_6"),
    ],
)
