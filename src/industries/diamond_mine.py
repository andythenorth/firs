"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import Industry, Tile, Sprite, Spriteset, SpriteLayout, IndustryLayout

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='diamond_mine',
                    accept_cargo_types=['ENSP'],
                    map_colour='55',
                    prospect_chance='0.75',
                    prob_in_game='4',
                    override='INDUSTRYTYPE_DIAMOND_MINE',
                    prob_random='7',
                    prod_multiplier='[8]',
                    prod_cargo_types=['DIAM'],
                    substitute='INDUSTRYTYPE_DIAMOND_MINE',
                    name='TTD_STR_INDUSTRY_NAME_DIAMOND_MINE',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_MINE))',
                    fund_cost_multiplier='232',
                    )

industry.economy_variations['MISTAH_KURTZ'].enabled = True

# industry uses layouts and sprites from default game, no custom layouts etc

