from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(
    id="vineyard",
    prod_cargo_types_with_multipliers=[
        ("BEER", 9),
        ("FRUT", 9),
    ],
    map_colour="85",
    prob_in_game="3",
    prob_map_gen="10",
    prospect_chance="0.75",
    name="string(STR_IND_VINEYARD)",
    extra_text_fund="string(STR_FUND_VINEYARD)",
    location_checks=dict(require_cluster=[72, 4]),
    nearby_station_name="string(STR_STATION_WINERY)",
    fund_cost_multiplier="54",
    prod_multiplier="[11, 8]",
    override_default_construction_states=True,
)

industry.enable_in_economy(
    "BASIC_TROPIC",
    locate_in_specific_biomes=[
        "less_west",
    ],
)

industry.add_tile(
    id="vineyard_tile_1",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(
        disallow_above_snowline=True,
        disallow_desert=True,
        disallow_industry_adjacent=True,
    ),
)
industry.add_tile(
    id="vineyard_tile_2",  # house
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
    id="vineyard_house_spritelayout",
    tile="vineyard_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="vineyard_shed_spritelayout",
    tile="vineyard_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_magic_spritelayout(
    type="slope_aware_trees",
    base_id="vineyard_slope_aware_ground_with_trees",
    tile="vineyard_tile_1",
    config={
        "ground_sprite": 4164,
        "trees_default": [1857, 1857, 1857, 1857, 1857, 1857, 1857, 1857, 1857],
    },
)

industry.add_industry_layout(
    id="vineyard_layout_1",
    layout=[
        (0, 0, "vineyard_slope_aware_ground_with_trees"),
        (0, 1, "vineyard_slope_aware_ground_with_trees"),
        (0, 2, "vineyard_shed_spritelayout"),
        (1, 0, "vineyard_slope_aware_ground_with_trees"),
        (1, 1, "vineyard_slope_aware_ground_with_trees"),
        (1, 2, "vineyard_slope_aware_ground_with_trees"),
        (2, 1, "vineyard_slope_aware_ground_with_trees"),
        (2, 2, "vineyard_house_spritelayout"),
    ],
)
industry.add_industry_layout(
    id="vineyard_layout_2",
    layout=[
        (0, 0, "vineyard_slope_aware_ground_with_trees"),
        (0, 1, "vineyard_slope_aware_ground_with_trees"),
        (0, 2, "vineyard_slope_aware_ground_with_trees"),
        (0, 3, "vineyard_slope_aware_ground_with_trees"),
        (1, 1, "vineyard_slope_aware_ground_with_trees"),
        (1, 2, "vineyard_slope_aware_ground_with_trees"),
        (1, 3, "vineyard_house_spritelayout"),
        (1, 4, "vineyard_shed_spritelayout"),
    ],
)
industry.add_industry_layout(
    id="vineyard_layout_3",
    layout=[
        (0, 0, "vineyard_slope_aware_ground_with_trees"),
        (0, 1, "vineyard_slope_aware_ground_with_trees"),
        (1, 0, "vineyard_slope_aware_ground_with_trees"),
        (1, 1, "vineyard_shed_spritelayout"),
        (2, 0, "vineyard_slope_aware_ground_with_trees"),
        (2, 1, "vineyard_house_spritelayout"),
        (3, 0, "vineyard_slope_aware_ground_with_trees"),
        (3, 1, "vineyard_slope_aware_ground_with_trees"),
    ],
)
industry.add_industry_layout(
    id="vineyard_layout_4",
    layout=[
        (0, 0, "vineyard_slope_aware_ground_with_trees"),
        (0, 1, "vineyard_slope_aware_ground_with_trees"),
        (0, 3, "vineyard_slope_aware_ground_with_trees"),
        (0, 4, "vineyard_slope_aware_ground_with_trees"),
        (1, 0, "vineyard_slope_aware_ground_with_trees"),
        (1, 1, "vineyard_slope_aware_ground_with_trees"),
        (1, 3, "vineyard_shed_spritelayout"),
        (1, 4, "vineyard_house_spritelayout"),
        (3, 0, "vineyard_slope_aware_ground_with_trees"),
        (3, 1, "vineyard_slope_aware_ground_with_trees"),
        (3, 3, "vineyard_slope_aware_ground_with_trees"),
        (3, 4, "vineyard_slope_aware_ground_with_trees"),
        (4, 0, "vineyard_slope_aware_ground_with_trees"),
        (4, 1, "vineyard_slope_aware_ground_with_trees"),
        (4, 3, "vineyard_slope_aware_ground_with_trees"),
        (4, 4, "vineyard_slope_aware_ground_with_trees"),
    ],
)
industry.add_industry_layout(
    id="vineyard_layout_5",
    layout=[
        (0, 1, "vineyard_slope_aware_ground_with_trees"),
        (0, 2, "vineyard_slope_aware_ground_with_trees"),
        (0, 3, "vineyard_slope_aware_ground_with_trees"),
        (0, 4, "vineyard_slope_aware_ground_with_trees"),
        (1, 0, "vineyard_slope_aware_ground_with_trees"),
        (1, 1, "vineyard_slope_aware_ground_with_trees"),
        (1, 2, "vineyard_slope_aware_ground_with_trees"),
        (1, 3, "vineyard_slope_aware_ground_with_trees"),
        (1, 4, "vineyard_slope_aware_ground_with_trees"),
        (1, 5, "vineyard_slope_aware_ground_with_trees"),
        (2, 0, "vineyard_slope_aware_ground_with_trees"),
        (2, 1, "vineyard_house_spritelayout"),
        (2, 2, "vineyard_slope_aware_ground_with_trees"),
        (2, 3, "vineyard_slope_aware_ground_with_trees"),
        (2, 4, "vineyard_slope_aware_ground_with_trees"),
        (2, 5, "vineyard_slope_aware_ground_with_trees"),
        (3, 1, "vineyard_shed_spritelayout"),
        (3, 2, "vineyard_slope_aware_ground_with_trees"),
        (3, 3, "vineyard_slope_aware_ground_with_trees"),
        (3, 4, "vineyard_slope_aware_ground_with_trees"),
    ],
)
