from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="timber_yard",
    accept_cargos_with_input_ratios=[("WDPR", 6), ("COAT", 2)],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("ENSP", 8)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="43",
    name="string(STR_IND_TIMBER_YARD)",
    nearby_station_name="string(STR_STATION_CREOSOTING)",
    fund_cost_multiplier="35",
    pollution_and_squalor_factor=1,
    provides_snow=True,
)


industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
    prod_cargo_types_with_output_ratios=[("BDMT", 8)],
    accept_cargos_with_input_ratios=[
        ("WDPR", 6),
        ("RFPR", 2),
    ],
)

# non-animated tile, allowed on slopes
industry.add_tile(
    id="timber_yard_tile_1",
    location_checks=TileLocationChecks(disallow_industry_adjacent=True),
)

# animated kiln-building tile, graphics break if built on slopes
industry.add_tile(
    id="timber_yard_tile_2",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

sprite_ground = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(sprites=[(80, 10, 64, 64, -31, -40)])
spriteset_2 = industry.add_spriteset(sprites=[(150, 10, 64, 64, -31, -34)])
# no spriteset 3 for this industry, historical reasons
spriteset_4 = industry.add_spriteset(sprites=[(290, 10, 64, 64, -31, -35)])
spriteset_5 = industry.add_spriteset(sprites=[(10, 10, 64, 64, -31, -26)])
spriteset_6 = industry.add_spriteset(sprites=[(150, 90, 64, 31, -31, -4)])
spriteset_7 = industry.add_spriteset(sprites=[(220, 90, 64, 31, -31, -4)])
spriteset_8 = industry.add_spriteset(sprites=[(290, 90, 64, 31, -31, -4)])
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=0,
    yoffset=3,
    zoffset=12,
)

industry.add_spritelayout(
    id="timber_yard_spritelayout_1",
    tile="timber_yard_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="timber_yard_spritelayout_2",
    tile="timber_yard_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
# no spritelayout 3 for this industry, historical reasons
industry.add_spritelayout(
    id="timber_yard_spritelayout_4",
    tile="timber_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="timber_yard_spritelayout_5",
    tile="timber_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="timber_yard_spritelayout_6",
    tile="timber_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="timber_yard_spritelayout_7",
    tile="timber_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="timber_yard_spritelayout_8",
    tile="timber_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)

industry.add_multi_tile_object(
    add_to_object_num=2,
    view_layout=[
        (0, 0, "timber_yard_spritelayout_2"),
        (0, 1, "timber_yard_spritelayout_1"),
    ],
)

industry.add_industry_layout(
    id="timber_yard_industry_layout_1",
    layout=[
        (0, 0, "timber_yard_spritelayout_2"),
        (0, 1, "timber_yard_spritelayout_1"),
        (0, 2, "timber_yard_spritelayout_5"),
        (1, 0, "timber_yard_spritelayout_6"),
        (1, 1, "timber_yard_spritelayout_4"),
        (1, 2, "timber_yard_spritelayout_8"),
        (2, 0, "timber_yard_spritelayout_8"),
        (2, 1, "timber_yard_spritelayout_4"),
        (2, 2, "timber_yard_spritelayout_7"),
        (3, 0, "timber_yard_spritelayout_6"),
        (3, 1, "timber_yard_spritelayout_5"),
        (3, 2, "timber_yard_spritelayout_6"),
    ],
)
industry.add_industry_layout(
    id="timber_yard_industry_layout_2",
    layout=[
        (0, 0, "timber_yard_spritelayout_2"),
        (0, 1, "timber_yard_spritelayout_1"),
        (0, 2, "timber_yard_spritelayout_5"),
        (0, 3, "timber_yard_spritelayout_6"),
        (1, 0, "timber_yard_spritelayout_8"),
        (1, 1, "timber_yard_spritelayout_8"),
        (1, 2, "timber_yard_spritelayout_4"),
        (1, 3, "timber_yard_spritelayout_6"),
        (2, 0, "timber_yard_spritelayout_5"),
        (2, 1, "timber_yard_spritelayout_6"),
        (2, 2, "timber_yard_spritelayout_4"),
        (2, 3, "timber_yard_spritelayout_7"),
    ],
)
industry.add_industry_layout(
    id="timber_yard_industry_layout_3",
    layout=[
        (0, 0, "timber_yard_spritelayout_6"),
        (0, 1, "timber_yard_spritelayout_4"),
        (0, 2, "timber_yard_spritelayout_2"),
        (0, 3, "timber_yard_spritelayout_1"),
        (0, 4, "timber_yard_spritelayout_8"),
        (1, 0, "timber_yard_spritelayout_8"),
        (1, 1, "timber_yard_spritelayout_4"),
        (1, 2, "timber_yard_spritelayout_6"),
        (1, 3, "timber_yard_spritelayout_5"),
        (1, 4, "timber_yard_spritelayout_7"),
    ],
)
industry.add_industry_layout(
    id="timber_yard_industry_layout_4",
    layout=[
        (0, 0, "timber_yard_spritelayout_4"),
        (0, 1, "timber_yard_spritelayout_7"),
        (1, 0, "timber_yard_spritelayout_4"),
        (1, 1, "timber_yard_spritelayout_6"),
        (2, 0, "timber_yard_spritelayout_2"),
        (2, 1, "timber_yard_spritelayout_1"),
        (3, 0, "timber_yard_spritelayout_8"),
        (3, 1, "timber_yard_spritelayout_6"),
        (4, 0, "timber_yard_spritelayout_5"),
        (4, 1, "timber_yard_spritelayout_6"),
    ],
)
