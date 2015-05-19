"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryPort, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryPort(id='bulk_terminal',
                    accept_cargo_types=['FOOD', 'FRUT', 'BEER'],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=[],
                    layouts='AUTO',
                    prob_in_game='2',
                    prob_random='6',
                    prod_multiplier='[9, 9]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='175',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='2',
                    spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER)',
                    location_checks=IndustryLocationChecks(incompatible={'bulk_terminal': 48}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_BULK_TERMINAL)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_INDUSTRY_HARBOUR))',
                    fund_cost_multiplier='152',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    override_default_construction_states=True)

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['FIRS'].accept_cargo_types = ['BDMT', 'PETR', 'FOOD']
industry.economy_variations['FIRS'].prod_cargo_types = ['FMSP', 'RFPR']
industry.economy_variations['FIRS'].prod_multiplier = '[7, 16]'
industry.economy_variations['FIRS'].prob_random = '3'

industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].accept_cargo_types = ['CLAY', 'FOOD']
industry.economy_variations['BASIC_TEMPERATE'].prod_cargo_types = ['FMSP', 'RFPR']
industry.economy_variations['BASIC_TEMPERATE'].prod_multiplier = '[7, 19]'

industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].accept_cargo_types = ['GRAI', 'IORE', 'PETR']
industry.economy_variations['BASIC_ARCTIC'].prod_cargo_types = ['FMSP', 'CLAY']
industry.economy_variations['BASIC_ARCTIC'].prod_multiplier = '[7, 12]'

industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['BASIC_TROPIC'].accept_cargo_types = ['AORE', 'RFPR', 'FOOD']
industry.economy_variations['BASIC_TROPIC'].prod_cargo_types = ['FMSP', 'MNSP']
industry.economy_variations['BASIC_TROPIC'].prod_multiplier = '[19, 19]'

industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].accept_cargo_types = ['OIL_', 'CORE', 'SUGR']
industry.economy_variations['MISTAH_KURTZ'].prod_cargo_types = ['BDMT', 'GRAI']

industry.add_tile(id='bulk_terminal_tile_1',
                  land_shape_flags='bitmask(LSF_ONLY_ON_FLAT_LAND)',
                  location_checks=TileLocationChecks(always_allow_founder=False))
industry.add_tile(id='bulk_terminal_tile_2',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  location_checks=TileLocationChecks(always_allow_founder=False,
                                                     require_coast=True))

