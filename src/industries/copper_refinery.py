"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='copper_refinery',
                    processed_cargos_and_output_ratios=[('CORE', 5), ('RFPR', 3)],
                    combined_cargos_boost_prod=True,
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['COPR'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='64',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(incompatible={'copper_refinery': 56,
                                                                         'copper_mine': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_COPPER_REFINERY)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_POWERHUNGRY))',
                    fund_cost_multiplier='200',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    extra_text_industry='STR_EXTRA_COPPER_REFINERY',
                    intro_year=1800,
                    graphics_change_dates = [] )

industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.add_tile(id='copper_refinery_tile_1',
                  animation_length=47,
                  animation_looping=True,
                  animation_speed=2,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'copper_refinery_spriteset_ground',
    type='concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'copper_refinery_spriteset_ground_overlay',
    type='empty',
)
spriteset_1 = industry.add_spriteset(
    id = 'copper_refinery_spriteset_1',
    sprites = [(10, 10, 64, 64, -31, -31)],
    zextent = 64
)
spriteset_2 = industry.add_spriteset(
    id = 'copper_refinery_spriteset_2',
    sprites = [(80, 10, 64, 64, -31, -26)],
    zextent = 90
)
spriteset_3 = industry.add_spriteset(
    id = 'copper_refinery_spriteset_3',
    sprites = [(150, 10, 64, 64, -31, -31)],
    zextent = 64
)
spriteset_4 = industry.add_spriteset(
    id = 'copper_refinery_spriteset_4',
    sprites = [(220, 10, 64, 128, -31, -95)],
    zextent = 64
)
spriteset_5 = industry.add_spriteset(
    id = 'copper_refinery_spriteset_5',
    sprites = [(290, 10, 64, 100, -31, -61)],
    zextent = 64
)
spriteset_6 = industry.add_spriteset(
    id = 'copper_refinery_spriteset_6',
    sprites = [(360, 10, 64, 100, -31, -61)],
    zextent = 64
)
spriteset_7 = industry.add_spriteset(
    id = 'copper_refinery_spriteset_7',
    sprites = [(430, 10, 64, 56, -31, -26)],
    zextent = 32
)
spriteset_8 = industry.add_spriteset(
    id = 'copper_refinery_spriteset_8',
    sprites = [(500, 10, 64, 56, -31, -26)],
    zextent = 32
)
spriteset_9 = industry.add_spriteset(
    id = 'copper_refinery_spriteset_9',
    sprites = [(570, 10, 64, 110, -31, -61)],
    zextent = 90
)
spriteset_10 = industry.add_spriteset(
    id = 'copper_refinery_spriteset_10',
    sprites = [(640, 10, 64, 110, -31, -61)],
    zextent = 90
)
spriteset_11 = industry.add_spriteset(
    id = 'copper_refinery_spriteset_11',
    sprites = [(710, 10, 64, 110, -31, -61)],
    zextent = 90
)
sprite_transformer = industry.add_sprite(
    sprite_number = 2054,
    zextent= 90
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type = 'dark_smoke_small',
    xoffset= 5,
    yoffset= 0,
    zoffset= 64,
)

industry.add_spritelayout(
    id = 'copper_refinery_spritelayout_tanks',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'copper_refinery_spritelayout_settling_pond',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'copper_refinery_spritelayout_big_shed',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'copper_refinery_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    smoke_sprites = [sprite_smoke],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'copper_refinery_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'copper_refinery_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'copper_refinery_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'copper_refinery_spritelayout_8',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'copper_refinery_spritelayout_9',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_9],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'copper_refinery_spritelayout_10',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_10],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'copper_refinery_spritelayout_11',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_11],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'copper_refinery_spritelayout_concrete',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'copper_refinery_spritelayout_transformer',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [sprite_transformer],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'copper_refinery_industry_layout_1',
    layout = [(0, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_big_shed'),
              (0, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_big_shed'),
              (0, 2, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_big_shed'),
              (0, 3, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_6'),
              (1, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_4'),
              (1, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (1, 2, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_concrete'),
              (1, 3, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_8'),
              (2, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (2, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (2, 2, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_4'),
              (2, 3, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_settling_pond'),
              (3, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (3, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (3, 2, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_4'),
              (3, 3, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_7'),
              (5, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_transformer'),
    ]
)
industry.add_industry_layout(
    id = 'copper_refinery_industry_layout_2',
    layout = [(0, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (0, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_concrete'),
              (0, 2, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (0, 3, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_concrete'),
              (0, 4, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_11'),
              (1, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (1, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_4'),
              (1, 2, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (1, 3, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_9'),
              (1, 4, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_10'),
              (2, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (2, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_big_shed'),
              (2, 2, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (2, 3, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_5'),
              (2, 4, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_6'),
              (3, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (3, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_concrete'),
              (3, 2, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (3, 3, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_8'),
              (3, 4, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_concrete'),
              (4, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (4, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_transformer'),
              (4, 2, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (4, 3, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_settling_pond'),
              (4, 4, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_7'),
    ]
)
industry.add_industry_layout(
    id = 'copper_refinery_industry_layout_3',
    layout = [(0, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_transformer'),
              (1, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_big_shed'),
              (1, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_settling_pond'),
              (2, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_4'),
              (2, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_8'),
              (3, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (3, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (4, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (4, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (5, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (5, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_tanks'),
              (6, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_7'),
              (6, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_7'),
              (7, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_9'),
              (7, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_11'),
              (8, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_9'),
              (8, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_10'),
              (9, 0, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_5'),
              (9, 1, 'copper_refinery_tile_1', 'copper_refinery_spritelayout_6'),
    ]
)
