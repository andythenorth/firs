from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(
    id="dairy_farm",
    prod_cargo_types_with_multipliers=[
        ("LVST", 12),
        ("MILK", 14),
    ],
    prob_in_game="3",
    prob_map_gen="11",
    map_colour="164",
    # fields aren't 100% appropriate, but without them there are zero farm fields planted in Basic Temperate economy
    special_flags=[
        "IND_FLAG_PLANT_FIELDS_PERIODICALLY",
        "IND_FLAG_PLANT_FIELDS_WHEN_BUILT",
    ],
    location_checks=dict(require_cluster=[72, 4]),
    prospect_chance="0.75",
    name="string(STR_IND_DAIRY_FARM)",
    extra_text_fund="string(STR_FUND_DAIRY_FARM)",
    nearby_station_name="string(STR_STATION_FARM_2)",
    fund_cost_multiplier="60",
    pollution_and_squalor_factor=1,
)

industry.enable_in_economy(
    "BASIC_TEMPERATE",
)

industry.add_tile(
    id="dairy_farm_tile_1",
    location_checks=TileLocationChecks(
        disallow_steep_slopes=True,
        disallow_above_snowline=True,
        disallow_desert=True,
        disallow_coast=True,
        disallow_industry_adjacent=True,
    ),
)

sprite_ground = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")
spriteset_ground_empty = industry.add_spriteset(type="empty")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_barn1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 52, -31, -21)],
)
spriteset_silo = industry.add_spriteset(
    sprites=[(80, 10, 64, 52, -31, -21)],
)
spriteset_barn2 = industry.add_spriteset(
    sprites=[(150, 10, 64, 52, -31, -21)],
)
spriteset_house = industry.add_spriteset(
    sprites=[(220, 10, 64, 52, -31, -21)],
)
spriteset_cows_bw = industry.add_spriteset(
    sprites=[(290, 10, 64, 52, -31, -21)],
)
spriteset_cows_brown = industry.add_spriteset(
    sprites=[(360, 10, 64, 52, -31, -21)],
)

industry.add_spritelayout(
    id="dairy_farm_spritelayout_barn1",
    tile="dairy_farm_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_barn1],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="dairy_farm_spritelayout_silo",
    tile="dairy_farm_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_silo],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="dairy_farm_spritelayout_barn2",
    tile="dairy_farm_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_barn2],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="dairy_farm_spritelayout_house",
    tile="dairy_farm_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_house],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="dairy_farm_spritelayout_cows_bw",
    tile="dairy_farm_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_cows_bw],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="dairy_farm_spritelayout_cows_brown",
    tile="dairy_farm_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_cows_brown],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="dairy_farm_spritelayout_cows_bw_dirt",
    tile="dairy_farm_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_cows_bw],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="dairy_farm_spritelayout_cows_brown_dirt",
    tile="dairy_farm_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_cows_brown],
    add_to_object_num=5,
)

industry.add_industry_layout(
    id="dairy_farm_industry_layout_1",
    layout=[
        (0, 0, "dairy_farm_spritelayout_cows_brown"),
        (0, 1, "dairy_farm_spritelayout_cows_bw"),
        (0, 2, "dairy_farm_spritelayout_house"),
        (2, 0, "dairy_farm_spritelayout_silo"),
        (2, 1, "dairy_farm_spritelayout_cows_bw_dirt"),
        (3, 0, "dairy_farm_spritelayout_barn1"),
        (3, 1, "dairy_farm_spritelayout_cows_brown_dirt"),
        (3, 2, "dairy_farm_spritelayout_barn2"),
    ],
)
industry.add_industry_layout(
    id="dairy_farm_industry_layout_2",
    layout=[
        (0, 0, "dairy_farm_spritelayout_cows_brown_dirt"),
        (0, 1, "dairy_farm_spritelayout_cows_bw_dirt"),
        (0, 2, "dairy_farm_spritelayout_barn1"),
        (1, 1, "dairy_farm_spritelayout_barn2"),
        (1, 2, "dairy_farm_spritelayout_silo"),
        (2, 0, "dairy_farm_spritelayout_cows_bw"),
        (2, 1, "dairy_farm_spritelayout_cows_brown"),
        (2, 2, "dairy_farm_spritelayout_house"),
    ],
)
industry.add_industry_layout(
    id="dairy_farm_industry_layout_3",
    layout=[
        (0, 1, "dairy_farm_spritelayout_barn1"),
        (0, 3, "dairy_farm_spritelayout_house"),
        (1, 0, "dairy_farm_spritelayout_barn2"),
        (1, 1, "dairy_farm_spritelayout_cows_brown_dirt"),
        (1, 3, "dairy_farm_spritelayout_cows_bw"),
        (2, 0, "dairy_farm_spritelayout_silo"),
        (2, 1, "dairy_farm_spritelayout_cows_bw_dirt"),
        (2, 3, "dairy_farm_spritelayout_cows_brown"),
    ],
)
