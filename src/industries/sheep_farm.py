from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(
    id="sheep_farm",
    prod_cargo_types_with_multipliers=[
        ("LVST", 12),
    ],
    prob_in_game="4",
    prob_map_gen="11",
    map_colour="168",
    location_checks=dict(require_cluster=[72, 4]),
    prospect_chance="0.75",
    name="string(STR_IND_SHEEPFARM)",
    nearby_station_name="string(STR_STATION_SHEEP_FOLD)",
    fund_cost_multiplier="45",
    provides_snow=True,
)

industry.add_tile(
    id="sheep_farm_tile_1",
    location_checks=TileLocationChecks(
        disallow_coast=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="empty")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 52, -31, -21)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 52, -31, -19)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 52, -31, -21)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 52, -31, -21)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 52, -31, -21)],
)

industry.add_spritelayout(
    id="sheep_farm_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="sheep_farm_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="sheep_farm_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="sheep_farm_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="sheep_farm_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    terrain_aware_ground=True,
)

industry.add_industry_layout(
    id="sheep_farm_industry_layout_1",
    layout=[
        (0, 0, "sheep_farm_tile_1", "sheep_farm_spritelayout_3"),
        (1, 0, "sheep_farm_tile_1", "sheep_farm_spritelayout_2"),
        (1, 2, "sheep_farm_tile_1", "sheep_farm_spritelayout_4"),
        (3, 0, "sheep_farm_tile_1", "sheep_farm_spritelayout_1"),
        (3, 1, "sheep_farm_tile_1", "sheep_farm_spritelayout_5"),
    ],
)
industry.add_industry_layout(
    id="sheep_farm_industry_layout_2",
    layout=[
        (0, 0, "sheep_farm_tile_1", "sheep_farm_spritelayout_2"),
        (0, 1, "sheep_farm_tile_1", "sheep_farm_spritelayout_1"),
        (0, 2, "sheep_farm_tile_1", "sheep_farm_spritelayout_4"),
        (2, 0, "sheep_farm_tile_1", "sheep_farm_spritelayout_3"),
        (2, 2, "sheep_farm_tile_1", "sheep_farm_spritelayout_5"),
    ],
)
