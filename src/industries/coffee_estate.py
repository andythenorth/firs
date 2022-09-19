from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(
    id="coffee_estate",
    prod_cargo_types_with_multipliers=[],
    map_colour="70",
    prob_in_game="3",
    prob_map_gen="10",
    prospect_chance="0.75",
    name="string(STR_IND_COFFEE_ESTATE)",
    extra_text_fund="string(STR_FUND_COFFEE_ESTATE)",
    location_checks=dict(require_cluster=[72, 4]),
    nearby_station_name="string(STR_STATION_ESTATE)",
    fund_cost_multiplier="54",
    override_default_construction_states=True,
)

industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
    prod_cargo_types_with_multipliers=[
        ("JAVA", 11),
        ("FRUT", 8),
    ],
)
industry.enable_in_economy(
    "BASIC_TROPIC",
    prod_cargo_types_with_multipliers=[
        ("JAVA", 9),
        ("FRUT", 9),
    ],
    locate_in_specific_biomes=[
        "less_west",
    ],
)

industry.add_tile(
    id="coffee_estate_tile_1",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(
        disallow_above_snowline=True,
        disallow_desert=True,
        disallow_industry_adjacent=True,
    ),
)
industry.add_tile(
    id="coffee_estate_tile_2",
    autoslope="return CB_RESULT_AUTOSLOPE",
    location_checks=TileLocationChecks(
        disallow_above_snowline=True,
        disallow_desert=True,
        disallow_industry_adjacent=True,
    ),
)

sprite_ground = industry.add_sprite(sprite_number=3962)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 59, -31, -28)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 59, -31, -28)],
)

industry.add_spritelayout(
    id="coffee_estate_house_spritelayout",
    tile="coffee_estate_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="coffee_estate_shed_spritelayout",
    tile="coffee_estate_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    add_to_object_num=2,
)
industry.add_magic_spritelayout(
    type="slope_aware_trees",
    base_id="coffee_estate_slope_aware_ground_with_trees_1",
    tile="coffee_estate_tile_1",
    config={
        "ground_sprite": 3962,
        "trees_default": [1850, 1850, 1850, 1850, 1850, 1871, 1823, 1850, 1850],
    },
)
industry.add_magic_spritelayout(
    type="slope_aware_trees",
    base_id="coffee_estate_slope_aware_ground_with_trees_2",
    tile="coffee_estate_tile_1",
    config={
        "ground_sprite": 3962,
        "trees_default": [1850, 1850, 1879, 1850, 1856, 1824, 1850, 1850, 1850],
    },
)
industry.add_magic_spritelayout(
    type="slope_aware_trees",
    base_id="coffee_estate_slope_aware_ground_with_trees_3",
    tile="coffee_estate_tile_1",
    config={
        "ground_sprite": 3962,
        "trees_default": [1852, 1850, 1938, 1850, 1850, 1850, 1850, 1881, 1850],
    },
)

