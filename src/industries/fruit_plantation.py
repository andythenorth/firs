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
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'fruit_plantation_shed',
    sprites = [(80, 10, 64, 59, -31, -28)],
    zextent = 32
)
building_0 = industry.add_sprite(
    sprite_number = 1633,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_1 = industry.add_sprite(
    sprite_number = 1689,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_2 = industry.add_sprite(
    sprite_number = 1620,
    yoffset = 7,
    yextent = 8,
)
building_3 = industry.add_sprite(
    sprite_number = 1633,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_4 = industry.add_sprite(
    sprite_number = 1620,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_5 = industry.add_sprite(
    sprite_number = 1633,
    yoffset = 7,
    yextent = 8,
)
building_6 = industry.add_sprite(
    sprite_number = 1620,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_7 = industry.add_sprite(
    sprite_number = 1633,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_8 = industry.add_sprite(
    sprite_number = 1689,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_9 = industry.add_sprite(
    sprite_number = 1689,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_10 = industry.add_sprite(
    sprite_number = 1620,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_11 = industry.add_sprite(
    sprite_number = 1689,
    yoffset = 7,
    yextent = 8,
)
building_20 = industry.add_sprite(
    sprite_number = 1831,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_21 = industry.add_sprite(
    sprite_number = 1832,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_22 = industry.add_sprite(
    sprite_number = 1830,
    yoffset = 7,
    yextent = 8,
)
building_23 = industry.add_sprite(
    sprite_number = 1831,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_24 = industry.add_sprite(
    sprite_number = 1830,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_25 = industry.add_sprite(
    sprite_number = 1831,
    yoffset = 7,
    yextent = 8,
)
building_26 = industry.add_sprite(
    sprite_number = 1830,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_27 = industry.add_sprite(
    sprite_number = 1831,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_28 = industry.add_sprite(
    sprite_number = 1832,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_29 = industry.add_sprite(
    sprite_number = 1832,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_30 = industry.add_sprite(
    sprite_number = 1830,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_31 = industry.add_sprite(
    sprite_number = 1832,
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
sprite_ground_4164 = industry.add_sprite(
    sprite_number = 4164
)
sprite_ground_4165 = industry.add_sprite(
    sprite_number = 4165
)
sprite_ground_4166 = industry.add_sprite(
    sprite_number = 4166
)
sprite_ground_4167 = industry.add_sprite(
    sprite_number = 4167
)
sprite_ground_4168 = industry.add_sprite(
    sprite_number = 4168
)
sprite_ground_4169 = industry.add_sprite(
    sprite_number = 4169
)
sprite_ground_4170 = industry.add_sprite(
    sprite_number = 4170
)
sprite_ground_4171 = industry.add_sprite(
    sprite_number = 4171
)
sprite_ground_4172 = industry.add_sprite(
    sprite_number = 4172
)
sprite_ground_4173 = industry.add_sprite(
    sprite_number = 4173
)
sprite_ground_4174 = industry.add_sprite(
    sprite_number = 4174
)
sprite_ground_4175 = industry.add_sprite(
    sprite_number = 4175
)
sprite_ground_4176 = industry.add_sprite(
    sprite_number = 4176
)
sprite_ground_4177 = industry.add_sprite(
    sprite_number = 4177
)
sprite_ground_4178 = industry.add_sprite(
    sprite_number = 4178
)
sprite_ground_4179 = industry.add_sprite(
    sprite_number = 4179
)
sprite_ground_4180 = industry.add_sprite(
    sprite_number = 4180
)
sprite_ground_4181 = industry.add_sprite(
    sprite_number = 4181
)
sprite_ground_4182 = industry.add_sprite(
    sprite_number = 4182
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
industry.add_spritelayout(
    id = 'fruit_plantation_597',
    ground_sprite = sprite_ground_4164,
    ground_overlay = sprite_ground_4164,
    building_sprites = [building_0, building_1, building_2, building_3],
)
industry.add_spritelayout(
    id = 'fruit_plantation_598',
    ground_sprite = sprite_ground_4165,
    ground_overlay = sprite_ground_4165,
    building_sprites = [building_4, building_1, building_5, building_6],
)
industry.add_spritelayout(
    id = 'fruit_plantation_599',
    ground_sprite = sprite_ground_4166,
    ground_overlay = sprite_ground_4166,
    building_sprites = [building_0, building_7, building_2, building_8],
)
industry.add_spritelayout(
    id = 'fruit_plantation_600',
    ground_sprite = sprite_ground_4167,
    ground_overlay = sprite_ground_4167,
    building_sprites = [building_9, building_10, building_5, building_6],
)
industry.add_spritelayout(
    id = 'fruit_plantation_601',
    ground_sprite = sprite_ground_4168,
    ground_overlay = sprite_ground_4168,
    building_sprites = [building_0, building_10, building_5, building_8],
)
industry.add_spritelayout(
    id = 'fruit_plantation_602',
    ground_sprite = sprite_ground_4169,
    ground_overlay = sprite_ground_4169,
    building_sprites = [building_4, building_7, building_11, building_6],
)
industry.add_spritelayout(
    id = 'fruit_plantation_603',
    ground_sprite = sprite_ground_4170,
    ground_overlay = sprite_ground_4170,
    building_sprites = [building_9, building_10, building_5, building_3],
)
industry.add_spritelayout(
    id = 'fruit_plantation_604',
    ground_sprite = sprite_ground_4171,
    ground_overlay = sprite_ground_4171,
    building_sprites = [building_4, building_1, building_2, building_3],
)
industry.add_spritelayout(
    id = 'fruit_plantation_605',
    ground_sprite = sprite_ground_4172,
    ground_overlay = sprite_ground_4172,
    building_sprites = [building_0, building_10, building_11, building_6],
)
industry.add_spritelayout(
    id = 'fruit_plantation_606',
    ground_sprite = sprite_ground_4173,
    ground_overlay = sprite_ground_4173,
    building_sprites = [building_0, building_10, building_2, building_8],
)
industry.add_spritelayout(
    id = 'fruit_plantation_607',
    ground_sprite = sprite_ground_4174,
    ground_overlay = sprite_ground_4174,
    building_sprites = [building_4, building_1, building_5, building_6],
)
industry.add_spritelayout(
    id = 'fruit_plantation_608',
    ground_sprite = sprite_ground_4175,
    ground_overlay = sprite_ground_4175,
    building_sprites = [building_4, building_10, building_2, building_8],
)
industry.add_spritelayout(
    id = 'fruit_plantation_609',
    ground_sprite = sprite_ground_4176,
    ground_overlay = sprite_ground_4176,
    building_sprites = [building_0, building_10, building_2, building_8],
)
industry.add_spritelayout(
    id = 'fruit_plantation_610',
    ground_sprite = sprite_ground_4177,
    ground_overlay = sprite_ground_4177,
    building_sprites = [building_4, building_1, building_5, building_6],
)
industry.add_spritelayout(
    id = 'fruit_plantation_611',
    ground_sprite = sprite_ground_4178,
    ground_overlay = sprite_ground_4178,
    building_sprites = [building_4, building_1, building_5, building_6],
)
industry.add_spritelayout(
    id = 'fruit_plantation_612',
    ground_sprite = sprite_ground_4179,
    ground_overlay = sprite_ground_4179,
    building_sprites = [building_9, building_7, building_2, building_3],
)
industry.add_spritelayout(
    id = 'fruit_plantation_613',
    ground_sprite = sprite_ground_4180,
    ground_overlay = sprite_ground_4180,
    building_sprites = [building_0, building_1, building_2, building_6],
)
industry.add_spritelayout(
    id = 'fruit_plantation_614',
    ground_sprite = sprite_ground_4181,
    ground_overlay = sprite_ground_4181,
    building_sprites = [building_4, building_7, building_2, building_8],
)
industry.add_spritelayout(
    id = 'fruit_plantation_615',
    ground_sprite = sprite_ground_4182,
    ground_overlay = sprite_ground_4182,
    building_sprites = [building_4, building_10, building_5, building_8],
)
industry.add_spritelayout(
    id = 'fruit_plantation_731',
    ground_sprite = sprite_ground_4145,
    ground_overlay = sprite_ground_4145,
    building_sprites = [building_20, building_21, building_22, building_23],
)
industry.add_spritelayout(
    id = 'fruit_plantation_732',
    ground_sprite = sprite_ground_4146,
    ground_overlay = sprite_ground_4146,
    building_sprites = [building_24, building_21, building_25, building_26],
)
industry.add_spritelayout(
    id = 'fruit_plantation_733',
    ground_sprite = sprite_ground_4147,
    ground_overlay = sprite_ground_4147,
    building_sprites = [building_20, building_27, building_22, building_28],
)
industry.add_spritelayout(
    id = 'fruit_plantation_734',
    ground_sprite = sprite_ground_4148,
    ground_overlay = sprite_ground_4148,
    building_sprites = [building_29, building_30, building_25, building_26],
)
industry.add_spritelayout(
    id = 'fruit_plantation_735',
    ground_sprite = sprite_ground_4149,
    ground_overlay = sprite_ground_4149,
    building_sprites = [building_20, building_30, building_25, building_28],
)
industry.add_spritelayout(
    id = 'fruit_plantation_736',
    ground_sprite = sprite_ground_4150,
    ground_overlay = sprite_ground_4150,
    building_sprites = [building_24, building_27, building_31, building_26],
)
industry.add_spritelayout(
    id = 'fruit_plantation_737',
    ground_sprite = sprite_ground_4151,
    ground_overlay = sprite_ground_4151,
    building_sprites = [building_29, building_30, building_25, building_23],
)
industry.add_spritelayout(
    id = 'fruit_plantation_738',
    ground_sprite = sprite_ground_4152,
    ground_overlay = sprite_ground_4152,
    building_sprites = [building_24, building_21, building_22, building_23],
)
industry.add_spritelayout(
    id = 'fruit_plantation_739',
    ground_sprite = sprite_ground_4153,
    ground_overlay = sprite_ground_4153,
    building_sprites = [building_20, building_30, building_31, building_26],
)
industry.add_spritelayout(
    id = 'fruit_plantation_740',
    ground_sprite = sprite_ground_4154,
    ground_overlay = sprite_ground_4154,
    building_sprites = [building_20, building_30, building_22, building_28],
)
industry.add_spritelayout(
    id = 'fruit_plantation_741',
    ground_sprite = sprite_ground_4155,
    ground_overlay = sprite_ground_4155,
    building_sprites = [building_24, building_21, building_25, building_26],
)
industry.add_spritelayout(
    id = 'fruit_plantation_742',
    ground_sprite = sprite_ground_4156,
    ground_overlay = sprite_ground_4156,
    building_sprites = [building_24, building_30, building_22, building_28],
)
industry.add_spritelayout(
    id = 'fruit_plantation_743',
    ground_sprite = sprite_ground_4157,
    ground_overlay = sprite_ground_4157,
    building_sprites = [building_20, building_30, building_22, building_28],
)
industry.add_spritelayout(
    id = 'fruit_plantation_744',
    ground_sprite = sprite_ground_4158,
    ground_overlay = sprite_ground_4158,
    building_sprites = [building_24, building_21, building_25, building_26],
)
industry.add_spritelayout(
    id = 'fruit_plantation_745',
    ground_sprite = sprite_ground_4159,
    ground_overlay = sprite_ground_4159,
    building_sprites = [building_24, building_21, building_25, building_26],
)
industry.add_spritelayout(
    id = 'fruit_plantation_746',
    ground_sprite = sprite_ground_4160,
    ground_overlay = sprite_ground_4160,
    building_sprites = [building_29, building_27, building_22, building_23],
)
industry.add_spritelayout(
    id = 'fruit_plantation_747',
    ground_sprite = sprite_ground_4161,
    ground_overlay = sprite_ground_4161,
    building_sprites = [building_20, building_21, building_22, building_26],
)
industry.add_spritelayout(
    id = 'fruit_plantation_748',
    ground_sprite = sprite_ground_4162,
    ground_overlay = sprite_ground_4162,
    building_sprites = [building_24, building_27, building_22, building_28],
)
industry.add_spritelayout(
    id = 'fruit_plantation_749',
    ground_sprite = sprite_ground_4163,
    ground_overlay = sprite_ground_4163,
    building_sprites = [building_24, building_30, building_25, building_28],
)

slope_switch_1 = industry.add_slope_graphics_switch('fruit_plantation_slope_switch_1',
                                                    slope_spritelayout_mapping={0: 'fruit_plantation_597',
                                                                                1: 'fruit_plantation_598',
                                                                                2: 'fruit_plantation_599',
                                                                                3: 'fruit_plantation_600',
                                                                                4: 'fruit_plantation_601',
                                                                                5: 'fruit_plantation_602',
                                                                                6: 'fruit_plantation_603',
                                                                                7: 'fruit_plantation_604',
                                                                                8: 'fruit_plantation_605',
                                                                                9: 'fruit_plantation_606',
                                                                                10: 'fruit_plantation_607',
                                                                                11: 'fruit_plantation_608',
                                                                                12: 'fruit_plantation_609',
                                                                                13: 'fruit_plantation_610',
                                                                                14: 'fruit_plantation_611',
                                                                                29: 'fruit_plantation_612',
                                                                                23: 'fruit_plantation_613',
                                                                                27: 'fruit_plantation_614',
                                                                                30: 'fruit_plantation_615'},
                                                    default_result='fruit_plantation_597')

"""
Tropic Climate support - not currently implemented, but will be restored so legacy code kept here
switch(FEAT_INDUSTRYTILES, SELF, ${industry.id}_750, nearby_tile_slope(0,0)) {
	0: ${industry.id}_731;
	1: ${industry.id}_732;
	2: ${industry.id}_733;
	3: ${industry.id}_734;
	4: ${industry.id}_735;
	5: ${industry.id}_736;
	6: ${industry.id}_737;
	7: ${industry.id}_738;
	8: ${industry.id}_739;
	9: ${industry.id}_740;
	10: ${industry.id}_741;
	11: ${industry.id}_742;
	12: ${industry.id}_743;
	13: ${industry.id}_744;
	14: ${industry.id}_745;
	29: ${industry.id}_746;
	23: ${industry.id}_747;
	27: ${industry.id}_748;
	30: ${industry.id}_749;
	${industry.id}_731;
}
"""

industry.add_industry_layout(
    id = 'fruit_plantation_layout_1',
    layout = [(0, 0, 'fruit_plantation_tile_1', slope_switch_1),
              (0, 1, 'fruit_plantation_tile_1', slope_switch_1),
              (0, 2, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 0, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 1, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 2, 'fruit_plantation_tile_1', slope_switch_1),
              (2, 1, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
              (2, 2, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'fruit_plantation_layout_2',
    layout = [(0, 0, 'fruit_plantation_tile_1', slope_switch_1),
              (0, 1, 'fruit_plantation_tile_1', slope_switch_1),
              (0, 2, 'fruit_plantation_tile_1', slope_switch_1),
              (0, 3, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
              (1, 1, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 2, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 3, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 4, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'fruit_plantation_layout_3',
    layout = [(0, 0, 'fruit_plantation_tile_1', slope_switch_1),
              (0, 1, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 0, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 1, 'fruit_plantation_tile_1', slope_switch_1),
              (2, 0, 'fruit_plantation_tile_1', slope_switch_1),
              (2, 1, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
              (3, 0, 'fruit_plantation_tile_1', slope_switch_1),
              (3, 1, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'fruit_plantation_layout_4',
    layout = [(0, 0, 'fruit_plantation_tile_1', slope_switch_1),
              (0, 1, 'fruit_plantation_tile_1', slope_switch_1),
              (0, 3, 'fruit_plantation_tile_1', slope_switch_1),
              (0, 4, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 0, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 1, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 3, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 4, 'fruit_plantation_tile_1', slope_switch_1),
              (3, 0, 'fruit_plantation_tile_1', slope_switch_1),
              (3, 1, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
              (3, 3, 'fruit_plantation_tile_1', slope_switch_1),
              (3, 4, 'fruit_plantation_tile_1', slope_switch_1),
              (4, 0, 'fruit_plantation_tile_1', slope_switch_1),
              (4, 1, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
              (4, 3, 'fruit_plantation_tile_1', slope_switch_1),
              (4, 4, 'fruit_plantation_tile_1', slope_switch_1),
    ]
)
industry.add_industry_layout(
    id = 'fruit_plantation_layout_5',
    layout = [(0, 1, 'fruit_plantation_tile_1', slope_switch_1),
              (0, 2, 'fruit_plantation_tile_1', slope_switch_1),
              (0, 3, 'fruit_plantation_tile_1', slope_switch_1),
              (0, 4, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 0, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 1, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 2, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 3, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 4, 'fruit_plantation_tile_1', slope_switch_1),
              (1, 5, 'fruit_plantation_tile_1', slope_switch_1),
              (3, 0, 'fruit_plantation_tile_1', slope_switch_1),
              (3, 1, 'fruit_plantation_tile_1', slope_switch_1),
              (3, 2, 'fruit_plantation_tile_1', slope_switch_1),
              (3, 3, 'fruit_plantation_tile_1', slope_switch_1),
              (3, 4, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
              (3, 5, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
              (4, 1, 'fruit_plantation_tile_1', slope_switch_1),
              (4, 2, 'fruit_plantation_tile_1', slope_switch_1),
              (4, 3, 'fruit_plantation_tile_1', slope_switch_1),
              (4, 4, 'fruit_plantation_tile_1', slope_switch_1),
    ]
)