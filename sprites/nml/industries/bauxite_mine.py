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

industry = Industry(id='bauxite_mine',
                    accept_cargo_types='[ENSP]',
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types='[AORE]',
                    layouts='[bauxite_mine_industry_layout_1_tilelayout]',
                    prob_in_game='10',
                    prob_random='6',
                    prod_multiplier='[19, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='71',
                    conflicting_ind_types='[]',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_EXTRACTIVE',
                    min_cargo_distr='5',
                    spec_flags='0',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_BAUXITE_MINE)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_IND_BAUXITE_MINE))',
                    fund_cost_multiplier='238',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS')

industry.add_tile(id='bauxite_mine_tile')

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS' # ground tile same as overlay tile
)
sprite_ground_overlay = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
sprite_1 = industry.add_sprite(
    sprite_number = 2039,
    zextent= 12,
)
# there is no sprite 2 for this industry, spritelayout_2 doesn't need a building sprite
sprite_3_anim = industry.add_sprite(
    sprite_number = '2028 + ((animation_frame < 33) ? (animation_frame %3) : 0)',
    xoffset= 2,
    yoffset= 3,
    xextent= 13,
    yextent= 12,
    zextent= 12,
)
sprite_4 = industry.add_sprite(
    sprite_number = 2036,
    zextent= 12,
)
sprite_5 = industry.add_sprite(
    sprite_number = 2033,
    zextent= 12,
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type = 'dark_smoke_small',
    xoffset= 0,
    yoffset= 2,
    zoffset= 38,
)

industry.add_spritelayout(
    id = 'bauxite_mine_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [sprite_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'bauxite_mine_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'bauxite_mine_spritelayout_3_anim',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [sprite_3_anim],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'bauxite_mine_spritelayout_4',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [sprite_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'bauxite_mine_spritelayout_5',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [sprite_5],
    smoke_sprites = [sprite_smoke],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'bauxite_mine_industry_layout_1',
    default_spritelayout = 'bauxite_mine_spritelayout_1',
    layout = [(0, 0, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_1'),
              (0, 1, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_1'),
              (0, 2, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_1'),
              (2, 0, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_5'),
              (2, 1, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_3_anim'),
              (2, 2, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_4'),
              (3, 0, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_1'),
              (3, 1, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_1'),
              (3, 2, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_2'),
              (4, 1, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_1'),
    ]
)
# Templating
industry.render_and_save_pnml()
