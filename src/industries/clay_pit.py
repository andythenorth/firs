"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryExtractive, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryExtractive(id='clay_pit',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['CLAY'],
                    layouts='AUTO',
                    prob_in_game='4',
                    prob_random='7',
                    prod_multiplier='[16, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='46',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='0',
                    # allow longer distance on clustering than usual, and more clusters, as industry is hard to locate
                    location_checks=IndustryLocationChecks(require_cluster=['clay_pit', [20, 90, 1, 4]],
                                                           incompatible={'brick_works': 16,
                                                                         'paper_mill': 16,
                                                                         'cement_plant': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_CLAY_PIT)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_PIT))',
                    fund_cost_multiplier='200',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    template="refactor_primary_waterpit.pypnml" )

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True

# 2 tiles for this industry: pit outer tile cannot be on slopes; pit inner tiles and processor tiles can be
# cases for both tiles ensure that tiles can only be built at same height as north tile
industry.add_tile(id='clay_pit_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_desert=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='clay_pit_tile_2',
		          foundations='return CB_RESULT_NO_FOUNDATIONS', # might not be needed, cargo-culted from previous code, didn't test; may be needed to stop rear foundations showing in some cases?
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_slopes=True,
                                                     disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'clay_pit_spriteset_ground',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'clay_pit_spriteset_1',
    sprites = [(10, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'clay_pit_spriteset_2',
    sprites = [(80, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'clay_pit_spriteset_4',
    sprites = [(220, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_5 = industry.add_spriteset(
    id = 'clay_pit_spriteset_5',
    sprites = [(290, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_6 = industry.add_spriteset(
    id = 'clay_pit_spriteset_6',
    sprites = [(360, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_7 = industry.add_spriteset(
    id = 'clay_pit_spriteset_7',
    sprites = [(10, 50, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_8 = industry.add_spriteset(
    id = 'clay_pit_spriteset_8',
    sprites = [(80, 50, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_10 = industry.add_spriteset(
    id = 'clay_pit_spriteset_10',
    sprites = [(220, 50, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_11 = industry.add_spriteset(
    id = 'clay_pit_spriteset_11',
    sprites = [(290, 50, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_12 = industry.add_spriteset(
    id = 'clay_pit_spriteset_12',
    sprites = [(360, 50, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_13 = industry.add_spriteset(
    id = 'clay_pit_spriteset_13',
    sprites = [(10, 90, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_14 = industry.add_spriteset(
    id = 'clay_pit_spriteset_14',
    sprites = [(80, 90, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_18 = industry.add_spriteset(
    id = 'clay_pit_spriteset_18',
    sprites = [(360, 90, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_19 = industry.add_spriteset(
    id = 'clay_pit_spriteset_19',
    sprites = [(10, 130, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_20 = industry.add_spriteset(
    id = 'clay_pit_spriteset_20',
    sprites = [(80, 130, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_22 = industry.add_spriteset(
    id = 'clay_pit_spriteset_22',
    sprites = [(220, 130, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_23 = industry.add_spriteset(
    id = 'clay_pit_spriteset_23',
    sprites = [(290, 130, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_24 = industry.add_spriteset(
    id = 'clay_pit_spriteset_24',
    sprites = [(360, 130, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_crane_1 = industry.add_spriteset(
    id = 'clay_pit_spriteset_crane_1',
    sprites = [(650, 10, 64, 71, -48, -55)],
    zextent = 32
)
spriteset_35 = industry.add_spriteset(
    id = 'clay_pit_spriteset_35',
    sprites = [(730, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_36 = industry.add_spriteset(
    id = 'clay_pit_spriteset_36',
    sprites = [(800, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_37 = industry.add_spriteset(
    id = 'clay_pit_spriteset_37',
    sprites = [(870, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_39 = industry.add_spriteset(
    id = 'clay_pit_spriteset_39',
    sprites = [(1010, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_40 = industry.add_spriteset(
    id = 'clay_pit_spriteset_40',
    sprites = [(1080, 10, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_41 = industry.add_spriteset(
    id = 'clay_pit_spriteset_41',
    sprites = [(1150, 10, 64, 34, -31, -3)],
    zextent = 32
)
spriteset_loader_and_hut = industry.add_spriteset(
    id = 'clay_pit_spriteset_loader_and_hut',
    sprites = [(800, 50, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_conveyor_1 = industry.add_spriteset(
    id = 'clay_pit_spriteset_conveyor_1',
    sprites = [(870, 50, 64, 51, -31, -20)],
    zextent = 32
)
spriteset_silo = industry.add_spriteset(
    id = 'clay_pit_spriteset_silo',
    sprites = [(1010, 50, 64, 64, -31, -35)],
    zextent = 32
)
spriteset_conveyor_2 = industry.add_spriteset(
    id = 'clay_pit_spriteset_conveyor_2',
    sprites = [(1080, 50, 64, 64, -31, -35)],
    zextent = 32
)
spriteset_crusher = industry.add_spriteset(
    id = 'clay_pit_spriteset_crusher',
    sprites = [(1150, 50, 64, 64, -31, -33)],
    zextent = 32
)

industry.add_spritelayout(
    id = 'clay_pit_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_1,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_2,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_4,
    building_sprites = [spriteset_crane_1],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_5,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_6,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_7,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_8',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_8,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_10',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_10,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_11',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_11,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_12',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_12,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_13',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_13,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_14',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_14,
    building_sprites = [],
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_16',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_14,
    building_sprites = [],
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_17',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_14,
    building_sprites = [],
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_18',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_18,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_19',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_19,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_20',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_20,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_22',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_22,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_23',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_23,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_24',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_24,
    building_sprites = [],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_35',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_35,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_36',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_36,
    building_sprites = [spriteset_loader_and_hut],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_37',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_37,
    building_sprites = [spriteset_conveyor_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_39',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_39,
    building_sprites = [spriteset_silo],
    fences = ['nw','ne','se']
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_40',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_40,
    building_sprites = [spriteset_conveyor_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'clay_pit_spritelayout_41',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_41,
    building_sprites = [spriteset_crusher],
    fences = ['nw','ne','se','sw']
)



industry.add_industry_layout(
    id = 'clay_pit_layout_1',
    layout = [(0, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_24'),
              (0, 1, 'clay_pit_tile_2', 'clay_pit_spritelayout_18'),
              (0, 2, 'clay_pit_tile_2', 'clay_pit_spritelayout_12'),
              (0, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_6'),
              (1, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_23'),
              (1, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_17'),
              (1, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_11'),
              (1, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_5'),
              (2, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_22'),
              (2, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_16'),
              (2, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_10'),
              (2, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_4'),
              (3, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_20'),
              (3, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_14'),
              (3, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_8'),
              (3, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_2'),
              (4, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_19'),
              (4, 1, 'clay_pit_tile_2', 'clay_pit_spritelayout_13'),
              (4, 2, 'clay_pit_tile_2', 'clay_pit_spritelayout_7'),
              (4, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_1'),
              (6, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_41'),
              (6, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_37'),
              (7, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_40'),
              (7, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_36'),
              (8, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_39'),
              (8, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_35'),
    ]
)

industry.add_industry_layout(
    id = 'clay_pit_layout_2',
    layout = [(0, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_24'),
              (0, 4, 'clay_pit_tile_2', 'clay_pit_spritelayout_18'),
              (0, 5, 'clay_pit_tile_2', 'clay_pit_spritelayout_12'),
              (0, 6, 'clay_pit_tile_2', 'clay_pit_spritelayout_6'),
              (1, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_37'),
              (1, 0, 'clay_pit_tile_1', 'clay_pit_spritelayout_41'),
              (1, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_23'),
              (1, 4, 'clay_pit_tile_1', 'clay_pit_spritelayout_17'),
              (1, 5, 'clay_pit_tile_1', 'clay_pit_spritelayout_11'),
              (1, 6, 'clay_pit_tile_2', 'clay_pit_spritelayout_5'),
              (2, 0, 'clay_pit_tile_1', 'clay_pit_spritelayout_40'),
              (2, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_36'),
              (2, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_22'),
              (2, 4, 'clay_pit_tile_1', 'clay_pit_spritelayout_16'),
              (2, 5, 'clay_pit_tile_1', 'clay_pit_spritelayout_10'),
              (2, 6, 'clay_pit_tile_2', 'clay_pit_spritelayout_4'),
              (3, 0, 'clay_pit_tile_1', 'clay_pit_spritelayout_39'),
              (3, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_35'),
              (3, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_20'),
              (3, 4, 'clay_pit_tile_1', 'clay_pit_spritelayout_14'),
              (3, 5, 'clay_pit_tile_1', 'clay_pit_spritelayout_8'),
              (3, 6, 'clay_pit_tile_2', 'clay_pit_spritelayout_2'),
              (4, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_19'),
              (4, 4, 'clay_pit_tile_2', 'clay_pit_spritelayout_13'),
              (4, 5, 'clay_pit_tile_2', 'clay_pit_spritelayout_7'),
              (4, 6, 'clay_pit_tile_2', 'clay_pit_spritelayout_1'),
    ]
)

industry.add_industry_layout(
    id = 'clay_pit_layout_3',
    layout = [(0, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_24'),
              (0, 1, 'clay_pit_tile_2', 'clay_pit_spritelayout_18'),
              (0, 2, 'clay_pit_tile_2', 'clay_pit_spritelayout_12'),
              (0, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_6'),
              (1, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_23'),
              (1, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_17'),
              (1, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_11'),
              (1, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_5'),
              (1, 5, 'clay_pit_tile_1', 'clay_pit_spritelayout_41'),
              (1, 6, 'clay_pit_tile_1', 'clay_pit_spritelayout_37'),
              (2, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_22'),
              (2, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_16'),
              (2, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_10'),
              (2, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_4'),
              (2, 5, 'clay_pit_tile_1', 'clay_pit_spritelayout_40'),
              (2, 6, 'clay_pit_tile_1', 'clay_pit_spritelayout_36'),
              (3, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_20'),
              (3, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_14'),
              (3, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_8'),
              (3, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_2'),
              (3, 5, 'clay_pit_tile_1', 'clay_pit_spritelayout_39'),
              (3, 6, 'clay_pit_tile_1', 'clay_pit_spritelayout_35'),
              (4, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_19'),
              (4, 1, 'clay_pit_tile_2', 'clay_pit_spritelayout_13'),
              (4, 2, 'clay_pit_tile_2', 'clay_pit_spritelayout_7'),
              (4, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_1'),
    ]
)
