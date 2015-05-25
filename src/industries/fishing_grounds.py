"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimary

industry = IndustryPrimary(id='fishing_grounds',
                    accept_cargo_types=[],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['FISH'],
                    layouts='[tilelayout_fishing_grounds_1, tilelayout_fishing_grounds_2, tilelayout_fishing_grounds_3, tilelayout_fishing_grounds_4]',
                    prob_in_game='12',
                    prob_random='12',
                    prod_multiplier='[7, 0]',
                    substitute='5',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='158',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_EXTRACTIVE',
                    min_cargo_distr='2',
                    spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER, IND_FLAG_NO_PRODUCTION_INCREASE, IND_FLAG_AI_CREATES_AIR_AND_SHIP_ROUTES)',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_FISHING_GROUND)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_WATER))',
                    fund_cost_multiplier='88',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    template="refactor_fishing_grounds.pypnml" )

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True

spriteset_1 = industry.add_spriteset(
    id = 'fishing_grounds_spriteset_1',
    sprites = [(10, 10, 64, 31, -31, 0)],
    zextent = 16
)
spriteset_2 = industry.add_spriteset(
    id = 'fishing_grounds_spriteset_2',
    sprites = [(80, 10, 64, 31, -31, 0)],
    zextent = 16
)
spriteset_3 = industry.add_spriteset(
    id = 'fishing_grounds_spriteset_3',
    sprites = [(150, 10, 64, 31, -31, 0)],
    zextent = 16
)
spriteset_4 = industry.add_spriteset(
    id = 'fishing_grounds_spriteset_4',
    sprites = [(220, 10, 64, 31, -31, 0)],
    zextent = 16
)
spriteset_5 = industry.add_spriteset(
    id = 'fishing_grounds_spriteset_5',
    sprites = [(290, 10, 64, 31, -31, -32)],
    zextent = 16
)
