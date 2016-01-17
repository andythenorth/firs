"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryPort, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryPort(id='liquids_terminal',
                    accept_cargo_types=['OIL_'],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['PETR', 'RFPR'],
                    layouts='AUTO',
                    prob_in_game='2',
                    prob_random='6',
                    prod_multiplier='[9, 9]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='164',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='2',
                    spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER)',
                    location_checks=IndustryLocationChecks(incompatible={'liquids_terminal': 48}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_LIQUIDS_TERMINAL)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_INDUSTRY_HARBOUR))',
                    fund_cost_multiplier='152',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    override_default_construction_states=True)

industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].accept_cargo_types = ['OIL_', 'EOIL']
industry.economy_variations['MISTAH_KURTZ'].prod_cargo_types = ['PETR', 'RFPR']
industry.economy_variations['MISTAH_KURTZ'].prod_multiplier = '[9, 9]'

industry.add_tile(id='liquids_terminal_tile_1',
                  land_shape_flags='bitmask(LSF_ONLY_ON_FLAT_LAND)',
                  location_checks=TileLocationChecks(always_allow_founder=False))
industry.add_tile(id='liquids_terminal_tile_2',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  location_checks=TileLocationChecks(always_allow_founder=False,
                                                     require_coast=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDSPRITE_WATER'
)
spriteset_ground_empty = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_ground',
    type = 'empty'
)
spriteset_concrete = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_concrete',
    sprites = [(10, 10, 64, 39, -31, -8)],
    always_draw = 1,
)
spriteset_jetty_se_nw = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_jetty_se_nw',
    sprites = [(10, 60, 64, 39, -31, -7)],
    zextent = 7,
    always_draw = 1,
)
spriteset_jetty_ne_sw = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_jetty_ne_sw',
    sprites = [(80, 60, 64, 39, -31, -7)],
    zextent = 7,
    always_draw = 1
)
spriteset_jetty_slope_nw_se = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_jetty_slope_nw_se',
    sprites = [(150, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_jetty_slope_ne_sw = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_jetty_slope_ne_sw',
    sprites = [(220, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_jetty_slope_se_nw = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_jetty_slope_se_nw',
    sprites = [(290, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_jetty_slope_sw_ne = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_jetty_slope_sw_ne',
    sprites = [(360, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_small_tanks = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_small_tanks',
    sprites = [(440, 110, 64, 84, -31, -43)],
    zoffset = 18,
)
spriteset_office = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_spriteset_office',
    sprites = [(440, 10, 64, 84, -31, -43)],
    zoffset = 18
)
spriteset_spherical_tank = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_spherical_tank',
    sprites = [(510, 10, 64, 84, -35, -61)],
)
spriteset_large_cylinder_tank = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_large_cylinder_tank',
    sprites = [(510, 110, 64, 84, -31, -43)],
    zoffset = 18,
)
spriteset_boat_1 = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_boat_1',
    sprites = [(10, 110, 64, 39, -35, -15)],
)
spriteset_boat_2 = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_boat_2',
    sprites = [(80, 110, 64, 39, -40, -12)],
)
spriteset_boat_3 = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_boat_3',
    sprites = [(150, 110, 64, 39, -13, -19)],
)
spriteset_boat_4 = industry.add_spriteset(
    id = 'liquids_terminal_spriteset_boat_4',
    sprites = [(220, 110, 64, 39, -27, -12)],
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_small_tanks',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_small_tanks]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_1_1',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_concrete, spriteset_large_cylinder_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_1_2',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_sw_ne, spriteset_concrete, spriteset_large_cylinder_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_1_3',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_cylinder_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_1_4',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_large_cylinder_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_1_5',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_large_cylinder_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_1_6',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_se_nw, spriteset_concrete, spriteset_large_cylinder_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_1_7',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_concrete, spriteset_large_cylinder_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_1_8',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_jetty_slope_sw_ne, spriteset_concrete, spriteset_large_cylinder_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_2_1',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_sw_ne, spriteset_concrete, spriteset_office]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_2_2',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_concrete, spriteset_office]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_2_3',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_office]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_2_4',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_office]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_2_5',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_office]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_2_6',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_se_nw, spriteset_concrete, spriteset_office]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_2_7',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_concrete, spriteset_office]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_2_8',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_jetty_slope_sw_ne, spriteset_concrete, spriteset_office]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_3_1',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_sw_ne, spriteset_concrete]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_3_2',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_concrete, spriteset_spherical_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_3_3',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_spherical_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_3_4',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_spherical_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_3_5',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_spherical_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_3_6',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_se_nw, spriteset_concrete, spriteset_spherical_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_3_7',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_concrete, spriteset_spherical_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_land_tile_3_8',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_jetty_slope_sw_ne, spriteset_concrete, spriteset_spherical_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_spherical_tank',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_concrete, spriteset_spherical_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_water_barge_sw_ne',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_boat_1]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_water_barge_ne_sw',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_boat_2]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_water_barge_se_nw',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_boat_3]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_water_barge_nw_se',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_boat_4]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_water_empty',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = []
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_office',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_office]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_large_cylinder_tank',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_cylinder_tank]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_crane_ne_sw',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_small_tanks]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_jetty_empty',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete]
)
industry.add_spritelayout(
    id = 'liquids_terminal_spritelayout_null',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = []
)

