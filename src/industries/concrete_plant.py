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
    nearby_station_name="string(STR_STATION_CONCRETE_PLANT)",
    fund_cost_multiplier="80",
    sprites_complete=True, # done enough for v5
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
shed_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 56, -31, -26)],
)
overhead_crane_1 = industry.add_spriteset(
    sprites=[(80, 10, 64, 56, -31, -26)],
)
conveyor_1 = industry.add_spriteset(
    sprites=[(150, 10, 64, 56, -31, -26)],
)
silo_1 = industry.add_spriteset(
    sprites=[(220, 10, 64, 56, -31, -31)],
)
aggregates = industry.add_spriteset(
    sprites=[(290, 10, 64, 31, -31, 0)],
)
rebar = industry.add_spriteset(
    sprites=[(360, 10, 64, 31, -31, 0)],
)
blocks_1 = industry.add_spriteset(
    sprites=[(10, 80, 64, 56, -31, -31)],
)
blocks_2 = industry.add_spriteset(
    sprites=[(80, 80, 64, 56, -31, -31)],
)
overhead_crane_2_rear = industry.add_spriteset(
    sprites=[(150, 80, 64, 56, -31, -31)],
)
overhead_crane_2_front = industry.add_spriteset(
    sprites=[(220, 80, 64, 56, -31, -31)],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_shed_1",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[shed_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_overhead_crane_1",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[overhead_crane_1],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_conveyor_1",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[conveyor_1],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_silo_1",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[silo_1],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_aggregates",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[aggregates],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_rebar",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[rebar],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_blocks_1",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[blocks_1],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_blocks_2",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[blocks_2],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_overhead_crane_2",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[overhead_crane_2_rear, blocks_2, overhead_crane_2_front],
)

# relatively large IRL, and these are probably regional, not town-local
industry.add_industry_layout(
    id="concrete_plant_industry_layout_1",
    layout=[
        (0, 0, "concrete_plant_spritelayout_blocks_1"),
        (0, 1, "concrete_plant_spritelayout_blocks_1"),
        (0, 2, "concrete_plant_spritelayout_blocks_1"),
        (1, 0, "concrete_plant_spritelayout_rebar"),
        (1, 1, "concrete_plant_spritelayout_overhead_crane_1"),
        (1, 2, "concrete_plant_spritelayout_blocks_2"),
        (2, 0, "concrete_plant_spritelayout_silo_1"),
        (2, 1, "concrete_plant_spritelayout_shed_1"),
        (2, 2, "concrete_plant_spritelayout_blocks_2"),
        (3, 0, "concrete_plant_spritelayout_conveyor_1"),
        (3, 1, "concrete_plant_spritelayout_shed_1"),
        (3, 2, "concrete_plant_spritelayout_overhead_crane_2"),
        (4, 0, "concrete_plant_spritelayout_aggregates"),
        (4, 1, "concrete_plant_spritelayout_blocks_1"),
        (4, 2, "concrete_plant_spritelayout_blocks_1"),
    ],
)
