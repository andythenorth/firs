"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryExtractive, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryExtractive(id='iron_ore_mine',
                    accept_cargo_types=['ENSP'],
                    map_colour='55',
                    prospect_chance='0.75',
                    prob_in_game='4',
                    override='18',
                    prob_random='7',
                    prod_multiplier='[19]',
                    prod_cargo_types=['IORE'],
                    substitute='18',
                    name='TTD_STR_INDUSTRY_NAME_IRON_ORE_MINE',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_MINE))',
                    fund_cost_multiplier='232',
                    )

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True

# industry uses layouts and sprites from default game, no custom layouts etc

