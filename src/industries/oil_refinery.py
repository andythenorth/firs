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

industry = Industry(id='oil_refinery',
                    accept_cargo_types=['OIL_'],
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    spec_flags='0',
                    prod_cargo_types=['RFPR', 'PETR'],
                    prob_in_game='2',
                    prob_random='4',
                    substitute='4',
                    map_colour='191',
                    fund_cost_multiplier='200',
                    name='TTD_STR_INDUSTRY_NAME_OIL_REFINERY',
                    override='4',
                    extra_text_industry='STR_EXTRA_OIL_REFINERY')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_TROPIC'].enabled = True

# industry uses layouts and sprites from default game, no custom layouts etc

