"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='dairy',
                    processed_cargos_and_output_ratios=[('MNSP', 3), ('MILK', 5)],
                    combined_cargos_boost_prod=True,
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['FOOD'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='15',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_PROCESSING',
                    min_cargo_distr='5',
                    spec_flags='bitmask(IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE)',
                    location_checks=IndustryLocationChecks(incompatible={'dairy': 56,
                                                                         'dairy_farm': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_DAIRY)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_MILL))',
                    fund_cost_multiplier='45',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    extra_text_industry='STR_EXTRA_DAIRY',
                    snakebite=True)

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True

# tile with animation for flag
industry.add_tile(id='dairy_tile_1',
                  animation_length=6,
                  animation_looping=True,
                  animation_speed=3,
                  location_checks=TileLocationChecks(disallow_slopes=True,
                                                     disallow_industry_adjacent=True))
# tile with animation for smoke
industry.add_tile(id='dairy_tile_2',
                  animation_length=7*6, # animation length should have a common factor for all tiles in industry
                  animation_looping=True,
                  animation_speed=3,
                  custom_animation_control={'macro':'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(disallow_slopes=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'dairy_spriteset_ground',
    type = 'concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'dairy_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'dairy_spriteset_1',
    sprites = [(10, 10, 64, 94, -31, -63)],
    zextent = 32
)
spriteset_flag_anim = industry.add_spriteset(
    id = 'dairy_spriteset_flag_anim',
    sprites = [(220, 120, 64, 64, -31, -65), (10, 120, 64, 64, -31, -65), (80, 120, 64, 64, -31, -65),
               (150, 120, 64, 64, -31, -65), (80, 120, 64, 64, -31, -65), (10, 120, 64, 64, -31, -65)],
    zextent = 32,
    animation_rate = 1
)
spriteset_ground_anim = industry.add_spriteset(
    id = 'dairy_spriteset_ground_anim',
    type = 'concrete',
    num_sprites_to_autofill = len(spriteset_flag_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_ground_overlay_anim = industry.add_spriteset(
    id = 'dairy_spriteset_ground_overlay_anim',
    type = 'empty',
    num_sprites_to_autofill = len(spriteset_flag_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_2 = industry.add_spriteset(
    id = 'dairy_spriteset_2',
    sprites = [(80, 10, 64, 94, -31, -63)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_flag_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_3 = industry.add_spriteset(
    id = 'dairy_spriteset_3',
    sprites = [(150, 10, 64, 94, -31, -62)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'dairy_spriteset_4',
    sprites = [(220, 10, 64, 94, -31, -43)],
    zextent = 24
)
spriteset_5 = industry.add_spriteset(
    id = 'dairy_spriteset_5',
    sprites = [(290, 10, 64, 94, -31, -43)],
    zextent = 24
)
spriteset_6 = industry.add_spriteset(
    id = 'dairy_spriteset_6',
    sprites = [(360, 10, 64, 94, -31, -43)],
    zextent = 24
)
spriteset_7 = industry.add_spriteset(
    id = 'dairy_spriteset_7',
    sprites = [(430, 10, 64, 94, -31, -43)],
    zextent = 48
)
spriteset_8 = industry.add_spriteset(
    id = 'dairy_spriteset_8',
    sprites = [(500, 10, 64, 94, -31, -63)],
    zextent = 16
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 0,
    yoffset= 12,
    zoffset= 56,
)

industry.add_spritelayout(
    id = 'dairy_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'dairy_spritelayout_2',
    ground_sprite = spriteset_ground_anim,
    ground_overlay = spriteset_ground_overlay_anim,
    building_sprites = [spriteset_2, spriteset_flag_anim],
    fences = ['nw','ne','se']
)
industry.add_spritelayout(
    id = 'dairy_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'dairy_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'dairy_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'dairy_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'dairy_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    smoke_sprites = [sprite_smoke],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'dairy_spritelayout_8',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'dairy_industry_layout_1',
    layout = [(0, 0, 'dairy_tile_2', 'dairy_spritelayout_7'),
              (0, 1, 'dairy_tile_1', 'dairy_spritelayout_5'),
              (1, 0, 'dairy_tile_1', 'dairy_spritelayout_6'),
              (1, 1, 'dairy_tile_1', 'dairy_spritelayout_4'),
              (2, 0, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (2, 1, 'dairy_tile_1', 'dairy_spritelayout_3'),
              (3, 0, 'dairy_tile_1', 'dairy_spritelayout_1'),
              (3, 1, 'dairy_tile_1', 'dairy_spritelayout_2')
    ]
)
industry.add_industry_layout(
    id = 'dairy_industry_layout_2',
    layout = [(0, 1, 'dairy_tile_2', 'dairy_spritelayout_7'),
              (0, 2, 'dairy_tile_1', 'dairy_spritelayout_5'),
              (1, 1, 'dairy_tile_1', 'dairy_spritelayout_6'),
              (1, 2, 'dairy_tile_1', 'dairy_spritelayout_4'),
              (2, 0, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (2, 1, 'dairy_tile_1', 'dairy_spritelayout_3'),
              (2, 2, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (3, 0, 'dairy_tile_1', 'dairy_spritelayout_1'),
              (3, 1, 'dairy_tile_1', 'dairy_spritelayout_2'),
              (3, 2, 'dairy_tile_1', 'dairy_spritelayout_8')
    ]
)
industry.add_industry_layout(
    id = 'dairy_industry_layout_3',
    layout = [(0, 0, 'dairy_tile_2', 'dairy_spritelayout_7'),
              (0, 1, 'dairy_tile_1', 'dairy_spritelayout_5'),
              (0, 2, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (1, 0, 'dairy_tile_1', 'dairy_spritelayout_6'),
              (1, 1, 'dairy_tile_1', 'dairy_spritelayout_4'),
              (1, 2, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (2, 1, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (2, 2, 'dairy_tile_1', 'dairy_spritelayout_3'),
              (3, 1, 'dairy_tile_1', 'dairy_spritelayout_1'),
              (3, 2, 'dairy_tile_1', 'dairy_spritelayout_2')
    ]
)
industry.add_industry_layout(
    id = 'dairy_industry_layout_4',
    layout = [(0, 0, 'dairy_tile_2', 'dairy_spritelayout_7'),
              (0, 1, 'dairy_tile_1', 'dairy_spritelayout_5'),
              (0, 2, 'dairy_tile_2', 'dairy_spritelayout_7'),
              (0, 3, 'dairy_tile_1', 'dairy_spritelayout_5'),
              (1, 0, 'dairy_tile_1', 'dairy_spritelayout_6'),
              (1, 1, 'dairy_tile_1', 'dairy_spritelayout_4'),
              (1, 2, 'dairy_tile_1', 'dairy_spritelayout_6'),
              (1, 3, 'dairy_tile_1', 'dairy_spritelayout_4'),
              (2, 0, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (2, 1, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (2, 2, 'dairy_tile_1', 'dairy_spritelayout_3'),
              (2, 3, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (3, 1, 'dairy_tile_1', 'dairy_spritelayout_1'),
              (3, 2, 'dairy_tile_1', 'dairy_spritelayout_2')
    ]
)
industry.add_industry_layout(
    id = 'dairy_industry_layout_5',
    layout = [(0, 0, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (0, 1, 'dairy_tile_1', 'dairy_spritelayout_3'),
              (0, 2, 'dairy_tile_2', 'dairy_spritelayout_7'),
              (0, 3, 'dairy_tile_1', 'dairy_spritelayout_5'),
              (1, 0, 'dairy_tile_1', 'dairy_spritelayout_1'),
              (1, 1, 'dairy_tile_1', 'dairy_spritelayout_2'),
              (1, 2, 'dairy_tile_1', 'dairy_spritelayout_6'),
              (1, 3, 'dairy_tile_1', 'dairy_spritelayout_4')
    ]
)
industry.add_industry_layout(
    id = 'dairy_industry_layout_6',
    layout = [(0, 0, 'dairy_tile_2', 'dairy_spritelayout_7'),
              (0, 1, 'dairy_tile_1', 'dairy_spritelayout_5'),
              (1, 0, 'dairy_tile_1', 'dairy_spritelayout_6'),
              (1, 1, 'dairy_tile_1', 'dairy_spritelayout_4'),
              (3, 0, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (3, 1, 'dairy_tile_1', 'dairy_spritelayout_3'),
              (4, 0, 'dairy_tile_1', 'dairy_spritelayout_1'),
              (4, 1, 'dairy_tile_1', 'dairy_spritelayout_2')
    ]
)
industry.add_industry_layout(
    id = 'dairy_industry_layout_7',
    layout = [(0, 0, 'dairy_tile_2', 'dairy_spritelayout_7'),
              (0, 1, 'dairy_tile_1', 'dairy_spritelayout_5'),
              (0, 3, 'dairy_tile_2', 'dairy_spritelayout_7'),
              (0, 4, 'dairy_tile_1', 'dairy_spritelayout_5'),
              (1, 0, 'dairy_tile_1', 'dairy_spritelayout_6'),
              (1, 1, 'dairy_tile_1', 'dairy_spritelayout_4'),
              (1, 3, 'dairy_tile_1', 'dairy_spritelayout_6'),
              (1, 4, 'dairy_tile_1', 'dairy_spritelayout_4'),
              (2, 0, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (2, 1, 'dairy_tile_1', 'dairy_spritelayout_3'),
              (2, 3, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (2, 4, 'dairy_tile_1', 'dairy_spritelayout_8'),
              (3, 0, 'dairy_tile_1', 'dairy_spritelayout_1'),
              (3, 1, 'dairy_tile_1', 'dairy_spritelayout_2')
    ]
)
