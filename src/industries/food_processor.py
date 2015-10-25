"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='food_processor',
                    processed_cargos_and_output_ratios=[('BEAN', 6), ('FRUT', 6)],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['FOOD'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='195',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_PROCESSING',
                    min_cargo_distr='5',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(incompatible={'food_processor': 56}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='TTD_STR_INDUSTRY_NAME_FOOD_PROCESSING_PLANT',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_IND_FOOD_PROCESSOR))',
                    fund_cost_multiplier='65',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    extra_text_industry='STR_EXTRA_FOOD_PROCESSING_PLANT' )

industry.economy_variations['BASIC_TROPIC'].enabled = True

industry.add_tile(id='food_processor_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'food_processor_spriteset_ground',
    type = 'concrete'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'food_processor_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'food_processor_spriteset_1',
    sprites = [(10, 10, 64, 87, -31, -56)],
    zextent = 64
)
spriteset_2 = industry.add_spriteset(
    id = 'food_processor_spriteset_2',
    sprites = [(80, 10, 64, 87, -31, -56)],
    zextent = 64
)
spriteset_3 = industry.add_spriteset(
    id = 'food_processor_spriteset_3',
    sprites = [(150, 10, 64, 87, -31, -56)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'food_processor_spriteset_4',
    sprites = [(220, 10, 64, 87, -31, -56)],
    zextent = 32
)

industry.add_spritelayout(
    id = 'food_processor_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'food_processor_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'food_processor_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'food_processor_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'food_processor_industry_layout_1',
    layout = [(0, 0, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (0, 1, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (0, 2, 'food_processor_tile_1', 'food_processor_spritelayout_3'),
              (1, 0, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (1, 1, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (1, 2, 'food_processor_tile_1', 'food_processor_spritelayout_3'),
              (2, 0, 'food_processor_tile_1', 'food_processor_spritelayout_2'),
              (2, 1, 'food_processor_tile_1', 'food_processor_spritelayout_2'),
              (2, 2, 'food_processor_tile_1', 'food_processor_spritelayout_4'),
              (3, 0, 'food_processor_tile_1', 'food_processor_spritelayout_4'),
              (3, 1, 'food_processor_tile_1', 'food_processor_spritelayout_4'),
              (3, 2, 'food_processor_tile_1', 'food_processor_spritelayout_4'),
    ]
)
industry.add_industry_layout(
    id = 'food_processor_industry_layout_2',
    layout = [(0, 0, 'food_processor_tile_1', 'food_processor_spritelayout_2'),
              (0, 1, 'food_processor_tile_1', 'food_processor_spritelayout_3'),
              (0, 2, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (0, 3, 'food_processor_tile_1', 'food_processor_spritelayout_3'),
              (1, 0, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (1, 1, 'food_processor_tile_1', 'food_processor_spritelayout_4'),
              (1, 2, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (1, 3, 'food_processor_tile_1', 'food_processor_spritelayout_3'),
              (2, 0, 'food_processor_tile_1', 'food_processor_spritelayout_2'),
              (2, 1, 'food_processor_tile_1', 'food_processor_spritelayout_4'),
              (2, 2, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (3, 0, 'food_processor_tile_1', 'food_processor_spritelayout_2'),
              (3, 1, 'food_processor_tile_1', 'food_processor_spritelayout_4'),
              (3, 2, 'food_processor_tile_1', 'food_processor_spritelayout_1')
    ]
)
industry.add_industry_layout(
    id = 'food_processor_industry_layout_3',
    layout = [(0, 0, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (0, 1, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (0, 2, 'food_processor_tile_1', 'food_processor_spritelayout_2'),
              (0, 3, 'food_processor_tile_1', 'food_processor_spritelayout_3'),
              (1, 0, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (1, 1, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (1, 2, 'food_processor_tile_1', 'food_processor_spritelayout_2'),
              (1, 3, 'food_processor_tile_1', 'food_processor_spritelayout_3'),
              (2, 0, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (2, 1, 'food_processor_tile_1', 'food_processor_spritelayout_1'),
              (2, 2, 'food_processor_tile_1', 'food_processor_spritelayout_4'),
              (2, 3, 'food_processor_tile_1', 'food_processor_spritelayout_4'),
    ]
)

