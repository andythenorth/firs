"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryOrganic, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryOrganic(id='basic_farm',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_FARM',
                    prod_cargo_types=['GRAI', 'LVST'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='11',
                    prod_multiplier='[10, 9]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='164',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='1',
                    spec_flags='bitmask(IND_FLAG_PLANT_FIELDS_PERIODICALLY, IND_FLAG_PLANT_FIELDS_WHEN_BUILT)',
                    location_checks=IndustryLocationChecks(require_cluster=['basic_farm', [20, 72, 1, 4]],
                                                           incompatible={'stockyard': 16,
                                                                         'brewery': 16,
                                                                         'grain_mill': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_BASICFARM)',
                    extra_text_fund='string(STR_FUND_BASIC_FARM)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_FARM))',
                    fund_cost_multiplier='49',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS' )

industry.economy_variations['BASIC_ARCTIC'].enabled = True

industry.add_tile(id='basic_farm_tile_1',
                  location_checks=TileLocationChecks(disallow_steep_slopes=True,
                                                     disallow_above_snowline=True,
                                                     disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'basic_farm_spriteset_ground',
    type = 'empty'
)
sprite_ground_mud = industry.add_sprite(
    sprite_number = 'GROUNDSPRITE_CLEARED'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'basic_farm_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'basic_farm_spriteset_1',
    sprites = [(10, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'basic_farm_spriteset_2',
    sprites = [(80, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_3 = industry.add_spriteset(
    id = 'basic_farm_spriteset_3',
    sprites = [(150, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'basic_farm_spriteset_4',
    sprites = [(220, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_5 = industry.add_spriteset(
    id = 'basic_farm_spriteset_5',
    sprites = [(290, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_6 = industry.add_spriteset(
    id = 'basic_farm_spriteset_6',
    sprites = [(360, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_7 = industry.add_spriteset(
    id = 'basic_farm_spriteset_7',
    sprites = [(430, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_8 = industry.add_spriteset(
    id = 'basic_farm_spriteset_8',
    sprites = [(500, 10, 64, 52, -31, -21)],
    zextent = 32
)

industry.add_spritelayout(
    id = 'basic_farm_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'basic_farm_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'basic_farm_spritelayout_3',
    ground_sprite = sprite_ground_mud,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
)
industry.add_spritelayout(
    id = 'basic_farm_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'basic_farm_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'basic_farm_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'basic_farm_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'basic_farm_spritelayout_8',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
    terrain_aware_ground = True
)

industry.add_industry_layout(
    id = 'basic_farm_industry_layout_1',
    layout = [(0, 2, 'basic_farm_tile_1', 'basic_farm_spritelayout_8'),
              (0, 3, 'basic_farm_tile_1', 'basic_farm_spritelayout_3'),
              (1, 0, 'basic_farm_tile_1', 'basic_farm_spritelayout_2'),
              (2, 0, 'basic_farm_tile_1', 'basic_farm_spritelayout_1'),
              (2, 2, 'basic_farm_tile_1', 'basic_farm_spritelayout_5'),
              (2, 3, 'basic_farm_tile_1', 'basic_farm_spritelayout_7'),
              (3, 2, 'basic_farm_tile_1', 'basic_farm_spritelayout_6'),
              (3, 3, 'basic_farm_tile_1', 'basic_farm_spritelayout_4'),
    ]
)
industry.add_industry_layout(
    id = 'basic_farm_industry_layout_2',
    layout = [(0, 0, 'basic_farm_tile_1', 'basic_farm_spritelayout_4'),
              (0, 2, 'basic_farm_tile_1', 'basic_farm_spritelayout_7'),
              (0, 3, 'basic_farm_tile_1', 'basic_farm_spritelayout_6'),
              (1, 0, 'basic_farm_tile_1', 'basic_farm_spritelayout_5'),
              (1, 3, 'basic_farm_tile_1', 'basic_farm_spritelayout_1'),
              (2, 0, 'basic_farm_tile_1', 'basic_farm_spritelayout_8'),
              (2, 1, 'basic_farm_tile_1', 'basic_farm_spritelayout_3'),
              (2, 2, 'basic_farm_tile_1', 'basic_farm_spritelayout_2'),
    ]
)
industry.add_industry_layout(
    id = 'basic_farm_industry_layout_3',
    layout = [(0, 0, 'basic_farm_tile_1', 'basic_farm_spritelayout_8'),
              (0, 1, 'basic_farm_tile_1', 'basic_farm_spritelayout_1'),
              (0, 2, 'basic_farm_tile_1', 'basic_farm_spritelayout_5'),
              (1, 0, 'basic_farm_tile_1', 'basic_farm_spritelayout_2'),
              (1, 2, 'basic_farm_tile_1', 'basic_farm_spritelayout_3'),
              (2, 0, 'basic_farm_tile_1', 'basic_farm_spritelayout_7'),
              (3, 0, 'basic_farm_tile_1', 'basic_farm_spritelayout_4'),
              (3, 2, 'basic_farm_tile_1', 'basic_farm_spritelayout_6'),
    ]
)