#empty tile
#covered store
#tanks
#silos
#cone silo
#warehouse
#large crane (4 angles)
#boat 1
#boat 2

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDSPRITE_WATER'
)
spriteset_ground_empty = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_ground',
    type = 'empty'
)
spriteset_concrete = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_concrete',
    sprites = [(10, 10, 64, 39, -31, -8)],
    always_draw = 1,
)
spriteset_crane_rails_nw_se = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_crane_rails_nw_se',
    sprites = [(80, 10, 64, 39, -31, -8)],
    always_draw = 1,
)
spriteset_crane_rails_ne_sw = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_crane_rails_ne_sw',
    sprites = [(150, 10, 64, 39, -31, -8)],
    always_draw = 1,
)
spriteset_jetty_se_nw = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_jetty_se_nw',
    sprites = [(10, 60, 64, 39, -31, -7)],
    zextent = 7,
    always_draw = 1,
)
spriteset_jetty_ne_sw = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_jetty_ne_sw',
    sprites = [(80, 60, 64, 39, -31, -7)],
    zextent = 7,
    always_draw = 1
)
spriteset_jetty_slope_nw_se = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_jetty_slope_nw_se',
    sprites = [(150, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_jetty_slope_ne_sw = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_jetty_slope_ne_sw',
    sprites = [(220, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_jetty_slope_se_nw = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_jetty_slope_se_nw',
    sprites = [(290, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_jetty_slope_sw_ne = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_jetty_slope_sw_ne',
    sprites = [(360, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_tanks = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_spriteset_tanks',
    sprites = [(440, 10, 64, 84, -31, -43)],
    zoffset = 18
)
spriteset_silos = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_silos',
    sprites = [(510, 10, 64, 84, -35, -61)],
)
spriteset_cone_silo = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_cone_silo',
    sprites = [(580, 10, 64, 84, -31, -61)],
)
spriteset_warehouse = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_warehouse',
    sprites = [(650, 10, 64, 84, -31, -61)],
)
spriteset_large_crane_ne_sw = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_large_crane_ne_sw',
    sprites = [(440, 110, 64, 84, -31, -43)],
    zoffset = 18,
)
spriteset_large_crane_nw_se = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_large_crane_nw_se',
    sprites = [(510, 110, 64, 84, -31, -43)],
    zoffset = 18,
)
spriteset_large_crane_se_nw = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_large_crane_se_nw',
    sprites = [(580, 110, 64, 84, -31, -43)],
    zoffset = 18,
)
spriteset_large_crane_sw_ne = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_large_crane_sw_ne',
    sprites = [(650, 110, 64, 84, -31, -43)],
    zoffset = 18,
)
spriteset_boat_1 = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_boat_1',
    sprites = [(10, 110, 64, 39, -35, -15)],
)
spriteset_boat_2 = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_boat_2',
    sprites = [(80, 110, 64, 39, -40, -12)],
)
spriteset_boat_3 = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_boat_3',
    sprites = [(150, 110, 64, 39, -13, -19)],
)
spriteset_boat_4 = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_boat_4',
    sprites = [(220, 110, 64, 39, -27, -12)],
)
spriteset_boat_5 = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_boat_5',
    sprites = [(290, 110, 64, 39, -15, -11)],
)
spriteset_boat_6 = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_boat_6',
    sprites = [(360, 110, 64, 39, -25, -20)],
)
spriteset_boat_7 = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_boat_7',
    sprites = [(360, 110, 64, 39, -29, -5)],
)
spriteset_boat_8 = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_boat_8',
    sprites = [(290, 110, 64, 39, -32, -21)],
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_crane_rails_nw_se',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_crane_rails_nw_se]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_crane_rails_ne_sw',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_crane_rails_ne_sw]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_1_1',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_1_2',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_sw_ne, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_1_3',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_1_4',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_1_5',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_1_6',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_se_nw, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_1_7',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_1_8',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_jetty_slope_sw_ne, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_2_1',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_sw_ne, spriteset_concrete, spriteset_warehouse]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_2_2',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_concrete, spriteset_warehouse, spriteset_warehouse]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_2_3',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_warehouse]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_2_4',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_warehouse]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_2_5',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_warehouse]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_2_6',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_se_nw, spriteset_concrete, spriteset_warehouse]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_2_7',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_concrete, spriteset_warehouse]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_land_tile_2_8',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_jetty_slope_sw_ne, spriteset_concrete, spriteset_warehouse]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_11',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_concrete, spriteset_silos]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_water_barge_sw_ne',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_boat_1]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_water_barge_ne_sw',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_boat_2]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_water_barge_se_nw',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_boat_3]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_water_barge_nw_se',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_boat_4]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_water_empty',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = []
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_water_coaster_ne_sw',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_boat_5]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_water_coaster_nw_se',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_boat_6]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_water_coaster_se_nw',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_boat_7]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_water_coaster_sw_ne',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_boat_8]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_cone_silo',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_cone_silo]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_crane_nw_se',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_crane_nw_se]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_crane_sw_ne',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_crane_sw_ne]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_crane_ne_sw',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_crane_ne_sw]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_crane_se_nw',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_crane_se_nw]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_jetty_empty',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_null',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = []
)

