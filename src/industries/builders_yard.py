"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryTertiary, TileLocationChecks, IndustryLocationChecks

industry = IndustryTertiary(id='builders_yard',
                    accept_cargo_types=['BDMT'],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=[],
                    layouts='AUTO',
                    prob_in_game='12',
                    prob_random='18',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='15',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_BLACK_HOLE',
                    min_cargo_distr='0',
                    location_checks=IndustryLocationChecks(incompatible={'builders_yard': 20,
                                                                         'hardware_store': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_BUILDERS_YARD)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_MILL))',
                    fund_cost_multiplier='16',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS' )

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.add_tile(id='builders_yard_tile_1',
                  location_checks=TileLocationChecks(require_houses_nearby=True,
                                                     require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'builders_yard_spriteset_ground',
    type = 'cobble',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'builders_yard_spriteset_ground_overlay',
    type = 'empty'
)
sheds_1 = industry.add_spriteset(
    id = 'builders_yard_spriteset_1',
    sprites = [(10, 10, 64, 56, -31, -26)],
    zextent = 16
)
sheds_2 = industry.add_spriteset(
    id = 'builders_yard_spriteset_2',
    sprites = [(80, 10, 64, 56, -31, -26)],
    zextent = 16
)
silo = industry.add_spriteset(
    id = 'builders_yard_spriteset_3',
    sprites = [(220, 10, 64, 64, -31, -34)],
    zextent = 16
)

industry.add_spritelayout(
    id = 'builders_yard_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [sheds_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'builders_yard_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [sheds_2],
)
industry.add_spritelayout(
    id = 'builders_yard_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [silo],
)

industry.add_industry_layout(
    id = 'builders_yard_industry_layout_1',
    layout = [(0, 0, 'builders_yard_tile_1', 'builders_yard_spritelayout_3'),
              (0, 1, 'builders_yard_tile_1', 'builders_yard_spritelayout_1'),
              (1, 0, 'builders_yard_tile_1', 'builders_yard_spritelayout_2'),
              (1, 1, 'builders_yard_tile_1', 'builders_yard_spritelayout_1'),
    ]
)
industry.add_industry_layout(
    id = 'builders_yard_industry_layout_2',
    layout = [(0, 0, 'builders_yard_tile_1', 'builders_yard_spritelayout_2'),
              (0, 1, 'builders_yard_tile_1', 'builders_yard_spritelayout_3'),
              (1, 0, 'builders_yard_tile_1', 'builders_yard_spritelayout_1'),
              (1, 1, 'builders_yard_tile_1', 'builders_yard_spritelayout_1'),
    ]
)
