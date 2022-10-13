from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="construction_plant",
    accept_cargos_with_input_ratios=[
        ("CMNT", 2),
        ("STSE", 2),
        ("STWR", 2),
        ("GLAS", 2),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("GOOD", 8)],
    prob_in_game="7",
    prob_map_gen="8",
    map_colour="166",
    name="string(STR_IND_CONSTRUCTION_PLANT)",
    nearby_station_name="string(STR_STATION_MERCHANTS_LANE)",
    fund_cost_multiplier="95",
)

industry.economy_variations['BETTER_LIVING_THROUGH_CHEMISTRY'].enabled = True

industry.economy_variations["STEELTOWN"].enabled = True


industry.add_tile(
    id="construction_plant_tile_1",
    location_checks=TileLocationChecks(
        require_houses_nearby=True,
        require_effectively_flat=True,
        disallow_industry_adjacent=True,
    ),
)

spriteset_ground = industry.add_spriteset(
    type="concrete",
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
    id="construction_plant_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[stacks_1],
)
industry.add_spritelayout(
    id="construction_plant_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[shed],
)
industry.add_spritelayout(
    id="construction_plant_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[silo],
)
industry.add_spritelayout(
    id="construction_plant_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[stacks_2],
)

industry.add_industry_layout(
    id="construction_plant_industry_layout_1",
    layout=[
        (0, 0, "construction_plant_tile_1", "construction_plant_spritelayout_3"),
        (0, 1, "construction_plant_tile_1", "construction_plant_spritelayout_4"),
        (1, 0, "construction_plant_tile_1", "construction_plant_spritelayout_2"),
        (1, 1, "construction_plant_tile_1", "construction_plant_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="construction_plant_industry_layout_2",
    layout=[
        (0, 0, "construction_plant_tile_1", "construction_plant_spritelayout_2"),
        (0, 1, "construction_plant_tile_1", "construction_plant_spritelayout_3"),
        (1, 0, "construction_plant_tile_1", "construction_plant_spritelayout_4"),
        (1, 1, "construction_plant_tile_1", "construction_plant_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="construction_plant_industry_layout_3",
    layout=[
        (0, 0, "construction_plant_tile_1", "construction_plant_spritelayout_3"),
        (0, 1, "construction_plant_tile_1", "construction_plant_spritelayout_2"),
        (1, 0, "construction_plant_tile_1", "construction_plant_spritelayout_1"),
        (1, 1, "construction_plant_tile_1", "construction_plant_spritelayout_4"),
    ],
)
industry.add_industry_layout(
    id="construction_plant_industry_layout_4",
    layout=[
        (0, 0, "construction_plant_tile_1", "construction_plant_spritelayout_2"),
        (0, 1, "construction_plant_tile_1", "construction_plant_spritelayout_1"),
        (1, 0, "construction_plant_tile_1", "construction_plant_spritelayout_3"),
        (1, 1, "construction_plant_tile_1", "construction_plant_spritelayout_4"),
    ],
)
