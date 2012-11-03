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

industry = Industry(id='grain_mill',
                    accept_cargo_types='[MNSP, GRAI]',
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types='[FOOD]',
                    layouts='[grain_mill_industry_layout_1_tilelayout, grain_mill_industry_layout_2_tilelayout, grain_mill_industry_layout_3_tilelayout, grain_mill_industry_layout_4_tilelayout]',
                    prob_in_game='10',
                    prob_random='10',
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
                    name='string(STR_IND_GRAIN_MILL)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_IND_GRAIN_MILL))',
                    fund_cost_multiplier='44',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS')

industry.add_tile(id='grain_mill_tile')

spriteset_ground_bakery = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_bakery',
    type='cobble',
)
spriteset_ground_overlay_1 = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_1',
    sprites = [(10, 10, 64, 31, -31, 0)],
)
spriteset_ground_overlay_2 = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_2',
    sprites = [(80, 10, 64, 31, -31, 0)]
)
spriteset_ground_overlay_3 = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_3',
    sprites = [(150, 10, 64, 31, -31, 0)]
)
spriteset_ground_overlay_4 = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_4',
    sprites = [(220, 10, 64, 31, -31, 0)]
)
spriteset_1 = industry.add_spriteset(
    id = 'grain_mill_spriteset_1',
    sprites = [(10, 10, 64, 31, -31, 0)]
)
spriteset_2 = industry.add_spriteset(
    id = 'grain_mill_spriteset_2',
    sprites = [(80, 10, 64, 31, -31, 0)]
)
spriteset_3 = industry.add_spriteset(
    id = 'grain_mill_spriteset_3',
    sprites = [(150, 60, 64, 82, -31, -51)],
    zextent = 48 # optional zextent value, will default to 16 if this param is omitted
)
spriteset_4 = industry.add_spriteset(
    id = 'grain_mill_spriteset_4',
    sprites = [(220, 60, 64, 82, -31, -51)],
    zextent = 48 # optional zextent value, will default to 16 if this param is omitted
)
spriteset_windmill_anim = industry.add_spriteset(
    id = 'grain_mill_spriteset_windmill_anim',
    sprites = [(10, 200, 64, 82, -31, -52), (80, 200, 64, 82, -31, -52), (150, 200, 64, 82, -31, -52),
               (220, 200, 64, 82, -31, -52), (290, 200, 64, 82, -31, -52), (360, 200, 64, 82, -31, -52)],
    zextent = 24, # optional zextent value, will default to 16 if this param is omitted
    animation_rate = 1
)
spriteset_ground_windmill = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_windmill',
    type = 'empty',
    num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_ground_overlay_windmill = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_windmill',
    sprites = [(10, 160, 64, 31, -31, 0)],
    num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)

industry.add_spritelayout(
    id = 'grain_mill_spritelayout_brickbakery_1',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_1,
    building_sprites = [],
    fences = ['nw','ne','se']
)
industry.add_spritelayout(
    id = 'grain_mill_spritelayout_brickbakery_2',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_2,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'grain_mill_spritelayout_brickbakery_3',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_3,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'grain_mill_spritelayout_brickbakery_4',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_4,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'grain_mill_spritelayout_windmill_anim',
    ground_sprite = spriteset_ground_windmill,
    ground_overlay = spriteset_ground_overlay_windmill,
    building_sprites = [spriteset_windmill_anim],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'grain_mill_industry_layout_1',
    default_spritelayout = 'grain_mill_spritelayout_brickbakery_3',
    layout = [(0, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (0, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (1, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_1'),
              (1, 1, 'grain_mill_tile','grain_mill_spritelayout_brickbakery_2')
    ]
)
industry.add_industry_layout(
    id = 'grain_mill_industry_layout_2',
    default_spritelayout = 'grain_mill_spritelayout_brickbakery_3',
    layout = [(0, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (0, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (1, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (1, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (2, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_1'),
              (2, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_2')
    ]
)
industry.add_industry_layout(
    id = 'grain_mill_industry_layout_3',
    default_spritelayout = 'grain_mill_spritelayout_brickbakery_3',
    layout = [(0, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (0, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (0, 2, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (0, 3, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (1, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_1'),
              (1, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_2'),
              (1, 2, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_1'),
              (1, 3, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_2')
    ]
)
industry.add_industry_layout(
    id = 'grain_mill_industry_layout_4',
    default_spritelayout = 'grain_mill_spritelayout_windmill_anim',
    layout = [(0, 0, 'grain_mill_tile', 'grain_mill_spritelayout_windmill_anim')]
)

# Templating
industry.render_and_save_pnml()
