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

industry = Industry(id='iron_works',
                    accept_cargo_types=['IORE', 'WOOD'],
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['STEL'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='194',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_PROCESSING',
                    min_cargo_distr='5',
                    spec_flags='0',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_IRON_WORKS)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_INDUSTRY_ESTATE))',
                    fund_cost_multiplier='69',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    extra_text_industry='STR_EXTRA_IRON_WORKS')

industry.economy_variations['FIRS'].enabled = True

industry.add_tile(id='iron_works_tile')
industry.add_tile(id='iron_works_tile_anim_1')
industry.add_tile(id='iron_works_tile_anim_2')

spriteset_ground = industry.add_spriteset(
    id = 'iron_works_spriteset_ground',
    type='cobble',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'iron_works_spriteset_ground_overlay',
    type='empty',
)
spriteset_1 = industry.add_spriteset(
    id = 'iron_works_spriteset_1',
    sprites = [(10, 10, 64, 70, -31, -40)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'iron_works_spriteset_2',
    sprites = [(80, 10, 64, 70, -31, -39)],
    zextent = 32
)
spriteset_3 = industry.add_spriteset(
    id = 'iron_works_spriteset_3',
    sprites = [(150, 10, 64, 70, -31, -39)],
    zextent = 32
)
spriteset_iron_pigs_anim = industry.add_spriteset(
    id = 'iron_works_spriteset_iron_pigs_1',
    sprites = [(220, 10, 64, 70, -31, -39), (290, 10, 64, 70, -31, -39), (360, 10, 64, 70, -31, -39)],
    zextent = 32,
    animation_rate = 1
)
spriteset_ground_pigs = industry.add_spriteset(
    id = 'iron_works_spriteset_ground_pigs',
    type='cobble',
    num_sprites_to_autofill = len(spriteset_iron_pigs_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_ground_overlay_pigs = industry.add_spriteset(
    id = 'iron_works_spriteset_ground_overlay_pigs',
    type='empty',
    num_sprites_to_autofill = len(spriteset_iron_pigs_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type = 'dark_smoke_small',
    xoffset= 0,
    yoffset= 4,
    zoffset= 23,
)

industry.add_spritelayout(
    id = 'iron_works_spritelayout_furnace_anim',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    smoke_sprites = [sprite_smoke],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'iron_works_spritelayout_large_shed',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'iron_works_spritelayout_large_shed_clerestory_roof',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'iron_works_spritelayout_iron_pigs_anim',
    ground_sprite = spriteset_ground_pigs,
    ground_overlay = spriteset_ground_overlay_pigs,
    building_sprites = [spriteset_iron_pigs_anim],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'iron_works_spritelayout_empty',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se']
)
industry.add_industry_layout(
    id = 'iron_works_industry_layout_1',
    layout = [(0, 0, 'iron_works_tile', 'iron_works_spritelayout_large_shed_clerestory_roof'),
              (0, 1, 'iron_works_tile_anim_1', 'iron_works_spritelayout_furnace_anim'),
              (0, 2, 'iron_works_tile_anim_2', 'iron_works_spritelayout_iron_pigs_anim'),
              (1, 0, 'iron_works_tile', 'iron_works_spritelayout_large_shed_clerestory_roof'),
              (1, 1, 'iron_works_tile_anim_1', 'iron_works_spritelayout_furnace_anim'),
              (1, 2, 'iron_works_tile_anim_2', 'iron_works_spritelayout_iron_pigs_anim'),
              (2, 0, 'iron_works_tile', 'iron_works_spritelayout_large_shed'),
              (2, 1, 'iron_works_tile', 'iron_works_spritelayout_empty'),
              (2, 2, 'iron_works_tile', 'iron_works_spritelayout_empty')
    ]
)
