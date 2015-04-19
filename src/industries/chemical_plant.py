"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='chemical_plant',
                    processed_cargos_and_output_ratios=[('OIL_', 6), ('NITR', 6)],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['RFPR'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='19',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_PROCESSING',
                    min_cargo_distr='5',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(incompatible={'chemical_plant': 56,
                                                                         'nitrate_mine': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_CHEMICAL_PLANT)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_INDUSTRY_ESTATE))',
                    fund_cost_multiplier='170',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    extra_text_industry='STR_EXTRA_CHEMICAL_PLANT',
                    snakebite=True)

industry.economy_variations['BASIC_TROPIC'].enabled = True

industry.add_tile(id='chemical_plant_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  location_checks=TileLocationChecks(disallow_slopes=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'chemical_plant_spriteset_ground',
    type='concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'chemical_plant_spriteset_ground_overlay',
    type='empty',
)

spriteset_1 = industry.add_spriteset(
    id = 'chemical_plant_spriteset_1',
    sprites = [(80, 10, 64, 114, -31, -88)],
    zextent = 48
)
spriteset_2 = industry.add_spriteset(
    id = 'chemical_plant_spriteset_2',
    sprites = [(150, 10, 64, 114, -31, -83)],
    zextent = 48
)
spriteset_3 = industry.add_spriteset(
    id = 'chemical_plant_spriteset_3',
    sprites = [(220, 10, 64, 114, -31, -83)],
    zextent = 48
)
spriteset_4 = industry.add_spriteset(
    id = 'chemical_plant_spriteset_4',
    sprites = [(290, 10, 64, 114, -31, -83)],
    zextent = 48
)
spriteset_5 = industry.add_spriteset(
    id = 'chemical_plant_spriteset_5',
    sprites = [(360, 10, 64, 66, -31, -35)],
    zextent = 48
)
spriteset_6 = industry.add_spriteset(
    id = 'chemical_plant_spriteset_6',
    sprites = [(430, 10, 64, 66, -31, -35)],
    zextent = 48
)
spriteset_7 = industry.add_spriteset(
    id = 'chemical_plant_spriteset_7',
    sprites = [(500, 10, 64, 66, -31, -35)],
    zextent = 48
)
spriteset_8 = industry.add_spriteset(
    id = 'chemical_plant_spriteset_8',
    sprites = [(570, 10, 64, 66, -31, -35)],
    zextent = 48
)
spriteset_9 = industry.add_spriteset(
    id = 'chemical_plant_spriteset_9',
    sprites = [(640, 10, 64, 66, -31, -35)],
    zextent = 48
)
spriteset_10 = industry.add_spriteset(
    id = 'chemical_plant_spriteset_10',
    sprites = [(710, 10, 64, 66, -31, -35)],
    zextent = 48
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 5,
    yoffset= 0,
    zoffset= 69,
    animation_frame_offset = 1
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 9,
    yoffset= 0,
    zoffset= 69,
)

industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    smoke_sprites = [sprite_smoke_1, sprite_smoke_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    fences = ['nw','ne']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_8',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_9',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_9],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_10',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_10],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_concrete',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'chemical_plant_industry_layout_1',
    layout = [(0, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_1'),
              (0, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_4'),
              (0, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_8'),
              (1, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_6'),
              (1, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_3'),
              (1, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_9'),
              (2, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_5'),
              (2, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_2'),
              (2, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
              (3, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_10'),
              (3, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_concrete'),
              (3, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
    ]
)
industry.add_industry_layout(
    id = 'chemical_plant_industry_layout_2',
    layout = [(0, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_1'),
              (0, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_6'),
              (1, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_4'),
              (1, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_5'),
              (2, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_3'),
              (2, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_10'),
              (3, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_2'),
              (3, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
              (4, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_8'),
              (4, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_9'),
    ]
)
industry.add_industry_layout(
    id = 'chemical_plant_industry_layout_3',
    layout = [(0, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_4'),
              (1, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_8'),
              (1, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_3'),
              (1, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
              (1, 3, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_6'),
              (2, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_9'),
              (2, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_2'),
              (2, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_1'),
              (2, 3, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_5'),
    ]
)
industry.add_industry_layout(
    id = 'chemical_plant_industry_layout_4',
    layout = [(0, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_4'),
              (1, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_1'),
              (1, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_3'),
              (1, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_6'),
              (1, 3, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_8'),
              (2, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
              (2, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_2'),
              (2, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_5'),
              (2, 3, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_9'),
    ]
)
industry.add_industry_layout(
    id = 'chemical_plant_industry_layout_5',
    layout = [(0, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_4'),
              (0, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
              (1, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_3'),
              (1, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
              (2, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_2'),
              (2, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_6'),
              (3, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_1'),
              (3, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_5'),
              (4, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_8'),
              (4, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_6'),
              (5, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_8'),
              (5, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_5'),
              (6, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_9'),
              (6, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_10'),
    ]
)
industry.add_industry_layout(
    id = 'chemical_plant_industry_layout_6',
    layout = [(0, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_4'),
              (0, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_8'),
              (0, 3, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_8'),
              (1, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_3'),
              (1, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_6'),
              (1, 3, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_6'),
              (2, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_2'),
              (2, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_5'),
              (2, 3, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_5'),
              (3, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_1'),
              (3, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_10'),
              (3, 3, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_concrete'),
              (4, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
              (4, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
              (4, 3, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_9'),
    ]
)
industry.add_industry_layout(
    id = 'chemical_plant_industry_layout_7',
    layout = [(0, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_4'),
              (0, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
              (0, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_1'),
              (0, 5, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_8'),
              (0, 6, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_10'),
              (1, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_3'),
              (1, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
              (1, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_6'),
              (1, 5, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_8'),
              (1, 6, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_6'),
              (2, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_2'),
              (2, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_concrete'),
              (2, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_5'),
              (2, 5, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_9'),
              (2, 6, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_5'),
              (4, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
              (4, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
              (4, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_9'),
              (4, 5, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_8'),
              (4, 6, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_10'),
              (5, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_7'),
              (5, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_10'),
              (5, 5, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_8'),
              (5, 6, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_9'),
    ]
)
