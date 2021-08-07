from industry import IndustryInformative, TileLocationChecks

industry = IndustryInformative(
    id="newspaper_office",
    prob_in_game="12",
    prob_map_gen="24",
    map_colour="168",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    special_flags=["IND_FLAG_ONLY_IN_TOWNS"],
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_NEWSPAPER_OFFICE)",
    nearby_station_name="string(STR_STATION_TOWN_3)",
    fund_cost_multiplier="15",
)

industry.economy_variations["BASIC_TEMPERATE"].enabled = True
industry.economy_variations["BASIC_ARCTIC"].enabled = True
industry.economy_variations["BASIC_TROPIC"].enabled = True
###industry.economy_variations['BETTER_LIVING_THROUGH_CHEMISTRY'].enabled = True
industry.economy_variations["IN_A_HOT_COUNTRY"].enabled = True
industry.economy_variations["STEELTOWN"].enabled = True

industry.add_tile(
    id="newspaper_office_tile_1",
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
    id="newspaper_office_spritelayout",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_industry_layout(
    id="newspaper_office_industry_layout",
    layout=[(0, 0, "newspaper_office_tile_1", "newspaper_office_spritelayout")],
)
