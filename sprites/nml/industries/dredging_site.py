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

industry = Industry(id='dredging_site',
                    accept_cargo_types='[ENSP]',
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types='[SAND, GRVL]',
                    layouts='[tilelayout_dredging_site_1]',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[13, 13]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='195',
                    conflicting_ind_types='[]',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_EXTRACTIVE',
                    min_cargo_distr='5',
                    spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER, IND_FLAG_AI_CREATES_AIR_AND_SHIP_ROUTES)',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_DREDGING_SITE)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_IND_DREDGING_SITE))',
                    fund_cost_multiplier='180',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS')

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDSPRITE_WATER',
)

spriteset_ground_overlay = industry.add_spriteset(
    id = 'dredging_site_spriteset_ground_overlay',
    type='empty',
)

spriteset_platform = industry.add_spriteset(
    id = 'dredging_site_spriteset_platform',
    sprites = [(10, 10, 64, 100, -31, -65)],
    zextent= 74
)

industry.add_spritelayout(
    id = 'dredging_site_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_platform]
)

# dredging site has one layout only, don't bother inserting templated industry layouts etc

# Templating
industry.render_and_save_pnml()
