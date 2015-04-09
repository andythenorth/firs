"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import Industry

industry = Industry(id='machine_shop',
                    accept_cargo_types=['STEL', 'PETR'],
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['FMSP', 'ENSP'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='48',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_PROCESSING',
                    min_cargo_distr='5',
                    spec_flags='0',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_MACHINE_SHOP)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_HEAVY_INDUSTRY))',
                    fund_cost_multiplier='145',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    extra_text_industry='STR_EXTRA_MACHINE_SHOP',
                    graphics_change_dates = [1920, 1945, 1970, 1990, 2010])

industry.economy_variations['FIRS'].enabled = True

industry.add_tile(id='machine_shop_tile')

spriteset_ground = industry.add_spriteset(
    id = 'machine_shop_spriteset_ground',
    type = 'concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'machine_shop_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'machine_shop_spriteset_1',
    sprites = [(10, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'machine_shop_spriteset_2',
    sprites = [(80, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_3 = industry.add_spriteset(
    id = 'machine_shop_spriteset_3',
    sprites = [(150, 10, 64, 78, -25, -12)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'machine_shop_spriteset_4',
    sprites = [(220, 10, 64, 78, -48, -28)],
    zextent = 32
)
spriteset_5 = industry.add_spriteset(
    id = 'machine_shop_spriteset_5',
    sprites = [(290, 10, 64, 78, -31, -47)],
    zextent = 32
)
spriteset_6 = industry.add_spriteset(
    id = 'machine_shop_spriteset_6',
    sprites = [(360, 10, 64, 78, -31, -47)],
    zextent = 78
)
spriteset_7 = industry.add_spriteset(
    id = 'machine_shop_spriteset_7',
    sprites = [(430, 10, 64, 78, -31, -47)],
    zextent = 32
)
spriteset_8 = industry.add_spriteset(
    id = 'machine_shop_spriteset_8',
    sprites = [(500, 10, 64, 85, -31, -54)],
    zextent = 32
)
spriteset_9 = industry.add_spriteset(
    id = 'machine_shop_spriteset_9',
    sprites = [(570, 10, 64, 85, -31, -54)],
    zextent = 64
)
spriteset_10 = industry.add_spriteset(
    id = 'machine_shop_spriteset_10',
    sprites = [(640, 10, 64, 85, -31, -54)],
    zextent = 64
)
spriteset_11 = industry.add_spriteset(
    id = 'machine_shop_spriteset_11',
    sprites = [(780, 10, 64, 31, -35, 2)],
    zextent = 32
)
spriteset_12 = industry.add_spriteset(
    id = 'machine_shop_spriteset_12',
    sprites = [(850, 10, 64, 31, -35, 2)],
    zextent = 32
)
spriteset_13 = industry.add_spriteset(
    id = 'machine_shop_spriteset_13',
    sprites = [(920, 10, 64, 49, -39, -15)],
    zextent = 32
)
# out of sequence for historical reasons
spriteset_14 = industry.add_spriteset(
    id = 'machine_shop_spriteset_14',
    sprites = [(710, 10, 64, 31, -28, -1)],
    zextent = 32
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type = 'dark_smoke_small',
    xoffset= 13,
    yoffset= 0,
    zoffset= 73,
)

industry.add_spritelayout(
    id = 'machine_shop_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'machine_shop_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'machine_shop_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'machine_shop_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'machine_shop_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'machine_shop_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    #building_sprites = [spriteset_6, spriteset_14], # commented due to spritesorter issues obscuring spriteset_14
    building_sprites = [spriteset_6],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'machine_shop_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'machine_shop_spritelayout_8',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
    smoke_sprites = [sprite_smoke],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'machine_shop_spritelayout_9',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_9],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'machine_shop_spritelayout_10',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_10],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'machine_shop_spritelayout_11',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_11],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'machine_shop_spritelayout_12',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_12],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'machine_shop_spritelayout_13',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_13],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'machine_shop_spritelayout_14',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)



industry.add_industry_layout(
    id = 'machine_shop_industry_layout_1',
    layout = [(0, 0, 'machine_shop_tile', 'machine_shop_spritelayout_2'),
              (0, 1, 'machine_shop_tile', 'machine_shop_spritelayout_7'),
              (0, 2, 'machine_shop_tile', 'machine_shop_spritelayout_14'),
              (1, 0, 'machine_shop_tile', 'machine_shop_spritelayout_6'),
              (1, 1, 'machine_shop_tile', 'machine_shop_spritelayout_5'),
              (1, 2, 'machine_shop_tile', 'machine_shop_spritelayout_13'),
              (2, 0, 'machine_shop_tile', 'machine_shop_spritelayout_2'),
              (2, 1, 'machine_shop_tile', 'machine_shop_spritelayout_10'),
              (2, 2, 'machine_shop_tile', 'machine_shop_spritelayout_12'),
              (3, 0, 'machine_shop_tile', 'machine_shop_spritelayout_9'),
              (3, 1, 'machine_shop_tile', 'machine_shop_spritelayout_8'),
              (3, 2, 'machine_shop_tile', 'machine_shop_spritelayout_11'),
              (4, 0, 'machine_shop_tile', 'machine_shop_spritelayout_3'),
              (4, 1, 'machine_shop_tile', 'machine_shop_spritelayout_4'),
              (4, 2, 'machine_shop_tile', 'machine_shop_spritelayout_13'),
              (5, 0, 'machine_shop_tile', 'machine_shop_spritelayout_2'),
              (5, 1, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (5, 2, 'machine_shop_tile', 'machine_shop_spritelayout_2'),
    ]
)
industry.add_industry_layout(
    id = 'machine_shop_industry_layout_2',
    layout = [(0, 0, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (0, 1, 'machine_shop_tile', 'machine_shop_spritelayout_7'),
              (0, 2, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (0, 3, 'machine_shop_tile', 'machine_shop_spritelayout_7'),
              (0, 4, 'machine_shop_tile', 'machine_shop_spritelayout_12'),
              (1, 0, 'machine_shop_tile', 'machine_shop_spritelayout_6'),
              (1, 1, 'machine_shop_tile', 'machine_shop_spritelayout_5'),
              (1, 2, 'machine_shop_tile', 'machine_shop_spritelayout_6'),
              (1, 3, 'machine_shop_tile', 'machine_shop_spritelayout_5'),
              (1, 4, 'machine_shop_tile', 'machine_shop_spritelayout_11'),
              (2, 0, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (2, 1, 'machine_shop_tile', 'machine_shop_spritelayout_10'),
              (2, 2, 'machine_shop_tile', 'machine_shop_spritelayout_14'),
              (2, 3, 'machine_shop_tile', 'machine_shop_spritelayout_3'),
              (2, 4, 'machine_shop_tile', 'machine_shop_spritelayout_4'),
              (3, 0, 'machine_shop_tile', 'machine_shop_spritelayout_9'),
              (3, 1, 'machine_shop_tile', 'machine_shop_spritelayout_8'),
              (3, 2, 'machine_shop_tile', 'machine_shop_spritelayout_13'),
              (3, 3, 'machine_shop_tile', 'machine_shop_spritelayout_2'),
              (3, 4, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
    ]
)
industry.add_industry_layout(
    id = 'machine_shop_industry_layout_3',
    layout = [(0, 0, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (0, 1, 'machine_shop_tile', 'machine_shop_spritelayout_7'),
              (0, 2, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (0, 3, 'machine_shop_tile', 'machine_shop_spritelayout_7'),
              (0, 4, 'machine_shop_tile', 'machine_shop_spritelayout_14'),
              (1, 0, 'machine_shop_tile', 'machine_shop_spritelayout_6'),
              (1, 1, 'machine_shop_tile', 'machine_shop_spritelayout_5'),
              (1, 2, 'machine_shop_tile', 'machine_shop_spritelayout_6'),
              (1, 3, 'machine_shop_tile', 'machine_shop_spritelayout_5'),
              (1, 4, 'machine_shop_tile', 'machine_shop_spritelayout_12'),
              (2, 0, 'machine_shop_tile', 'machine_shop_spritelayout_3'),
              (2, 1, 'machine_shop_tile', 'machine_shop_spritelayout_4'),
              (2, 2, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (2, 3, 'machine_shop_tile', 'machine_shop_spritelayout_10'),
              (2, 4, 'machine_shop_tile', 'machine_shop_spritelayout_11'),
              (3, 0, 'machine_shop_tile', 'machine_shop_spritelayout_2'),
              (3, 1, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (3, 2, 'machine_shop_tile', 'machine_shop_spritelayout_9'),
              (3, 3, 'machine_shop_tile', 'machine_shop_spritelayout_8'),
              (3, 4, 'machine_shop_tile', 'machine_shop_spritelayout_13'),
    ]
)
industry.add_industry_layout(
    id = 'machine_shop_industry_layout_4',
    layout = [(0, 0, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (0, 1, 'machine_shop_tile', 'machine_shop_spritelayout_7'),
              (0, 2, 'machine_shop_tile', 'machine_shop_spritelayout_13'),
              (0, 3, 'machine_shop_tile', 'machine_shop_spritelayout_3'),
              (0, 4, 'machine_shop_tile', 'machine_shop_spritelayout_4'),
              (1, 0, 'machine_shop_tile', 'machine_shop_spritelayout_6'),
              (1, 1, 'machine_shop_tile', 'machine_shop_spritelayout_5'),
              (1, 2, 'machine_shop_tile', 'machine_shop_spritelayout_2'),
              (1, 3, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (1, 4, 'machine_shop_tile', 'machine_shop_spritelayout_12'),
              (2, 0, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (2, 1, 'machine_shop_tile', 'machine_shop_spritelayout_7'),
              (2, 2, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (2, 3, 'machine_shop_tile', 'machine_shop_spritelayout_10'),
              (2, 4, 'machine_shop_tile', 'machine_shop_spritelayout_11'),
              (3, 0, 'machine_shop_tile', 'machine_shop_spritelayout_6'),
              (3, 1, 'machine_shop_tile', 'machine_shop_spritelayout_5'),
              (3, 2, 'machine_shop_tile', 'machine_shop_spritelayout_9'),
              (3, 3, 'machine_shop_tile', 'machine_shop_spritelayout_8'),
              (3, 4, 'machine_shop_tile', 'machine_shop_spritelayout_13'),
    ]
)
industry.add_industry_layout(
    id = 'machine_shop_industry_layout_5',
    layout = [(0, 0, 'machine_shop_tile', 'machine_shop_spritelayout_3'),
              (0, 1, 'machine_shop_tile', 'machine_shop_spritelayout_4'),
              (0, 2, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (0, 3, 'machine_shop_tile', 'machine_shop_spritelayout_7'),
              (0, 4, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (0, 5, 'machine_shop_tile', 'machine_shop_spritelayout_10'),
              (1, 0, 'machine_shop_tile', 'machine_shop_spritelayout_12'),
              (1, 1, 'machine_shop_tile', 'machine_shop_spritelayout_11'),
              (1, 2, 'machine_shop_tile', 'machine_shop_spritelayout_6'),
              (1, 3, 'machine_shop_tile', 'machine_shop_spritelayout_5'),
              (1, 4, 'machine_shop_tile', 'machine_shop_spritelayout_9'),
              (1, 5, 'machine_shop_tile', 'machine_shop_spritelayout_8'),
              (2, 0, 'machine_shop_tile', 'machine_shop_spritelayout_13'),
              (2, 1, 'machine_shop_tile', 'machine_shop_spritelayout_13'),
              (2, 2, 'machine_shop_tile', 'machine_shop_spritelayout_14'),
              (2, 3, 'machine_shop_tile', 'machine_shop_spritelayout_2'),
              (2, 4, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
              (2, 5, 'machine_shop_tile', 'machine_shop_spritelayout_1'),
    ]
)
