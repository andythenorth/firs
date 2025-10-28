from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="feed_mill",
    accept_cargos_with_input_ratios=[
        ("GRAI", 6),
        ("MOLA", 6),
    ],
    prod_cargo_types_with_output_ratios=[
        ("FMSP", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="186",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    special_flags=["IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE"],
    name="string(STR_IND_FEED_MILL)",
    nearby_station_name="string(STR_STATION_MILLS)",
    fund_cost_multiplier="170",
    sprites_complete=False,
    animated_tiles_fixed=False,
)

industry.enable_in_economy(
    "MILD_MILD_WEST",
)

industry.add_tile(
    id="feed_mill_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(500, 10, 64, 66, -31, -35)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(570, 10, 64, 66, -31, -35)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(710, 10, 64, 66, -31, -35)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(80, 10, 64, 88, -31, -58)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(150, 10, 64, 88, -31, -59)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(220, 10, 64, 88, -31, -64)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(360, 10, 64, 73, -31, -45)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(430, 10, 64, 66, -31, -38)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=1,
    yoffset=0,
    zoffset=62,
    animation_frame_offset=1,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big", xoffset=1, yoffset=-3, zoffset=62
)

industry.add_spritelayout(
    id="feed_mill_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="feed_mill_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="feed_mill_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="feed_mill_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="feed_mill_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="feed_mill_spritelayout_6_anim",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    smoke_sprites=[sprite_smoke_2, sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="feed_mill_spritelayout_7",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="feed_mill_spritelayout_8",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="feed_mill_spritelayout_9",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="feed_mill_industry_layout_1",
    layout=[
        (0, 0, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (0, 1, "feed_mill_tile_1", "feed_mill_spritelayout_2"),
        (0, 2, "feed_mill_tile_1", "feed_mill_spritelayout_1"),
        (0, 3, "feed_mill_tile_1", "feed_mill_spritelayout_1"),
        (1, 0, "feed_mill_tile_1", "feed_mill_spritelayout_8"),
        (1, 1, "feed_mill_tile_1", "feed_mill_spritelayout_4"),
        (1, 2, "feed_mill_tile_1", "feed_mill_spritelayout_5"),
        (1, 3, "feed_mill_tile_1", "feed_mill_spritelayout_6_anim"),
        (2, 0, "feed_mill_tile_1", "feed_mill_spritelayout_7"),
        (2, 1, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (2, 2, "feed_mill_tile_1", "feed_mill_spritelayout_3"),
        (2, 3, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
    ],
)
industry.add_industry_layout(
    id="feed_mill_industry_layout_2",
    layout=[
        (0, 0, "feed_mill_tile_1", "feed_mill_spritelayout_8"),
        (0, 1, "feed_mill_tile_1", "feed_mill_spritelayout_4"),
        (0, 2, "feed_mill_tile_1", "feed_mill_spritelayout_5"),
        (0, 3, "feed_mill_tile_1", "feed_mill_spritelayout_6_anim"),
        (0, 4, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (1, 0, "feed_mill_tile_1", "feed_mill_spritelayout_7"),
        (1, 1, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (1, 2, "feed_mill_tile_1", "feed_mill_spritelayout_3"),
        (1, 3, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (1, 4, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (2, 0, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (2, 1, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (2, 2, "feed_mill_tile_1", "feed_mill_spritelayout_1"),
        (2, 3, "feed_mill_tile_1", "feed_mill_spritelayout_1"),
        (2, 4, "feed_mill_tile_1", "feed_mill_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="feed_mill_industry_layout_3",
    layout=[
        (0, 0, "feed_mill_tile_1", "feed_mill_spritelayout_2"),
        (0, 1, "feed_mill_tile_1", "feed_mill_spritelayout_2"),
        (0, 2, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (1, 0, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (1, 1, "feed_mill_tile_1", "feed_mill_spritelayout_4"),
        (1, 2, "feed_mill_tile_1", "feed_mill_spritelayout_3"),
        (2, 0, "feed_mill_tile_1", "feed_mill_spritelayout_8"),
        (2, 1, "feed_mill_tile_1", "feed_mill_spritelayout_5"),
        (2, 2, "feed_mill_tile_1", "feed_mill_spritelayout_6_anim"),
        (3, 0, "feed_mill_tile_1", "feed_mill_spritelayout_7"),
        (3, 1, "feed_mill_tile_1", "feed_mill_spritelayout_3"),
        (3, 2, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (4, 0, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (4, 1, "feed_mill_tile_1", "feed_mill_spritelayout_1"),
        (4, 2, "feed_mill_tile_1", "feed_mill_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="feed_mill_industry_layout_4",
    layout=[
        (0, 0, "feed_mill_tile_1", "feed_mill_spritelayout_1"),
        (0, 1, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (0, 2, "feed_mill_tile_1", "feed_mill_spritelayout_8"),
        (1, 0, "feed_mill_tile_1", "feed_mill_spritelayout_1"),
        (1, 1, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
        (1, 2, "feed_mill_tile_1", "feed_mill_spritelayout_7"),
        (2, 0, "feed_mill_tile_1", "feed_mill_spritelayout_4"),
        (2, 1, "feed_mill_tile_1", "feed_mill_spritelayout_5"),
        (2, 2, "feed_mill_tile_1", "feed_mill_spritelayout_6_anim"),
        (3, 0, "feed_mill_tile_1", "feed_mill_spritelayout_2"),
        (3, 1, "feed_mill_tile_1", "feed_mill_spritelayout_3"),
        (3, 2, "feed_mill_tile_1", "feed_mill_spritelayout_9"),
    ],
)
