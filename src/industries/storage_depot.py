from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="storage_depot",
    accept_cargos_with_input_ratios=[
        ("VEHI", 1),
        ("ITEM", 4),
        ("SHIP", 1),
        ("ARTY", 1),
        ("AVEH", 1),
    ],
    prod_cargo_types_with_output_ratios=[
        ("FRNT", 8),
    ],
    prob_in_game="0",
    prob_map_gen="10",
    map_colour="207",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    location_checks=dict(
        same_type_distance=32,
    ),
    name="string(STR_IND_STORAGE_DEPOT)",
    special_flags=["IND_FLAG_ONLY_IN_TOWNS"],
    nearby_station_name="string(STR_STATION_VEHICLE_DISTRIBUTOR)",
    fund_cost_multiplier="8",
    provides_snow=True,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)

industry.add_tile(
    id="general_store_tile_1",
    location_checks=TileLocationChecks(require_road_adjacent=True),
)

spriteset_ground = industry.add_spriteset(
    type="pavement",
)
spriteset_ground_overlay = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(sprites=[(10, 60, 64, 48, -31, -18)])
industry.add_spritelayout(
    id="general_store_spritelayout",
    tile="general_store_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_industry_layout(
    id="general_store_industry_layout",
    layout=[(0, 0, "general_store_spritelayout")],
)
