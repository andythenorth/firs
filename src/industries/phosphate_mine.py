"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryExtractive, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryExtractive(id='phosphate_mine',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['PHOS', 'CLAY'],
                    layouts='AUTO',
                    prob_in_game='4',
                    prob_random='7',
                    prod_multiplier='[16, 10]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='46',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='0',
                    # allow longer distance on clustering than usual, and more clusters, as industry is hard to locate
                    location_checks=IndustryLocationChecks(require_cluster=['phosphate_mine', [20, 90, 1, 4]],
                                                           incompatible={'brick_works': 16,
                                                                         'paper_mill': 16,
                                                                         'cement_plant': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_PHOSPHATE_MINE)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_PIT))',
                    fund_cost_multiplier='200',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    template="refactor_primary_waterpit.pypnml" )

industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].prob_random = '1'
industry.economy_variations['MISTAH_KURTZ'].prob_in_game = '10'

# 2 tiles for this industry: pit outer tile cannot be on slopes; pit inner tiles and processor tiles can be
# cases for both tiles ensure that tiles can only be built at same height as north tile
industry.add_tile(id='phosphate_mine_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_desert=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='phosphate_mine_tile_2',
                  animation_length=56,
                  animation_looping=True,
                  animation_speed=4,
                  custom_animation_control={'macro':'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
		          foundations='return CB_RESULT_NO_FOUNDATIONS', # might not be needed, cargo-culted from previous code, didn't test; may be needed to stop rear foundations showing in some cases?
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_slopes=True,
                                                     disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_ground',
    type = 'empty'
)
spriteset_animated_dozer = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_animated_dozer',
    sprites = [(440, 90, 64, 31, -31, 0), (510, 90, 64, 31, -31, 0), (580, 90, 64, 31, -31, 0),
               (650, 90, 64, 31, -31, 0), (720, 90, 64, 31, -31, 0), (790, 90, 64, 31, -31, 0),
               (790, 90, 64, 31, -31, 0), (720, 90, 64, 31, -31, 0), (650, 90, 64, 31, -31, 0),
               (580, 90, 64, 31, -31, 0), (510, 90, 64, 31, -31, 0), (440, 90, 64, 31, -31, 0)],
    zextent = 32,
    animation_rate = 1,
    custom_sprite_selector = '(animation_frame < 36) ? (animation_frame % 12) : 0',
)
spriteset_ground_animated_tile = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_ground_animated_tile',
    type = 'empty',
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_1 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_1',
    sprites = [(10, 90, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_2 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_2',
    sprites = [(80, 90, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_4 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_4',
    sprites = [(150, 90, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_5 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_5',
    sprites = [(220, 90, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_6 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_6',
    sprites = [(290, 90, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_7 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_7',
    sprites = [(10, 50, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_8 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_8',
    sprites = [(80, 50, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_10 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_10',
    sprites = [(150, 50, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_11 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_11',
    sprites = [(220, 50, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_12 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_12',
    sprites = [(290, 50, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_19 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_19',
    sprites = [(10, 10, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_20 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_20',
    sprites = [(80, 10, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_22 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_22',
    sprites = [(150, 10, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_23 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_23',
    sprites = [(220, 10, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_24 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_24',
    sprites = [(290, 10, 64, 31, -31, 0)],
    zextent = 32,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_pile = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_pile',
    sprites = [(360, 50, 64, 31, -63, -16)],
    zextent = 64,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_crane_1 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_crane_1',
    sprites = [(440, 10, 64, 71, -48, -55), (440, 10, 64, 71, -48, -55), (510, 10, 64, 71, -48, -55),
               (580, 10, 64, 71, -48, -55), (650, 10, 64, 71, -48, -55), (650, 10, 64, 71, -48, -55),
               (650, 10, 64, 71, -48, -55), (580, 10, 64, 71, -48, -55), (510, 10, 64, 71, -48, -55),
               (440, 10, 64, 71, -48, -55), (440, 10, 64, 71, -48, -55), (440, 10, 64, 71, -48, -55)],
    zextent = 64,
    animation_rate = 1,
    custom_sprite_selector = '(animation_frame > 32) ? (animation_frame % 12) : 0',
)
spriteset_pit_conveyor_0 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_pit_conveyor_0',
    sprites = [(10, 130, 64, 64, -31, -22)],
    zextent = 64,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_pit_conveyor_1 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_pit_conveyor_1',
    sprites = [(80, 130, 64, 64, -31, -22)],
    zextent = 64,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_pit_conveyor_2 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_pit_conveyor_2',
    sprites = [(150, 130, 64, 64, -31, -22)],
    zextent = 64,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_pit_conveyor_3 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_pit_conveyor_3',
    sprites = [(220, 130, 64, 64, -31, -22)],
    zextent = 64,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_pit_conveyor_4 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_pit_conveyor_4',
    sprites = [(290, 130, 64, 64, -31, -22)],
    zextent = 64,
    num_sprites_to_autofill = len(spriteset_animated_dozer.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_39 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_39',
    sprites = [(870, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_40 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_40',
    sprites = [(940, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_41 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_41',
    sprites = [(1010, 10, 64, 34, -31, -3)],
    zextent = 32
)
spriteset_silo = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_silo',
    sprites = [(870, 50, 64, 64, -31, -35)],
    zextent = 32
)
spriteset_conveyor_2 = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_conveyor_2',
    sprites = [(940, 50, 64, 64, -31, -35)],
    zextent = 32
)
spriteset_crusher = industry.add_spriteset(
    id = 'phosphate_mine_spriteset_crusher',
    sprites = [(1010, 50, 64, 64, -31, -33)],
    zextent = 32
)

industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_1',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_1,
    building_sprites = [],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_2',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_2,
    building_sprites = [spriteset_pit_conveyor_0],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_4',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_4,
    building_sprites = [],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_5',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_5,
    building_sprites = [spriteset_crane_1, spriteset_pile],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_6',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_6,
    building_sprites = [],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_7',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_7,
    building_sprites = [],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_8',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_8,
    building_sprites = [spriteset_animated_dozer],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_10',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_10,
    building_sprites = [],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_11',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_11,
    building_sprites = [],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_12',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_12,
    building_sprites = [],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_19',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_19,
    building_sprites = [],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_20',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_20,
    building_sprites = [spriteset_pit_conveyor_1],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_22',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_22,
    building_sprites = [spriteset_pit_conveyor_2],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_23',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_23,
    building_sprites = [spriteset_pit_conveyor_3],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_24',
    ground_sprite = spriteset_ground_animated_tile,
    ground_overlay = spriteset_24,
    building_sprites = [spriteset_pit_conveyor_4],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_39',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_39,
    building_sprites = [spriteset_silo],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_40',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_40,
    building_sprites = [spriteset_conveyor_2],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'phosphate_mine_spritelayout_41',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_41,
    building_sprites = [spriteset_crusher],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)


industry.add_industry_layout(
    id = 'phosphate_mine_layout_1',
    layout = [(0, 1, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_24'),
              (0, 2, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_12'),
              (0, 3, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_6'),
              (1, 0, 'phosphate_mine_tile_1', 'phosphate_mine_spritelayout_41'),
              (1, 1, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_23'),
              (1, 2, 'phosphate_mine_tile_1', 'phosphate_mine_spritelayout_11'),
              (1, 3, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_5'),
              (2, 0, 'phosphate_mine_tile_1', 'phosphate_mine_spritelayout_40'),
              (2, 1, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_22'),
              (2, 2, 'phosphate_mine_tile_1', 'phosphate_mine_spritelayout_10'),
              (2, 3, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_4'),
              (3, 0, 'phosphate_mine_tile_1', 'phosphate_mine_spritelayout_39'),
              (3, 1, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_20'),
              (3, 2, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_8'),
              (3, 3, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_2'),
              (4, 1, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_19'),
              (4, 2, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_7'),
              (4, 3, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_1'),
    ]
)

industry.add_industry_layout(
    id = 'phosphate_mine_layout_2',
    layout = [(0, 0, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_24'),
              (0, 1, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_12'),
              (0, 2, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_6'),
              (1, 0, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_23'),
              (1, 1, 'phosphate_mine_tile_1', 'phosphate_mine_spritelayout_11'),
              (1, 2, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_5'),
              (1, 3, 'phosphate_mine_tile_1', 'phosphate_mine_spritelayout_41'),
              (2, 0, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_22'),
              (2, 1, 'phosphate_mine_tile_1', 'phosphate_mine_spritelayout_10'),
              (2, 2, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_4'),
              (2, 3, 'phosphate_mine_tile_1', 'phosphate_mine_spritelayout_40'),
              (3, 0, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_20'),
              (3, 1, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_8'),
              (3, 2, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_2'),
              (3, 3, 'phosphate_mine_tile_1', 'phosphate_mine_spritelayout_39'),
              (4, 0, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_19'),
              (4, 1, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_7'),
              (4, 2, 'phosphate_mine_tile_2', 'phosphate_mine_spritelayout_1'),
    ]
)