industry.add_industry_layout(
    id="coffee_estate_layout_1",
    layout=[
        (0, 0, "coffee_estate_slope_aware_ground_with_trees_2"),
        (0, 1, "coffee_estate_slope_aware_ground_with_trees_3"),
        (0, 2, "coffee_estate_shed_spritelayout"),
        (1, 0, "coffee_estate_slope_aware_ground_with_trees_1"),
        (1, 1, "coffee_estate_slope_aware_ground_with_trees_1"),
        (1, 2, "coffee_estate_house_spritelayout"),
        (2, 1, "coffee_estate_slope_aware_ground_with_trees_2"),
        (2, 2, "coffee_estate_slope_aware_ground_with_trees_1"),
    ],
)
industry.add_industry_layout(
    id="coffee_estate_layout_2",
    layout=[
        (0, 0, "coffee_estate_slope_aware_ground_with_trees_1"),
        (0, 1, "coffee_estate_slope_aware_ground_with_trees_2"),
        (0, 2, "coffee_estate_slope_aware_ground_with_trees_2"),
        (0, 3, "coffee_estate_slope_aware_ground_with_trees_3"),
        (1, 1, "coffee_estate_slope_aware_ground_with_trees_2"),
        (1, 2, "coffee_estate_slope_aware_ground_with_trees_1"),
        (1, 3, "coffee_estate_shed_spritelayout"),
        (1, 4, "coffee_estate_house_spritelayout"),
    ],
)
industry.add_industry_layout(
    id="coffee_estate_layout_3",
    layout=[
        (0, 0, "coffee_estate_slope_aware_ground_with_trees_1"),
        (0, 1, "coffee_estate_slope_aware_ground_with_trees_2"),
        (1, 0, "coffee_estate_slope_aware_ground_with_trees_1"),
        (1, 1, "coffee_estate_house_spritelayout"),
        (2, 0, "coffee_estate_slope_aware_ground_with_trees_3"),
        (2, 1, "coffee_estate_shed_spritelayout"),
        (3, 0, "coffee_estate_slope_aware_ground_with_trees_2"),
        (3, 1, "coffee_estate_slope_aware_ground_with_trees_1"),
    ],
)
industry.add_industry_layout(
    id="coffee_estate_layout_4",
    layout=[
        (0, 0, "coffee_estate_slope_aware_ground_with_trees_1"),
        (0, 1, "coffee_estate_slope_aware_ground_with_trees_2"),
        (0, 3, "coffee_estate_slope_aware_ground_with_trees_3"),
        (0, 4, "coffee_estate_slope_aware_ground_with_trees_2"),
        (1, 0, "coffee_estate_slope_aware_ground_with_trees_1"),
        (1, 1, "coffee_estate_slope_aware_ground_with_trees_2"),
        (1, 3, "coffee_estate_house_spritelayout"),
        (1, 4, "coffee_estate_shed_spritelayout"),
        (3, 0, "coffee_estate_slope_aware_ground_with_trees_1"),
        (3, 1, "coffee_estate_slope_aware_ground_with_trees_2"),
        (3, 3, "coffee_estate_slope_aware_ground_with_trees_1"),
        (3, 4, "coffee_estate_slope_aware_ground_with_trees_2"),
        (4, 0, "coffee_estate_slope_aware_ground_with_trees_1"),
        (4, 1, "coffee_estate_slope_aware_ground_with_trees_1"),
        (4, 3, "coffee_estate_slope_aware_ground_with_trees_1"),
        (4, 4, "coffee_estate_slope_aware_ground_with_trees_2"),
    ],
)
industry.add_industry_layout(
    id="coffee_estate_layout_5",
    layout=[
        (0, 1, "coffee_estate_slope_aware_ground_with_trees_1"),
        (0, 2, "coffee_estate_slope_aware_ground_with_trees_2"),
        (0, 3, "coffee_estate_slope_aware_ground_with_trees_2"),
        (0, 4, "coffee_estate_slope_aware_ground_with_trees_1"),
        (1, 0, "coffee_estate_slope_aware_ground_with_trees_1"),
        (1, 1, "coffee_estate_slope_aware_ground_with_trees_2"),
        (1, 2, "coffee_estate_slope_aware_ground_with_trees_1"),
        (1, 3, "coffee_estate_slope_aware_ground_with_trees_2"),
        (1, 4, "coffee_estate_slope_aware_ground_with_trees_1"),
        (1, 5, "coffee_estate_slope_aware_ground_with_trees_2"),
        (2, 0, "coffee_estate_slope_aware_ground_with_trees_3"),
        (2, 1, "coffee_estate_shed_spritelayout"),
        (2, 2, "coffee_estate_slope_aware_ground_with_trees_2"),
        (2, 3, "coffee_estate_slope_aware_ground_with_trees_1"),
        (2, 4, "coffee_estate_slope_aware_ground_with_trees_2"),
        (2, 5, "coffee_estate_slope_aware_ground_with_trees_1"),
        (3, 1, "coffee_estate_house_spritelayout"),
        (3, 2, "coffee_estate_slope_aware_ground_with_trees_2"),
        (3, 3, "coffee_estate_slope_aware_ground_with_trees_1"),
        (3, 4, "coffee_estate_slope_aware_ground_with_trees_2"),
    ],
)
