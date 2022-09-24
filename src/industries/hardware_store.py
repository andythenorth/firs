from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="hardware_store",
    accept_cargo_types=[],
    prod_cargo_types=[],
    prob_in_game="18",
    prob_map_gen="24",
    prod_multiplier="[0, 0]",
    map_colour="169",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    special_flags=["IND_FLAG_ONLY_IN_TOWNS"],
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_HARDWARE_STORE)",
    nearby_station_name="string(STR_STATION_TOWN_1)",
    fund_cost_multiplier="15",
    provides_snow=True,
)

industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
    accept_cargo_types=["GOOD", "BDMT"],
)


industry.add_tile(
    id="hardware_store_tile_1",
    location_checks=TileLocationChecks(require_road_adjacent=True),
)

hardware_store_spriteset_ground = industry.add_spriteset(
    type="slab",
)
hardware_store_spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)
hardware_store_spriteset = industry.add_spriteset(sprites=[(0, 0, 64, 64, -31, -33)])

industry.add_spritelayout(
    id="hardware_store_spritelayout",
    tile="hardware_store_tile_1",
    ground_sprite=hardware_store_spriteset_ground,
    ground_overlay=hardware_store_spriteset_ground_overlay,
    building_sprites=[hardware_store_spriteset],
)
industry.add_industry_layout(
    id="hardware_store_industry_layout",
    layout=[(0, 0, "hardware_store_spritelayout")],
)
