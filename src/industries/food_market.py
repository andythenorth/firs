from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="food_market",
    accept_cargo_types=[
        "FOOD",
        "FRUT",
        "BEER",
    ],
    prod_cargo_types=[],
    prob_in_game="12",
    prob_map_gen="24",
    prod_multiplier="[0, 0]",
    map_colour="191",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    special_flags=["IND_FLAG_ONLY_IN_TOWNS"],
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_FOOD_MARKET)",
    nearby_station_name="string(STR_STATION_TOWN_3)",
    fund_cost_multiplier="15",
    provides_snow=True,
)

industry.add_tile(
    id="food_market_tile_1",
    location_checks=TileLocationChecks(require_road_adjacent=True),
)

spriteset_ground = industry.add_spriteset(
    type="slab",
)
spriteset_ground_overlay = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(sprites=[(10, 60, 64, 36, -31, -4)])
sprite_tree_1 = industry.add_sprite(
    sprite_number="nearby_tile_terrain_type(0, 0) != TILETYPE_SNOW ? 1639 : 1793",
    xoffset=11,
    yoffset=1,
    xextent=6,
    yextent=6,
)
sprite_tree_2 = industry.add_sprite(
    sprite_number="nearby_tile_terrain_type(0, 0) != TILETYPE_SNOW ? 1639 : 1793",
    xoffset=11,
    yoffset=6,
    xextent=6,
    yextent=6,
)

industry.add_spritelayout(
    id="food_market_spritelayout",
    tile="food_market_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1, sprite_tree_1, sprite_tree_2],
)
industry.add_industry_layout(
    id="food_market_industry_layout",
    layout=[(0, 0, "food_market_spritelayout")],
)
