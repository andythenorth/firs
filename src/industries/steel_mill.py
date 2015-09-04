"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='steel_mill',
                    processed_cargos_and_output_ratios=[('IORE', 3), ('COAL', 2), ('SCMT', 3)],
                    prob_in_game='3',
                    prob_random='5',
                    location_checks=IndustryLocationChecks(incompatible={'steel_mill': 56,
                                                                         'junk_yard': 16,
                                                                         'coal_mine': 16,
                                                                         'iron_ore_mine': 16,
                                                                         'junk_yard': 16}),
                    prod_cargo_types=['STEL'],
                    substitute='8',
                    map_colour='9',
                    fund_cost_multiplier='200',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_POWERHUNGRY))',
                    name='TTD_STR_INDUSTRY_NAME_STEEL_MILL',
                    override='8',
                    extra_text_industry='STR_EXTRA_STEELMILL',
                    template="refactor_steel_mill.pypnml",
                    intro_year=1850)

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].intro_year = 1800

# industry uses layouts and sprites from default game, no custom layouts etc

