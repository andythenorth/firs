"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='paper_mill',
                    processed_cargos_and_output_ratios=[('CLAY', 2), ('WOOD', 4), ('RFPR', 2)],
                    prod_cargo_types=['GOOD', 'MNSP'],
                    prob_in_game='3',
                    prob_random='5',
                    location_checks=IndustryLocationChecks(incompatible={'paper_mill': 56,
                                                                         'forest': 16,
                                                                         'clay_pit': 16}),
                    substitute='14',
                    map_colour='184',
                    fund_cost_multiplier='120',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_MILL))',
                    name='TTD_STR_INDUSTRY_NAME_PAPER_MILL',
                    override='14',
                    extra_text_industry='STR_EXTRA_PAPER_MILL',
                    template="refactor_paper_mill.pypnml" )

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].prod_cargo_types=['PAPR', 'MNSP']

# industry uses layouts and sprites from default game, no custom layouts etc

