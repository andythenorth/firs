"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from firs import Industry, Tile, Sprite, Spriteset, SpriteLayout, IndustryLayout

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='recycling_depot',
                    accept_cargo_types='[]',
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types='[RCYC]',
                    layouts='AUTO',
                    prob_in_game='20',
                    prob_random='20',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='191',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_EXTRACTIVE',
                    min_cargo_distr='2',
                    spec_flags='0',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_RECYCLING_DEPOT)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_IND_RECYCLING_DEPOT))',
                    fund_cost_multiplier='118',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS')

industry.economy_variations['BASIC_TEMPERATE'].disabled = True
industry.economy_variations['BASIC_ARCTIC'].disabled = True
industry.economy_variations['BASIC_TROPIC'].disabled = True

industry.add_tile(id='recycling_depot_tile')

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_SLABS',
    sprite_number_snow = 'GROUNDTILE_SLABS',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'recycling_depot_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_hut = industry.add_spriteset(
    id = 'recycling_depot_spriteset_hut',
    sprites = [(10, 10, 64, 31, -31, 0)]
)
spriteset_no_hut = industry.add_spriteset(
    id = 'recycling_depot_spriteset_no_hut',
    sprites = [(80, 10, 64, 31, -31, 0)]
)

industry.add_spritelayout(
    id = 'recycling_depot_spritelayout_hut',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_hut],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'recycling_depot_spritelayout_no_hut',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_no_hut],
    fences = ['nw','ne','se','sw']
)
industry.add_industry_layout(
    id = 'recycling_depot_industry_layout',
    layout = [(0, 0, 'recycling_depot_tile', 'recycling_depot_spritelayout_hut'),
              (0, 1, 'recycling_depot_tile', 'recycling_depot_spritelayout_no_hut'),
              (1, 0, 'recycling_depot_tile', 'recycling_depot_spritelayout_no_hut'),
              (1, 1, 'recycling_depot_tile', 'recycling_depot_spritelayout_no_hut')
    ]
)