industry.add_slope_graphics_switch('bulk_terminal_slope_switch_1',
                                   slope_spritelayout_mapping={0: 'bulk_terminal_spritelayout_land_tile_1_1',
                                                               1: 'bulk_terminal_spritelayout_land_tile_1_4',
                                                               2: 'bulk_terminal_spritelayout_land_tile_1_8',
                                                               3: 'bulk_terminal_spritelayout_land_tile_1_2',
                                                               4: 'bulk_terminal_spritelayout_land_tile_1_6',
                                                               5: 'bulk_terminal_spritelayout_land_tile_1_5',
                                                               6: 'bulk_terminal_spritelayout_land_tile_1_7',
                                                               7: 'bulk_terminal_spritelayout_land_tile_1_1',
                                                               8: 'bulk_terminal_spritelayout_land_tile_1_3',
                                                               9: 'bulk_terminal_spritelayout_land_tile_1_4',
                                                               10: 'bulk_terminal_spritelayout_land_tile_1_8',
                                                               11: 'bulk_terminal_spritelayout_land_tile_1_2',
                                                               12: 'bulk_terminal_spritelayout_land_tile_1_6',
                                                               13: 'bulk_terminal_spritelayout_land_tile_1_5',
                                                               14: 'bulk_terminal_spritelayout_land_tile_1_7'},
                                   default_result='bulk_terminal_spritelayout_land_tile_1_1')

industry.add_slope_graphics_switch('bulk_terminal_slope_switch_2',
                                   slope_spritelayout_mapping={0: 'bulk_terminal_spritelayout_land_tile_2_2',
                                                               1: 'bulk_terminal_spritelayout_land_tile_2_4',
                                                               2: 'bulk_terminal_spritelayout_land_tile_2_8',
                                                               3: 'bulk_terminal_spritelayout_land_tile_2_1',
                                                               4: 'bulk_terminal_spritelayout_land_tile_2_6',
                                                               5: 'bulk_terminal_spritelayout_land_tile_2_5',
                                                               6: 'bulk_terminal_spritelayout_land_tile_2_7',
                                                               7: 'bulk_terminal_spritelayout_land_tile_2_2',
                                                               8: 'bulk_terminal_spritelayout_land_tile_2_3',
                                                               9: 'bulk_terminal_spritelayout_land_tile_2_4',
                                                               10: 'bulk_terminal_spritelayout_land_tile_2_8',
                                                               11: 'bulk_terminal_spritelayout_land_tile_2_1',
                                                               12: 'bulk_terminal_spritelayout_land_tile_2_6',
                                                               13: 'bulk_terminal_spritelayout_land_tile_2_5',
                                                               14: 'bulk_terminal_spritelayout_land_tile_2_7'},
                                   default_result='bulk_terminal_spritelayout_land_tile_2_2')