slope_switch_1 =industry.add_slope_graphics_switch('liquids_terminal_slope_switch_1',
                                                    slope_spritelayout_mapping={0: 'liquids_terminal_spritelayout_land_tile_1_1',
                                                                                1: 'liquids_terminal_spritelayout_land_tile_1_4',
                                                                                2: 'liquids_terminal_spritelayout_land_tile_1_8',
                                                                                3: 'liquids_terminal_spritelayout_land_tile_1_2',
                                                                                4: 'liquids_terminal_spritelayout_land_tile_1_6',
                                                                                5: 'liquids_terminal_spritelayout_land_tile_1_5',
                                                                                6: 'liquids_terminal_spritelayout_land_tile_1_7',
                                                                                7: 'liquids_terminal_spritelayout_land_tile_1_1',
                                                                                8: 'liquids_terminal_spritelayout_land_tile_1_3',
                                                                                9: 'liquids_terminal_spritelayout_land_tile_1_4',
                                                                                10: 'liquids_terminal_spritelayout_land_tile_1_8',
                                                                                11: 'liquids_terminal_spritelayout_land_tile_1_2',
                                                                                12: 'liquids_terminal_spritelayout_land_tile_1_6',
                                                                                13: 'liquids_terminal_spritelayout_land_tile_1_5',
                                                                                14: 'liquids_terminal_spritelayout_land_tile_1_7'},
                                                    default_result='liquids_terminal_spritelayout_land_tile_1_1')

slope_switch_2 = industry.add_slope_graphics_switch('liquids_terminal_slope_switch_2',
                                                    slope_spritelayout_mapping={0: 'liquids_terminal_spritelayout_land_tile_2_2',
                                                                                1: 'liquids_terminal_spritelayout_land_tile_2_4',
                                                                                2: 'liquids_terminal_spritelayout_land_tile_2_8',
                                                                                3: 'liquids_terminal_spritelayout_land_tile_2_1',
                                                                                4: 'liquids_terminal_spritelayout_land_tile_2_6',
                                                                                5: 'liquids_terminal_spritelayout_land_tile_2_5',
                                                                                6: 'liquids_terminal_spritelayout_land_tile_2_7',
                                                                                7: 'liquids_terminal_spritelayout_land_tile_2_2',
                                                                                8: 'liquids_terminal_spritelayout_land_tile_2_3',
                                                                                9: 'liquids_terminal_spritelayout_land_tile_2_4',
                                                                                10: 'liquids_terminal_spritelayout_land_tile_2_8',
                                                                                11: 'liquids_terminal_spritelayout_land_tile_2_1',
                                                                                12: 'liquids_terminal_spritelayout_land_tile_2_6',
                                                                                13: 'liquids_terminal_spritelayout_land_tile_2_5',
                                                                                14: 'liquids_terminal_spritelayout_land_tile_2_7'},
                                                    default_result='liquids_terminal_spritelayout_land_tile_2_2')

