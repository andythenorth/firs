"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import Industry
import global_constants

industry = Industry(id='trading_post',
                    accept_cargo_types=['FOOD', 'FRUT', 'BEER'],
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=[],
                    layouts='AUTO',
                    prob_in_game='2',
                    prob_random='6',
                    prod_multiplier='[9, 9]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='36',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_BLACK_HOLE',
                    min_cargo_distr='2',
                    spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER)',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_TRADING_POST)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_INDUSTRY_HARBOUR))',
                    fund_cost_multiplier='152',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    override_default_construction_states=True,
                    supply_requirements=global_constants.supply_requirements['import_export'])

industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].accept_cargo_types = ['DIAM', 'JAVA', 'RUBR']
industry.economy_variations['MISTAH_KURTZ'].prod_cargo_types = ['GOOD', 'FMSP']

industry.add_tile(id='trading_post_tile')

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDSPRITE_WATER'
)
spriteset_ground_empty = industry.add_spriteset(
    id = 'trading_post_spriteset_ground',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'trading_post_spriteset_1',
    sprites = [(10, 10, 64, 39, -31, -8)],
    always_draw = 1,
)
spriteset_2 = industry.add_spriteset(
    id = 'trading_post_spriteset_2',
    sprites = [(10, 60, 64, 39, -31, -7)],
    zextent = 7,
    always_draw = 1,
)
spriteset_3 = industry.add_spriteset(
    id = 'trading_post_spriteset_3',
    sprites = [(80, 60, 64, 39, -31, -7)],
    zextent = 7,
    always_draw = 1
)
spriteset_4 = industry.add_spriteset(
    id = 'trading_post_spriteset_4',
    sprites = [(150, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_5 = industry.add_spriteset(
    id = 'trading_post_spriteset_5',
    sprites = [(220, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_6 = industry.add_spriteset(
    id = 'trading_post_spriteset_6',
    sprites = [(290, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_7 = industry.add_spriteset(
    id = 'trading_post_spriteset_7',
    sprites = [(360, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_8 = industry.add_spriteset(
    id = 'trading_post_spriteset_8',
    sprites = [(80, 10, 64, 39, -31, 0)],
    zoffset = 18
)
spriteset_9 = industry.add_spriteset(
    id = 'trading_post_spriteset_9',
    sprites = [(150, 10, 64, 39, -31, 0)],
    yoffset = 4,
    zoffset = 27,
    yextent = 12,

)
spriteset_9b = industry.add_spriteset(
    id = 'trading_post_spriteset_9b',
    sprites = [(150, 10, 64, 39, -31, -7)],
    xoffset = 0,
    zoffset = 12,
    xextent = 11,

)
spriteset_10 = industry.add_spriteset(
    id = 'trading_post_spriteset_10',
    sprites = [(220, 10, 64, 39, -31, -7)],
    yoffset = 0,
    zoffset = 12,
    yextent = 12,
)
spriteset_11 = industry.add_spriteset(
    id = 'trading_post_spriteset_11',
    sprites = [(10, 110, 64, 39, -35, -15)],
)
spriteset_12 = industry.add_spriteset(
    id = 'trading_post_spriteset_12',
    sprites = [(80, 110, 64, 39, -31, -14)],
)
spriteset_13 = industry.add_spriteset(
    id = 'trading_post_spriteset_13',
    sprites = [(150, 110, 64, 39, -31, -8)],
)
spriteset_14 = industry.add_spriteset(
    id = 'trading_post_spriteset_14',
    sprites = [(220, 110, 64, 39, -27, -12)],
)
spriteset_17 = industry.add_spriteset(
    id = 'trading_post_spriteset_17',
    sprites = [(360, 10, 64, 39, -31, 0)],
    zoffset = 18,
)

# trading_post_spritelayout_1 fell out of use and was removed
# trading_post_spritelayout_2 fell out of use and was removed
industry.add_spritelayout(
    id = 'trading_post_spritelayout_3',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_2, spriteset_3, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_4',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_3, spriteset_4, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_5',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_5, spriteset_4, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_6',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_5, spriteset_2, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_7',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_6, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_8',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_6, spriteset_7, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_9',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_7, spriteset_1, spriteset_17]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_10',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_1]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_11',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_2, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_12',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_3, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_13',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_2, spriteset_3, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_14',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_3, spriteset_4, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_15',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_5, spriteset_4, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_16',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_5, spriteset_2, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_17',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_6, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_18',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_6, spriteset_7, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_19',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_7, spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_20',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_1, spriteset_8]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_21',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_11]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_22',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_12]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_23',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_13]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_24',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_14]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_25',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_14]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_26',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = []
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_27',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = []
)
# trading_post_spritelayout_28 fell out of use and was removed
industry.add_spritelayout(
    id = 'trading_post_spritelayout_29',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_2, spriteset_3, spriteset_1, spriteset_10]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_30',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_2, spriteset_3, spriteset_1, spriteset_9b]
)
industry.add_spritelayout(
    id = 'trading_post_spritelayout_null',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = []
)

industry.add_industry_layout(
    id = 'trading_post_industry_layout_1',
    layout = [(0, 2, 'trading_post_tile_1', 'trading_post_spritelayout_27'),
              (0, 3, 'trading_post_tile_2', 'trading_post_slope_switch_1'),
              (1, 0, '255', 'trading_post_spritelayout_null'),
              (1, 1, 'trading_post_tile_1', 'trading_post_spritelayout_11'),
              (1, 2, 'trading_post_tile_1', 'trading_post_spritelayout_29'),
              (1, 3, 'trading_post_tile_2', 'trading_post_slope_switch_2'),
              (2, 1, 'trading_post_tile_1', 'trading_post_spritelayout_24'),
              (2, 2, 'trading_post_tile_1', 'trading_post_spritelayout_24'),
    ]
)
industry.add_industry_layout(
    id = 'trading_post_industry_layout_2',
    layout = [(0, 0, '255', 'trading_post_spritelayout_null'),
              (0, 1, '255', 'trading_post_spritelayout_null'),
              (0, 2, '255', 'trading_post_spritelayout_null'),
              (1, 0, 'trading_post_tile_1', 'trading_post_spritelayout_23'),
              (1, 1, 'trading_post_tile_1', 'trading_post_spritelayout_23'),
              (1, 255, '255', 'trading_post_spritelayout_null'),
              (2, 0, 'trading_post_tile_1', 'trading_post_spritelayout_30'),
              (2, 1, 'trading_post_tile_1', 'trading_post_spritelayout_12'),
              (2, 2, 'trading_post_tile_1', 'trading_post_spritelayout_21'),
              (2, 255, '255', 'trading_post_spritelayout_null'),
              (3, 1, 'trading_post_tile_2', 'trading_post_slope_switch_2'),
              (3, 2, 'trading_post_tile_2', 'trading_post_slope_switch_1'),
    ]
)
industry.add_industry_layout(
    id = 'trading_post_industry_layout_3',
    layout = [(0, 0, 'trading_post_tile_2', 'trading_post_slope_switch_2'),
              (0, 1, 'trading_post_tile_2', 'trading_post_slope_switch_2'),
              (0, 2, 'trading_post_tile_2', 'trading_post_slope_switch_1'),
              (1, 0, 'trading_post_tile_1', 'trading_post_spritelayout_24'),
              (1, 2, 'trading_post_tile_1', 'trading_post_spritelayout_30'),
              (2, 1, 'trading_post_tile_1', 'trading_post_spritelayout_26'),
              (2, 2, 'trading_post_tile_1', 'trading_post_spritelayout_29'),
              (2, 3, 'trading_post_tile_1', 'trading_post_spritelayout_22'),
              (2, 4, '255', 'trading_post_spritelayout_null'),
              (3, 2, '255', 'trading_post_spritelayout_null'),
              (3, 3, '255', 'trading_post_spritelayout_null'),
    ]
)
industry.add_industry_layout(
    id = 'trading_post_industry_layout_4',
    layout = [(0, 0, 'trading_post_tile_2', 'trading_post_slope_switch_2'),
              (0, 1, '255', 'trading_post_spritelayout_null'),
              (1, 0, 'trading_post_tile_2', 'trading_post_slope_switch_2'),
              (1, 1, 'trading_post_tile_1', 'trading_post_spritelayout_29'),
              (1, 2, 'trading_post_tile_1', 'trading_post_spritelayout_30'),
              (1, 3, '255', 'trading_post_spritelayout_null'),
              (2, 0, 'trading_post_tile_2', 'trading_post_slope_switch_1'),
              (2, 1, 'trading_post_tile_1', 'trading_post_spritelayout_25'),
              (2, 2, '255', 'trading_post_spritelayout_null'),
              (3, 2, '255', 'trading_post_spritelayout_null'),
              (3, 3, '255', 'trading_post_spritelayout_null'),
    ]
)
industry.add_industry_layout(
    id = 'trading_post_industry_layout_5',
    layout = [(0, 0, 'trading_post_tile_2', 'trading_post_slope_switch_1'),
              (1, 0, 'trading_post_tile_2', 'trading_post_slope_switch_2'),
              (1, 2, '255', 'trading_post_spritelayout_null'),
              (2, 0, 'trading_post_tile_1', 'trading_post_spritelayout_13'),
              (2, 1, 'trading_post_tile_1', 'trading_post_spritelayout_29'),
              (2, 2, 'trading_post_tile_1', 'trading_post_spritelayout_30'),
              (2, 3, '255', 'trading_post_spritelayout_null'),
              (3, 255, '255', 'trading_post_spritelayout_null'),
              (3, 0, 'trading_post_tile_1', 'trading_post_spritelayout_24'),
              (3, 1, 'trading_post_tile_1', 'trading_post_spritelayout_24'),
              (3, 2, 'trading_post_tile_1', 'trading_post_spritelayout_24'),
              (3, 3, '255', 'trading_post_spritelayout_null'),
              (4, 255, '255', 'trading_post_spritelayout_null'),
              (4, 0, '255', 'trading_post_spritelayout_null'),
              (4, 1, '255', 'trading_post_spritelayout_null'),
              (4, 2, '255', 'trading_post_spritelayout_null'),
              (4, 3, '255', 'trading_post_spritelayout_null'),
    ]
)
