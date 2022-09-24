from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(
    id="herding_coop",
    prod_cargo_types_with_multipliers=[
        ("FOOD", 7),
    ],
    prob_in_game="14",
    prob_map_gen="14",
    map_colour="207",
    special_flags=["IND_FLAG_NO_PRODUCTION_INCREASE"],
    # herding_coop doesn't cluster, by design - no industry location checks needed
    prospect_chance="0.75",
    name="string(STR_IND_HERDING_COOP)",
    extra_text_fund="string(STR_FUND_HERDING_COOP)",
    nearby_station_name="string(STR_STATION_HERDING_COOP)",
    fund_cost_multiplier="88",
)

industry.enable_in_economy(
    "BASIC_ARCTIC",
)

industry.add_tile(
    id="herding_coop_tile_1",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        disallow_desert=True, disallow_coast=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="empty")
sprite_ground_mud = industry.add_sprite(sprite_number=3943)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 52, -31, -21)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 52, -31, -21)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 52, -31, -21)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 52, -31, -21)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 52, -31, -21)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 52, -31, -21)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=1,
    yoffset=0,
    zoffset=12,
)

industry.add_spritelayout(
    id="herding_coop_spritelayout_large_hut",
    tile="herding_coop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke_1],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="herding_coop_spritelayout_brown_hut",
    tile="herding_coop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="herding_coop_spritelayout_two_brown_huts",
    tile="herding_coop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="herding_coop_spritelayout_paddock_1",
    tile="herding_coop_tile_1",
    ground_sprite=sprite_ground_mud,
    ground_overlay=sprite_ground_mud,
    building_sprites=[spriteset_4],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="herding_coop_spritelayout_paddock_2",
    tile="herding_coop_tile_1",
    ground_sprite=sprite_ground_mud,
    ground_overlay=sprite_ground_mud,
    building_sprites=[spriteset_5],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="herding_coop_spritelayout_small_hut_logs",
    tile="herding_coop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    terrain_aware_ground=True,
)

industry.add_industry_layout(
    id="herding_coop_industry_layout_1",
    layout=[
        (0, 0, "herding_coop_spritelayout_paddock_2"),
        (0, 1, "herding_coop_spritelayout_paddock_1"),
        (0, 2, "herding_coop_spritelayout_large_hut"),
        (1, 0, "herding_coop_spritelayout_brown_hut"),
        (1, 1, "herding_coop_spritelayout_two_brown_huts"),
        (1, 2, "herding_coop_spritelayout_small_hut_logs"),
        (2, 0, "herding_coop_spritelayout_brown_hut"),
        (2, 1, "herding_coop_spritelayout_two_brown_huts"),
        (2, 2, "herding_coop_spritelayout_paddock_1"),
    ],
)
industry.add_industry_layout(
    id="herding_coop_industry_layout_2",
    layout=[
        (0, 0, "herding_coop_spritelayout_two_brown_huts"),
        (0, 1, "herding_coop_spritelayout_paddock_1"),
        (0, 2, "herding_coop_spritelayout_paddock_2"),
        (1, 0, "herding_coop_spritelayout_brown_hut"),
        (1, 1, "herding_coop_spritelayout_two_brown_huts"),
        (1, 2, "herding_coop_spritelayout_brown_hut"),
        (2, 0, "herding_coop_spritelayout_paddock_1"),
        (2, 1, "herding_coop_spritelayout_large_hut"),
        (2, 2, "herding_coop_spritelayout_small_hut_logs"),
    ],
)
industry.add_industry_layout(
    id="herding_coop_industry_layout_3",
    layout=[
        (0, 0, "herding_coop_spritelayout_two_brown_huts"),
        (0, 1, "herding_coop_spritelayout_large_hut"),
        (0, 2, "herding_coop_spritelayout_paddock_2"),
        (0, 3, "herding_coop_spritelayout_small_hut_logs"),
        (1, 0, "herding_coop_spritelayout_brown_hut"),
        (1, 1, "herding_coop_spritelayout_two_brown_huts"),
        (1, 2, "herding_coop_spritelayout_brown_hut"),
        (1, 3, "herding_coop_spritelayout_paddock_1"),
    ],
)
industry.add_industry_layout(
    id="herding_coop_industry_layout_4",
    layout=[
        (0, 0, "herding_coop_spritelayout_two_brown_huts"),
        (0, 1, "herding_coop_spritelayout_paddock_1"),
        (1, 0, "herding_coop_spritelayout_brown_hut"),
        (1, 1, "herding_coop_spritelayout_two_brown_huts"),
        (2, 0, "herding_coop_spritelayout_paddock_2"),
        (2, 1, "herding_coop_spritelayout_small_hut_logs"),
        (3, 0, "herding_coop_spritelayout_brown_hut"),
        (3, 1, "herding_coop_spritelayout_large_hut"),
    ],
)
