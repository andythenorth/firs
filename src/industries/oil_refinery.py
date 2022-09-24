from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="oil_refinery",
    accept_cargos_with_input_ratios=[
        ("OIL_", 8),
    ],
    prod_cargo_types_with_output_ratios=[
        ("PETR", 3),
        ("NAPH", 3),
        ("BITU", 2),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="191",
    special_flags=["IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE"],
    fund_cost_multiplier="200",
    name="TTD_STR_INDUSTRY_NAME_OIL_REFINERY",
    nearby_station_name="string(STR_STATION_REFINERY)",
)

industry.add_tile(
    id="oil_refinery_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 66, -31, -35)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 128, -31, -96)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 128, -31, -96)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 128, -31, -96)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 66, -31, -35)],
)

industry.add_spritelayout(
    id="oil_refinery_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="oil_refinery_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="oil_refinery_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="oil_refinery_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="oil_refinery_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="oil_refinery_industry_layout_1",
    layout=[
        (0, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (0, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (0, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (0, 3, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (0, 4, "oil_refinery_tile_1", "oil_refinery_spritelayout_2"),
        (1, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (1, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (1, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_4"),
        (1, 3, "oil_refinery_tile_1", "oil_refinery_spritelayout_2"),
        (1, 4, "oil_refinery_tile_1", "oil_refinery_spritelayout_5"),
        (2, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (2, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (2, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_4"),
        (2, 3, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (2, 4, "oil_refinery_tile_1", "oil_refinery_spritelayout_5"),
    ],
)
industry.add_industry_layout(
    id="oil_refinery_industry_layout_2",
    layout=[
        (0, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_2"),
        (0, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (0, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (0, 3, "oil_refinery_tile_1", "oil_refinery_spritelayout_4"),
        (1, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_2"),
        (1, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_4"),
        (1, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (1, 3, "oil_refinery_tile_1", "oil_refinery_spritelayout_2"),
        (2, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_5"),
        (2, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (2, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (2, 3, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (3, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_5"),
        (3, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (3, 3, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="oil_refinery_industry_layout_3",
    layout=[
        (0, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_2"),
        (0, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (0, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (0, 3, "oil_refinery_tile_1", "oil_refinery_spritelayout_4"),
        (0, 4, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (0, 5, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (1, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (1, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_4"),
        (1, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (1, 3, "oil_refinery_tile_1", "oil_refinery_spritelayout_2"),
        (1, 4, "oil_refinery_tile_1", "oil_refinery_spritelayout_5"),
        (1, 5, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (2, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_4"),
        (2, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (2, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (2, 3, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (2, 4, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (2, 5, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (3, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_5"),
        (3, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (3, 3, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (3, 4, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (3, 5, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="oil_refinery_industry_layout_4",
    layout=[
        (0, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (0, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (0, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (1, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (1, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (1, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (2, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (2, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (2, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (3, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_4"),
        (3, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_1"),
        (3, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_5"),
        (4, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_4"),
        (4, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (4, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_5"),
        (5, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_2"),
        (5, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (5, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_4"),
        (6, 0, "oil_refinery_tile_1", "oil_refinery_spritelayout_5"),
        (6, 1, "oil_refinery_tile_1", "oil_refinery_spritelayout_3"),
        (6, 2, "oil_refinery_tile_1", "oil_refinery_spritelayout_2"),
    ],
)
