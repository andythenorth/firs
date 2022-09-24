from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="copper_mine",
    prod_cargo_types_with_multipliers=[
        ("CORE", 20),
    ],
    prob_in_game="7",
    prob_map_gen="7",
    map_colour="10",
    location_checks=dict(require_cluster=[70, 3]),
    prospect_chance="0.75",
    name="TTD_STR_INDUSTRY_NAME_COPPER_ORE_MINE",
    nearby_station_name="string(STR_STATION_COPPER_LODE)",
    fund_cost_multiplier="238",
    pollution_and_squalor_factor=1,
)

industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
)
industry.enable_in_economy(
    "BASIC_TROPIC",
    locate_in_specific_biomes=[
        "more_west",
    ],
)

industry.add_tile(
    id="copper_mine_tile_1",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(disallow_industry_adjacent=True),
)

sprite_ground = industry.add_sprite(
    sprite_number="GROUNDTILE_MUD_TRACKS"  # ground tile same as overlay tile
)
sprite_ground_overlay = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")
sprite_1 = industry.add_sprite(
    sprite_number=2039,
)
# there is no sprite 2 for this industry, spritelayout_2 doesn't need a building sprite
sprite_3_anim = industry.add_sprite(
    sprite_number="2028 + ((animation_frame < 33) ? (animation_frame %3) : 0)",
    xoffset=2,
    yoffset=3,
    xextent=13,
    yextent=12,
)
sprite_4 = industry.add_sprite(
    sprite_number=2036,
)
sprite_5 = industry.add_sprite(
    sprite_number=2033,
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=0,
    yoffset=2,
    zoffset=38,
)

industry.add_spritelayout(
    id="copper_mine_spritelayout_1",
    tile="copper_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[sprite_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_mine_spritelayout_2",
    tile="copper_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_mine_spritelayout_3_anim",
    tile="copper_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[sprite_3_anim],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_mine_spritelayout_4",
    tile="copper_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[sprite_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="copper_mine_spritelayout_5",
    tile="copper_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[sprite_5],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="copper_mine_industry_layout_1",
    layout=[
        (0, 0, "copper_mine_spritelayout_1"),
        (0, 1, "copper_mine_spritelayout_1"),
        (0, 2, "copper_mine_spritelayout_1"),
        (1, 0, "copper_mine_spritelayout_5"),
        (1, 1, "copper_mine_spritelayout_3_anim"),
        (1, 2, "copper_mine_spritelayout_4"),
        (2, 0, "copper_mine_spritelayout_1"),
        (2, 1, "copper_mine_spritelayout_1"),
        (2, 2, "copper_mine_spritelayout_2"),
        (3, 1, "copper_mine_spritelayout_1"),
    ],
)
