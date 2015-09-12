"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryTertiary, TileLocationChecks, IndustryLocationChecks

industry = IndustryTertiary(id='power_plant',
                    accept_cargo_types=['COAL'],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=[],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='14',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_BLACK_HOLE',
                    min_cargo_distr='2',
                    location_checks=IndustryLocationChecks(incompatible={'power_plant': 56,
                                                                         'coal_mine': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_POWER_PLANT)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_TOWN))',
                    fund_cost_multiplier='15',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    intro_year=1900)

industry.economy_variations['FIRS'].enabled = True

industry.add_tile(id='power_plant_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  custom_animation_control={'macro':'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))
sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
sprite_ground_overlay = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
sprite_1 = industry.add_sprite(
    sprite_number = '2047'
)
sprite_2 = industry.add_sprite(
    sprite_number = '2050'
)
sprite_3 = industry.add_sprite(
    sprite_number = '2053'
)
sprite_4 = industry.add_sprite(
    sprite_number = '2054'
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 3,
    yoffset= 0,
    zoffset= 36
)

industry.add_spritelayout(
    id = 'power_plant_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [sprite_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'power_plant_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [sprite_2],
    smoke_sprites = [sprite_smoke_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'power_plant_spritelayout_3',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [sprite_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'power_plant_spritelayout_4',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [sprite_4],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'power_plant_industry_layout',
    layout = [(0, 0, 'power_plant_tile_1', 'power_plant_spritelayout_1'),
              (1, 0, 'power_plant_tile_1', 'power_plant_spritelayout_2'),
              (2, 0, 'power_plant_tile_1', 'power_plant_spritelayout_3'),
              (3, 0, 'power_plant_tile_1', 'power_plant_spritelayout_4')]
)

