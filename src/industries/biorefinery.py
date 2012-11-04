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

industry = Industry(id='biorefinery',
                    accept_cargo_types='[GRAI, SGBT]',
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types='[RFPR, PETR]',
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='186',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_PROCESSING',
                    min_cargo_distr='5',
                    spec_flags='bitmask(IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE)',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_BIOREFINERY)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_IND_BIOREFINERY))',
                    fund_cost_multiplier='170',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS')

industry.economy_variations['BASIC'].disabled = True

industry.add_tile(id='biorefinery_tile')

spriteset_ground = industry.add_spriteset(
    id = 'biorefinery_spriteset_ground',
    type = 'concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'biorefinery_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'biorefinery_spriteset_1',
    sprites = [(500, 10, 64, 66, -31, -35)],
    zextent = 48
)
spriteset_2 = industry.add_spriteset(
    id = 'biorefinery_spriteset_2',
    sprites = [(570, 10, 64, 66, -31, -35)],
    zextent = 48
)
spriteset_3 = industry.add_spriteset(
    id = 'biorefinery_spriteset_3',
    sprites = [(710, 10, 64, 66, -31, -35)],
    zextent = 48
)
spriteset_4 = industry.add_spriteset(
    id = 'biorefinery_spriteset_4',
    sprites = [(80, 10, 64, 88, -31, -58)],
    zextent = 48
)
spriteset_5 = industry.add_spriteset(
    id = 'biorefinery_spriteset_5',
    sprites = [(150, 10, 64, 88, -31, -59)],
    zextent = 48
)
spriteset_6 = industry.add_spriteset(
    id = 'biorefinery_spriteset_6',
    sprites = [(220, 10, 64, 88, -31, -64)],
    zextent = 48
)
spriteset_7 = industry.add_spriteset(
    id = 'biorefinery_spriteset_7',
    sprites = [(360, 10, 64, 73, -31, -45)],
    zextent = 48
)
spriteset_8 = industry.add_spriteset(
    id = 'biorefinery_spriteset_8',
    sprites = [(430, 10, 64, 66, -31, -38)],
    zextent = 48
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 1,
    yoffset= 0,
    zoffset= 62,
    animation_frame_offset = 1
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 1,
    yoffset= -3,
    zoffset= 62
)

industry.add_spritelayout(
    id = 'biorefinery_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'biorefinery_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'biorefinery_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'biorefinery_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'biorefinery_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'biorefinery_spritelayout_6_anim',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    smoke_sprites = [sprite_smoke_2, sprite_smoke_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'biorefinery_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'biorefinery_spritelayout_8',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'biorefinery_spritelayout_9',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'biorefinery_industry_layout_1',
    default_spritelayout = 'biorefinery_spritelayout_9',
    layout = [(0, 0, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (0, 2, 'biorefinery_tile', 'biorefinery_spritelayout_2'),
              (0, 3, 'biorefinery_tile', 'biorefinery_spritelayout_1'),
              (0, 4, 'biorefinery_tile', 'biorefinery_spritelayout_1'),
              (1, 0, 'biorefinery_tile', 'biorefinery_spritelayout_8'),
              (1, 2, 'biorefinery_tile', 'biorefinery_spritelayout_4'),
              (1, 3, 'biorefinery_tile', 'biorefinery_spritelayout_5'),
              (1, 4, 'biorefinery_tile', 'biorefinery_spritelayout_6_anim'),
              (2, 0, 'biorefinery_tile', 'biorefinery_spritelayout_7'),
              (2, 2, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (2, 3, 'biorefinery_tile', 'biorefinery_spritelayout_3'),
              (2, 4, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
    ]
)
industry.add_industry_layout(
    id = 'biorefinery_industry_layout_2',
    default_spritelayout = 'biorefinery_spritelayout_9',
    layout = [(0, 0, 'biorefinery_tile', 'biorefinery_spritelayout_8'),
              (0, 1, 'biorefinery_tile', 'biorefinery_spritelayout_4'),
              (0, 2, 'biorefinery_tile', 'biorefinery_spritelayout_5'),
              (0, 3, 'biorefinery_tile', 'biorefinery_spritelayout_6_anim'),
              (0, 4, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (1, 0, 'biorefinery_tile', 'biorefinery_spritelayout_7'),
              (1, 1, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (1, 2, 'biorefinery_tile', 'biorefinery_spritelayout_3'),
              (1, 3, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (1, 4, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (2, 0, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (2, 1, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (2, 2, 'biorefinery_tile', 'biorefinery_spritelayout_1'),
              (2, 3, 'biorefinery_tile', 'biorefinery_spritelayout_1'),
              (2, 4, 'biorefinery_tile', 'biorefinery_spritelayout_2'),
    ]
)
industry.add_industry_layout(
    id = 'biorefinery_industry_layout_3',
    default_spritelayout = 'biorefinery_spritelayout_9',
    layout = [(0, 0, 'biorefinery_tile', 'biorefinery_spritelayout_2'),
              (0, 2, 'biorefinery_tile', 'biorefinery_spritelayout_2'),
              (0, 3, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (1, 0, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (1, 2, 'biorefinery_tile', 'biorefinery_spritelayout_4'),
              (1, 3, 'biorefinery_tile', 'biorefinery_spritelayout_3'),
              (2, 0, 'biorefinery_tile', 'biorefinery_spritelayout_8'),
              (2, 2, 'biorefinery_tile', 'biorefinery_spritelayout_5'),
              (2, 3, 'biorefinery_tile', 'biorefinery_spritelayout_6_anim'),
              (3, 0, 'biorefinery_tile', 'biorefinery_spritelayout_7'),
              (3, 2, 'biorefinery_tile', 'biorefinery_spritelayout_3'),
              (3, 3, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (4, 0, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (4, 2, 'biorefinery_tile', 'biorefinery_spritelayout_1'),
              (4, 3, 'biorefinery_tile', 'biorefinery_spritelayout_1'),
    ]
)
industry.add_industry_layout(
    id = 'biorefinery_industry_layout_4',
    default_spritelayout = 'biorefinery_spritelayout_9',
    layout = [(0, 0, 'biorefinery_tile', 'biorefinery_spritelayout_1'),
              (0, 1, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (0, 2, 'biorefinery_tile', 'biorefinery_spritelayout_8'),
              (1, 0, 'biorefinery_tile', 'biorefinery_spritelayout_1'),
              (1, 1, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
              (1, 2, 'biorefinery_tile', 'biorefinery_spritelayout_7'),
              (3, 0, 'biorefinery_tile', 'biorefinery_spritelayout_4'),
              (3, 1, 'biorefinery_tile', 'biorefinery_spritelayout_5'),
              (3, 2, 'biorefinery_tile', 'biorefinery_spritelayout_6_anim'),
              (4, 0, 'biorefinery_tile', 'biorefinery_spritelayout_2'),
              (4, 1, 'biorefinery_tile', 'biorefinery_spritelayout_3'),
              (4, 2, 'biorefinery_tile', 'biorefinery_spritelayout_9'),
    ]
)

