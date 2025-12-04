from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="garage",
    accept_cargos_with_input_ratios=[
        ("BMAT", 8),
    ],
    prod_cargo_types_with_output_ratios=[
        # over-production of vehicles isn't wanted
        ("VEHI", 8),
    ],
    prob_in_game="0",  # low chance of build during gameplay
    prob_map_gen="5",
    map_colour="141",
    colour_scheme_name="scheme_7_bowie",
    name="string(STR_IND_GARAGE)",
    life_type = "IND_LIFE_TYPE_BLACK_HOLE"
    special_flags=["IND_FLAG_ONLY_IN_TOWNS"],
    nearby_station_name="string(STR_STATION_AUTOMOTIVE)",
    fund_cost_multiplier="145",
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)

industry.add_tile(
    id="hardware_store_tile_1",
    location_checks=TileLocationChecks(require_road_adjacent=True),
)

hardware_store_spriteset_ground = industry.add_spriteset(
    type="pavement",
)
hardware_store_spriteset = industry.add_spriteset(sprites=[(0, 0, 64, 64, -31, -33)])

industry.add_spritelayout(
    id="hardware_store_spritelayout",
    tile="hardware_store_tile_1",
    ground_sprite=hardware_store_spriteset_ground,
    ground_overlay=None,
    building_sprites=[hardware_store_spriteset],
)
industry.add_industry_layout(
    id="hardware_store_industry_layout",
    layout=[(0, 0, "hardware_store_spritelayout")],
)
