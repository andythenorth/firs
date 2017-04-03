"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(id='orchard_piggery',
                    map_colour='86',
                    prob_in_game='4',
                    prob_random='11',
                    prospect_chance='0.75',
                    name='string(STR_IND_ORCHARD_PIGGERY)',
                    extra_text_fund='string(STR_FUND_ORCHARD_PIGGERY)',
                    layouts='AUTO',
                    location_checks=dict(require_cluster=['orchard_piggery', [20, 72, 1, 4]]),
                    prod_cargo_types=['FRUT','LVST'],
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_ANIMALS))',
                    fund_cost_multiplier='54',
                    prod_multiplier='[9, 8]',
                    override_default_construction_states=True)

industry.economy_variations['BASIC_TEMPERATE'].enabled = True

industry.add_tile(id='orchard_piggery_tile_1',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_desert=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='orchard_piggery_tile_2',
             	  autoslope='return CB_RESULT_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_desert=True,
                                                     disallow_industry_adjacent=True))


sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'orchard_piggery_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'orchard_piggery_house',
    sprites = [(10, 10, 64, 59, -31, -28)],
)

industry.add_spritelayout(
    id = 'orchard_piggery_house_spritelayout',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
)
industry.add_magic_spritelayout(
    type = 'slope_aware_trees',
    base_id = 'orchard_piggery_slope_aware_ground_with_trees_1',
    config = {'ground_sprite': 4164,
              'trees_default': [1620, 1619, 1689, 1620]}
)
industry.add_magic_spritelayout(
    type = 'slope_aware_trees',
    base_id = 'orchard_piggery_slope_aware_ground_with_trees_2',
    config = {'ground_sprite': 4164,
              'trees_default': [1647, 1668, 1621, 1619]}
)

industry.add_industry_layout(
    id = 'orchard_piggery_layout_1',
    layout = [(0, 0, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (0, 1, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_2'),
              (0, 2, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (1, 0, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_2'),
              (1, 1, 'orchard_piggery_tile_2', 'orchard_piggery_house_spritelayout'),
              (1, 2, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (2, 1, 'orchard_piggery_tile_2', 'orchard_piggery_house_spritelayout'),
              (2, 2, 'orchard_piggery_tile_2', 'orchard_piggery_house_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'orchard_piggery_layout_2',
    layout = [(0, 0, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (0, 1, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (0, 2, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_2'),
              (0, 3, 'orchard_piggery_tile_2', 'orchard_piggery_house_spritelayout'),
              (1, 1, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_2'),
              (1, 2, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (1, 3, 'orchard_piggery_tile_2', 'orchard_piggery_house_spritelayout'),
              (1, 4, 'orchard_piggery_tile_2', 'orchard_piggery_house_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'orchard_piggery_layout_3',
    layout = [(0, 0, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_2'),
              (0, 1, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (1, 0, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (1, 1, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_2'),
              (2, 0, 'orchard_piggery_tile_2', 'orchard_piggery_house_spritelayout'),
              (2, 1, 'orchard_piggery_tile_2', 'orchard_piggery_house_spritelayout'),
              (3, 0, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (3, 1, 'orchard_piggery_tile_2', 'orchard_piggery_house_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'orchard_piggery_layout_4',
    layout = [(0, 0, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (0, 1, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (0, 3, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_2'),
              (0, 4, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (1, 0, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (1, 1, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (1, 3, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_2'),
              (1, 4, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (3, 0, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_2'),
              (3, 1, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (3, 3, 'orchard_piggery_tile_2', 'orchard_piggery_house_spritelayout'),
              (3, 4, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (4, 0, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_2'),
              (4, 1, 'orchard_piggery_tile_2', 'orchard_piggery_house_spritelayout'),
              (4, 3, 'orchard_piggery_tile_1', 'orchard_piggery_slope_aware_ground_with_trees_1'),
              (4, 4, 'orchard_piggery_tile_2', 'orchard_piggery_house_spritelayout'),
    ]
)
