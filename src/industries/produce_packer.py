from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="produce_packer",
    accept_cargos_with_input_ratios=[],
    prod_cargo_types_with_output_ratios=[
        ("FOOD", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="181",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    name="string(STR_IND_PRODUCE_PACKER)",
    nearby_station_name="string(STR_STATION_FOOD_CORPORATION)",
    fund_cost_multiplier="65",
    sprites_complete=False,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "MILD_MILD_WEST",
    accept_cargos_with_input_ratios=[
        ("AAPL", 3),
        ("VEG_", 3),
        ("FRUT", 3),
        ("PACK", 3),
    ],
    prod_cargo_types_with_output_ratios=[
        ("FOOD", 8),
    ],
    # location checks must be per economy when keystone industries are used
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[
            ["farm", "orchard_piggery"],
            72,
        ]
    ),
)

industry.add_tile(
    id="produce_packer_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True
    ),
)

spriteset_ground = industry.add_spriteset(type="asphalt")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 87, -31, -56)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 87, -31, -56)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 87, -31, -56)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 87, -31, -56)],
)

industry.add_spritelayout(
    id="produce_packer_spritelayout_1",
    tile="produce_packer_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="produce_packer_spritelayout_2",
    tile="produce_packer_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="produce_packer_spritelayout_3",
    tile="produce_packer_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="produce_packer_spritelayout_4",
    tile="produce_packer_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="produce_packer_spritelayout_empty",
    tile="produce_packer_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)

industry.add_industry_layout(
    id="produce_packer_industry_layout_1",
    layout=[
        (0, 0, "produce_packer_spritelayout_1"),
        (0, 1, "produce_packer_spritelayout_1"),
        (0, 2, "produce_packer_spritelayout_3"),
        (1, 0, "produce_packer_spritelayout_1"),
        (1, 1, "produce_packer_spritelayout_1"),
        (1, 2, "produce_packer_spritelayout_3"),
        (2, 0, "produce_packer_spritelayout_2"),
        (2, 1, "produce_packer_spritelayout_2"),
        (2, 2, "produce_packer_spritelayout_4"),
        (3, 0, "produce_packer_spritelayout_4"),
        (3, 1, "produce_packer_spritelayout_4"),
        (3, 2, "produce_packer_spritelayout_4"),
    ],
)
industry.add_industry_layout(
    id="produce_packer_industry_layout_2",
    layout=[
        (0, 0, "produce_packer_spritelayout_2"),
        (0, 1, "produce_packer_spritelayout_3"),
        (0, 2, "produce_packer_spritelayout_1"),
        (0, 3, "produce_packer_spritelayout_3"),
        (1, 0, "produce_packer_spritelayout_1"),
        (1, 1, "produce_packer_spritelayout_4"),
        (1, 2, "produce_packer_spritelayout_1"),
        (1, 3, "produce_packer_spritelayout_3"),
        (2, 0, "produce_packer_spritelayout_2"),
        (2, 1, "produce_packer_spritelayout_4"),
        (2, 2, "produce_packer_spritelayout_1"),
        (3, 0, "produce_packer_spritelayout_2"),
        (3, 1, "produce_packer_spritelayout_4"),
        (3, 2, "produce_packer_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="produce_packer_industry_layout_3",
    layout=[
        (0, 0, "produce_packer_spritelayout_1"),
        (0, 1, "produce_packer_spritelayout_1"),
        (0, 2, "produce_packer_spritelayout_2"),
        (0, 3, "produce_packer_spritelayout_3"),
        (1, 0, "produce_packer_spritelayout_1"),
        (1, 1, "produce_packer_spritelayout_1"),
        (1, 2, "produce_packer_spritelayout_2"),
        (1, 3, "produce_packer_spritelayout_3"),
        (2, 0, "produce_packer_spritelayout_1"),
        (2, 1, "produce_packer_spritelayout_1"),
        (2, 2, "produce_packer_spritelayout_4"),
        (2, 3, "produce_packer_spritelayout_4"),
    ],
)