industry.add_industry_layout(
    id = 'bulk_terminal_industry_layout_1',
    layout = [
              (0, 0, '255', 'bulk_terminal_spritelayout_null'),
              (0, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_empty'),
              (0, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_coaster_se_nw'),
              (0, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_empty'),
              (0, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_se_nw'),
              (0, 5, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (1, 0, '255', 'bulk_terminal_spritelayout_null'),
              (1, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_rails_nw_se'),
              (1, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_se_nw'),
              (1, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_rails_nw_se'),
              (1, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_jetty_empty'),
              (1, 5, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (2, 0, '255', 'bulk_terminal_spritelayout_null'),
              (2, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_barge_se_nw'),
              (2, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_empty'),
              (2, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_barge_se_nw'),
              (2, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_cone_silo'),
              (2, 5, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (3, 0, '255', 'bulk_terminal_spritelayout_null'),
              (3, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_se_nw'),
              (3, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_se_nw'),
              (3, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_rails_nw_se'),
              (3, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_11'),
              (3, 5, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (4, 0, '255', 'bulk_terminal_spritelayout_null'),
              (4, 1, '255', 'bulk_terminal_spritelayout_null'),
              (4, 2, '255', 'bulk_terminal_spritelayout_null'),
              (4, 3, '255', 'bulk_terminal_spritelayout_null'),
              (4, 4, '255', 'bulk_terminal_spritelayout_null'),
    ]
)
industry.add_industry_layout(
    id = 'bulk_terminal_industry_layout_2',
    layout = [(0, 0, '255', 'bulk_terminal_spritelayout_null'),
              (0, 1, '255', 'bulk_terminal_spritelayout_null'),
              (0, 2, '255', 'bulk_terminal_spritelayout_null'),
              (0, 3, '255', 'bulk_terminal_spritelayout_null'),
              (0, 4, '255', 'bulk_terminal_spritelayout_null'),
              (1, 0, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_ne_sw'),
              (1, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_empty'),
              (1, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_rails_ne_sw'),
              (1, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_barge_sw_ne'),
              (1, 4, '255', 'bulk_terminal_spritelayout_null'),
              (2, 0, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_rails_ne_sw'),
              (2, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_coaster_sw_ne'),
              (2, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_ne_sw'),
              (2, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_empty'),
              (2, 4, '255', 'bulk_terminal_spritelayout_null'),
              (3, 0, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_ne_sw'),
              (3, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_empty'),
              (3, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_rails_ne_sw'),
              (3, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_barge_sw_ne'),
              (3, 4, '255', 'bulk_terminal_spritelayout_null'),
              (4, 0, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_11'),
              (4, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_cone_silo'),
              (4, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_jetty_empty'),
              (4, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_ne_sw'),
              (4, 4, '255', 'bulk_terminal_spritelayout_null'),
              (5, 0, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (5, 1, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (5, 2, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (5, 3, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
    ]

)
industry.add_industry_layout(
    id = 'bulk_terminal_industry_layout_3',
    layout = [
              (0, 1, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (0, 2, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (0, 3, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (0, 4, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (1, 0, '255', 'bulk_terminal_spritelayout_null'),
              (1, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_sw_ne'),
              (1, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_jetty_empty'),
              (1, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_11'),
              (1, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_cone_silo'),
              (2, 0, '255', 'bulk_terminal_spritelayout_null'),
              (2, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_empty'),
              (2, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_rails_ne_sw'),
              (2, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_barge_ne_sw'),
              (2, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_sw_ne'),
              (3, 0, '255', 'bulk_terminal_spritelayout_null'),
              (3, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_coaster_ne_sw'),
              (3, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_sw_ne'),
              (3, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_empty'),
              (3, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_rails_ne_sw'),
              (4, 0, '255', 'bulk_terminal_spritelayout_null'),
              (4, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_empty'),
              (4, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_rails_ne_sw'),
              (4, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_barge_ne_sw'),
              (4, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_sw_ne'),
              (5, 0, '255', 'bulk_terminal_spritelayout_null'),
              (5, 1, '255', 'bulk_terminal_spritelayout_null'),
              (5, 2, '255', 'bulk_terminal_spritelayout_null'),
              (5, 3, '255', 'bulk_terminal_spritelayout_null'),
              (5, 4, '255', 'bulk_terminal_spritelayout_null'),
    ]
)
industry.add_industry_layout(
    id = 'bulk_terminal_industry_layout_4',
    layout = [(0, 0, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (0, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_11'),
              (0, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_nw_se'),
              (0, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_rails_nw_se'),
              (0, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_nw_se'),
              (0, 5, '255', 'bulk_terminal_spritelayout_null'),
              (1, 0, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (1, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_cone_silo'),
              (1, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_empty'),
              (1, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_coaster_nw_se'),
              (1, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_empty'),
              (1, 5, '255', 'bulk_terminal_spritelayout_null'),
              (2, 0, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (2, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_jetty_empty'),
              (2, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_rails_nw_se'),
              (2, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_nw_se'),
              (2, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_rails_nw_se'),
              (2, 5, '255', 'bulk_terminal_spritelayout_null'),
              (3, 0, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (3, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_crane_nw_se'),
              (3, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_barge_nw_se'),
              (3, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_empty'),
              (3, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_water_barge_nw_se'),
              (3, 5, '255', 'bulk_terminal_spritelayout_null'),
              (4, 1, '255', 'bulk_terminal_spritelayout_null'),
              (4, 2, '255', 'bulk_terminal_spritelayout_null'),
              (4, 3, '255', 'bulk_terminal_spritelayout_null'),
              (4, 4, '255', 'bulk_terminal_spritelayout_null'),
              (4, 5, '255', 'bulk_terminal_spritelayout_null'),
    ]
)
