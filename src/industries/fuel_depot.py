from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="fuel_depot",
    accept_cargo_types=[
        "PETR",
    ],
    prob_in_game="3",
    prob_map_gen="6",
    map_colour="186",
    special_flags=["IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE"],
    name="string(STR_IND_FUEL_DEPOT)",
    nearby_station_name="string(STR_STATION_FUEL_DEPOT)",
    intro_year=1930,
    fund_cost_multiplier="4"
)

industry.enable_in_economy(
    "PLAINS_TRAINS_AND_STEEL",
)

industry.add_tile(
    id="fuel_depot_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
spriteset_ground = industry.add_spriteset(
    type="concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 66, -31, -38)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 66, -31, -38)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 66, -31, -38)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 66, -31, -38)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 66, -31, -38)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 66, -31, -38)],
)

industry.add_spritelayout(
    id="fuel_depot_spritelayout_empty",
    tile="fuel_depot_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fuel_depot_spritelayout_1",
    tile="fuel_depot_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fuel_depot_spritelayout_2",
    tile="fuel_depot_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fuel_depot_spritelayout_3",
    tile="fuel_depot_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fuel_depot_spritelayout_4",
    tile="fuel_depot_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fuel_depot_spritelayout_5",
    tile="fuel_depot_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fuel_depot_spritelayout_6",
    tile="fuel_depot_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_industry_layout(
    id="fuel_depot_industry_layout_1",
    layout=[
        (0, 0, "fuel_depot_spritelayout_2"),
        (0, 1, "fuel_depot_spritelayout_2"),
        (1, 0, "fuel_depot_spritelayout_3"),
        (1, 1, "fuel_depot_spritelayout_6"),
    ],
)
industry.add_industry_layout(
    id="fuel_depot_industry_layout_2",
    layout=[
        (0, 0, "fuel_depot_spritelayout_2"),
        (0, 1, "fuel_depot_spritelayout_5"),
        (1, 1, "fuel_depot_spritelayout_3"),
    ],
)
industry.add_industry_layout(
    id="fuel_depot_industry_layout_3",
    layout=[
        (0, 0, "fuel_depot_spritelayout_1"),
        (0, 1, "fuel_depot_spritelayout_5"),
        (0, 2, "fuel_depot_spritelayout_3"),
    ],
)
industry.add_industry_layout(
    id="fuel_depot_industry_layout_4",
    layout=[
        (0, 0, "fuel_depot_spritelayout_1"),
        (1, 0, "fuel_depot_spritelayout_2"),
        (2, 0, "fuel_depot_spritelayout_4"),
    ],
)

