from industry import IndustryPrimaryPort, TileLocationChecks

industry = IndustryPrimaryPort(id='port',
                               accept_cargo_types=['FOOD', 'FRUT', 'BEER'],
                               prod_cargo_types=[],
                               prob_in_game='2',
                               prob_random='6',
                               prod_multiplier='[9, 9]',
                               map_colour='186',
                               spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER)',
                               location_checks=dict(same_type_distance=16),
                               prospect_chance='0.75',
                               name='string(STR_IND_PORT)',
                               nearby_station_name='string(STR_STATION_INDUSTRY_HARBOUR_2)',
                               fund_cost_multiplier='152',
                               override_default_construction_states=True)

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['FIRS'].accept_cargo_types = ['GOOD', 'FRUT', 'MNSP']
industry.economy_variations['FIRS'].prod_cargo_types = ['ENSP', 'FMSP']
industry.economy_variations['FIRS'].prod_multiplier = '[9, 7]'

industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].accept_cargo_types = ['BEER', 'GOOD']
industry.economy_variations['BASIC_TEMPERATE'].prod_cargo_types = ['ENSP']
industry.economy_variations['BASIC_TEMPERATE'].prod_multiplier = '[19]'

industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].accept_cargo_types = ['PAPR', 'ZINC']
industry.economy_variations['BASIC_ARCTIC'].prod_cargo_types = ['ENSP']
industry.economy_variations['BASIC_ARCTIC'].prod_multiplier = '[9]'

industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['BASIC_TROPIC'].accept_cargo_types = ['COPR', 'JAVA', 'WOOL']
industry.economy_variations['BASIC_TROPIC'].prod_cargo_types = ['ENSP', 'GOOD']
industry.economy_variations['BASIC_TROPIC'].prod_multiplier = '[8, 17]'

industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].accept_cargo_types = ['WDPR', 'COPR', 'FRUT']
industry.economy_variations['MISTAH_KURTZ'].prod_cargo_types = ['ENSP', 'GOOD']
industry.economy_variations['MISTAH_KURTZ'].prod_multiplier = '[17, 14]'

industry.economy_variations['STEELTOWN'].enabled = True
industry.economy_variations['STEELTOWN'].accept_cargo_types = ['FOOD', 'PIPE']
industry.economy_variations['STEELTOWN'].prod_cargo_types = ['ZINC', 'RUBR']
industry.economy_variations['STEELTOWN'].prod_multiplier = '[16, 16]'

industry.add_tile(id='port_tile_1',
                  land_shape_flags='bitmask(LSF_ONLY_ON_FLAT_LAND)',
                  location_checks=TileLocationChecks(always_allow_founder=False))
industry.add_tile(id='port_tile_2',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  location_checks=TileLocationChecks(always_allow_founder=False,
                                                     require_coast=True))
