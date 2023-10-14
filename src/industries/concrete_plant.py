from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="concrete_plant",
    accept_cargos_with_input_ratios=[
        ("CMNT", 3),
        ("GRVL", 3),
        ("RBAR", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("CCPR", 7),
        ("ENSP", 1),  # small ENSP output
    ],
    prob_in_game="6",
    prob_map_gen="9",
    prod_multiplier="[0, 0]",
    map_colour="10",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    name="string(STR_IND_CONCRETE_PLANT)",
    nearby_station_name="string(STR_STATION_MERCHANTS_LANE)",
    fund_cost_multiplier="80",
)


industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="concrete_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True,
        disallow_industry_adjacent=True,
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
stacks_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 56, -31, -26)],
)
shed = industry.add_spriteset(
    sprites=[(80, 10, 64, 56, -31, -26)],
)
silo = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -34)],
)
stacks_2 = industry.add_spriteset(
    sprites=[(150, 10, 64, 56, -31, -26)],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_1",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[stacks_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_2",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[shed],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_3",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[silo],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_4",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[stacks_2],
)

# relatively large IRL, and these are probably regional, not town-local
industry.add_industry_layout(
    id="concrete_plant_industry_layout_1",
    layout=[
        (0, 0, "concrete_plant_spritelayout_4"),
        (0, 1, "concrete_plant_spritelayout_1"),
        (0, 2, "concrete_plant_spritelayout_4"),
        (1, 0, "concrete_plant_spritelayout_3"),
        (1, 1, "concrete_plant_spritelayout_2"),
        (1, 2, "concrete_plant_spritelayout_1"),
        (2, 0, "concrete_plant_spritelayout_1"),
        (2, 1, "concrete_plant_spritelayout_3"),
        (2, 2, "concrete_plant_spritelayout_3"),
        (3, 0, "concrete_plant_spritelayout_2"),
        (3, 1, "concrete_plant_spritelayout_4"),
        (3, 2, "concrete_plant_spritelayout_2"),
        (4, 0, "concrete_plant_spritelayout_2"),
        (4, 1, "concrete_plant_spritelayout_4"),
        (4, 2, "concrete_plant_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="concrete_plant_industry_layout_2",
    layout=[
        (0, 0, "concrete_plant_spritelayout_1"),
        (0, 1, "concrete_plant_spritelayout_3"),
        (0, 2, "concrete_plant_spritelayout_1"),
        (0, 3, "concrete_plant_spritelayout_4"),
        (0, 4, "concrete_plant_spritelayout_4"),
        (1, 0, "concrete_plant_spritelayout_2"),
        (1, 1, "concrete_plant_spritelayout_4"),
        (1, 2, "concrete_plant_spritelayout_2"),
        (1, 3, "concrete_plant_spritelayout_3"),
        (1, 4, "concrete_plant_spritelayout_3"),
        (2, 0, "concrete_plant_spritelayout_2"),
        (2, 1, "concrete_plant_spritelayout_4"),
        (2, 2, "concrete_plant_spritelayout_2"),
        (2, 3, "concrete_plant_spritelayout_3"),
        (2, 4, "concrete_plant_spritelayout_3"),
    ],
)
