from industry import IndustryInformative, TileLocationChecks

industry = IndustryInformative(
    id="plaza",
    prob_in_game="12",
    prob_map_gen="24",
    map_colour="168",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    special_flags=["IND_FLAG_ONLY_IN_TOWNS"],
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_PLAZA)",
    nearby_station_name="string(STR_STATION_PLAZA)",
    fund_cost_multiplier="15",
)

industry.enable_in_economy(
    "BASIC_TEMPERATE",
)
industry.enable_in_economy(
    "BASIC_ARCTIC",
)
industry.enable_in_economy(
    "BASIC_TROPIC",
)
industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
)
industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="plaza_tile_1",
    location_checks=TileLocationChecks(require_road_adjacent=True),
)

spriteset_ground = industry.add_spriteset(
    type="slab",
)
spriteset_ground_overlay = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(sprites=[(10, 60, 64, 48, -31, -18)])

industry.add_spritelayout(
    tile="plaza_tile_1",
    id="plaza_spritelayout",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)

industry.add_industry_layout(
    id="plaza_industry_layout",
    layout=[(0, 0, "plaza_spritelayout")],
)