sprite_ground = industry.add_sprite(
    sprite_number='GROUNDSPRITE_WATER'
)
spriteset_ground_empty = industry.add_spriteset(
    type='empty'
)
spriteset_concrete = industry.add_spriteset(
    sprites=[(10, 10, 64, 39, -31, -8)],
    always_draw=1,
)
spriteset_jetty_se_nw = industry.add_spriteset(
    sprites=[(10, 60, 64, 39, -31, -7)],
    always_draw=1,
)
spriteset_jetty_ne_sw = industry.add_spriteset(
    sprites=[(80, 60, 64, 39, -31, -7)],
    always_draw=1
)
spriteset_jetty_slope_nw_se = industry.add_spriteset(
    sprites=[(150, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_ne_sw = industry.add_spriteset(
    sprites=[(220, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_se_nw = industry.add_spriteset(
    sprites=[(290, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_sw_ne = industry.add_spriteset(
    sprites=[(360, 60, 64, 39, -31, -7)],
)
spriteset_warehouse = industry.add_spriteset(
    sprites=[(440, 10, 64, 74, -31, -34)],
    zoffset=18
)
spriteset_9 = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, 0)],
    yoffset=4,
    zoffset=27,
    yextent=12,

)
spriteset_9b = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, 0)],
    xoffset=5,
    zoffset=40,
    xextent=11,

)
spriteset_10 = industry.add_spriteset(
    sprites=[(220, 10, 64, 39, -31, -7)],
    yoffset=4,
    zoffset=27,
    yextent=12,
)
spriteset_11 = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -35, -15)],
)
spriteset_12 = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -31, -14)],
)
spriteset_13 = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -31, -8)],
)
spriteset_14 = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -27, -12)],
)
spriteset_15 = industry.add_spriteset(
    sprites=[(290, 110, 64, 39, -15, -11)],
)
spriteset_16 = industry.add_spriteset(
    sprites=[(360, 110, 64, 39, -45, -15)],
)
spriteset_truck = industry.add_spriteset(
    sprites=[(360, 10, 64, 39, -31, 0)],
    zoffset=18,
)
# spritelayout numbers have gaps for historical reasons
industry.add_spritelayout(
    id='port_spritelayout_2',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_truck]
)
industry.add_spritelayout(
    id='port_spritelayout_11',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_concrete, spriteset_warehouse]
)
industry.add_spritelayout(
    id='port_spritelayout_12',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_ne_sw, spriteset_concrete, spriteset_warehouse]
)
industry.add_spritelayout(
    id='port_spritelayout_13',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_warehouse]
)
industry.add_spritelayout(
    id='port_spritelayout_21',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_11]
)
industry.add_spritelayout(
    id='port_spritelayout_22',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_12]
)
industry.add_spritelayout(
    id='port_spritelayout_23',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_13]
)
industry.add_spritelayout(
    id='port_spritelayout_24',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_14]
)
industry.add_spritelayout(
    id='port_spritelayout_25',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_14]
)
industry.add_spritelayout(
    id='port_spritelayout_26',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_15]
)
industry.add_spritelayout(
    id='port_spritelayout_27',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_16]
)
industry.add_spritelayout(
    id='port_spritelayout_28',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_9]
)
industry.add_spritelayout(
    id='port_spritelayout_29',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_10]
)
industry.add_spritelayout(
    id='port_spritelayout_30',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_9b]
)
industry.add_spritelayout(
    id='port_spritelayout_null',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[]
)
industry.add_magic_spritelayout(
    type='harbour_coast_foundations',
    base_id='port_spritelayout_coast_warehouse',
    config={'ground_sprite': spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
            'building_sprites': [spriteset_concrete, spriteset_warehouse],
            'foundation_sprites': {'ne_sw': spriteset_jetty_ne_sw,
                                   'se_nw': spriteset_jetty_se_nw,
                                   'slope_nw_se': spriteset_jetty_slope_nw_se,
                                   'slope_ne_sw': spriteset_jetty_slope_ne_sw,
                                   'slope_se_nw': spriteset_jetty_slope_se_nw,
                                   'slope_sw_ne': spriteset_jetty_slope_sw_ne}}
)
industry.add_magic_spritelayout(
    type='harbour_coast_foundations',
    base_id='port_spritelayout_coast_truck',
    config={'ground_sprite': spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
            'building_sprites': [spriteset_concrete, spriteset_truck],
            'foundation_sprites': {'ne_sw': spriteset_jetty_ne_sw,
                                   'se_nw': spriteset_jetty_se_nw,
                                   'slope_nw_se': spriteset_jetty_slope_nw_se,
                                   'slope_ne_sw': spriteset_jetty_slope_ne_sw,
                                   'slope_se_nw': spriteset_jetty_slope_se_nw,
                                   'slope_sw_ne': spriteset_jetty_slope_sw_ne}}
)

