"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryOrganic, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryOrganic(id='ranch',
                    accept_cargo_types=['FMSP'],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_FARM',
                    prod_cargo_types=['LVST', 'WOOL'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='21',
                    prod_multiplier='[4, 4]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='14',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_ORGANIC',
                    min_cargo_distr='1',
                    spec_flags='0',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_RANCH)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_FARM))',
                    fund_cost_multiplier='45',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    )

industry.economy_variations['BASIC_TROPIC'].enabled = True

industry.add_tile(id='ranch_tile')

spriteset_ground = industry.add_spriteset(
    id = 'ranch_spriteset_ground',
    type = 'empty'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'ranch_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'ranch_spriteset_1',
    sprites = [(10, 10, 64, 52, -31, -21)],
    zextent = 24
)
spriteset_2 = industry.add_spriteset(
    id = 'ranch_spriteset_2',
    sprites = [(80, 10, 64, 52, -31, -19)],
    zextent = 24
)
spriteset_3 = industry.add_spriteset(
    id = 'ranch_spriteset_3',
    sprites = [(150, 10, 64, 52, -31, -21)],
    zextent = 24
)
spriteset_4 = industry.add_spriteset(
    id = 'ranch_spriteset_4',
    sprites = [(220, 10, 64, 52, -31, -21)],
    zextent = 8
)
spriteset_5 = industry.add_spriteset(
    id = 'ranch_spriteset_5',
    sprites = [(290, 10, 64, 52, -31, -21)],
    zextent = 8
)

industry.add_spritelayout(
    id = 'ranch_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1]
)
industry.add_spritelayout(
    id = 'ranch_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
)
industry.add_spritelayout(
    id = 'ranch_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
)
industry.add_spritelayout(
    id = 'ranch_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
)
industry.add_spritelayout(
    id = 'ranch_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
)

industry.add_industry_layout(
    id = 'ranch_industry_layout_1',
    layout = [(0, 0, 'ranch_tile', 'ranch_spritelayout_3'),
              (1, 0, 'ranch_tile', 'ranch_spritelayout_2'),
              (1, 2, 'ranch_tile', 'ranch_spritelayout_4'),
              (3, 0, 'ranch_tile', 'ranch_spritelayout_1'),
              (3, 1, 'ranch_tile', 'ranch_spritelayout_5'),
    ]
)
industry.add_industry_layout(
    id = 'ranch_industry_layout_2',
    layout = [(0, 0, 'ranch_tile', 'ranch_spritelayout_2'),
              (0, 1, 'ranch_tile', 'ranch_spritelayout_1'),
              (0, 2, 'ranch_tile', 'ranch_spritelayout_4'),
              (2, 0, 'ranch_tile', 'ranch_spritelayout_3'),
              (2, 2, 'ranch_tile', 'ranch_spritelayout_5'),
    ]
)

