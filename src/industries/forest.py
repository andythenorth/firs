"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryOrganic, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryOrganic(id='forest',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    prob_in_game='3',
                    prob_random='10',
                    map_colour='81',
                    prospect_chance='0.75',
                    layouts='[tilelayout_forest_1, tilelayout_forest_2, tilelayout_forest_3]',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['WOOD'],
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    location_checks=IndustryLocationChecks(require_cluster=['forest', [20, 72, 1, 3]],
                                                           incompatible={'sawmill': 16,
                                                                         'paper_mill': 16}),
                    name='TTD_STR_INDUSTRY_NAME_FOREST',
                    fund_cost_multiplier='95',
                    prod_multiplier='[19]',
                    substitute='INDUSTRYTYPE_FOREST',
                    graphics_change_dates = [1935],
                    template="refactor_forest.pypnml" )

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True

# industry uses layouts and sprites from default game, no custom layouts etc

