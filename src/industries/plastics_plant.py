from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="plastics_plant",
    accept_cargos_with_input_ratios=[
        ("PLAS", 5),
        ("KAOL", 2),
        ("PRCH", 1),
    ],
    prod_cargo_types_with_output_ratios=[
        ("GOOD", 4),
        ("HWAR", 4),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="209",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    name="string(STR_IND_PLASTICS_PLANT)",
    nearby_station_name="string(STR_STATION_MOULDINGS)",
    fund_cost_multiplier="125",
    intro_year="1900",
    provides_snow=True,
    sprites_complete=False,
    animated_tiles_fixed=False,
)

industry.enable_in_economy(
    "MILD_MILD_WEST",
)

industry.add_tile(
    id="plastics_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="asphalt")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 62, -31, -31)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 62, -31, -31)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 55, -31, -24)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 55, -31, -24)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 55, -31, -24)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 87, -31, -56)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 87, -31, -56)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 87, -31, -56)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 55, -31, -24)],
)

industry.add_spritelayout(
    id="plastics_plant_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plastics_plant_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plastics_plant_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plastics_plant_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plastics_plant_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plastics_plant_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plastics_plant_spritelayout_7",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plastics_plant_spritelayout_8",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plastics_plant_spritelayout_9",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="plastics_plant_spritelayout_10",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="plastics_plant_industry_layout_1",
    layout=[
        (0, 0, "plastics_plant_tile_1", "plastics_plant_spritelayout_2"),
        (0, 1, "plastics_plant_tile_1", "plastics_plant_spritelayout_1"),
        (0, 2, "plastics_plant_tile_1", "plastics_plant_spritelayout_10"),
        (1, 0, "plastics_plant_tile_1", "plastics_plant_spritelayout_2"),
        (1, 1, "plastics_plant_tile_1", "plastics_plant_spritelayout_1"),
        (1, 2, "plastics_plant_tile_1", "plastics_plant_spritelayout_10"),
        (2, 0, "plastics_plant_tile_1", "plastics_plant_spritelayout_10"),
        (2, 1, "plastics_plant_tile_1", "plastics_plant_spritelayout_7"),
        (2, 2, "plastics_plant_tile_1", "plastics_plant_spritelayout_9"),
        (3, 0, "plastics_plant_tile_1", "plastics_plant_spritelayout_8"),
        (3, 1, "plastics_plant_tile_1", "plastics_plant_spritelayout_6"),
        (3, 2, "plastics_plant_tile_1", "plastics_plant_spritelayout_10"),
        (4, 0, "plastics_plant_tile_1", "plastics_plant_spritelayout_5"),
        (4, 1, "plastics_plant_tile_1", "plastics_plant_spritelayout_4"),
        (4, 2, "plastics_plant_tile_1", "plastics_plant_spritelayout_3"),
    ],
)
industry.add_industry_layout(
    id="plastics_plant_industry_layout_2",
    layout=[
        (0, 0, "plastics_plant_tile_1", "plastics_plant_spritelayout_8"),
        (0, 1, "plastics_plant_tile_1", "plastics_plant_spritelayout_7"),
        (0, 2, "plastics_plant_tile_1", "plastics_plant_spritelayout_9"),
        (1, 0, "plastics_plant_tile_1", "plastics_plant_spritelayout_8"),
        (1, 1, "plastics_plant_tile_1", "plastics_plant_spritelayout_6"),
        (1, 2, "plastics_plant_tile_1", "plastics_plant_spritelayout_10"),
        (2, 0, "plastics_plant_tile_1", "plastics_plant_spritelayout_5"),
        (2, 1, "plastics_plant_tile_1", "plastics_plant_spritelayout_4"),
        (2, 2, "plastics_plant_tile_1", "plastics_plant_spritelayout_3"),
        (3, 0, "plastics_plant_tile_1", "plastics_plant_spritelayout_2"),
        (3, 1, "plastics_plant_tile_1", "plastics_plant_spritelayout_1"),
        (3, 2, "plastics_plant_tile_1", "plastics_plant_spritelayout_10"),
    ],
)
industry.add_industry_layout(
    id="plastics_plant_industry_layout_3",
    layout=[
        (0, 0, "plastics_plant_tile_1", "plastics_plant_spritelayout_2"),
        (0, 1, "plastics_plant_tile_1", "plastics_plant_spritelayout_1"),
        (0, 2, "plastics_plant_tile_1", "plastics_plant_spritelayout_10"),
        (0, 3, "plastics_plant_tile_1", "plastics_plant_spritelayout_7"),
        (0, 4, "plastics_plant_tile_1", "plastics_plant_spritelayout_9"),
        (1, 0, "plastics_plant_tile_1", "plastics_plant_spritelayout_2"),
        (1, 1, "plastics_plant_tile_1", "plastics_plant_spritelayout_1"),
        (1, 2, "plastics_plant_tile_1", "plastics_plant_spritelayout_8"),
        (1, 3, "plastics_plant_tile_1", "plastics_plant_spritelayout_6"),
        (1, 4, "plastics_plant_tile_1", "plastics_plant_spritelayout_10"),
        (2, 0, "plastics_plant_tile_1", "plastics_plant_spritelayout_2"),
        (2, 1, "plastics_plant_tile_1", "plastics_plant_spritelayout_1"),
        (2, 2, "plastics_plant_tile_1", "plastics_plant_spritelayout_5"),
        (2, 3, "plastics_plant_tile_1", "plastics_plant_spritelayout_4"),
        (2, 4, "plastics_plant_tile_1", "plastics_plant_spritelayout_3"),
    ],
)
