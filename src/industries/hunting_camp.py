"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryNoSupplies, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryNoSupplies(id='hunting_camp',
                    accept_cargo_types=[],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['FOOD'],
                    layouts='AUTO',
                    prob_in_game='14',
                    prob_random='14',
                    prod_multiplier='[5, 0]',
                    substitute='5',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='158',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_EXTRACTIVE',
                    spec_flags='bitmask(IND_FLAG_NO_PRODUCTION_INCREASE)',
                    location_checks=IndustryLocationChecks(incompatible={'hunting_camp': 56}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_HUNTING_CAMP)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_HUNTING_CAMP))',
                    fund_cost_multiplier='88',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS')

industry.economy_variations['BASIC_ARCTIC'].enabled = True

industry.add_tile(id='hunting_camp_tile_1',
                  location_checks=TileLocationChecks(disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'hunting_camp_spriteset_ground',
    type = 'empty'
)
sprite_ground_mud = industry.add_sprite(
    sprite_number = 'GROUNDSPRITE_CLEARED'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'hunting_camp_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'hunting_camp_spriteset_1',
    sprites = [(10, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_1_ground = industry.add_spriteset(
    id = 'hunting_camp_spriteset_1_ground',
    sprites = [(10, 70, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'hunting_camp_spriteset_2',
    sprites = [(80, 10, 64, 52, -31, -21)],
    zextent = 32
)
spriteset_2_ground = industry.add_spriteset(
    id = 'hunting_camp_spriteset_2_ground',
    sprites = [(80, 70, 64, 52, -31, -21)],
    zextent = 32
)

industry.add_spritelayout(
    id = 'hunting_camp_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_1_ground,
    building_sprites = [spriteset_1],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'hunting_camp_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_2_ground,
    building_sprites = [spriteset_2],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'hunting_camp_spritelayout_3',
    ground_sprite = sprite_ground_mud,
    ground_overlay = sprite_ground_mud,
    building_sprites = [],
    terrain_aware_ground = True
)

industry.add_industry_layout(
    id = 'hunting_camp_industry_layout_1',
    layout = [(0, 1, 'hunting_camp_tile_1', 'hunting_camp_spritelayout_3'),
              (0, 2, 'hunting_camp_tile_1', 'hunting_camp_spritelayout_1'),
              (1, 0, 'hunting_camp_tile_1', 'hunting_camp_spritelayout_2'),
              (1, 2, 'hunting_camp_tile_1', 'hunting_camp_spritelayout_2'),
    ]
)
industry.add_industry_layout(
    id = 'hunting_camp_industry_layout_2',
    layout = [(0, 0, 'hunting_camp_tile_1', 'hunting_camp_spritelayout_2'),
              (0, 1, 'hunting_camp_tile_1', 'hunting_camp_spritelayout_2'),
              (0, 2, 'hunting_camp_tile_1', 'hunting_camp_spritelayout_1'),
              (1, 0, 'hunting_camp_tile_1', 'hunting_camp_spritelayout_3'),
    ]
)
industry.add_industry_layout(
    id = 'hunting_camp_industry_layout_3',
    layout = [(0, 0, 'hunting_camp_tile_1', 'hunting_camp_spritelayout_2'),
              (0, 1, 'hunting_camp_tile_1', 'hunting_camp_spritelayout_1'),
              (1, 0, 'hunting_camp_tile_1', 'hunting_camp_spritelayout_2'),
              (1, 2, 'hunting_camp_tile_1', 'hunting_camp_spritelayout_3'),
    ]
)
