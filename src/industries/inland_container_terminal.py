from industry import IndustryPrimaryPort, TileLocationChecks

industry = IndustryPrimaryPort(
    id="inland_container_terminal",
    accept_cargo_types=[],
    prod_cargo_types_with_multipliers=[],
    prob_in_game="2",
    prob_map_gen="8",
    map_colour="43",
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_INLAND_CONTAINER_TERMINAL)",
    nearby_station_name="string(STR_STATION_INLAND_CONTAINER_TERMINAL)",
    fund_cost_multiplier="152",
)

industry.enable_in_economy(
    "PLAINS_TRAINS_AND_STEEL",
    prod_cargo_types_with_multipliers=[
        ("GOOD", 20)
    ],
    accept_cargo_types=["GOOD"],    
    fund_cost_multiplier="18",
    intro_year=1965,
    
)

industry.add_tile(
    id="inland_container_terminal_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True,
        disallow_coast=True,
    ),
)

spriteset_ground = industry.add_spriteset(
    type="slab",
)

spriteset_ground_overlay = industry.add_spriteset(type="empty")

spriteset_1 = industry.add_spriteset(sprites=[(10, 10, 64, 79, -31, -48)])
industry.add_spritelayout(
    id="inland_container_terminal_spritelayout_1",
    tile="inland_container_terminal_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)

spriteset_2 = industry.add_spriteset(sprites=[(80, 10, 64, 79, -31, -48)])
industry.add_spritelayout(
    id="inland_container_terminal_spritelayout_2",
    tile="inland_container_terminal_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)

spriteset_3 = industry.add_spriteset(sprites=[(150, 10, 64, 79, -31, -48)])
industry.add_spritelayout(
    id="inland_container_terminal_spritelayout_3",
    tile="inland_container_terminal_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)

spriteset_4 = industry.add_spriteset(sprites=[(220, 10, 64, 79, -31, -48)])
industry.add_spritelayout(
    id="inland_container_terminal_spritelayout_4",
    tile="inland_container_terminal_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)

spriteset_5 = industry.add_spriteset(sprites=[(290, 10, 64, 79, -31, -48)])
industry.add_spritelayout(
    id="inland_container_terminal_spritelayout_5",
    tile="inland_container_terminal_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)

spriteset_6 = industry.add_spriteset(sprites=[(360, 10, 64, 79, -31, -48)])
industry.add_spritelayout(
    id="inland_container_terminal_spritelayout_6",
    tile="inland_container_terminal_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="inland_container_terminal_industry_layout",
    layout=[
        (0, 0, "inland_container_terminal_spritelayout_1"),
        (1, 0, "inland_container_terminal_spritelayout_2"),
        (2, 0, "inland_container_terminal_spritelayout_4"),
        (0, 1, "inland_container_terminal_spritelayout_5"),
        (1, 1, "inland_container_terminal_spritelayout_3"),
        (2, 1, "inland_container_terminal_spritelayout_6"),
        ],
)