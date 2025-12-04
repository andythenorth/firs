from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="bunker_base",
    accept_cargo_types=["FRNT"],
    prod_cargo_types=[],
    prob_in_game="18",
    prob_map_gen="24",
    prod_multiplier="[0, 0]",
    map_colour="169",
    colour_scheme_name="scheme_3_hendrix",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_BUNKER_BASE)",
    nearby_station_name="string(STR_STATION_TOWN_1)",
    fund_cost_multiplier="15",
    provides_snow=True,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
)


industry.add_tile(
    id="builders_yard_tile_1",
    location_checks=TileLocationChecks(
        require_houses_nearby=True,
        require_effectively_flat=True,
        disallow_industry_adjacent=True,
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
stacks_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 56, -31, -26)],
    always_draw=True,
)
shed = industry.add_spriteset(
    sprites=[(80, 10, 64, 56, -31, -26)],
)
silo = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -34)],
)
stacks_2 = industry.add_spriteset(
    sprites=[(150, 10, 64, 56, -31, -26)],
    always_draw=True,
)
industry.add_spritelayout(
    id="builders_yard_spritelayout_1",
    tile="builders_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[stacks_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="builders_yard_spritelayout_2",
    tile="builders_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[shed],
)
industry.add_spritelayout(
    id="builders_yard_spritelayout_3",
    tile="builders_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[silo],
)
industry.add_spritelayout(
    id="builders_yard_spritelayout_4",
    tile="builders_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[stacks_2],
)

industry.add_industry_layout(
    id="builders_yard_industry_layout_1",
    layout=[
        (0, 0, "builders_yard_spritelayout_3"),
        (0, 1, "builders_yard_spritelayout_4"),
        (1, 0, "builders_yard_spritelayout_2"),
        (1, 1, "builders_yard_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="builders_yard_industry_layout_2",
    layout=[
        (0, 0, "builders_yard_spritelayout_2"),
        (0, 1, "builders_yard_spritelayout_3"),
        (1, 0, "builders_yard_spritelayout_4"),
        (1, 1, "builders_yard_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="builders_yard_industry_layout_3",
    layout=[
        (0, 0, "builders_yard_spritelayout_3"),
        (0, 1, "builders_yard_spritelayout_2"),
        (1, 0, "builders_yard_spritelayout_1"),
        (1, 1, "builders_yard_spritelayout_4"),
    ],
)
industry.add_industry_layout(
    id="builders_yard_industry_layout_4",
    layout=[
        (0, 0, "builders_yard_spritelayout_2"),
        (0, 1, "builders_yard_spritelayout_1"),
        (1, 0, "builders_yard_spritelayout_3"),
        (1, 1, "builders_yard_spritelayout_4"),
    ],
)
