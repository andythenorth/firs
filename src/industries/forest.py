"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryOrganic, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryOrganic(id='forest',
                    prob_in_game='3',
                    prob_random='10',
                    map_colour='81',
                    prospect_chance='0.75',
                    layouts='AUTO',
                    prod_cargo_types=['WOOD'],
                    location_checks=IndustryLocationChecks(require_cluster=['forest', [20, 72, 1, 3]],
                                                           incompatible={'sawmill': 16,
                                                                         'paper_mill': 16}),
                    name='TTD_STR_INDUSTRY_NAME_FOREST',
                    extra_text_fund='string(STR_FUND_FOREST)',
                    fund_cost_multiplier='95',
                    prod_multiplier='[19]',
                    substitute='INDUSTRYTYPE_FOREST',
                    graphics_change_dates = [1935])

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].prod_cargo_types = ['WOOD', 'PULP']
industry.economy_variations['BASIC_ARCTIC'].prod_multiplier = '[18, 18]'
industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.add_tile(id='forest_tile_1',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='forest_tile_2',
                  location_checks=TileLocationChecks(disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'forest_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'forest_equipment_1',
    sprites = [(10, 10, 64, 59, -31, -28)],
)
spriteset_2 = industry.add_spriteset(
    id = 'forest_equipment_2',
    sprites = [(80, 10, 64, 59, -31, -28)],
)
"""
    xoffsets and yoffsets might be needed from these
    spriteset(spriteset_crane, "src/graphics/industries/forest_1.png") { tmpl_building_sprite(10, 10, 78, -45) }
    spriteset(spriteset_bulldozer, "src/graphics/industries/forest_1.png") { tmpl_building_sprite(80, 10, 78, -45) }
    spriteset(spriteset_tracks_snowtile, "src/graphics/industries/forest_1_snow.png") { tmpl_building_sprite(220, 10, 78, -45) }
"""

industry.add_spritelayout(
    id = 'forest_equipment_spritelayout',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1, spriteset_2],
)
industry.add_magic_spritelayout(
    type = 'slope_aware_trees',
    base_id = 'forest_slope_aware_ground_with_trees',
    config = {'ground_sprite': 'GROUNDSPRITE_NORMAL',
              'trees_default': [1593, 1593, 1689, 1586],
              'trees_tropic': [1923, 1915, 1923, 1586],
              'trees_snow': [1811, 1809, 1811, 1809]}
)

industry.add_industry_layout(
    id = 'forest_layout_1',
    layout = [(0, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (0, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (0, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (1, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (1, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (1, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (2, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (2, 2, 'forest_tile_2', 'forest_equipment_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'forest_layout_2',
    layout = [(0, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (0, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (0, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (1, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (1, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (1, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (3, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (3, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (3, 2, 'forest_tile_2', 'forest_equipment_spritelayout'),
              (4, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (4, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (4, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
    ]
)
industry.add_industry_layout(
    id = 'forest_layout_3',
    layout = [(0, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (0, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (0, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (1, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (1, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (1, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (1, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (1, 4, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (2, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (2, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (2, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (2, 3, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (3, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (3, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (3, 2, 'forest_tile_2', 'forest_equipment_spritelayout'),
              (4, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (4, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (5, 0, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (5, 1, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
              (5, 2, 'forest_tile_1', 'forest_slope_aware_ground_with_trees'),
    ]
)
