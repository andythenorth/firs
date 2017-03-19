"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryOrganic, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryOrganic(id='fruit_plantation',
                    map_colour='86',
                    prob_in_game='4',
                    prob_random='10',
                    prospect_chance='0.75',
                    name='TTD_STR_INDUSTRY_NAME_FRUIT_PLANTATION',
                    extra_text_fund='string(STR_FUND_FRUIT_PLANTATION)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_PLANTATION))',
                    layouts='AUTO',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(require_cluster=['fruit_plantation', [20, 72, 1, 4]],
                                                           incompatible={'brewery': 16}),
                    prod_cargo_types=['FRUT'],
                    fund_cost_multiplier='54',
                    prod_multiplier='[16]')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.add_tile(id='fruit_plantation_tile_1',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='fruit_plantation_tile_2', # house
             	  autoslope='return CB_RESULT_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'fruit_plantation_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'fruit_plantation_house',
    sprites = [(10, 10, 64, 59, -31, -28)],
)
spriteset_2 = industry.add_spriteset(
    id = 'fruit_plantation_shed',
    sprites = [(80, 10, 64, 59, -31, -28)],
)

industry.add_spritelayout(
    id = 'fruit_plantation_house_spritelayout',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
)
industry.add_spritelayout(
    id = 'fruit_plantation_shed_spritelayout',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
)
industry.add_magic_spritelayout(
    type = 'slope_aware_trees',
    base_id = 'fruit_plantation_slope_aware_ground_with_trees',
    config = {'ground_sprite': 4164,
              'trees': [1620, 1633, 1689, 1620],
              'trees_tropic': [1832, 1830, 1831, 1832]}
)

industry.add_industry_layout(
    id = 'fruit_plantation_layout_1',
    layout = [(0, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (0, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (0, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (2, 1, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
              (2, 2, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'fruit_plantation_layout_2',
    layout = [(0, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (0, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (0, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (0, 3, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
              (1, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 4, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'fruit_plantation_layout_3',
    layout = [(0, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (0, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (2, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (2, 1, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
              (3, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (3, 1, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'fruit_plantation_layout_4',
    layout = [(0, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (0, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (0, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (0, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (3, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (3, 1, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
              (3, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (3, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (4, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (4, 1, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
              (4, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (4, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
    ]
)
industry.add_industry_layout(
    id = 'fruit_plantation_layout_5',
    layout = [(0, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (0, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (0, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (0, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (1, 5, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (3, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (3, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (3, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (3, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (3, 4, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
              (3, 5, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
              (4, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (4, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (4, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
              (4, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees'),
    ]
)