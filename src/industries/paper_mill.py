"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='paper_mill',
                    processed_cargos_and_output_ratios=[('CLAY', 2), ('WOOD', 4), ('RFPR', 2)],
                    combined_cargos_boost_prod=True,
                    prod_cargo_types=['GOOD', 'MNSP'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='14',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='184',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(incompatible={'paper_mill': 56,
                                                                         'forest': 16,
                                                                         'clay_pit': 16}),
                    remove_cost_multiplier='0',
                    fund_cost_multiplier='120',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_MILL))',
                    name='TTD_STR_INDUSTRY_NAME_PAPER_MILL',
                    override='14')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].prod_cargo_types = ['PAPR']
industry.economy_variations['BASIC_ARCTIC'].processed_cargos_and_output_ratios = [('CLAY', 2), ('PULP', 4), ('SULP', 2)]

# industry uses layouts and sprites from default game, no custom layouts etc

industry.add_tile(id='paper_mill_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'paper_mill_spriteset_ground',
    type = 'concrete'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'paper_mill_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'paper_mill_spriteset_1',
    sprites = [(10, 10, 64, 62, -31, -31)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'paper_mill_spriteset_2',
    sprites = [(80, 10, 64, 62, -31, -31)],
    zextent = 32
)
spriteset_3 = industry.add_spriteset(
    id = 'paper_mill_spriteset_3',
    sprites = [(150, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'paper_mill_spriteset_4',
    sprites = [(220, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_5 = industry.add_spriteset(
    id = 'paper_mill_spriteset_5',
    sprites = [(290, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_6 = industry.add_spriteset(
    id = 'paper_mill_spriteset_6',
    sprites = [(360, 10, 64, 87, -31, -56)],
    zextent = 52
)
spriteset_7 = industry.add_spriteset(
    id = 'paper_mill_spriteset_7',
    sprites = [(430, 10, 64, 87, -31, -56)],
    zextent = 52
)
spriteset_8 = industry.add_spriteset(
    id = 'paper_mill_spriteset_8',
    sprites = [(500, 10, 64, 87, -31, -56)],
    zextent = 52
)
spriteset_9 = industry.add_spriteset(
    id = 'paper_mill_spriteset_9',
    sprites = [(570, 10, 64, 55, -31, -24)],
    zextent = 32
)

industry.add_spritelayout(
    id = 'paper_mill_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'paper_mill_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'paper_mill_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'paper_mill_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'paper_mill_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'paper_mill_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'paper_mill_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'paper_mill_spritelayout_8',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'paper_mill_spritelayout_9',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_9],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'paper_mill_spritelayout_10',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'paper_mill_industry_layout_1',
    layout = [(0, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_2'),
              (0, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_1'),
              (0, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_10'),
              (1, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_2'),
              (1, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_1'),
              (1, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_10'),
              (2, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_10'),
              (2, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_7'),
              (2, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_9'),
              (3, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_8'),
              (3, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_6'),
              (3, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_10'),
              (4, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_5'),
              (4, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_4'),
              (4, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_3')
    ]
)
