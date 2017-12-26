from industry import IndustryPrimaryPort, TileLocationChecks

industry = IndustryPrimaryPort(id='wharf',
                               accept_cargo_types=['FOOD', 'FRUT', 'BEER'],
                               prod_cargo_types=[],
                               prob_in_game='2',
                               prob_random='6',
                               prod_multiplier='[7, 6]',
                               map_colour='37',
                               spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER)',
                               location_checks=dict(same_type_distance=16),
                               prospect_chance='0.75',
                               name='string(STR_IND_WHARF)',
                               nearby_station_name='string(STR_STATION_INDUSTRY_HARBOUR_3)',
                               fund_cost_multiplier='152',
                               override_default_construction_states=True)

# in Steeltown, there is a deliberate feedback loop with COPR > POWR + ENSP > more COPR (and more ENSP)
# this is to allow an easy kickstart of ENSP, when all other chains are so tightly connected
industry.economy_variations['STEELTOWN'].enabled = True
industry.economy_variations['STEELTOWN'].accept_cargo_types = ['FMSP', 'POWR']
industry.economy_variations['STEELTOWN'].prod_cargo_types = ['COPR', 'ENSP']
industry.economy_variations['STEELTOWN'].prod_multiplier = '[16, 12]'
industry.economy_variations['STEELTOWN'].name = 'string(STR_IND_WHARF)'

industry.add_tile(id='wharf_tile_1',
                  land_shape_flags='bitmask(LSF_ONLY_ON_FLAT_LAND)',
                  location_checks=TileLocationChecks(always_allow_founder=False))
industry.add_tile(id='wharf_tile_2',
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
spriteset_large_warehouse = industry.add_spriteset(
    sprites=[(80, 10, 64, 39, -31, 0)],
    zoffset=18
)
spriteset_9 = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, 0)],
    yoffset=4,
    zoffset=27,
    yextent=12,

)
spriteset_9b = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, -7)],
    xoffset=0,
    zoffset=12,
    xextent=11,

)
spriteset_10 = industry.add_spriteset(
    sprites=[(220, 10, 64, 39, -31, -7)],
    yoffset=0,
    zoffset=12,
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
spriteset_small_warehouse = industry.add_spriteset(
    sprites=[(360, 10, 64, 39, -31, 0)],
    zoffset=18,
)

industry.add_spritelayout(
    id='wharf_spritelayout_11',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_concrete, spriteset_large_warehouse]
)
industry.add_spritelayout(
    id='wharf_spritelayout_12',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_warehouse]
)
industry.add_spritelayout(
    id='wharf_spritelayout_13',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_warehouse]
)
industry.add_spritelayout(
    id='wharf_spritelayout_21',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_11]
)
industry.add_spritelayout(
    id='wharf_spritelayout_22',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_12]
)
industry.add_spritelayout(
    id='wharf_spritelayout_23',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_13]
)
industry.add_spritelayout(
    id='wharf_spritelayout_24',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_14]
)
industry.add_spritelayout(
    id='wharf_spritelayout_25',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_14]
)
industry.add_spritelayout(
    id='wharf_spritelayout_26',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[]
)
industry.add_spritelayout(
    id='wharf_spritelayout_27',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[]
)
# wharf_spritelayout_28 fell out of use and was removed
industry.add_spritelayout(
    id='wharf_spritelayout_29',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_10]
)
industry.add_spritelayout(
    id='wharf_spritelayout_30',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_9b]
)
industry.add_spritelayout(
    id='wharf_spritelayout_null',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[]
)
industry.add_magic_spritelayout(
    type='harbour_coast_foundations',
    base_id='wharf_spritelayout_coast_small_warehouse',
    config={'ground_sprite': spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
            'building_sprites': [spriteset_concrete, spriteset_small_warehouse],
            'foundation_sprites': {'ne_sw': spriteset_jetty_ne_sw,
                                   'se_nw': spriteset_jetty_se_nw,
                                   'slope_nw_se': spriteset_jetty_slope_nw_se,
                                   'slope_ne_sw': spriteset_jetty_slope_ne_sw,
                                   'slope_se_nw': spriteset_jetty_slope_se_nw,
                                   'slope_sw_ne': spriteset_jetty_slope_sw_ne}}
)
industry.add_magic_spritelayout(
    type='harbour_coast_foundations',
    base_id='wharf_spritelayout_coast_large_warehouse',
    config={'ground_sprite': spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
            'building_sprites': [spriteset_concrete, spriteset_large_warehouse],
            'foundation_sprites': {'ne_sw': spriteset_jetty_ne_sw,
                                   'se_nw': spriteset_jetty_se_nw,
                                   'slope_nw_se': spriteset_jetty_slope_nw_se,
                                   'slope_ne_sw': spriteset_jetty_slope_ne_sw,
                                   'slope_se_nw': spriteset_jetty_slope_se_nw,
                                   'slope_sw_ne': spriteset_jetty_slope_sw_ne}}
)

