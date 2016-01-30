"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='supply_yard',
                    processed_cargos_and_output_ratios=[('VEHI', 8), ('PETR', 8), ('GOOD', 8)],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['FMSP', 'ENSP'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='133',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(incompatible={'supply_yard': 56}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_SUPPLY_YARD)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_HEAVY_INDUSTRY))',
                    fund_cost_multiplier='145',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    intro_year=1800,
                    extra_text_industry='STR_EXTRA_SUPPLY_YARD, string(STR_EXTRA_SUPPLY_YARD_VEHICLES_SUBSTR)')

industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].processed_cargos_and_output_ratios = [('BDMT', 8), ('PETR', 8), ('GOOD', 8)]
industry.economy_variations['MISTAH_KURTZ'].extra_text_industry = 'STR_EXTRA_SUPPLY_YARD, string(STR_EXTRA_SUPPLY_YARD_BUILDING_MATERIALS_SUBSTR)'

industry.add_tile(id='supply_yard_tile_1',
                  animation_length=71,
                  animation_looping=True,
                  animation_speed=2,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'supply_yard_spriteset_ground',
    type = 'concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'supply_yard_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'supply_yard_spriteset_1',
    sprites = [(10, 10, 64, 64, -31, -32)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'supply_yard_spriteset_2',
    sprites = [(80, 10, 64, 64, -31, -32)],
    zextent = 32
)
spriteset_3 = industry.add_spriteset(
    id = 'supply_yard_spriteset_3',
    sprites = [(150, 10, 64, 64, -31, -32)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'supply_yard_spriteset_4',
    sprites = [(220, 10, 64, 64, -31, -32)],
    zextent = 32
)
spriteset_5 = industry.add_spriteset(
    id = 'supply_yard_spriteset_5',
    sprites = [(290, 10, 64, 64, -31, -32)],
    zextent = 32
)
spriteset_6 = industry.add_spriteset(
    id = 'supply_yard_spriteset_6',
    sprites = [(360, 10, 64, 64, -31, -32)],
    zextent = 32
)
industry.add_spritelayout(
    id = 'supply_yard_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'supply_yard_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'supply_yard_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'supply_yard_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'supply_yard_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'supply_yard_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    fences = ['nw','ne','se','sw']
)


industry.add_industry_layout(
    id = 'supply_yard_industry_layout_1',
    layout = [(0, 0, 'supply_yard_tile_1', 'supply_yard_spritelayout_1'),
              (0, 1, 'supply_yard_tile_1', 'supply_yard_spritelayout_2'),
              (0, 2, 'supply_yard_tile_1', 'supply_yard_spritelayout_3'),
              (0, 3, 'supply_yard_tile_1', 'supply_yard_spritelayout_1'),
              (1, 0, 'supply_yard_tile_1', 'supply_yard_spritelayout_4'),
              (1, 1, 'supply_yard_tile_1', 'supply_yard_spritelayout_5'),
              (1, 2, 'supply_yard_tile_1', 'supply_yard_spritelayout_6'),
              (1, 3, 'supply_yard_tile_1', 'supply_yard_spritelayout_2'),
    ]
)

industry.add_industry_layout(
    id = 'supply_yard_industry_layout_2',
    layout = [(0, 0, 'supply_yard_tile_1', 'supply_yard_spritelayout_1'),
              (0, 1, 'supply_yard_tile_1', 'supply_yard_spritelayout_1'),
              (1, 0, 'supply_yard_tile_1', 'supply_yard_spritelayout_2'),
              (1, 1, 'supply_yard_tile_1', 'supply_yard_spritelayout_2'),
              (1, 2, 'supply_yard_tile_1', 'supply_yard_spritelayout_6'),
              (2, 0, 'supply_yard_tile_1', 'supply_yard_spritelayout_5'),
              (2, 1, 'supply_yard_tile_1', 'supply_yard_spritelayout_4'),
              (2, 2, 'supply_yard_tile_1', 'supply_yard_spritelayout_3'),
    ]
)

industry.add_industry_layout(
    id = 'supply_yard_industry_layout_3',
    layout = [(0, 0, 'supply_yard_tile_1', 'supply_yard_spritelayout_2'),
              (0, 1, 'supply_yard_tile_1', 'supply_yard_spritelayout_6'),
              (1, 0, 'supply_yard_tile_1', 'supply_yard_spritelayout_1'),
              (1, 1, 'supply_yard_tile_1', 'supply_yard_spritelayout_1'),
              (2, 0, 'supply_yard_tile_1', 'supply_yard_spritelayout_2'),
              (2, 1, 'supply_yard_tile_1', 'supply_yard_spritelayout_3'),
              (3, 0, 'supply_yard_tile_1', 'supply_yard_spritelayout_5'),
              (3, 1, 'supply_yard_tile_1', 'supply_yard_spritelayout_4'),
    ]
)
