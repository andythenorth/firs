"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryPort, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryPort(id='port',
                    accept_cargo_types=['FOOD', 'FRUT', 'BEER'],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=[],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[9, 9]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='186',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='2',
                    spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER)',
                    location_checks=IndustryLocationChecks(incompatible={'port': 48}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_PORT)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_IND_PORT))',
                    fund_cost_multiplier='152',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    override_default_construction_states=True)

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['FIRS'].accept_cargo_types = ['GOOD', 'FRUT', 'MNSP']
industry.economy_variations['FIRS'].prod_cargo_types = ['ENSP']
industry.economy_variations['FIRS'].prod_multiplier = '[9]'
industry.economy_variations['FIRS'].prob_random = '3'

industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].accept_cargo_types = ['BEER', 'GOOD']
industry.economy_variations['BASIC_TEMPERATE'].prod_cargo_types = ['ENSP']
industry.economy_variations['BASIC_TEMPERATE'].prod_multiplier = '[19, 0]'

industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].accept_cargo_types = ['PAPR', 'BEER', 'FOOD']
industry.economy_variations['BASIC_ARCTIC'].prod_cargo_types = ['ENSP', 'GOOD']
industry.economy_variations['BASIC_ARCTIC'].prod_multiplier = '[7, 16]'

industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['BASIC_TROPIC'].accept_cargo_types = ['WOOL', 'JAVA', 'COPR']
industry.economy_variations['BASIC_TROPIC'].prod_cargo_types = ['ENSP', 'GOOD']
industry.economy_variations['BASIC_TROPIC'].prod_multiplier = '[17, 17]'

industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].accept_cargo_types = ['WOOD', 'FICR', 'FRUT']
industry.economy_variations['MISTAH_KURTZ'].prod_cargo_types = ['ENSP', 'MNSP']

industry.add_tile(id='port_tile_1',
                  land_shape_flags='bitmask(LSF_ONLY_ON_FLAT_LAND)',
                  location_checks=TileLocationChecks(always_allow_founder=False))
industry.add_tile(id='port_tile_2',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  location_checks=TileLocationChecks(always_allow_founder=False,
                                                     require_coast=True))
sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDSPRITE_WATER'
)
spriteset_ground_empty = industry.add_spriteset(
    id = 'port_spriteset_ground',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'port_spriteset_1',
    sprites = [(10, 10, 64, 39, -31, -8)],
    always_draw = 1,
)
spriteset_2 = industry.add_spriteset(
    id = 'port_spriteset_2',
    sprites = [(10, 60, 64, 39, -31, -7)],
    zextent = 7,
    always_draw = 1,
)
spriteset_3 = industry.add_spriteset(
    id = 'port_spriteset_3',
    sprites = [(80, 60, 64, 39, -31, -7)],
    zextent = 7,
    always_draw = 1
)
spriteset_4 = industry.add_spriteset(
    id = 'port_spriteset_4',
    sprites = [(150, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_5 = industry.add_spriteset(
    id = 'port_spriteset_5',
    sprites = [(220, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_6 = industry.add_spriteset(
    id = 'port_spriteset_6',
    sprites = [(290, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_7 = industry.add_spriteset(
    id = 'port_spriteset_7',
    sprites = [(360, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_8 = industry.add_spriteset(
    id = 'port_spriteset_8',
    sprites = [(440, 10, 64, 74, -31, -34)],
    zoffset = 18
)
spriteset_9 = industry.add_spriteset(
    id = 'port_spriteset_9',
    sprites = [(150, 10, 64, 39, -31, 0)],
    yoffset = 4,
    zoffset = 27,
    yextent = 12,

)
spriteset_9b = industry.add_spriteset(
    id = 'port_spriteset_9b',
    sprites = [(150, 10, 64, 39, -31, 0)],
    xoffset = 5,
    zoffset = 40,
    xextent = 11,

)
spriteset_10 = industry.add_spriteset(
    id = 'port_spriteset_10',
    sprites = [(220, 10, 64, 39, -31, -7)],
    yoffset = 4,
    zoffset = 27,
    yextent = 12,
)
spriteset_11 = industry.add_spriteset(
    id = 'port_spriteset_11',
    sprites = [(10, 110, 64, 39, -35, -15)],
)
spriteset_12 = industry.add_spriteset(
    id = 'port_spriteset_12',
    sprites = [(80, 110, 64, 39, -31, -14)],
)
spriteset_13 = industry.add_spriteset(
    id = 'port_spriteset_13',
    sprites = [(150, 110, 64, 39, -31, -8)],
)
spriteset_14 = industry.add_spriteset(
    id = 'port_spriteset_14',
    sprites = [(220, 110, 64, 39, -27, -12)],
)
spriteset_15 = industry.add_spriteset(
    id = 'port_spriteset_15',
    sprites = [(290, 110, 64, 39, -15, -11)],
)
spriteset_16 = industry.add_spriteset(
    id = 'port_spriteset_16',
    sprites = [(360, 110, 64, 39, -45, -15)],
)
spriteset_17 = industry.add_spriteset(
    id = 'port_spriteset_17',
    sprites = [(360, 10, 64, 39, -31, 0)],
    zoffset = 18,
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_1_1',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_1]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_1_2',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_7, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_1_3',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_2, spriteset_3, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_1_4',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_3, spriteset_4, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_1_5',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_5, spriteset_4, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_1_6',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_5, spriteset_2, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_1_7',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_6, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_1_8',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_6, spriteset_7, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_2_1',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_7, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_2_2',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_2_3',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_2, spriteset_3, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_2_4',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_3, spriteset_4, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_2_5',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_5, spriteset_4, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_2_6',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_5, spriteset_2, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_2_7',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_6, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'port_spritelayout_land_tile_2_8',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_6, spriteset_7, spriteset_1, spriteset_8]
)
# spritelayout numbers have gaps for historical reasons
industry.add_spritelayout(
    id = 'port_spritelayout_2',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_2, spriteset_3, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'port_spritelayout_11',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_2, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'port_spritelayout_12',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_3, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'port_spritelayout_13',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_2, spriteset_3, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'port_spritelayout_21',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_11]
)
industry.add_spritelayout(
    id = 'port_spritelayout_22',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_12]
)
industry.add_spritelayout(
    id = 'port_spritelayout_23',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_13]
)
industry.add_spritelayout(
    id = 'port_spritelayout_24',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_14]
)
industry.add_spritelayout(
    id = 'port_spritelayout_25',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_14]
)
industry.add_spritelayout(
    id = 'port_spritelayout_26',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_15]
)
industry.add_spritelayout(
    id = 'port_spritelayout_27',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_16]
)
industry.add_spritelayout(
    id = 'port_spritelayout_28',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_2, spriteset_3, spriteset_1, spriteset_9]
)
industry.add_spritelayout(
    id = 'port_spritelayout_29',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_2, spriteset_3, spriteset_1, spriteset_10]
)
industry.add_spritelayout(
    id = 'port_spritelayout_30',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_2, spriteset_3, spriteset_1, spriteset_9b]
)
industry.add_spritelayout(
    id = 'port_spritelayout_null',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = []
)

slope_switch_1 = industry.add_slope_graphics_switch('port_slope_switch_1',
                                                    slope_spritelayout_mapping={0: 'port_spritelayout_land_tile_1_1',
                                                                                1: 'port_spritelayout_land_tile_1_4',
                                                                                2: 'port_spritelayout_land_tile_1_8',
                                                                                3: 'port_spritelayout_land_tile_1_2',
                                                                                4: 'port_spritelayout_land_tile_1_6',
                                                                                5: 'port_spritelayout_land_tile_1_5',
                                                                                6: 'port_spritelayout_land_tile_1_7',
                                                                                7: 'port_spritelayout_land_tile_1_1',
                                                                                8: 'port_spritelayout_land_tile_1_3',
                                                                                9: 'port_spritelayout_land_tile_1_4',
                                                                                10: 'port_spritelayout_land_tile_1_8',
                                                                                11: 'port_spritelayout_land_tile_1_2',
                                                                                12: 'port_spritelayout_land_tile_1_6',
                                                                                13: 'port_spritelayout_land_tile_1_5',
                                                                                14: 'port_spritelayout_land_tile_1_7'},
                                                    default_result='port_spritelayout_land_tile_1_1')

slope_switch_2 = industry.add_slope_graphics_switch('port_slope_switch_2',
                                                    slope_spritelayout_mapping={0: 'port_spritelayout_land_tile_2_2',
                                                                                1: 'port_spritelayout_land_tile_2_4',
                                                                                2: 'port_spritelayout_land_tile_2_8',
                                                                                3: 'port_spritelayout_land_tile_2_1',
                                                                                4: 'port_spritelayout_land_tile_2_6',
                                                                                5: 'port_spritelayout_land_tile_2_5',
                                                                                6: 'port_spritelayout_land_tile_2_7',
                                                                                7: 'port_spritelayout_land_tile_2_2',
                                                                                8: 'port_spritelayout_land_tile_2_3',
                                                                                9: 'port_spritelayout_land_tile_2_4',
                                                                                10: 'port_spritelayout_land_tile_2_8',
                                                                                11: 'port_spritelayout_land_tile_2_1',
                                                                                12: 'port_spritelayout_land_tile_2_6',
                                                                                13: 'port_spritelayout_land_tile_2_5',
                                                                                14: 'port_spritelayout_land_tile_2_7'},
                                                    default_result='port_spritelayout_land_tile_2_2')

industry.add_industry_layout(
    id = 'port_industry_layout_1',
    layout = [(0, 3, 'port_tile_1', 'port_spritelayout_27'),
              (0, 4, 'port_tile_2', slope_switch_1),
              (1, 0, '255', 'port_spritelayout_null'),
              (1, 1, 'port_tile_1', 'port_spritelayout_11'),
              (1, 2, 'port_tile_1', 'port_spritelayout_29'),
              (1, 3, 'port_tile_1', 'port_spritelayout_11'),
              (1, 4, 'port_tile_2', slope_switch_2),
              (2, 1, 'port_tile_1', 'port_spritelayout_24'),
              (2, 2, 'port_tile_1', 'port_spritelayout_24'),
    ]
)
industry.add_industry_layout(
    id = 'port_industry_layout_2',
    layout = [(0, 0, '255', 'port_spritelayout_null'),
              (0, 1, '255', 'port_spritelayout_null'),
              (0, 2, '255', 'port_spritelayout_null'),
              (1, 0, 'port_tile_1', 'port_spritelayout_23'),
              (1, 1, 'port_tile_1', 'port_spritelayout_23'),
              (1, 255, '255', 'port_spritelayout_null'),
              (2, 0, 'port_tile_1', 'port_spritelayout_30'),
              (2, 1, 'port_tile_1', 'port_spritelayout_12'),
              (2, 2, 'port_tile_1', 'port_spritelayout_21'),
              (2, 255, '255', 'port_spritelayout_null'),
              (3, 1, 'port_tile_2', slope_switch_2),
              (3, 2, 'port_tile_2', slope_switch_1),
    ]
)
industry.add_industry_layout(
    id = 'port_industry_layout_3',
    layout = [(0, 0, 'port_tile_2', slope_switch_2),
              (0, 1, 'port_tile_2', slope_switch_2),
              (0, 2, 'port_tile_2', slope_switch_2),
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
    id = 'port_industry_layout_4',
    layout = [(0, 0, 'port_tile_2', slope_switch_2),
              (0, 1, 'port_tile_1', 'port_spritelayout_2'),
              (0, 2, 'port_tile_1', 'port_spritelayout_29'),
              (0, 3, 'port_tile_1', 'port_spritelayout_11'),
              (0, 4, 'port_tile_1', 'port_spritelayout_28'),
              (0, 5, '255', 'port_spritelayout_null'),
              (1, 0, 'port_tile_2', slope_switch_2),
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
    id = 'port_industry_layout_5',
    layout = [(0, 0, 'port_tile_2', slope_switch_2),
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
