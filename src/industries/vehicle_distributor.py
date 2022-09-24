from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="vehicle_distributor",
    accept_cargo_types=[
        "VEHI",
    ],
    prod_cargo_types_with_multipliers=[],
    prob_in_game="3",
    prob_map_gen="10",
    map_colour="207",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    location_checks=dict(
        same_type_distance=32,
    ),
    prospect_chance="0.75",
    name="string(STR_IND_VEHICLE_DISTRIBUTOR)",
    nearby_station_name="string(STR_STATION_VEHICLE_DISTRIBUTOR)",
    fund_cost_multiplier="8",
    provides_snow=True,
)

industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="vehicle_distributor_tile_1",
    location_checks=TileLocationChecks(
        # require_road_adjacent=True,
        require_houses_nearby=True,
        require_effectively_flat=True,
    ),
)

spriteset_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(sprites=[(10, 60, 64, 59, -31, -28)])
spriteset_2 = industry.add_spriteset(sprites=[(80, 60, 64, 59, -31, -28)])

industry.add_spritelayout(
    id="vehicle_distributor_spritelayout_1",
    tile="vehicle_distributor_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="vehicle_distributor_spritelayout_2",
    tile="vehicle_distributor_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="vehicle_distributor_industry_layout_1",
    layout=[
        (0, 0, "vehicle_distributor_spritelayout_1"),
        (0, 1, "vehicle_distributor_spritelayout_2"),
        (0, 2, "vehicle_distributor_spritelayout_2"),
        (1, 0, "vehicle_distributor_spritelayout_1"),
        (1, 1, "vehicle_distributor_spritelayout_2"),
        (1, 2, "vehicle_distributor_spritelayout_2"),
        (2, 0, "vehicle_distributor_spritelayout_1"),
        (2, 1, "vehicle_distributor_spritelayout_2"),
        (2, 2, "vehicle_distributor_spritelayout_2"),
        (3, 0, "vehicle_distributor_spritelayout_2"),
        (3, 1, "vehicle_distributor_spritelayout_2"),
        (3, 2, "vehicle_distributor_spritelayout_2"),
    ],
)
