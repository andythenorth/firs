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

industry = Industry(id='stockyard',
                    accept_cargo_types=['MNSP', 'LVST'],
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['FOOD'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='176',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_PROCESSING',
                    min_cargo_distr='5',
                    spec_flags='bitmask(IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE)',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_STOCKYARD)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_IND_STOCKYARD))',
                    fund_cost_multiplier='145',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    extra_text_industry='STR_EXTRA_MEAT_PACKER')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True

industry.add_tile(id='stockyard_tile')

spriteset_ground = industry.add_spriteset(
    id = 'stockyard_spriteset_ground',
    type = 'concrete'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'stockyard_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'stockyard_spriteset_1',
    sprites = [(10, 10, 64, 44, -31, -13)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'stockyard_spriteset_2',
    sprites = [(80, 10, 64, 74, -31, -43)],
    zextent = 32
)
spriteset_3 = industry.add_spriteset(
    id = 'stockyard_spriteset_3',
    sprites = [(150, 10, 64, 88, -31, -57)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'stockyard_spriteset_4',
    sprites = [(220, 10, 64, 85, -31, -54)],
    zextent = 32
)
spriteset_5 = industry.add_spriteset(
    id = 'stockyard_spriteset_5',
    sprites = [(290, 10, 64, 104, -31, -73)],
    zextent = 96
)
spriteset_6 = industry.add_spriteset(
    id = 'stockyard_spriteset_6',
    sprites = [(360, 10, 64, 91, -31, -60)],
    zextent = 64
)
spriteset_7 = industry.add_spriteset(
    id = 'stockyard_spriteset_7',
    sprites = [(430, 10, 64, 98, -31, -67)],
    zextent = 64
)
spriteset_8 = industry.add_spriteset(
    id = 'stockyard_spriteset_8',
    sprites = [(500, 10, 64, 54, -31, -23)],
    zextent = 48
)
spriteset_9 = industry.add_spriteset(
    id = 'stockyard_spriteset_9',
    sprites = [(570, 10, 64, 76, -31, -45)],
    zextent = 48
)
spriteset_10 = industry.add_spriteset(
    id = 'stockyard_spriteset_10',
    sprites = [(640, 10, 64, 32, -31, -1)],
    zextent = 48
)
spriteset_11 = industry.add_spriteset(
    id = 'stockyard_spriteset_11',
    sprites = [(710, 10, 64, 49, -31, -18)],
    zextent = 8
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 17,
    yoffset= 9,
    zoffset= 99,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 20,
    yoffset= 9,
    zoffset= 100,
    animation_frame_offset = 1
)

industry.add_spritelayout(
    id = 'stockyard_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'stockyard_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'stockyard_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'stockyard_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'stockyard_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    smoke_sprites = [sprite_smoke_1, sprite_smoke_2],
    fences = ['nw','se','sw']
)
industry.add_spritelayout(
    id = 'stockyard_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    fences = ['nw','se','sw']
)
industry.add_spritelayout(
    id = 'stockyard_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    fences = ['nw','se','sw']
)
industry.add_spritelayout(
    id = 'stockyard_spritelayout_8',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
    fences = ['nw','ne','se']
)
industry.add_spritelayout(
    id = 'stockyard_spritelayout_9',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_9],
    fences = ['nw','ne','se']
)
industry.add_spritelayout(
    id = 'stockyard_spritelayout_10',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_10],
    fences = ['nw','ne','se']
)
industry.add_spritelayout(
    id = 'stockyard_spritelayout_11',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_11],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'stockyard_spritelayout_12',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se']
)

industry.add_industry_layout(
    id = 'stockyard_industry_layout_1',
    layout = [(0, 0, 'stockyard_tile', 'stockyard_spritelayout_12'),
              (0, 1, 'stockyard_tile', 'stockyard_spritelayout_12'),
              (0, 2, 'stockyard_tile', 'stockyard_spritelayout_11'),
              (0, 3, 'stockyard_tile', 'stockyard_spritelayout_12'),
              (1, 0, 'stockyard_tile', 'stockyard_spritelayout_12'),
              (1, 1, 'stockyard_tile', 'stockyard_spritelayout_8'),
              (1, 2, 'stockyard_tile', 'stockyard_spritelayout_9'),
              (1, 3, 'stockyard_tile', 'stockyard_spritelayout_10'),
              (3, 0, 'stockyard_tile', 'stockyard_spritelayout_12'),
              (3, 1, 'stockyard_tile', 'stockyard_spritelayout_5'),
              (3, 2, 'stockyard_tile', 'stockyard_spritelayout_6'),
              (3, 3, 'stockyard_tile', 'stockyard_spritelayout_7'),
              (4, 0, 'stockyard_tile', 'stockyard_spritelayout_1'),
              (4, 1, 'stockyard_tile', 'stockyard_spritelayout_2'),
              (4, 2, 'stockyard_tile', 'stockyard_spritelayout_3'),
              (4, 3, 'stockyard_tile', 'stockyard_spritelayout_4'),
    ]
)

