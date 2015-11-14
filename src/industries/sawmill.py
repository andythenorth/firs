"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='sawmill',
                    processed_cargos_and_output_ratios=[('WOOD', 6)],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['WDPR'],
                    prob_in_game='3',
                    prob_random='5',
                    layouts='AUTO',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='194',
                    min_cargo_distr='5',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(require_cluster=['forest', [16, 60, 5, 4]]),
                    remove_cost_multiplier='0',
                    name='TTD_STR_INDUSTRY_NAME_SAWMILL',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    fund_cost_multiplier='97',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    extra_text_industry='STR_EXTRA_SAWMILL')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.add_tile(id='sawmill_tile_1',
                  location_checks=TileLocationChecks(disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS' # ground tile same as overlay tile
)

spriteset_ground_overlay = industry.add_spriteset(
    id = 'sawmill_spriteset_ground_overlay',
    type = 'empty'
)
sprite_hut_1 = industry.add_sprite(
    sprite_number = '2069'
)
sprite_hut_2 = industry.add_sprite(
    sprite_number = '2063'
)
sprite_logs_1 = industry.add_sprite(
    sprite_number = '2066'
)
sprite_logs_2 = industry.add_sprite(
    sprite_number = '2070'
)
sprite_logs_3 = industry.add_sprite(
    sprite_number = '2071'
)

industry.add_spritelayout(
    id = 'sawmill_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [sprite_hut_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'sawmill_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [sprite_hut_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'sawmill_spritelayout_3',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [sprite_logs_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'sawmill_spritelayout_4',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [sprite_logs_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'sawmill_spritelayout_5',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [sprite_logs_3],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'sawmill_industry_layout_1',
    layout = [(0, 0, 'sawmill_tile_1', 'sawmill_spritelayout_1'),
              (0, 1, 'sawmill_tile_1', 'sawmill_spritelayout_2'),
              (0, 2, 'sawmill_tile_1', 'sawmill_spritelayout_4'),
              (1, 0, 'sawmill_tile_1', 'sawmill_spritelayout_1'),
              (1, 1, 'sawmill_tile_1', 'sawmill_spritelayout_2'),
              (1, 2, 'sawmill_tile_1', 'sawmill_spritelayout_3'),
              (2, 0, 'sawmill_tile_1', 'sawmill_spritelayout_4'),
              (2, 1, 'sawmill_tile_1', 'sawmill_spritelayout_5'),
    ]
)
