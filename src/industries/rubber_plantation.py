"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryOrganic, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryOrganic(id='rubber_plantation',
                    map_colour='39',
                    prob_in_game='4',
                    prob_random='11',
                    prospect_chance='0.75',
                    name='TTD_STR_INDUSTRY_NAME_RUBBER_PLANTATION',
                    extra_text_fund='string(STR_FUND_RUBBER_PLANTATION)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_PLANTATION))',
                    layouts='AUTO',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(require_cluster=['rubber_plantation', [20, 72, 1, 4]]),
                    prod_cargo_types=['RUBR'],
                    fund_cost_multiplier='54',
                    prod_multiplier='[16]')

industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.add_tile(id='rubber_plantation_tile_1',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='rubber_plantation_tile_2', # house
             	  autoslope='return CB_RESULT_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))


sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'rubber_plantation_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'rubber_plantation_house',
    sprites = [(10, 10, 64, 59, -31, -28)],
)
spriteset_2 = industry.add_spriteset(
    id = 'rubber_plantation_shed',
    sprites = [(80, 10, 64, 59, -31, -28)],
)

industry.add_spritelayout(
    id = 'rubber_plantation_house_spritelayout',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
)
industry.add_spritelayout(
    id = 'rubber_plantation_shed_spritelayout',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
)
industry.add_magic_spritelayout(
    type = 'slope_aware_trees',
    base_id = 'rubber_plantation_slope_aware_ground_with_trees',
    config = {'ground_sprite': 4145,
              'trees_default': [1909, 1907, 1908, 1909]}
)

industry.add_industry_layout(
    id = 'rubber_plantation_layout_1',
    layout = [(0, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (0, 2, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 2, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
              (2, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (2, 2, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'rubber_plantation_layout_2',
    layout = [(0, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (0, 2, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
              (0, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 2, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 4, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'rubber_plantation_layout_3',
    layout = [(0, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (2, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (2, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (3, 0, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
              (3, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (4, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (4, 1, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'rubber_plantation_layout_4',
    layout = [(0, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (0, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (0, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (3, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (3, 1, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
              (3, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (3, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (4, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (4, 1, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
              (4, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (4, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
    ]
)
industry.add_industry_layout(
    id = 'rubber_plantation_layout_5',
    layout = [(0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (0, 2, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (0, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (0, 5, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 2, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
              (1, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 5, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (1, 6, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (2, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (2, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (2, 2, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
              (2, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (2, 5, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (2, 6, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (3, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (3, 2, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (3, 5, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
              (3, 6, 'rubber_plantation_tile_1', 'rubber_plantation_slope_aware_ground_with_trees'),
    ]
)