slope_switch_3 = industry.add_slope_graphics_switch('liquids_terminal_slope_switch_3',
                                                    slope_spritelayout_mapping={0: 'liquids_terminal_spritelayout_land_tile_3_2',
                                                                                1: 'liquids_terminal_spritelayout_land_tile_3_4',
                                                                                2: 'liquids_terminal_spritelayout_land_tile_3_8',
                                                                                3: 'liquids_terminal_spritelayout_land_tile_3_1',
                                                                                4: 'liquids_terminal_spritelayout_land_tile_3_6',
                                                                                5: 'liquids_terminal_spritelayout_land_tile_3_5',
                                                                                6: 'liquids_terminal_spritelayout_land_tile_3_7',
                                                                                7: 'liquids_terminal_spritelayout_land_tile_3_2',
                                                                                8: 'liquids_terminal_spritelayout_land_tile_3_3',
                                                                                9: 'liquids_terminal_spritelayout_land_tile_3_4',
                                                                                10: 'liquids_terminal_spritelayout_land_tile_3_8',
                                                                                11: 'liquids_terminal_spritelayout_land_tile_3_1',
                                                                                12: 'liquids_terminal_spritelayout_land_tile_3_6',
                                                                                13: 'liquids_terminal_spritelayout_land_tile_3_5',
                                                                                14: 'liquids_terminal_spritelayout_land_tile_3_7'},
                                                    default_result='liquids_terminal_spritelayout_land_tile_3_2')
