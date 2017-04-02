"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(id='diamond_mine',
                    map_colour='69',
                    prospect_chance='0.75',
                    prob_random='3',
                    prob_in_game='5',
                    override='INDUSTRYTYPE_DIAMOND_MINE',
                    prod_multiplier='[8]',
                    location_checks=dict(require_cluster=['diamond_mine', [20, 70, 1, 3]]),
                    prod_cargo_types=['DIAM'],
                    substitute='INDUSTRYTYPE_DIAMOND_MINE',
                    name='TTD_STR_INDUSTRY_NAME_DIAMOND_MINE',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_MINE))',
                    fund_cost_multiplier='232',
                    template="refactor/refactor_diamond_mine.pynml" )

industry.economy_variations['MISTAH_KURTZ'].enabled = True

# !! legacy template has 9 tiles but the industry only needs one (added already to make tile location checks work as hax)
industry.add_tile(id='diamond_mine_tile_1',
                  location_checks=TileLocationChecks(disallow_slopes=True,
                                                     disallow_industry_adjacent=True))

# industry uses layouts and sprites from default game, no custom layouts etc
