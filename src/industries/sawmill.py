"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import Industry

industry = Industry(id='sawmill',
                    accept_cargo_types=['WOOD'],
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_cargo_types=['WDPR'],
                    prob_in_game='2',
                    prob_random='5',
                    substitute='2',
                    map_colour='194',
                    fund_cost_multiplier='97',
                    name='TTD_STR_INDUSTRY_NAME_SAWMILL',
                    override='2',
                    extra_text_industry='STR_EXTRA_SAWMILL')

industry.economy_variations['FIRS'].enabled = True

# industry uses layouts and sprites from default game, no custom layouts etc

