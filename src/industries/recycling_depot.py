"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryTownProducer, TileLocationChecks

industry = IndustryPrimaryTownProducer(id='recycling_depot',
                    accept_cargo_types=[],
                    prod_cargo_types=['RCYC'],
                    layouts='AUTO',
                    prob_in_game='20',
                    prob_random='20',
                    prod_multiplier='[0, 0]',
                    map_colour='191',
                    life_type='IND_LIFE_TYPE_EXTRACTIVE',
                    location_checks=dict(incompatible={'recycling_plant': 16,
                                                                         'recycling_depot': 20},
                                                           town_industry_count=['recycling_depot', 0, 0],
                                                           prevent_player_founding=True),
                    remove_cost_multiplier='0',
                    name='string(STR_IND_RECYCLING_DEPOT)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_INDUSTRY_ESTATE))',
                    fund_cost_multiplier='118',
                    intro_year=1978)

industry.economy_variations['FIRS'].enabled = True

industry.add_tile(id='recycling_depot_tile_1',
                  location_checks=TileLocationChecks(always_allow_founder=False,
                                                    require_houses_nearby=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_SLABS',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'recycling_depot_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_hut = industry.add_spriteset(
    id = 'recycling_depot_spriteset_hut',
    sprites = [(10, 10, 64, 31, -31, 0)]
)
spriteset_no_hut = industry.add_spriteset(
    id = 'recycling_depot_spriteset_no_hut',
    sprites = [(80, 10, 64, 31, -31, 0)]
)

industry.add_spritelayout(
    id = 'recycling_depot_spritelayout_hut',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_hut],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'recycling_depot_spritelayout_no_hut',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_no_hut],
    fences = ['nw','ne','se','sw']
)
industry.add_industry_layout(
    id = 'recycling_depot_industry_layout',
    layout = [(0, 0, 'recycling_depot_tile_1', 'recycling_depot_spritelayout_hut'),
              (0, 1, 'recycling_depot_tile_1', 'recycling_depot_spritelayout_no_hut'),
              (1, 0, 'recycling_depot_tile_1', 'recycling_depot_spritelayout_no_hut'),
              (1, 1, 'recycling_depot_tile_1', 'recycling_depot_spritelayout_no_hut')
    ]
)

