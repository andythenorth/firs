"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryExtractive, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryExtractive(id='manganese_mine',
                    map_colour='16',
                    prospect_chance='0.75',
                    prob_in_game='4',
                    override='18',
                    prob_random='7',
                    location_checks=IndustryLocationChecks(require_cluster=['manganese_mine', [20, 70, 1, 3]],
                                                           incompatible={'bulk_terminal': 16}),
                    prod_multiplier='[20]',
                    prod_cargo_types=['MNO2'],
                    substitute='18',
                    name='string(STR_IND_MANGANESE_MINE)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_MINE))',
                    fund_cost_multiplier='232',
                    template='refactor_iron_ore_mine.pypnml' )

industry.economy_variations['MISTAH_KURTZ'].enabled = True

# industry uses layouts and sprites from default game, no custom layouts etc

