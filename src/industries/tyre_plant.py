"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='tyre_plant',
                    processed_cargos_and_output_ratios=[('RUBR', 6), ('RFPR', 2)],
                    combined_cargos_boost_prod=True,
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['VPTS'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='2',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(incompatible={'tyre_plant': 56}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_TYRE_PLANT)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_HEAVY_INDUSTRY))',
                    fund_cost_multiplier='120',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    extra_text_industry='STR_EXTRA_TYRE_PLANT',
                    intro_year=1832 )

industry.economy_variations['BASIC_ARCTIC'].enabled = True

industry.add_tile(id='tyre_plant_tile_1',
                  animation_length=71,
                  animation_looping=True,
                  animation_speed=2,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))


spriteset_ground = industry.add_spriteset(
    id = 'tyre_plant_spriteset_ground',
    type = 'concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'tyre_plant_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'tyre_plant_spriteset_1',
    sprites = [(10, 60, 64, 90, -31, -58)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'tyre_plant_spriteset_2',
    sprites = [(80, 60, 64, 90, -31, -58)],
    zextent = 32
)
spriteset_3 = industry.add_spriteset(
    id = 'tyre_plant_spriteset_3',
    sprites = [(150, 60, 64, 90, -31, -58)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'tyre_plant_spriteset_4',
    sprites = [(220, 60, 64, 90, -31, -58)],
    zextent = 32
)
spriteset_5 = industry.add_spriteset(
    id = 'tyre_plant_spriteset_5',
    sprites = [(290, 60, 64, 64, -31, -32)],
    zextent = 32
)
spriteset_7 = industry.add_spriteset(
    id = 'tyre_plant_spriteset_7',
    sprites = [(430, 60, 64, 31, -31, 0)],
    zextent = 32
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_small',
    xoffset= -5,
    yoffset= 0,
    zoffset= 26,
)

industry.add_spritelayout(
    id = 'tyre_plant_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'tyre_plant_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'tyre_plant_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'tyre_plant_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    smoke_sprites = [sprite_smoke],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'tyre_plant_spritelayout_horizontal_tanks',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'tyre_plant_spritelayout_tyres_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'tyre_plant_industry_layout_1',
    layout = [(0, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_3'),
              (0, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_3'),
              (0, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_4'),
              (0, 3, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_1'),
              (1, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_2'),
              (1, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_2'),
              (1, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_horizontal_tanks'),
              (1, 3, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_1'),
              (2, 0, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_3'),
              (2, 1, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_1'),
              (2, 2, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_1'),
              (2, 3, 'tyre_plant_tile_1', 'tyre_plant_spritelayout_tyres_1'),
    ]
)
