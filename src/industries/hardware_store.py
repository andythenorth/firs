"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryTertiary, TileLocationChecks, IndustryLocationChecks

industry = IndustryTertiary(id='hardware_store',
                    accept_cargo_types=['GOOD', 'BDMT'],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=[],
                    layouts='AUTO',
                    prob_in_game='12',
                    prob_random='24',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='15',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_BLACK_HOLE',
                    min_cargo_distr='2',
                    spec_flags='bitmask(IND_FLAG_ONLY_IN_TOWNS)',
                    location_checks=IndustryLocationChecks(incompatible={'hardware_store': 20,
                                                                         'petrol_pump': 16,
                                                                         'builders_yard': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_HARDWARE_STORE)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_TOWN))',
                    fund_cost_multiplier='15',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    snakebite=True)

industry.economy_variations['FIRS'].enabled = True

industry.add_tile(id='hardware_store_tile_1',
                  land_shape_flags='bitmask(LSF_ONLY_ON_FLAT_LAND)',
                  location_checks=TileLocationChecks(require_road_adjacent=['nw', 'ne', 'sw', 'se']))

hardware_store_spriteset_ground = industry.add_spriteset(
    id = 'hardware_store_spriteset_ground',
    type='slab',
)
hardware_store_spriteset_ground_overlay = industry.add_spriteset(
    id = 'hardware_store_spriteset_ground_overlay',
    type = 'empty',
)
hardware_store_spriteset = industry.add_spriteset(
    id = 'hardware_store_spriteset',
    sprites = [(0, 0, 64, 64, -31, -33)]
)

industry.add_spritelayout(
    id = 'hardware_store_spritelayout',
    ground_sprite = hardware_store_spriteset_ground,
    ground_overlay = hardware_store_spriteset_ground_overlay,
    building_sprites = [hardware_store_spriteset]
)
industry.add_industry_layout(
    id = 'hardware_store_industry_layout',
    layout = [(0, 0, 'hardware_store_tile_1', 'hardware_store_spritelayout')]
)
