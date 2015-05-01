"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary

industry = IndustrySecondary(id='oil_refinery',
                    processed_cargos_and_output_ratios=[('OIL_', 6)],
                    spec_flags='0',
                    prod_cargo_types=['RFPR', 'PETR'],
                    prob_in_game='2',
                    prob_random='4',
                    substitute='4',
                    map_colour='191',
                    fund_cost_multiplier='200',
                    name='TTD_STR_INDUSTRY_NAME_OIL_REFINERY',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_REFINERY))',
                    override='4',
                    extra_text_industry='STR_EXTRA_OIL_REFINERY',
                    template="refactor_oil_refinery.pypnml" )

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True

# industry uses layouts and sprites from default game, no custom layouts etc

