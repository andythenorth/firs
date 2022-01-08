from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="polyethylene_plant",
    accept_cargos_with_input_ratios=[
        ("C2H4", 8),
    ],
    prod_cargo_types_with_output_ratios=[
        ("PLAS", 8),
    ],
    combined_cargos_boost_prod=True,
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="209",
    name="string(STR_IND_POLYETHYLENE_PLANT)",
    nearby_station_name="string(STR_STATION_MOULDINGS)",
    fund_cost_multiplier="125",
    intro_year="1900",
)

###industry.enable_in_economy("BETTER_LIVING_THROUGH_CHEMISTRY")

industry.add_tile(
    id="polyethylene_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="concrete")
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
    id="polyethylene_plant_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="polyethylene_plant_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="polyethylene_plant_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="polyethylene_plant_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="polyethylene_plant_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="polyethylene_plant_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="polyethylene_plant_spritelayout_7",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="polyethylene_plant_spritelayout_8",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="polyethylene_plant_spritelayout_9",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="polyethylene_plant_spritelayout_10",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="polyethylene_plant_industry_layout_1",
    layout=[
        (0, 0, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_2"),
        (0, 1, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_1"),
        (0, 2, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_10"),
        (1, 0, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_2"),
        (1, 1, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_1"),
        (1, 2, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_10"),
        (2, 0, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_10"),
        (2, 1, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_7"),
        (2, 2, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_9"),
        (3, 0, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_8"),
        (3, 1, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_6"),
        (3, 2, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_10"),
        (4, 0, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_5"),
        (4, 1, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_4"),
        (4, 2, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_3"),
    ],
)
industry.add_industry_layout(
    id="polyethylene_plant_industry_layout_2",
    layout=[
        (0, 0, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_8"),
        (0, 1, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_7"),
        (0, 2, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_9"),
        (1, 0, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_8"),
        (1, 1, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_6"),
        (1, 2, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_10"),
        (2, 0, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_5"),
        (2, 1, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_4"),
        (2, 2, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_3"),
        (3, 0, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_2"),
        (3, 1, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_1"),
        (3, 2, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_10"),
    ],
)
industry.add_industry_layout(
    id="polyethylene_plant_industry_layout_3",
    layout=[
        (0, 0, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_2"),
        (0, 1, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_1"),
        (0, 2, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_10"),
        (0, 3, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_7"),
        (0, 4, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_9"),
        (1, 0, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_2"),
        (1, 1, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_1"),
        (1, 2, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_8"),
        (1, 3, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_6"),
        (1, 4, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_10"),
        (2, 0, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_2"),
        (2, 1, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_1"),
        (2, 2, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_5"),
        (2, 3, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_4"),
        (2, 4, "polyethylene_plant_tile_1", "polyethylene_plant_spritelayout_3"),
    ],
)