industry.add_industry_layout(
    id='wharf_industry_layout_1',
    layout=[(0, 2, 'wharf_tile_1', 'wharf_spritelayout_27'),
            (0, 3, 'wharf_tile_2', 'wharf_spritelayout_coast_small_warehouse'),
            (1, 0, '255', 'wharf_spritelayout_null'),
            (1, 1, 'wharf_tile_1', 'wharf_spritelayout_11'),
            (1, 2, 'wharf_tile_1', 'wharf_spritelayout_29'),
            (1, 3, 'wharf_tile_2', 'wharf_spritelayout_coast_large_warehouse'),
            (2, 1, 'wharf_tile_1', 'wharf_spritelayout_24'),
            (2, 2, 'wharf_tile_1', 'wharf_spritelayout_24'),
            ]
)
industry.add_industry_layout(
    id='wharf_industry_layout_2',
    layout=[(0, 0, '255', 'wharf_spritelayout_null'),
            (0, 1, '255', 'wharf_spritelayout_null'),
            (0, 2, '255', 'wharf_spritelayout_null'),
            (1, 0, 'wharf_tile_1', 'wharf_spritelayout_23'),
            (1, 1, 'wharf_tile_1', 'wharf_spritelayout_23'),
            (1, 255, '255', 'wharf_spritelayout_null'),
            (2, 0, 'wharf_tile_1', 'wharf_spritelayout_30'),
            (2, 1, 'wharf_tile_1', 'wharf_spritelayout_12'),
            (2, 2, 'wharf_tile_1', 'wharf_spritelayout_21'),
            (2, 255, '255', 'wharf_spritelayout_null'),
            (3, 1, 'wharf_tile_2', 'wharf_spritelayout_coast_large_warehouse'),
            (3, 2, 'wharf_tile_2', 'wharf_spritelayout_coast_small_warehouse'),
            ]
)
industry.add_industry_layout(
    id='wharf_industry_layout_3',
    layout=[(0, 0, 'wharf_tile_2', 'wharf_spritelayout_coast_large_warehouse'),
            (0, 1, 'wharf_tile_2', 'wharf_spritelayout_coast_large_warehouse'),
            (0, 2, 'wharf_tile_2', 'wharf_spritelayout_coast_small_warehouse'),
            (1, 0, 'wharf_tile_1', 'wharf_spritelayout_24'),
            (1, 2, 'wharf_tile_1', 'wharf_spritelayout_30'),
            (2, 1, 'wharf_tile_1', 'wharf_spritelayout_26'),
            (2, 2, 'wharf_tile_1', 'wharf_spritelayout_29'),
            (2, 3, 'wharf_tile_1', 'wharf_spritelayout_22'),
            (2, 4, '255', 'wharf_spritelayout_null'),
            (3, 2, '255', 'wharf_spritelayout_null'),
            (3, 3, '255', 'wharf_spritelayout_null'),
            ]
)
industry.add_industry_layout(
    id='wharf_industry_layout_4',
    layout=[(0, 0, 'wharf_tile_2', 'wharf_spritelayout_coast_large_warehouse'),
            (0, 1, '255', 'wharf_spritelayout_null'),
            (1, 0, 'wharf_tile_2', 'wharf_spritelayout_coast_large_warehouse'),
            (1, 1, 'wharf_tile_1', 'wharf_spritelayout_29'),
            (1, 2, 'wharf_tile_1', 'wharf_spritelayout_30'),
            (1, 3, '255', 'wharf_spritelayout_null'),
            (2, 0, 'wharf_tile_2', 'wharf_spritelayout_coast_small_warehouse'),
            (2, 1, 'wharf_tile_1', 'wharf_spritelayout_25'),
            (2, 2, '255', 'wharf_spritelayout_null'),
            (3, 2, '255', 'wharf_spritelayout_null'),
            (3, 3, '255', 'wharf_spritelayout_null'),
            ]
)
industry.add_industry_layout(
    id='wharf_industry_layout_5',
    layout=[(0, 0, 'wharf_tile_2', 'wharf_spritelayout_coast_small_warehouse'),
            (1, 0, 'wharf_tile_2', 'wharf_spritelayout_coast_large_warehouse'),
            (1, 2, '255', 'wharf_spritelayout_null'),
            (2, 0, 'wharf_tile_1', 'wharf_spritelayout_13'),
            (2, 1, 'wharf_tile_1', 'wharf_spritelayout_29'),
            (2, 2, 'wharf_tile_1', 'wharf_spritelayout_30'),
            (2, 3, '255', 'wharf_spritelayout_null'),
            (3, 255, '255', 'wharf_spritelayout_null'),
            (3, 0, 'wharf_tile_1', 'wharf_spritelayout_24'),
            (3, 1, 'wharf_tile_1', 'wharf_spritelayout_24'),
            (3, 2, 'wharf_tile_1', 'wharf_spritelayout_24'),
            (3, 3, '255', 'wharf_spritelayout_null'),
            (4, 255, '255', 'wharf_spritelayout_null'),
            (4, 0, '255', 'wharf_spritelayout_null'),
            (4, 1, '255', 'wharf_spritelayout_null'),
            (4, 2, '255', 'wharf_spritelayout_null'),
            (4, 3, '255', 'wharf_spritelayout_null'),
            ]
)
