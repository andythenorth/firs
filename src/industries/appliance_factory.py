from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="appliance_factory",
    accept_cargos_with_input_ratios=[
        # lots of inputs, but only 3 are required (see industry.py for the kludge to make that work)
        # all input ratios *must* be 3
        # note also that it's deliberately easy to get a partly-efficient supply of Goods from a Wharf by combining POWR and COAT
        ("STSH", 3),
        ("POWR", 3),
        ("PUMP", 3),
        ("COAT", 3),
        ("SEAL", 3),
    ],
    prod_cargo_types_with_output_ratios=[
        ("GOOD", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="194",
    name="string(STR_IND_APPLIANCE_FACTORY)",
    nearby_station_name="string(STR_STATION_APPLIANCE_FACTORY)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
    sprites_complete=True,
)

industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="appliance_factory_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="asphalt")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 44, -31, -13)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 74, -31, -43)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 88, -31, -57)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 85, -31, -54)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 104, -31, -73)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 91, -31, -60)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 98, -31, -67)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 54, -31, -23)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 76, -31, -45)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(640, 10, 64, 32, -31, -1)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(710, 10, 64, 49, -31, -18)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=17,
    yoffset=9,
    zoffset=99,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=20,
    yoffset=9,
    zoffset=100,
    animation_frame_offset=1,
)

industry.add_spritelayout(
    id="appliance_factory_spritelayout_1",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_2",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_3",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_4",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_5",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
    fences=["nw", "se", "sw"],
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_6",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "se", "sw"],
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_7",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "se", "sw"],
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_8",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_9",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_10",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_11",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_11],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_12",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se"],
)

industry.add_industry_layout(
    id="appliance_factory_industry_layout_1",
    layout=[
        (0, 0, "appliance_factory_spritelayout_12"),
        (0, 1, "appliance_factory_spritelayout_12"),
        (0, 2, "appliance_factory_spritelayout_11"),
        (0, 3, "appliance_factory_spritelayout_12"),
        (1, 0, "appliance_factory_spritelayout_12"),
        (1, 1, "appliance_factory_spritelayout_8"),
        (1, 2, "appliance_factory_spritelayout_9"),
        (1, 3, "appliance_factory_spritelayout_10"),
        (3, 0, "appliance_factory_spritelayout_12"),
        (3, 1, "appliance_factory_spritelayout_5"),
        (3, 2, "appliance_factory_spritelayout_6"),
        (3, 3, "appliance_factory_spritelayout_7"),
        (4, 0, "appliance_factory_spritelayout_1"),
        (4, 1, "appliance_factory_spritelayout_2"),
        (4, 2, "appliance_factory_spritelayout_3"),
        (4, 3, "appliance_factory_spritelayout_4"),
    ],
)
