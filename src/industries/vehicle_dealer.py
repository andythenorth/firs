"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryTertiary, TileLocationChecks, IndustryLocationChecks

industry = IndustryTertiary(id='vehicle_dealer',
                    accept_cargo_types=['PETR', 'VEHI'],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    layouts='AUTO',
                    prod_cargo_types=[],
                    prob_in_game='14',
                    prob_random='14',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='68',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_BLACK_HOLE',
                    min_cargo_distr='2',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(incompatible={'vehicle_dealer': 20}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_VEHICLE_DEALER)',
                    fund_cost_multiplier='8',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    intro_year=1900 )

industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='vehicle_dealer_tile_1',
                  location_checks=TileLocationChecks(require_road_adjacent=True,
                                                     require_effectively_flat=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_SLABS',
    sprite_number_snow = 'GROUNDTILE_SLABS',
)
sprite_ground_overlay = industry.add_sprite(
    sprite_number = 'GROUNDTILE_SLABS',
    sprite_number_snow = 'GROUNDTILE_SLABS',
)
spriteset_1 = industry.add_spriteset(
    id = 'vehicle_dealer_spriteset_1',
    sprites = [(10, 60, 64, 59, -31, -28)]
)
spriteset_2 = industry.add_spriteset(
    id = 'vehicle_dealer_spriteset_2',
    sprites = [(80, 60, 64, 59, -31, -28)]
)

industry.add_spritelayout(
    id = 'vehicle_dealer_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_1]
)
industry.add_spritelayout(
    id = 'vehicle_dealer_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_2]
)

industry.add_industry_layout(
    id = 'vehicle_dealer_industry_layout_1',
    layout = [(0, 0, 'vehicle_dealer_tile_1', 'vehicle_dealer_spritelayout_1'),
              (0, 1, 'vehicle_dealer_tile_1', 'vehicle_dealer_spritelayout_2')
    ]
)
industry.add_industry_layout(
    id = 'vehicle_dealer_industry_layout_2',
    layout = [(0, 0, 'vehicle_dealer_tile_1', 'vehicle_dealer_spritelayout_1'),
              (1, 0, 'vehicle_dealer_tile_1', 'vehicle_dealer_spritelayout_2')
    ]
)

