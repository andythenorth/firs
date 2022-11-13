from industry import IndustryPrimaryAgricultural, TileLocationChecks

industry = IndustryPrimaryAgricultural(
    id="grain_elevator",
    prod_cargo_types_with_multipliers=[("GRAI", 10)],
    prob_in_game="3",
    prob_map_gen="8",
    map_colour="189",
    
    # basic grain_elevator doesn't cluster, by design - no industry location checks needed
    prospect_chance="0.75",
    name="string(STR_IND_GRAIN_ELEVATOR)",
    extra_text_fund="string(STR_FUND_ELEVATOR)",
    nearby_station_name="string(STR_STATION_ELEVATOR)",
    fund_cost_multiplier="30",
)

# definitely not in Arctic Basic, grain_elevator has been added and removed more than once from that economy :P

industry.enable_in_economy(
    "PLAINS_TRAINS_AND_STEEL",
    fund_cost_multiplier="4",
)

industry.add_tile(
    id="grain_elevator_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True,
        disallow_above_snowline=True,
        disallow_desert=True,
        disallow_coast=True,
        disallow_industry_adjacent=True,
    ),
)

spriteset_ground = industry.add_spriteset(type="dirty_concrete")
spriteset_ground_overlay = industry.add_spriteset(type="empty")

spriteset_1 = industry.add_spriteset(sprites=[(10, 10, 64, 114, -31, -83)])
spriteset_2 = industry.add_spriteset(sprites=[(80, 10, 64, 114, -31, -83)])

spriteset_3 = industry.add_spriteset(sprites=[(150, 10, 64, 114, -31, -83)])
spriteset_4 = industry.add_spriteset(sprites=[(220, 10, 64, 114, -31, -83)])
spriteset_5 = industry.add_spriteset(sprites=[(290, 10, 64, 114, -31, -83)])

spriteset_6 = industry.add_spriteset(sprites=[(360, 10, 64, 114, -31, -83)])
spriteset_7 = industry.add_spriteset(sprites=[(430, 10, 64, 114, -31, -83)])


industry.add_spritelayout(
    id="grain_elevator_spritelayout_1",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)

industry.add_spritelayout(
    id="grain_elevator_spritelayout_2",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)

industry.add_spritelayout(
    id="grain_elevator_spritelayout_3",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)

industry.add_spritelayout(
    id="grain_elevator_spritelayout_4",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)

industry.add_spritelayout(
    id="grain_elevator_spritelayout_5",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
)

industry.add_spritelayout(
    id="grain_elevator_spritelayout_6",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
)

industry.add_spritelayout(
    id="grain_elevator_spritelayout_7",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
)

industry.add_industry_layout(
    id="grain_elevator_industry_layout_1",
    layout=[
        (1, 0, "grain_elevator_spritelayout_1"),
        (0, 0, "grain_elevator_spritelayout_2"),
    ],
)

industry.add_industry_layout(
    id="grain_elevator_industry_layout_2",
    layout=[
        (1, 1, "grain_elevator_spritelayout_3"),
        (0, 1, "grain_elevator_spritelayout_4"),
        (0, 0, "grain_elevator_spritelayout_5"),
    ],
)

industry.add_industry_layout(
    id="grain_elevator_industry_layout_3",
    layout=[
        (0, 1, "grain_elevator_spritelayout_6"),
        (0, 0, "grain_elevator_spritelayout_7"),
    ],
)

