from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="field_coal",
    prod_cargo_types_with_multipliers=[("COAL", 20)],
    accept_cargo_types = "AVEH"
    life_type = "IND_LIFE_TYPE_BLACK_HOLE"
    prob_in_game="0",
    prob_map_gen="7",
    map_colour="1",
    colour_scheme_name="scheme_1_elton",
    location_checks=dict(require_cluster=[70, 3]),
    prospect_chance="0.0",
    name="string(STR_IND_FIELD_COAL)",
    nearby_station_name="string(STR_STATION_COLLIERY)",
    fund_cost_multiplier="252",
    pollution_and_squalor_factor=1,
    provides_snow=True,
    primary_production_random_factor_set="wide_range",
    sprites_complete=True,
    animated_tiles_fixed=True,
)
industry.enable_in_economy(
    "WAR_ECONOMY",
    prob_map_gen="3",
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
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="vineyard_shed_spritelayout",
    tile="vineyard_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=None,
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
