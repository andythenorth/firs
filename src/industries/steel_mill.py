"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='steel_mill',
                    processed_cargos_and_output_ratios=[('IORE', 3), ('COAL', 2), ('SCMT', 3)],
                    combined_cargos_boost_prod=True,
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['STEL'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='9',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='bitmask()',
                    location_checks=IndustryLocationChecks(incompatible={'steel_mill': 56,
                                                                         'junk_yard': 16,
                                                                         'coal_mine': 16,
                                                                         'iron_ore_mine': 16,
                                                                         'junk_yard': 16}),
                    remove_cost_multiplier='0',
                    name='TTD_STR_INDUSTRY_NAME_STEEL_MILL',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_POWERHUNGRY))',
                    fund_cost_multiplier='200',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    extra_text_industry='STR_EXTRA_STEELMILL',
                    intro_year=1850)


industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].intro_year = 1800

industry.add_tile(id='steel_mill_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  custom_animation_control={'macro':'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

industry.add_tile(id='steel_mill_tile_2',
                  animation_length=30,
                  animation_looping=True,
                  animation_speed=4,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS' # ground tile same as overlay tile
)
sprite_ground_overlay = industry.add_spriteset(
    id = 'steel_mill_sprite_ground_overlay',
    type='empty',
)
spriteset_ground_tile_dark = industry.add_spriteset(
    id = 'steel_mill_spriteset_ground_tile_dark',
    sprites = [(500, 10, 64, 122, -31, -90)],
)
spriteset_greeble = industry.add_spriteset(
    id = 'steel_mill_spriteset_greeble',
    sprites = [(150, 10, 64, 122, -31, -90)],
    zextent = 12
)
spriteset_blast_furnace_2 = industry.add_spriteset(
    id = 'steel_mill_spriteset_blast_furnace_2',
    sprites = [(10, 10, 64, 144, -31, -115)],
    zextent = 130
)
spriteset_blast_furnace_1 = industry.add_spriteset(
    id = 'steel_mill_spriteset_blast_furnace_1',
    sprites = [(80, 10, 64, 122, -31, -90)],
    zextent = 12
)
spriteset_small_shed = industry.add_spriteset(
    id = 'steel_mill_spriteset_small_shed',
    sprites = [(220, 10, 64, 122, -31, -90)],
    zextent = 32
)
spriteset_ladle_transporter = industry.add_spriteset(
    id = 'steel_mill_spriteset_ladle_transporter',
    sprites = [(290, 10, 64, 122, -31, -90)],
    zextent = 12
)
spriteset_brick_building = industry.add_spriteset(
    id = 'steel_mill_spriteset_brick_building',
    sprites = [(360, 10, 64, 122, -31, -90)],
    zextent = 12
)
spriteset_small_tanks = industry.add_spriteset(
    id = 'steel_mill_spriteset_small_tanks',
    sprites = [(430, 10, 64, 122, -31, -90)],
    zextent = 12
)
spriteset_large_shed_rear_part = industry.add_spriteset(
    id = 'steel_mill_spriteset_large_shed_rear_part',
    sprites = [(570, 10, 64, 122, -31, -90)],
    zextent = 12
)
spriteset_large_shed_front_part_animated = industry.add_spriteset(
    id = 'steel_mill_spriteset_large_shed_front_part_animated',
    sprites = [(10, 160, 64, 122, -31, -90), (80, 160, 64, 122, -31, -90), (150, 160, 64, 122, -31, -90),
               (220, 160, 64, 122, -31, -90), (290, 160, 64, 122, -31, -90), (360, 160, 64, 122, -31, -90),
               (430, 160, 64, 122, -31, -90), (500, 160, 64, 122, -31, -90), (570, 160, 64, 122, -31, -90),
               (640, 160, 64, 122, -31, -90)],
    zextent = 32,
    animation_rate = 1,
    custom_sprite_selector = '(animation_frame < 10) ? (animation_frame % 10) : 0',
)
spriteset_ground_tile_dark_animated = industry.add_spriteset(
    id = 'steel_mill_spriteset_ground_tile_dark_animated',
    sprites = [(500, 10, 64, 122, -31, -90)],
    num_sprites_to_autofill = len(spriteset_large_shed_front_part_animated.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_casting_shed_animated = industry.add_spriteset(
    id = 'steel_mill_spriteset_casting_shed_animated',
    sprites = [(10, 310, 64, 122, -31, -90), (80, 310, 64, 122, -31, -90), (150, 310, 64, 122, -31, -90),
               (220, 310, 64, 122, -31, -90), (290, 310, 64, 122, -31, -90), (360, 310, 64, 122, -31, -90),
               (430, 310, 64, 122, -31, -90), (500, 310, 64, 122, -31, -90), (570, 310, 64, 122, -31, -90),
               (640, 310, 64, 122, -31, -90)],
    zextent = 32,
    animation_rate = 1,
    custom_sprite_selector = '(animation_frame < 10) ? (animation_frame % 10) : 0',
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 5,
    yoffset= 6,
    zoffset= 68,
)

industry.add_spritelayout(
    id = 'steel_mill_spritelayout_empty',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'steel_mill_spritelayout_greeble',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_greeble],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'steel_mill_spritelayout_blast_furnace_1',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_blast_furnace_1],
    smoke_sprites = [sprite_smoke],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'steel_mill_spritelayout_blast_furnace_2',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_blast_furnace_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'steel_mill_spritelayout_small_shed',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_small_shed],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'steel_mill_spritelayout_ladle_transporter',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_ladle_transporter],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'steel_mill_spritelayout_brick_building',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_brick_building],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'steel_mill_spritelayout_small_tanks',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_small_tanks],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'steel_mill_spritelayout_large_shed_rear_part',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_large_shed_rear_part],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'steel_mill_spritelayout_large_shed_front_part',
    ground_sprite = spriteset_ground_tile_dark_animated,
    ground_overlay = spriteset_ground_tile_dark_animated,
    building_sprites = [spriteset_large_shed_front_part_animated],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'steel_mill_spritelayout_casting_shed',
    ground_sprite = spriteset_ground_tile_dark_animated,
    ground_overlay = spriteset_ground_tile_dark_animated,
    building_sprites = [spriteset_casting_shed_animated],
    fences = ['nw','ne','se','sw']
)
industry.add_industry_layout(
    id = 'steel_mill_industry_layout_1',
    layout = [(0, 0, 'steel_mill_tile_1', 'steel_mill_spritelayout_small_shed'),
              (0, 1, 'steel_mill_tile_1', 'steel_mill_spritelayout_empty'),
              (0, 2, 'steel_mill_tile_1', 'steel_mill_spritelayout_large_shed_rear_part'),
              (1, 0, 'steel_mill_tile_1', 'steel_mill_spritelayout_small_tanks'),
              (1, 1, 'steel_mill_tile_2', 'steel_mill_spritelayout_casting_shed'),
              (1, 2, 'steel_mill_tile_2', 'steel_mill_spritelayout_large_shed_front_part'),
              (2, 0, 'steel_mill_tile_1', 'steel_mill_spritelayout_blast_furnace_1'),
              (2, 1, 'steel_mill_tile_1', 'steel_mill_spritelayout_blast_furnace_2'),
              (2, 2, 'steel_mill_tile_1', 'steel_mill_spritelayout_small_shed'),
              (3, 0, 'steel_mill_tile_1', 'steel_mill_spritelayout_blast_furnace_1'),
              (3, 1, 'steel_mill_tile_1', 'steel_mill_spritelayout_blast_furnace_2'),
              (3, 2, 'steel_mill_tile_1', 'steel_mill_spritelayout_greeble'),
              (4, 0, 'steel_mill_tile_1', 'steel_mill_spritelayout_small_tanks'),
              (4, 1, 'steel_mill_tile_1', 'steel_mill_spritelayout_brick_building'),
              (4, 2, 'steel_mill_tile_1', 'steel_mill_spritelayout_ladle_transporter'),
    ]
)
industry.add_industry_layout(
    id = 'steel_mill_industry_layout_2',
    layout = [(0, 0, 'steel_mill_tile_1', 'steel_mill_spritelayout_small_tanks'),
              (0, 1, 'steel_mill_tile_1', 'steel_mill_spritelayout_empty'),
              (0, 2, 'steel_mill_tile_1', 'steel_mill_spritelayout_large_shed_rear_part'),
              (0, 3, 'steel_mill_tile_1', 'steel_mill_spritelayout_empty'),
              (0, 4, 'steel_mill_tile_1', 'steel_mill_spritelayout_ladle_transporter'),
              (1, 0, 'steel_mill_tile_1', 'steel_mill_spritelayout_brick_building'),
              (1, 1, 'steel_mill_tile_2', 'steel_mill_spritelayout_casting_shed'),
              (1, 2, 'steel_mill_tile_2', 'steel_mill_spritelayout_large_shed_front_part'),
              (1, 3, 'steel_mill_tile_1', 'steel_mill_spritelayout_blast_furnace_1'),
              (1, 4, 'steel_mill_tile_1', 'steel_mill_spritelayout_blast_furnace_2'),
              (2, 0, 'steel_mill_tile_1', 'steel_mill_spritelayout_empty'),
              (2, 1, 'steel_mill_tile_1', 'steel_mill_spritelayout_large_shed_rear_part'),
              (2, 2, 'steel_mill_tile_1', 'steel_mill_spritelayout_blast_furnace_1'),
              (2, 3, 'steel_mill_tile_1', 'steel_mill_spritelayout_blast_furnace_2'),
              (2, 4, 'steel_mill_tile_1', 'steel_mill_spritelayout_small_shed'),
              (3, 0, 'steel_mill_tile_2', 'steel_mill_spritelayout_casting_shed'),
              (3, 1, 'steel_mill_tile_2', 'steel_mill_spritelayout_large_shed_front_part'),
              (3, 2, 'steel_mill_tile_1', 'steel_mill_spritelayout_blast_furnace_1'),
              (3, 3, 'steel_mill_tile_1', 'steel_mill_spritelayout_blast_furnace_2'),
              (3, 4, 'steel_mill_tile_1', 'steel_mill_spritelayout_greeble'),
    ]
)
