"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='oil_refinery',
                    processed_cargos_and_output_ratios=[('OIL_', 6)],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['RFPR', 'PETR'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='191',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_PROCESSING',
                    min_cargo_distr='5',
                    spec_flags='bitmask(IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE)',
                    location_checks=IndustryLocationChecks(incompatible={'oil_refinery': 56,
                                                                         'oil_rig': 16,
                                                                         'oil_wells': 16}),
                    fund_cost_multiplier='200',
                    name='TTD_STR_INDUSTRY_NAME_OIL_REFINERY',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_REFINERY))',
                    extra_text_industry='STR_EXTRA_OIL_REFINERY',
                    intro_year=1830)

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True

industry.add_tile(id='oil_refinery_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'oil_refinery_spriteset_ground',
    type = 'concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'oil_refinery_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'oil_refinery_spriteset_1',
    sprites = [(10, 10, 64, 66, -31, -35)],
    zextent = 48
)
spriteset_2 = industry.add_spriteset(
    id = 'oil_refinery_spriteset_2',
    sprites = [(80, 10, 64, 128, -31, -96)],
    zextent = 48
)
spriteset_3 = industry.add_spriteset(
    id = 'oil_refinery_spriteset_3',
    sprites = [(150, 10, 64, 128, -31, -96)],
    zextent = 48
)
spriteset_4 = industry.add_spriteset(
    id = 'oil_refinery_spriteset_4',
    sprites = [(220, 10, 64, 128, -31, -96)],
    zextent = 48
)
spriteset_5 = industry.add_spriteset(
    id = 'oil_refinery_spriteset_5',
    sprites = [(290, 10, 64, 66, -31, -35)],
    zextent = 48
)

industry.add_spritelayout(
    id = 'oil_refinery_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'oil_refinery_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'oil_refinery_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'oil_refinery_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'oil_refinery_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'oil_refinery_industry_layout_1',
    layout = [(0, 0, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_1'),
              (0, 1, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_1'),
              (0, 2, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_3'),
              (0, 3, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_3'),
              (0, 4, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_2'),
              (1, 0, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_1'),
              (1, 1, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_1'),
              (1, 2, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_4'),
              (1, 3, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_2'),
              (1, 4, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_5'),
              (2, 0, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_1'),
              (2, 1, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_1'),
              (2, 2, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_4'),
              (2, 3, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_3'),
              (2, 4, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_5'),
    ]
)
industry.add_industry_layout(
    id = 'oil_refinery_industry_layout_2',
    layout = [(0, 0, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_2'),
              (0, 1, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_3'),
              (0, 2, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_3'),
              (0, 3, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_4'),
              (1, 0, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_2'),
              (1, 1, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_4'),
              (1, 2, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_3'),
              (1, 3, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_2'),
              (2, 0, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_5'),
              (2, 1, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_1'),
              (2, 2, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_1'),
              (2, 3, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_1'),
              (3, 1, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_5'),
              (3, 2, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_1'),
              (3, 3, 'oil_refinery_tile_1', 'oil_refinery_spritelayout_1'),
    ]
)
