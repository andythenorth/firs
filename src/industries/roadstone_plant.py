from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="roadstone_plant",
    accept_cargo_types=[
        "BDMT",
    ],
    prod_cargo_types=[],
    prob_in_game="12",
    prob_map_gen="18",
    prod_multiplier="[0, 0]",
    map_colour="169",
    colour_scheme_name="scheme_3_hendrix",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    name="string(STR_IND_ROADSTONE_PLANT)",
    nearby_station_name="string(STR_STATION_BUILDERS_YARD)",
    fund_cost_multiplier="16",
    provides_snow=False,
    sprites_complete=False,
    animated_tiles_fixed=True,
)


industry.enable_in_economy(
    "MILD_MILD_WEST",
    accept_cargo_types=[
        "BITU",
        "CMNT",
        "GRVL",
        "SLAG",
    ],
    vulcan_config={
        "map_curator": {
            "curation_function": "MinimumRatioToTowns",
            "min_population": 800,  # we force GS-placed roadstone plants into larger towns only
            "max_population": 0,
            "industry_town_ratio": 1,
        }
    },
)

industry.add_tile(
    id="roadstone_plant_tile_1",
    location_checks=TileLocationChecks(
        require_houses_nearby=True,
        require_effectively_flat=True,
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
    id="roadstone_plant_spritelayout_1",
    tile="roadstone_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[stacks_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="roadstone_plant_spritelayout_2",
    tile="roadstone_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[shed],
)
industry.add_spritelayout(
    id="roadstone_plant_spritelayout_3",
    tile="roadstone_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[silo],
)
industry.add_spritelayout(
    id="roadstone_plant_spritelayout_4",
    tile="roadstone_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[stacks_2],
)

industry.add_industry_layout(
    id="roadstone_plant_industry_layout_1",
    layout=[
        (0, 0, "roadstone_plant_spritelayout_3"),
        (0, 1, "roadstone_plant_spritelayout_4"),
        (1, 0, "roadstone_plant_spritelayout_2"),
        (1, 1, "roadstone_plant_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="roadstone_plant_industry_layout_2",
    layout=[
        (0, 0, "roadstone_plant_spritelayout_2"),
        (0, 1, "roadstone_plant_spritelayout_3"),
        (1, 0, "roadstone_plant_spritelayout_4"),
        (1, 1, "roadstone_plant_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="roadstone_plant_industry_layout_3",
    layout=[
        (0, 0, "roadstone_plant_spritelayout_3"),
        (0, 1, "roadstone_plant_spritelayout_2"),
        (1, 0, "roadstone_plant_spritelayout_1"),
        (1, 1, "roadstone_plant_spritelayout_4"),
    ],
)
industry.add_industry_layout(
    id="roadstone_plant_industry_layout_4",
    layout=[
        (0, 0, "roadstone_plant_spritelayout_2"),
        (0, 1, "roadstone_plant_spritelayout_1"),
        (1, 0, "roadstone_plant_spritelayout_3"),
        (1, 1, "roadstone_plant_spritelayout_4"),
    ],
)
