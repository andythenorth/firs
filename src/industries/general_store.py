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

industry = Industry(id='general_store',
                    accept_cargo_types=['FOOD', 'GOOD', 'BEER'],
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=[],
                    layouts='AUTO',
                    prob_in_game='12',
                    prob_random='24',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='14',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_BLACK_HOLE',
                    min_cargo_distr='2',
                    spec_flags='bitmask(IND_FLAG_ONLY_IN_TOWNS)',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_GENERAL_STORE)',
                    fund_cost_multiplier='15',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    )

industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_TROPIC'].enabled = True


industry.add_tile(id='general_store_tile')

spriteset_ground = industry.add_spriteset(
    id = 'general_store_spriteset_ground',
    type='slab',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'general_store_spriteset_ground_overlay',
    sprites = [(10, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(
    id = 'general_store_spriteset',
    sprites = [(10, 60, 64, 48, -31, -18)]
)
industry.add_spritelayout(
    id = 'general_store_spritelayout',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1]
)
industry.add_industry_layout(
    id = 'general_store_industry_layout',
    layout = [(0, 0, 'general_store_tile', 'general_store_spritelayout')]
)
