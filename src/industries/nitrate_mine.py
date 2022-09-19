from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="nitrate_mine",
    prod_cargo_types_with_multipliers=[
        ("FMSP", 12),
        ("NITR", 17),
    ],
    prob_in_game="4",
    prob_map_gen="7",
    map_colour="121",
    location_checks=dict(require_cluster=[70, 3]),
    prospect_chance="0.75",
    name="string(STR_IND_NITRATE_MINE)",
    nearby_station_name="string(STR_STATION_SALTPETER_WORKS)",
    fund_cost_multiplier="180",
    pollution_and_squalor_factor=1,
)

industry.enable_in_economy(
    "BASIC_TROPIC",
    locate_in_specific_biomes=[
        "more_west",
    ],
)

industry.add_tile(
    id="nitrate_mine_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

sprite_ground = industry.add_sprite(
    sprite_number="GROUNDTILE_MUD_TRACKS"  # ground tile same as overlay tile
)

spriteset_ground_overlay = industry.add_spriteset(type="empty")

spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 110, -31, -70)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -32)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -31)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -31)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -31)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -31)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 64, -31, -31)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 64, -31, -31)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 64, -31, -31)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=8,
    yoffset=2,
    zoffset=70,
)

industry.add_spritelayout(
    id="nitrate_mine_spritelayout_chimney",
    tile="nitrate_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="nitrate_mine_spritelayout_large_shed",
    tile="nitrate_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="nitrate_mine_spritelayout_conveyors",
    tile="nitrate_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="nitrate_mine_spritelayout_processor",
    tile="nitrate_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="nitrate_mine_spritelayout_raised_tanks",
    tile="nitrate_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="nitrate_mine_spritelayout_raised_shed",
    tile="nitrate_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="nitrate_mine_spritelayout_machinery",
    tile="nitrate_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="nitrate_mine_spritelayout_hut",
    tile="nitrate_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="nitrate_mine_spritelayout_nitrate_pile",
    tile="nitrate_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_multi_tile_object(
    add_to_object_num=1,
    view_layout=[
        (0, 0, "nitrate_mine_spritelayout_processor"),
        (1, 0, "nitrate_mine_spritelayout_conveyors"),
        (2, 0, "nitrate_mine_spritelayout_large_shed"),
    ],
)

industry.add_industry_layout(
    id="nitrate_mine_industry_layout_1",
    layout=[
        (0, 0, "nitrate_mine_spritelayout_chimney"),
        (0, 1, "nitrate_mine_spritelayout_raised_shed"),
        (0, 2, "nitrate_mine_spritelayout_hut"),
        (1, 0, "nitrate_mine_spritelayout_raised_tanks"),
        (1, 1, "nitrate_mine_spritelayout_raised_tanks"),
        (1, 2, "nitrate_mine_spritelayout_nitrate_pile"),
        (2, 0, "nitrate_mine_spritelayout_processor"),
        (2, 1, "nitrate_mine_spritelayout_processor"),
        (2, 2, "nitrate_mine_spritelayout_nitrate_pile"),
        (3, 0, "nitrate_mine_spritelayout_conveyors"),
        (3, 1, "nitrate_mine_spritelayout_conveyors"),
        (3, 2, "nitrate_mine_spritelayout_nitrate_pile"),
        (4, 0, "nitrate_mine_spritelayout_large_shed"),
        (4, 1, "nitrate_mine_spritelayout_large_shed"),
        (4, 2, "nitrate_mine_spritelayout_machinery"),
    ],
)
industry.add_industry_layout(
    id="nitrate_mine_industry_layout_2",
    layout=[
        (0, 0, "nitrate_mine_spritelayout_raised_tanks"),
        (0, 1, "nitrate_mine_spritelayout_processor"),
        (0, 2, "nitrate_mine_spritelayout_processor"),
        (0, 3, "nitrate_mine_spritelayout_raised_shed"),
        (1, 0, "nitrate_mine_spritelayout_chimney"),
        (1, 1, "nitrate_mine_spritelayout_conveyors"),
        (1, 2, "nitrate_mine_spritelayout_conveyors"),
        (1, 3, "nitrate_mine_spritelayout_nitrate_pile"),
        (2, 0, "nitrate_mine_spritelayout_machinery"),
        (2, 1, "nitrate_mine_spritelayout_large_shed"),
        (2, 2, "nitrate_mine_spritelayout_large_shed"),
        (2, 3, "nitrate_mine_spritelayout_hut"),
    ],
)
