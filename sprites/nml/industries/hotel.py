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

industry = Industry(id='hotel',
                    accept_cargo_types='[FOOD, BEER, PASS]',
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types='[PASS]',
                    layouts='[hotel_industry_layout_tilelayout]',
                    prob_in_game='20',
                    prob_random='10',
                    prod_multiplier='[20, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='190',
                    conflicting_ind_types='[hotel]',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_BLACK_HOLE',
                    min_cargo_distr='2',
                    spec_flags='bitmask(IND_FLAG_BUILT_NEAR_TOWN)',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_HOTEL)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_IND_HOTEL))',
                    fund_cost_multiplier='15',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS')

industry.add_tile(id='hotel_tile')

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDSPRITE_CLEARED'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'hotel_spriteset_ground',
    type='empty',
)
sprite_building_1 = industry.add_sprite(
    sprite_number = '(terrain_type == TILETYPE_SNOW) ? 4583 : 4475'
)
sprite_building_2 = industry.add_sprite(
    sprite_number = '(terrain_type == TILETYPE_SNOW) ? 4584 : 4476'
)

industry.add_spritelayout(
    id = 'hotel_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [sprite_building_1]
)
industry.add_spritelayout(
    id = 'hotel_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [sprite_building_2]
)

industry.add_industry_layout(
    id = 'hotel_industry_layout',
    default_spritelayout = 'hotel_spritelayout_1',
    layout = [(0, 0, 'hotel_tile', 'hotel_spritelayout_1'),
              (1, 0, 'hotel_tile', 'hotel_spritelayout_1'),
              (0, 1, 'hotel_tile', 'hotel_spritelayout_2'),
              (1, 1, 'hotel_tile', 'hotel_spritelayout_2')
    ]
)

# Templating
industry.render_and_save_pnml()
