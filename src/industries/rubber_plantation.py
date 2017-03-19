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
building_20 = industry.add_sprite(
    sprite_number = 1908,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_21 = industry.add_sprite(
    sprite_number = 1909,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_22 = industry.add_sprite(
    sprite_number = 1907,
    yoffset = 7,
    yextent = 8,
)
building_23 = industry.add_sprite(
    sprite_number = 1908,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_24 = industry.add_sprite(
    sprite_number = 1907,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_25 = industry.add_sprite(
    sprite_number = 1908,
    yoffset = 7,
    yextent = 8,
)
building_26 = industry.add_sprite(
    sprite_number = 1907,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_27 = industry.add_sprite(
    sprite_number = 1908,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_28 = industry.add_sprite(
    sprite_number = 1909,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_29 = industry.add_sprite(
    sprite_number = 1909,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_30 = industry.add_sprite(
    sprite_number = 1907,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_31 = industry.add_sprite(
    sprite_number = 1909,
    yoffset = 7,
    yextent = 8,
)
sprite_ground_4145 = industry.add_sprite(
    sprite_number = 4145
)
sprite_ground_4146 = industry.add_sprite(
    sprite_number = 4146
)
sprite_ground_4147 = industry.add_sprite(
    sprite_number = 4147
)
sprite_ground_4148 = industry.add_sprite(
    sprite_number = 4148
)
sprite_ground_4149 = industry.add_sprite(
    sprite_number = 4149
)
sprite_ground_4150 = industry.add_sprite(
    sprite_number = 4150
)
sprite_ground_4151 = industry.add_sprite(
    sprite_number = 4151
)
sprite_ground_4152 = industry.add_sprite(
    sprite_number = 4152
)
sprite_ground_4153 = industry.add_sprite(
    sprite_number = 4153
)
sprite_ground_4154 = industry.add_sprite(
    sprite_number = 4154
)
sprite_ground_4155 = industry.add_sprite(
    sprite_number = 4155
)
sprite_ground_4156 = industry.add_sprite(
    sprite_number = 4156
)
sprite_ground_4157 = industry.add_sprite(
    sprite_number = 4157
)
sprite_ground_4158 = industry.add_sprite(
    sprite_number = 4158
)
sprite_ground_4159 = industry.add_sprite(
    sprite_number = 4159
)
sprite_ground_4160 = industry.add_sprite(
    sprite_number = 4160
)
sprite_ground_4161 = industry.add_sprite(
    sprite_number = 4161
)
sprite_ground_4162 = industry.add_sprite(
    sprite_number = 4162
)
sprite_ground_4163 = industry.add_sprite(
    sprite_number = 4163
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
industry.add_spritelayout(
    id = 'rubber_plantation_731',
    ground_sprite = sprite_ground_4145,
    ground_overlay = sprite_ground_4145,
    building_sprites = [building_20, building_21, building_22, building_23],
)
industry.add_spritelayout(
    id = 'rubber_plantation_732',
    ground_sprite = sprite_ground_4146,
    ground_overlay = sprite_ground_4146,
    building_sprites = [building_24, building_21, building_25, building_26],
)
industry.add_spritelayout(
    id = 'rubber_plantation_733',
    ground_sprite = sprite_ground_4147,
    ground_overlay = sprite_ground_4147,
    building_sprites = [building_20, building_27, building_22, building_28],
)
industry.add_spritelayout(
    id = 'rubber_plantation_734',
    ground_sprite = sprite_ground_4148,
    ground_overlay = sprite_ground_4148,
    building_sprites = [building_29, building_30, building_25, building_26],
)
industry.add_spritelayout(
    id = 'rubber_plantation_735',
    ground_sprite = sprite_ground_4149,
    ground_overlay = sprite_ground_4149,
    building_sprites = [building_20, building_30, building_25, building_28],
)
industry.add_spritelayout(
    id = 'rubber_plantation_736',
    ground_sprite = sprite_ground_4150,
    ground_overlay = sprite_ground_4150,
    building_sprites = [building_24, building_27, building_31, building_26],
)
industry.add_spritelayout(
    id = 'rubber_plantation_737',
    ground_sprite = sprite_ground_4151,
    ground_overlay = sprite_ground_4151,
    building_sprites = [building_29, building_30, building_25, building_23],
)
industry.add_spritelayout(
    id = 'rubber_plantation_738',
    ground_sprite = sprite_ground_4152,
    ground_overlay = sprite_ground_4152,
    building_sprites = [building_24, building_21, building_22, building_23],
)
industry.add_spritelayout(
    id = 'rubber_plantation_739',
    ground_sprite = sprite_ground_4153,
    ground_overlay = sprite_ground_4153,
    building_sprites = [building_20, building_30, building_31, building_26],
)
industry.add_spritelayout(
    id = 'rubber_plantation_740',
    ground_sprite = sprite_ground_4154,
    ground_overlay = sprite_ground_4154,
    building_sprites = [building_20, building_30, building_22, building_28],
)
industry.add_spritelayout(
    id = 'rubber_plantation_741',
    ground_sprite = sprite_ground_4155,
    ground_overlay = sprite_ground_4155,
    building_sprites = [building_24, building_21, building_25, building_26],
)
industry.add_spritelayout(
    id = 'rubber_plantation_742',
    ground_sprite = sprite_ground_4156,
    ground_overlay = sprite_ground_4156,
    building_sprites = [building_24, building_30, building_22, building_28],
)
industry.add_spritelayout(
    id = 'rubber_plantation_743',
    ground_sprite = sprite_ground_4157,
    ground_overlay = sprite_ground_4157,
    building_sprites = [building_20, building_30, building_22, building_28],
)
industry.add_spritelayout(
    id = 'rubber_plantation_744',
    ground_sprite = sprite_ground_4158,
    ground_overlay = sprite_ground_4158,
    building_sprites = [building_24, building_21, building_25, building_26],
)
industry.add_spritelayout(
    id = 'rubber_plantation_745',
    ground_sprite = sprite_ground_4159,
    ground_overlay = sprite_ground_4159,
    building_sprites = [building_24, building_21, building_25, building_26],
)
industry.add_spritelayout(
    id = 'rubber_plantation_746',
    ground_sprite = sprite_ground_4160,
    ground_overlay = sprite_ground_4160,
    building_sprites = [building_29, building_27, building_22, building_23],
)
industry.add_spritelayout(
    id = 'rubber_plantation_747',
    ground_sprite = sprite_ground_4161,
    ground_overlay = sprite_ground_4161,
    building_sprites = [building_20, building_21, building_22, building_26],
)
industry.add_spritelayout(
    id = 'rubber_plantation_748',
    ground_sprite = sprite_ground_4162,
    ground_overlay = sprite_ground_4162,
    building_sprites = [building_24, building_27, building_22, building_28],
)
industry.add_spritelayout(
    id = 'rubber_plantation_749',
    ground_sprite = sprite_ground_4163,
    ground_overlay = sprite_ground_4163,
    building_sprites = [building_24, building_30, building_25, building_28],
)

slope_switch_1 = industry.add_slope_graphics_switch('rubber_plantation_slope_switch_1',
                                                    slope_spritelayout_mapping={0: 'rubber_plantation_731',
                                                                                1: 'rubber_plantation_732',
                                                                                2: 'rubber_plantation_733',
                                                                                3: 'rubber_plantation_734',
                                                                                4: 'rubber_plantation_735',
                                                                                5: 'rubber_plantation_736',
                                                                                6: 'rubber_plantation_737',
                                                                                7: 'rubber_plantation_738',
                                                                                8: 'rubber_plantation_739',
                                                                                9: 'rubber_plantation_740',
                                                                                10: 'rubber_plantation_741',
                                                                                11: 'rubber_plantation_742',
                                                                                12: 'rubber_plantation_743',
                                                                                13: 'rubber_plantation_744',
                                                                                14: 'rubber_plantation_745',
                                                                                29: 'rubber_plantation_746',
                                                                                23: 'rubber_plantation_747',
                                                                                27: 'rubber_plantation_748',
                                                                                30: 'rubber_plantation_749'},
                                                    default_result='rubber_plantation_731')

industry.add_industry_layout(
    id = 'rubber_plantation_layout_1',
    layout = [(0, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (0, 2, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 2, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
              (2, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (2, 2, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'rubber_plantation_layout_2',
    layout = [(0, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (0, 2, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
              (0, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 2, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 4, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'rubber_plantation_layout_3',
    layout = [(0, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (2, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (2, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (3, 0, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
              (3, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (4, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (4, 1, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'rubber_plantation_layout_4',
    layout = [(0, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (0, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (0, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (3, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (3, 1, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
              (3, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (3, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (4, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (4, 1, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
              (4, 3, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (4, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
    ]
)
industry.add_industry_layout(
    id = 'rubber_plantation_layout_5',
    layout = [(0, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (0, 2, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (0, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (0, 5, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 2, 'rubber_plantation_tile_2', 'rubber_plantation_shed_spritelayout'),
              (1, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 5, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (1, 6, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (2, 0, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (2, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (2, 2, 'rubber_plantation_tile_2', 'rubber_plantation_house_spritelayout'),
              (2, 4, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (2, 5, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (2, 6, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (3, 1, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (3, 2, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (3, 5, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
              (3, 6, 'rubber_plantation_tile_1', 'rubber_plantation_slope_switch_1'),
    ]
)