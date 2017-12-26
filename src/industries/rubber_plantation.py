from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(id='rubber_plantation',
                                  map_colour='121',
                                  prob_in_game='4',
                                  prob_random='11',
                                  prospect_chance='0.75',
                                  name='TTD_STR_INDUSTRY_NAME_RUBBER_PLANTATION',
                                  extra_text_fund='string(STR_FUND_RUBBER_PLANTATION)',
                                  nearby_station_name='string(STR_STATION_TAPPERS_SHED)',
                                  location_checks=dict(cluster=[72, 4]),
                                  prod_cargo_types=['RUBR'],
                                  fund_cost_multiplier='54',
                                  prod_multiplier='[16]',
                                  override_default_construction_states=True)

industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.add_tile(id='rubber_plantation_tile_1',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='rubber_plantation_tile_2',  # house
                  autoslope='return CB_RESULT_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))


sprite_ground = industry.add_sprite(
    sprite_number=3962
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 59, -31, -28)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 59, -31, -28)],
)

industry.add_spritelayout(
    id='rubber_plantation_house_spritelayout',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id='rubber_plantation_shed_spritelayout',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)
industry.add_magic_spritelayout(
    type='slope_aware_trees',
    base_id='rubber_plantation_slope_aware_ground_with_trees_1',
    config={'ground_sprite': 4145,
            'trees_default': [1908, 1908, 1908, 1908]}
)
industry.add_magic_spritelayout(
    type='slope_aware_trees',
    base_id='rubber_plantation_slope_aware_ground_with_trees_2',
    config={'ground_sprite': 4145,
            'trees_default': [1906, 1905, 1905, 1907]}
)

industry.add_industry_layout(
    id='rubber_plantation_layout_1',
    layout=[(0, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (0, 2, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 2, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
            (2, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_2'),
            (2, 2, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
            ]
)
industry.add_industry_layout(
    id='rubber_plantation_layout_2',
    layout=[(0, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (0, 2, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
            (0, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 2, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_2'),
            (1, 4, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
            ]
)
industry.add_industry_layout(
    id='rubber_plantation_layout_3',
    layout=[(0, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_2'),
            (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (2, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (2, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (3, 0, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
            (3, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_2'),
            (4, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (4, 1, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
            ]
)
industry.add_industry_layout(
    id='rubber_plantation_layout_4',
    layout=[(0, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (0, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (0, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (3, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (3, 1, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
            (3, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (3, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (4, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_2'),
            (4, 1, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
            (4, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (4, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            ]
)
industry.add_industry_layout(
    id='rubber_plantation_layout_5',
    layout=[(0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (0, 2, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (0, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (0, 5, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 2, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
            (1, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 5, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (1, 6, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (2, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (2, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (2, 2, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
            (2, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (2, 5, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (2, 6, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (3, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (3, 2, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_2'),
            (3, 5, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            (3, 6, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees_1'),
            ]
)
