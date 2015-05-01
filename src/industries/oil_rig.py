"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryExtractive

industry = IndustryPrimaryExtractive(id='oil_rig',
                    prod_cargo_types=['OIL_', 'PASS'],
                    prob_in_game='6',
                    prob_random='6',
                    prod_multiplier='[29, 4]',
                    substitute='5',
                    map_colour='152',
                    spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER, IND_FLAG_AI_CREATES_AIR_AND_SHIP_ROUTES)',
                    prospect_chance='0.75',
                    name='TTD_STR_INDUSTRY_NAME_OIL_RIG',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_WATER))',
                    fund_cost_multiplier='255',
                    override='5',
                    template="refactor_oil_rig.pypnml" )

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True

# industry uses layouts and sprites from default game, no custom layouts etc

