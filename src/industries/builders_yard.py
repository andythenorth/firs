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

industry = Industry(id='builders_yard',
                    accept_cargo_types=['BDMT'],
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=[],
                    layouts='AUTO',
                    prob_in_game='12',
                    prob_random='18',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='15',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_BLACK_HOLE',
                    min_cargo_distr='0',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_BUILDERS_YARD)',
                    fund_cost_multiplier='16',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    )

industry.economy_variations['FIRS'].enabled = True

industry.add_tile(id='builders_yard_tile')

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'builders_yard_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'builders_yard_spriteset_1',
    sprites = [(10, 10, 64, 51, -31, -13)],
    zextent = 16
)
spriteset_2 = industry.add_spriteset(
    id = 'builders_yard_spriteset_2',
    sprites = [(80, 10, 64, 51, -31, -13)],
    zextent = 16
)

industry.add_spritelayout(
    id = 'builders_yard_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1]
)
industry.add_spritelayout(
    id = 'builders_yard_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
)

industry.add_industry_layout(
    id = 'builders_yard_industry_layout_1',
    layout = [(0, 0, 'builders_yard_tile', 'builders_yard_spritelayout_1'),
              (0, 1, 'builders_yard_tile', 'builders_yard_spritelayout_2'),
    ]
)
industry.add_industry_layout(
    id = 'builders_yard_industry_layout_2',
    layout = [(0, 0, 'builders_yard_tile', 'builders_yard_spritelayout_1'),
              (1, 0, 'builders_yard_tile', 'builders_yard_spritelayout_2'),
    ]
)
