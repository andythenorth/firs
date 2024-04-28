from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="supply_yard",
    accept_cargos_with_input_ratios=[],
    prod_cargo_types_with_output_ratios=[],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="161",
    name="string(STR_IND_SUPPLY_YARD)",
    nearby_station_name="string(STR_STATION_BASE)",
    fund_cost_multiplier="110",
    sprites_complete=True,
)

industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
    accept_cargos_with_input_ratios=[
        ("BDMT", 8),
        ("PETR", 8),
        ("GOOD", 8),
    ],
    prod_cargo_types_with_output_ratios=[
        ("ENSP", 4),
        ("FMSP", 4),
    ],
)
# industry.economy_variations['IN_A_HOT_COUNTRY'].accept_cargos_with_input_ratios = [('CMNT', 8), ('PETR', 8), ('VEHI', 8), ('BOOM', 8), ('WDPR', 8)]

industry.add_tile(
    id="supply_yard_tile_1",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 64, -31, -32)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -32)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -32)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -32)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -32)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -32)],
)
industry.add_spritelayout(
    id="supply_yard_spritelayout_1",
    tile="supply_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="supply_yard_spritelayout_2",
    tile="supply_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="supply_yard_spritelayout_3",
    tile="supply_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="supply_yard_spritelayout_4",
    tile="supply_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="supply_yard_spritelayout_5",
    tile="supply_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="supply_yard_spritelayout_6",
    tile="supply_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=6,
)


industry.add_industry_layout(
    id="supply_yard_industry_layout_1",
    layout=[
        (0, 0, "supply_yard_spritelayout_1"),
        (0, 1, "supply_yard_spritelayout_2"),
        (0, 2, "supply_yard_spritelayout_3"),
        (0, 3, "supply_yard_spritelayout_1"),
        (1, 0, "supply_yard_spritelayout_4"),
        (1, 1, "supply_yard_spritelayout_5"),
        (1, 2, "supply_yard_spritelayout_6"),
        (1, 3, "supply_yard_spritelayout_2"),
    ],
)

industry.add_industry_layout(
    id="supply_yard_industry_layout_2",
    layout=[
        (0, 0, "supply_yard_spritelayout_1"),
        (0, 1, "supply_yard_spritelayout_1"),
        (1, 0, "supply_yard_spritelayout_2"),
        (1, 1, "supply_yard_spritelayout_2"),
        (1, 2, "supply_yard_spritelayout_6"),
        (2, 0, "supply_yard_spritelayout_5"),
        (2, 1, "supply_yard_spritelayout_4"),
        (2, 2, "supply_yard_spritelayout_3"),
    ],
)

industry.add_industry_layout(
    id="supply_yard_industry_layout_3",
    layout=[
        (0, 0, "supply_yard_spritelayout_2"),
        (0, 1, "supply_yard_spritelayout_6"),
        (1, 0, "supply_yard_spritelayout_1"),
        (1, 1, "supply_yard_spritelayout_1"),
        (2, 0, "supply_yard_spritelayout_2"),
        (2, 1, "supply_yard_spritelayout_3"),
        (3, 0, "supply_yard_spritelayout_5"),
        (3, 1, "supply_yard_spritelayout_4"),
    ],
)