industry.add_industry_layout(
    id = 'liquids_terminal_industry_layout_1',
    layout = [
              (0, 0, '255', 'liquids_terminal_spritelayout_null'),
              (0, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (0, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (0, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_office'),
              (0, 4, 'liquids_terminal_tile_2', slope_switch_3),
              (1, 0, '255', 'liquids_terminal_spritelayout_null'),
              (1, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_small_tanks'),
              (1, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_small_tanks'),
              (1, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_jetty_empty'),
              (1, 4, 'liquids_terminal_tile_2', slope_switch_2),
              (2, 0, '255', 'liquids_terminal_spritelayout_null'),
              (2, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_barge_se_nw'),
              (2, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (2, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (2, 4, 'liquids_terminal_tile_2', slope_switch_1),
              (3, 0, '255', 'liquids_terminal_spritelayout_null'),
              (3, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (3, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (3, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (3, 4, 'liquids_terminal_tile_2', slope_switch_1),
              (4, 0, '255', 'liquids_terminal_spritelayout_null'),
              (4, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (4, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_barge_nw_se'),
              (4, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (4, 4, 'liquids_terminal_tile_2', slope_switch_1),
              (5, 0, '255', 'liquids_terminal_spritelayout_null'),
              (5, 1, '255', 'liquids_terminal_spritelayout_null'),
              (5, 2, '255', 'liquids_terminal_spritelayout_null'),
              (5, 3, '255', 'liquids_terminal_spritelayout_null'),
              (5, 4, '255', 'liquids_terminal_spritelayout_null'),
    ]
)
industry.add_industry_layout(
    id = 'liquids_terminal_industry_layout_2',
    layout = [(0, 0, '255', 'liquids_terminal_spritelayout_null'),
              (0, 1, '255', 'liquids_terminal_spritelayout_null'),
              (0, 2, '255', 'liquids_terminal_spritelayout_null'),
              (0, 3, '255', 'liquids_terminal_spritelayout_null'),
              (0, 4, '255', 'liquids_terminal_spritelayout_null'),
              (0, 5, '255', 'liquids_terminal_spritelayout_null'),
              (1, 0, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (1, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (1, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_barge_sw_ne'),
              (1, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_small_tanks'),
              (1, 4, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (1, 5, '255', 'liquids_terminal_spritelayout_null'),
              (2, 0, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (2, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (2, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (2, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_small_tanks'),
              (2, 4, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_barge_ne_sw'),
              (2, 5, '255', 'liquids_terminal_spritelayout_null'),
              (3, 0, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (3, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (3, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (3, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_jetty_empty'),
              (3, 4, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_office'),
              (3, 5, '255', 'liquids_terminal_spritelayout_null'),
              (4, 0, 'liquids_terminal_tile_2', slope_switch_1),
              (4, 1, 'liquids_terminal_tile_2', slope_switch_1),
              (4, 2, 'liquids_terminal_tile_2', slope_switch_1),
              (4, 3, 'liquids_terminal_tile_2', slope_switch_2),
              (4, 4, 'liquids_terminal_tile_2', slope_switch_3),
    ]

)
industry.add_industry_layout(
    id = 'liquids_terminal_industry_layout_3',
    layout = [
              (0, 1, 'liquids_terminal_tile_2', slope_switch_3),
              (0, 2, 'liquids_terminal_tile_2', slope_switch_2),
              (0, 3, 'liquids_terminal_tile_2', slope_switch_1),
              (0, 4, 'liquids_terminal_tile_2', slope_switch_1),
              (0, 5, 'liquids_terminal_tile_2', slope_switch_1),
              (1, 0, '255', 'liquids_terminal_spritelayout_null'),
              (1, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_office'),
              (1, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_jetty_empty'),
              (1, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (1, 4, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (1, 5, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (2, 0, '255', 'liquids_terminal_spritelayout_null'),
              (2, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (2, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_small_tanks'),
              (2, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (2, 4, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (2, 5, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_barge_se_nw'),
              (3, 0, '255', 'liquids_terminal_spritelayout_null'),
              (3, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (3, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_crane_ne_sw'),
              (3, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_barge_ne_sw'),
              (3, 4, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (3, 5, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (4, 0, '255', 'liquids_terminal_spritelayout_null'),
              (4, 1, '255', 'liquids_terminal_spritelayout_null'),
              (4, 2, '255', 'liquids_terminal_spritelayout_null'),
              (4, 3, '255', 'liquids_terminal_spritelayout_null'),
              (4, 4, '255', 'liquids_terminal_spritelayout_null'),
              (4, 5, '255', 'liquids_terminal_spritelayout_null'),
    ]
)
industry.add_industry_layout(
    id = 'liquids_terminal_industry_layout_4',
    layout = [(0, 0, 'liquids_terminal_tile_2', slope_switch_1),
              (0, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (0, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (0, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (0, 4, '255', 'liquids_terminal_spritelayout_null'),
              (1, 0, 'liquids_terminal_tile_2', slope_switch_1),
              (1, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (1, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (1, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (1, 4, '255', 'liquids_terminal_spritelayout_null'),
              (2, 0, 'liquids_terminal_tile_2', slope_switch_1),
              (2, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_large_cylinder_tank'),
              (2, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (2, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_barge_nw_se'),
              (2, 4, '255', 'liquids_terminal_spritelayout_null'),
              (3, 0, 'liquids_terminal_tile_2', slope_switch_2),
              (3, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_jetty_empty'),
              (3, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_small_tanks'),
              (3, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_small_tanks'),
              (3, 4, '255', 'liquids_terminal_spritelayout_null'),
              (4, 0, 'liquids_terminal_tile_2', slope_switch_3),
              (4, 1, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_office'),
              (4, 2, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_barge_ne_sw'),
              (4, 3, 'liquids_terminal_tile_1', 'liquids_terminal_spritelayout_water_empty'),
              (4, 4, '255', 'liquids_terminal_spritelayout_null'),
              (5, 1, '255', 'liquids_terminal_spritelayout_null'),
              (5, 2, '255', 'liquids_terminal_spritelayout_null'),
              (5, 3, '255', 'liquids_terminal_spritelayout_null'),
              (5, 4, '255', 'liquids_terminal_spritelayout_null'),
    ]
)
