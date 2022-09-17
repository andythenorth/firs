from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="furniture_factory",
    accept_cargos_with_input_ratios=[
        ("WDPR", 6),
        ("COAT", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("FURN", 8),
    ],
    prob_in_game="7",
    prob_map_gen="8",
    map_colour="186",
    name="string(STR_IND_FURNITURE_FACTORY)",
    nearby_station_name="string(STR_STATION_JOINERS_SHOP)",
    fund_cost_multiplier="95",
    provides_snow=True,
)


industry.add_tile(
    id="furniture_factory_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)


spriteset_ground = industry.add_spriteset(
    type="cobble",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 88, -31, -42)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 88, -31, -44)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 88, -31, -42)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 88, -31, -42)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 60, 64, 88, -31, -42)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 60, 64, 88, -31, -41)],
)

industry.add_spritelayout(
    id="furniture_factory_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="furniture_factory_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="furniture_factory_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="furniture_factory_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="furniture_factory_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="furniture_factory_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="furniture_factory_industry_layout_1",
    layout=[
        (0, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_3"),
        (1, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_5"),
        (1, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_2"),
        (2, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_4"),
        (2, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="furniture_factory_industry_layout_2",
    layout=[
        (0, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_5"),
        (0, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_3"),
        (1, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_4"),
        (1, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_2"),
        (2, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_6"),
        (2, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="furniture_factory_industry_layout_3",
    layout=[
        (0, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_3"),
        (0, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_6"),
        (1, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_2"),
        (1, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_3"),
        (2, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_1"),
        (2, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_2"),
        (3, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_5"),
        (3, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_1"),
        (4, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_4"),
        (4, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_6"),
    ],
)
industry.add_industry_layout(
    id="furniture_factory_industry_layout_4",
    layout=[
        (0, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_5"),
        (0, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_6"),
        (1, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_4"),
        (1, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_6"),
        (2, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_3"),
        (2, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_3"),
        (3, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_2"),
        (3, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_2"),
        (4, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_1"),
        (4, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="furniture_factory_industry_layout_5",
    layout=[
        (0, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_5"),
        (0, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_3"),
        (0, 2, "furniture_factory_tile_1", "furniture_factory_spritelayout_3"),
        (1, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_4"),
        (1, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_2"),
        (1, 2, "furniture_factory_tile_1", "furniture_factory_spritelayout_2"),
        (2, 0, "furniture_factory_tile_1", "furniture_factory_spritelayout_6"),
        (2, 1, "furniture_factory_tile_1", "furniture_factory_spritelayout_1"),
        (2, 2, "furniture_factory_tile_1", "furniture_factory_spritelayout_1"),
    ],
)
