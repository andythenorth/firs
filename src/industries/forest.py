from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(id='forest',
                                  prob_in_game='3',
                                  prob_random='10',
                                  map_colour='83',
                                  prospect_chance='0.75',
                                  prod_cargo_types=['WOOD'],
                                  location_checks=dict(cluster=[72, 3]),
                                  name='TTD_STR_INDUSTRY_NAME_FOREST',
                                  extra_text_fund='string(STR_FUND_FOREST)',
                                  fund_cost_multiplier='95',
                                  prod_multiplier='[19]',
                                  substitute='INDUSTRYTYPE_FOREST',
                                  nearby_station_name='string(STR_STATION_FOREST)',
                                  graphics_change_dates=[1935, 1990],
                                  override_default_construction_states=True)

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].prod_cargo_types = ['WOOD']
industry.economy_variations['BASIC_ARCTIC'].prod_multiplier = '[24]'
industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.add_tile(id='forest_tile_1',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='forest_tile_2',
                  location_checks=TileLocationChecks(disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 78, -31, -45)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 78, -31, -45)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 78, -31, -45)],
)

industry.add_spritelayout(
    id='forest_equipment_spritelayout',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1, spriteset_2],
)
industry.add_spritelayout(
    id='forest_wood_stack_spritelayout',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_magic_spritelayout(
    type='slope_aware_trees',
    base_id='forest_slope_aware_ground_with_trees_uniform',
    config={'ground_sprite': 3943,
            'trees_default': [1712, 1712, 1712, 1712, 1712, 1712, 1712, 1712, 1712],
            'trees_snow': [1768, 1768, 1768, 1768, 1768, 1768, 1768, 1768, 1768],
            'trees_tropic': [1838, 1838, 1838, 1838, 1838, 1838, 1838, 1838, 1838]}
)
industry.add_magic_spritelayout(
    type='slope_aware_trees',
    base_id='forest_slope_aware_ground_with_trees_dying',
    config={'ground_sprite': 3943,
            'trees_default': [1715, 1595, 1710, 1714],
            'trees_snow': [1771, 1767, 1766, 1770],
            'trees_tropic': [1870, 1839, 1873, 1836]}
)


industry.add_industry_layout(
    id='forest_layout_1',
    layout=[(0, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (0, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (0, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
            (2, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (2, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (2, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
            (3, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
            (3, 1, 'forest_tile_2', 'forest_wood_stack_spritelayout'),
            (3, 2, 'forest_tile_2', 'forest_equipment_spritelayout')
            ]
)
industry.add_industry_layout(
    id='forest_layout_2',
    layout=[(0, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (0, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (0, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (0, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (0, 4, 'forest_tile_2', 'forest_equipment_spritelayout'),
            (1, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
            (1, 4, 'forest_tile_2', 'forest_wood_stack_spritelayout'),
            (2, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (2, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (2, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (2, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
            (2, 4, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying')
            ]
)
industry.add_industry_layout(
    id='forest_layout_3',
    layout=[(0, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (0, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (0, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (0, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (2, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (2, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
            (2, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
            (2, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
            (3, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
            (3, 1, 'forest_tile_2', 'forest_wood_stack_spritelayout'),
            (3, 2, 'forest_tile_2', 'forest_equipment_spritelayout'),
            (3, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying')
            ]
)
industry.add_industry_layout(
    id='forest_layout_4',
    layout=[(0, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (0, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (0, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (0, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (1, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
            (2, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (2, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (2, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
            (2, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
            (3, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (3, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying'),
            (3, 2, 'forest_tile_2', 'forest_equipment_spritelayout'),
            (4, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (4, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (4, 2, 'forest_tile_2', 'forest_wood_stack_spritelayout'),
            (5, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (5, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_uniform'),
            (5, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees_dying')
            ]
)
