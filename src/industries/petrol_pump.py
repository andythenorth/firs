from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="petrol_pump",
    accept_cargo_types=[
        "FOOD",
        "GOOD",
        "PETR",
    ],
    prod_cargo_types=[],
    prob_in_game="8",
    prob_map_gen="8",
    prod_multiplier="[0, 0]",
    map_colour="169",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_PETROLPUMP)",
    nearby_station_name="string(STR_STATION_PUMPS)",
    fund_cost_multiplier="8",
    provides_snow=True,
    sprites_complete=True,
    animated_tiles_fixed=False,
)

industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
)


industry.add_tile(
    id="petrol_pump_tile_1",
    location_checks=TileLocationChecks(
        require_road_adjacent=True, require_effectively_flat=True
    ),
)

sprite_ground = industry.add_sprite(
    sprite_number="GROUNDTILE_SLABS",
)
sprite_ground_overlay = industry.add_sprite(
    sprite_number="GROUNDTILE_SLABS",
)
spriteset_1 = industry.add_spriteset(sprites=[(10, 60, 64, 59, -31, -28)])
spriteset_2 = industry.add_spriteset(sprites=[(80, 60, 64, 59, -31, -28)])

industry.add_spritelayout(
    id="petrol_pump_spritelayout_1",
    tile="petrol_pump_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id="petrol_pump_spritelayout_2",
    tile="petrol_pump_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_2],
)

industry.add_industry_layout(
    id="petrol_pump_industry_layout_1",
    layout=[
        (0, 0, "petrol_pump_spritelayout_1"),
        (0, 1, "petrol_pump_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="petrol_pump_industry_layout_2",
    layout=[
        (0, 0, "petrol_pump_spritelayout_1"),
        (1, 0, "petrol_pump_spritelayout_2"),
    ],
)
