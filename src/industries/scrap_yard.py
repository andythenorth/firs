from industry import IndustryTownProducerPopulationDependent, TileLocationChecks

industry = IndustryTownProducerPopulationDependent(
    id="scrap_yard",
    prod_cargo_types_with_multipliers=[("SCMT", 32)],  # prod dependent on town popn
    prob_in_game="3",
    prob_map_gen="7",
    map_colour="64",
    location_checks=dict(require_town_min_population=400),
    prospect_chance="0.75",
    name="string(STR_IND_SCRAP_YARD)",
    nearby_station_name="string(STR_STATION_BONEYARD)",
    fund_cost_multiplier="101",
    provides_snow=True,
)


industry.enable_in_economy(
    "BASIC_TEMPERATE",
)

industry.enable_in_economy(
    "STEELTOWN",
    prob_map_gen="14",
)

industry.add_tile(
    id="scrap_yard_tile_1",
    location_checks=TileLocationChecks(
        disallow_steep_slopes=True,
        require_houses_nearby=True,
        disallow_industry_adjacent=True,
    ),
)

sprite_ground = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 55, -31, -24)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 55, -31, -24)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 55, -31, -24)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 55, -31, -24)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 55, -31, -24)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 55, -31, -24)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 55, -31, -24)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 55, -31, -24)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 55, -31, -24)],
)

industry.add_spritelayout(
    id="scrap_yard_spritelayout_1",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_2",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_3",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_4",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_5",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_6",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_7",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_8",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_9",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
)

industry.add_industry_layout(
    id="scrap_yard_industry_layout_1",
    layout=[
        (0, 2, "scrap_yard_spritelayout_2"),
        (1, 1, "scrap_yard_spritelayout_2"),
        (1, 2, "scrap_yard_spritelayout_9"),
        (2, 1, "scrap_yard_spritelayout_1"),
        (2, 2, "scrap_yard_spritelayout_8"),
        (3, 1, "scrap_yard_spritelayout_4"),
        (3, 2, "scrap_yard_spritelayout_7"),
        (4, 0, "scrap_yard_spritelayout_5"),
        (4, 1, "scrap_yard_spritelayout_3"),
        (4, 2, "scrap_yard_spritelayout_6"),
    ],
)
industry.add_industry_layout(
    id="scrap_yard_industry_layout_2",
    layout=[
        (0, 1, "scrap_yard_spritelayout_7"),
        (1, 1, "scrap_yard_spritelayout_1"),
        (1, 2, "scrap_yard_spritelayout_8"),
        (2, 0, "scrap_yard_spritelayout_5"),
        (2, 1, "scrap_yard_spritelayout_3"),
        (2, 2, "scrap_yard_spritelayout_6"),
    ],
)
industry.add_industry_layout(
    id="scrap_yard_industry_layout_3",
    layout=[
        (0, 3, "scrap_yard_spritelayout_2"),
        (1, 1, "scrap_yard_spritelayout_2"),
        (1, 3, "scrap_yard_spritelayout_9"),
        (2, 1, "scrap_yard_spritelayout_1"),
        (2, 3, "scrap_yard_spritelayout_8"),
        (3, 1, "scrap_yard_spritelayout_4"),
        (3, 3, "scrap_yard_spritelayout_7"),
        (4, 0, "scrap_yard_spritelayout_5"),
        (4, 1, "scrap_yard_spritelayout_3"),
        (4, 3, "scrap_yard_spritelayout_6"),
    ],
)
