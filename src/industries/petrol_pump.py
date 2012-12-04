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

industry = Industry(id='petrol_pump',
                    accept_cargo_types='[FOOD, GOOD, PETR]',
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    layouts='AUTO',
                    prod_cargo_types='[]',
                    prob_in_game='14',
                    prob_random='14',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='15',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_BLACK_HOLE',
                    min_cargo_distr='2',
                    spec_flags='0',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_PETROLPUMP)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_IND_PETROLPUMP))',
                    fund_cost_multiplier='8',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS')

industry.add_tile(id='petrol_pump_tile')

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_SLABS',
    sprite_number_snow = 'GROUNDTILE_SLABS',
)
sprite_ground_overlay = industry.add_sprite(
    sprite_number = 'GROUNDTILE_SLABS',
    sprite_number_snow = 'GROUNDTILE_SLABS',
)
spriteset_1 = industry.add_spriteset(
    id = 'petrol_pump_spriteset_1',
    sprites = [(10, 60, 64, 59, -31, -28)]
)
spriteset_2 = industry.add_spriteset(
    id = 'petrol_pump_spriteset_2',
    sprites = [(80, 60, 64, 59, -31, -28)]
)

industry.add_spritelayout(
    id = 'petrol_pump_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_1]
)
industry.add_spritelayout(
    id = 'petrol_pump_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_2]
)

industry.add_industry_layout(
    id = 'petrol_pump_industry_layout_1',
    layout = [(0, 0, 'petrol_pump_tile', 'petrol_pump_spritelayout_1'),
              (0, 1, 'petrol_pump_tile', 'petrol_pump_spritelayout_2')
    ]
)
industry.add_industry_layout(
    id = 'petrol_pump_industry_layout_2',
    layout = [(0, 0, 'petrol_pump_tile', 'petrol_pump_spritelayout_1'),
              (1, 0, 'petrol_pump_tile', 'petrol_pump_spritelayout_2')
    ]
)

