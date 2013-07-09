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

industry = Industry(id='brewery',
                    accept_cargo_types=['MNSP', 'FRUT', 'GRAI'],
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['BEER'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='191',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_PROCESSING',
                    min_cargo_distr='5',
                    spec_flags='0',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_BREWERY)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_TOWN))',
                    fund_cost_multiplier='50',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    extra_text_industry='STR_EXTRA_BREWERY, string(STR_EXTRA_BREWERY_GRAIN_SUBSTR), string(STR_EXTRA_BREWERY_FRUIT_SUBSTR)')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.economy_variations['BASIC_TEMPERATE'].extra_text_industry = 'STR_EXTRA_BREWERY, string(STR_EXTRA_BREWERY_FRUIT_SUBSTR)'
industry.economy_variations['BASIC_TEMPERATE'].name = 'string(STR_IND_BREWERY_CIDER_MILL)'
industry.economy_variations['BASIC_ARCTIC'].extra_text_industry = 'STR_EXTRA_BREWERY, string(STR_EXTRA_BREWERY_GRAIN_SUBSTR)'

industry.add_tile(id='brewery_tile')

spriteset_ground = industry.add_spriteset(
    id = 'brewery_spriteset_ground',
    type = 'cobble',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'brewery_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'brewery_spriteset_1',
    sprites = [(10, 60, 64, 91, -31, -60)],
    zextent = 48
)
spriteset_2 = industry.add_spriteset(
    id = 'brewery_spriteset_2',
    sprites = [(80, 60, 64, 91, -31, -60)],
    zextent = 48
)
spriteset_3 = industry.add_spriteset(
    id = 'brewery_spriteset_3',
    sprites = [(150, 60, 64, 91, -31, -60)],
    zextent = 48
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_small',
    xoffset= 8,
    yoffset= 0,
    zoffset= 55,
)

industry.add_spritelayout(
    id = 'brewery_spritelayout_1_anim',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    smoke_sprites = [sprite_smoke],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'brewery_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'brewery_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'brewery_industry_layout_1',
    layout = [(0, 2, 'brewery_tile', 'brewery_spritelayout_3'),
              (1, 0, 'brewery_tile', 'brewery_spritelayout_1_anim'),
              (1, 2, 'brewery_tile', 'brewery_spritelayout_2')
    ]
)
industry.add_industry_layout(
    id = 'brewery_industry_layout_2',
    layout = [(0, 0, 'brewery_tile', 'brewery_spritelayout_3'),
              (1, 0, 'brewery_tile', 'brewery_spritelayout_2'),
              (2, 0, 'brewery_tile', 'brewery_spritelayout_1_anim')
    ]
)
industry.add_industry_layout(
    id = 'brewery_industry_layout_3',
    layout = [(0, 1, 'brewery_tile', 'brewery_spritelayout_3'),
              (1, 0, 'brewery_tile', 'brewery_spritelayout_1_anim'),
              (1, 1, 'brewery_tile', 'brewery_spritelayout_2')
    ]
)
industry.add_industry_layout(
    id = 'brewery_industry_layout_4',
    layout = [(0, 0, 'brewery_tile', 'brewery_spritelayout_1_anim'),
              (1, 0, 'brewery_tile', 'brewery_spritelayout_3'),
              (2, 0, 'brewery_tile', 'brewery_spritelayout_2')
    ]
)
industry.add_industry_layout(
    id = 'brewery_industry_layout_5',
    layout = [(0, 0, 'brewery_tile', 'brewery_spritelayout_3'),
              (0, 1, 'brewery_tile', 'brewery_spritelayout_3'),
              (1, 0, 'brewery_tile', 'brewery_spritelayout_2'),
              (1, 1, 'brewery_tile', 'brewery_spritelayout_2'),
              (2, 0, 'brewery_tile', 'brewery_spritelayout_1_anim')
    ]
)