industry.add_industry_layout(
    id='port_industry_layout_1',
    layout=[(0, 3, 'port_tile_1', 'port_spritelayout_27'),
            (0, 4, 'port_tile_2', 'port_spritelayout_coast_truck'),
            (1, 0, '255', 'port_spritelayout_null'),
            (1, 1, 'port_tile_1', 'port_spritelayout_11'),
            (1, 2, 'port_tile_1', 'port_spritelayout_29'),
            (1, 3, 'port_tile_1', 'port_spritelayout_11'),
            (1, 4, 'port_tile_2', 'port_spritelayout_coast_warehouse'),
            (2, 1, 'port_tile_1', 'port_spritelayout_24'),
            (2, 2, 'port_tile_1', 'port_spritelayout_24'),
            ]
)
industry.add_industry_layout(
    id='port_industry_layout_2',
    layout=[(0, 0, '255', 'port_spritelayout_null'),
            (0, 1, '255', 'port_spritelayout_null'),
            (0, 2, '255', 'port_spritelayout_null'),
            (1, 0, 'port_tile_1', 'port_spritelayout_23'),
            (1, 1, 'port_tile_1', 'port_spritelayout_23'),
            (1, 255, '255', 'port_spritelayout_null'),
            (2, 0, 'port_tile_1', 'port_spritelayout_30'),
            (2, 1, 'port_tile_1', 'port_spritelayout_12'),
            (2, 2, 'port_tile_1', 'port_spritelayout_21'),
            (2, 255, '255', 'port_spritelayout_null'),
            (3, 1, 'port_tile_2', 'port_spritelayout_coast_warehouse'),
            (3, 2, 'port_tile_2', 'port_spritelayout_coast_truck'),
            ]
)
industry.add_industry_layout(
    id='port_industry_layout_3',
    layout=[(0, 0, 'port_tile_2', 'port_spritelayout_coast_warehouse'),
            (0, 1, 'port_tile_2', 'port_spritelayout_coast_warehouse'),
            (0, 2, 'port_tile_2', 'port_spritelayout_coast_warehouse'),
            (1, 0, 'port_tile_1', 'port_spritelayout_24'),
            (1, 2, 'port_tile_1', 'port_spritelayout_2'),
            (2, 1, 'port_tile_1', 'port_spritelayout_26'),
            (2, 2, 'port_tile_1', 'port_spritelayout_28'),
            (2, 3, 'port_tile_1', 'port_spritelayout_22'),
            (2, 4, '255', 'port_spritelayout_null'),
            (3, 2, '255', 'port_spritelayout_null'),
            (3, 3, '255', 'port_spritelayout_null'),
            ]
)
industry.add_industry_layout(
    id='port_industry_layout_4',
    layout=[(0, 0, 'port_tile_2', 'port_spritelayout_coast_warehouse'),
            (0, 1, 'port_tile_1', 'port_spritelayout_2'),
            (0, 2, 'port_tile_1', 'port_spritelayout_29'),
            (0, 3, 'port_tile_1', 'port_spritelayout_11'),
            (0, 4, 'port_tile_1', 'port_spritelayout_28'),
            (0, 5, '255', 'port_spritelayout_null'),
            (1, 0, 'port_tile_2', 'port_spritelayout_coast_warehouse'),
            (1, 1, 'port_tile_1', 'port_spritelayout_28'),
            (1, 2, 'port_tile_1', 'port_spritelayout_25'),
            (1, 4, 'port_tile_1', 'port_spritelayout_25'),
            (1, 5, '255', 'port_spritelayout_null'),
            (2, 3, '255', 'port_spritelayout_null'),
            (2, 4, '255', 'port_spritelayout_null'),
            (2, 5, '255', 'port_spritelayout_null'),
            ]
)
industry.add_industry_layout(
    id='port_industry_layout_5',
    layout=[(0, 0, 'port_tile_2', 'port_spritelayout_coast_warehouse'),
            (1, 0, 'port_tile_1', 'port_spritelayout_12'),
            (1, 2, '255', 'port_spritelayout_null'),
            (2, 0, 'port_tile_1', 'port_spritelayout_12'),
            (2, 1, 'port_tile_1', 'port_spritelayout_29'),
            (2, 2, 'port_tile_1', 'port_spritelayout_28'),
            (2, 3, '255', 'port_spritelayout_null'),
            (3, 0, 'port_tile_1', 'port_spritelayout_12'),
            (3, 1, 'port_tile_1', 'port_spritelayout_2'),
            (3, 2, 'port_tile_1', 'port_spritelayout_28'),
            (3, 3, '255', 'port_spritelayout_null'),
            (4, 255, '255', 'port_spritelayout_null'),
            (4, 0, 'port_tile_1', 'port_spritelayout_13'),
            (4, 1, 'port_tile_1', 'port_spritelayout_24'),
            (4, 2, 'port_tile_1', 'port_spritelayout_24'),
            (4, 3, '255', 'port_spritelayout_null'),
            (5, 255, '255', 'port_spritelayout_null'),
            (5, 0, '255', 'port_spritelayout_null'),
            (5, 1, '255', 'port_spritelayout_null'),
            (5, 2, '255', 'port_spritelayout_null'),
            (5, 3, '255', 'port_spritelayout_null'),
            ]
)
