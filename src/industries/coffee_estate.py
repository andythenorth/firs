"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryOrganic, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryOrganic(id='coffee_estate',
                    map_colour='71',
                    prob_in_game='3',
                    prob_random='10',
                    prospect_chance='0.75',
                    name='string(STR_IND_COFFEE_ESTATE)',
                    extra_text_fund='string(STR_FUND_COFFEE_ESTATE)',
                    layouts='AUTO',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(require_cluster=['coffee_estate', [20, 72, 1, 4]]),
                    prod_cargo_types=['JAVA', 'FRUT'],
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_PLANTATION))',
                    fund_cost_multiplier='54',
                    prod_multiplier='[11, 8]')

industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['BASIC_TROPIC'].prod_multiplier = '[9, 9]'


industry.add_tile(id='coffee_estate_tile_1',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_desert=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='coffee_estate_tile_2', # house
             	  autoslope='return CB_RESULT_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_desert=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'coffee_estate_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'coffee_estate_house',
    sprites = [(10, 10, 64, 59, -31, -28)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'coffee_estate_shed',
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
    id = 'coffee_estate_house_spritelayout',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
)
industry.add_spritelayout(
    id = 'coffee_estate_shed_spritelayout',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
)
industry.add_magic_spritelayout(
    type = 'slope_aware_trees',
    id = 'coffee_estate_slope_aware_ground_with_trees',
    config = {'trees': [1620, 1633, 1689, 1620]}
)

industry.add_spritelayout(
    id = 'coffee_estate_597',
    ground_sprite = sprite_ground_4164,
    ground_overlay = sprite_ground_4164,
    building_sprites = [building_0, building_1, building_2, building_3],
)
industry.add_spritelayout(
    id = 'coffee_estate_598',
    ground_sprite = sprite_ground_4165,
    ground_overlay = sprite_ground_4165,
    building_sprites = [building_4, building_1, building_5, building_6],
)
industry.add_spritelayout(
    id = 'coffee_estate_599',
    ground_sprite = sprite_ground_4166,
    ground_overlay = sprite_ground_4166,
    building_sprites = [building_0, building_7, building_2, building_8],
)
industry.add_spritelayout(
    id = 'coffee_estate_600',
    ground_sprite = sprite_ground_4167,
    ground_overlay = sprite_ground_4167,
    building_sprites = [building_9, building_10, building_5, building_6],
)
industry.add_spritelayout(
    id = 'coffee_estate_601',
    ground_sprite = sprite_ground_4168,
    ground_overlay = sprite_ground_4168,
    building_sprites = [building_0, building_10, building_5, building_8],
)
industry.add_spritelayout(
    id = 'coffee_estate_602',
    ground_sprite = sprite_ground_4169,
    ground_overlay = sprite_ground_4169,
    building_sprites = [building_4, building_7, building_11, building_6],
)
industry.add_spritelayout(
    id = 'coffee_estate_603',
    ground_sprite = sprite_ground_4170,
    ground_overlay = sprite_ground_4170,
    building_sprites = [building_9, building_10, building_5, building_3],
)
industry.add_spritelayout(
    id = 'coffee_estate_604',
    ground_sprite = sprite_ground_4171,
    ground_overlay = sprite_ground_4171,
    building_sprites = [building_4, building_1, building_2, building_3],
)
industry.add_spritelayout(
    id = 'coffee_estate_605',
    ground_sprite = sprite_ground_4172,
    ground_overlay = sprite_ground_4172,
    building_sprites = [building_0, building_10, building_11, building_6],
)
industry.add_spritelayout(
    id = 'coffee_estate_606',
    ground_sprite = sprite_ground_4173,
    ground_overlay = sprite_ground_4173,
    building_sprites = [building_0, building_10, building_2, building_8],
)
industry.add_spritelayout(
    id = 'coffee_estate_607',
    ground_sprite = sprite_ground_4174,
    ground_overlay = sprite_ground_4174,
    building_sprites = [building_4, building_1, building_5, building_6],
)
industry.add_spritelayout(
    id = 'coffee_estate_608',
    ground_sprite = sprite_ground_4175,
    ground_overlay = sprite_ground_4175,
    building_sprites = [building_4, building_10, building_2, building_8],
)
industry.add_spritelayout(
    id = 'coffee_estate_609',
    ground_sprite = sprite_ground_4176,
    ground_overlay = sprite_ground_4176,
    building_sprites = [building_0, building_10, building_2, building_8],
)
industry.add_spritelayout(
    id = 'coffee_estate_610',
    ground_sprite = sprite_ground_4177,
    ground_overlay = sprite_ground_4177,
    building_sprites = [building_4, building_1, building_5, building_6],
)
industry.add_spritelayout(
    id = 'coffee_estate_611',
    ground_sprite = sprite_ground_4178,
    ground_overlay = sprite_ground_4178,
    building_sprites = [building_4, building_1, building_5, building_6],
)
industry.add_spritelayout(
    id = 'coffee_estate_612',
    ground_sprite = sprite_ground_4179,
    ground_overlay = sprite_ground_4179,
    building_sprites = [building_9, building_7, building_2, building_3],
)
industry.add_spritelayout(
    id = 'coffee_estate_613',
    ground_sprite = sprite_ground_4180,
    ground_overlay = sprite_ground_4180,
    building_sprites = [building_0, building_1, building_2, building_6],
)
industry.add_spritelayout(
    id = 'coffee_estate_614',
    ground_sprite = sprite_ground_4181,
    ground_overlay = sprite_ground_4181,
    building_sprites = [building_4, building_7, building_2, building_8],
)
industry.add_spritelayout(
    id = 'coffee_estate_615',
    ground_sprite = sprite_ground_4182,
    ground_overlay = sprite_ground_4182,
    building_sprites = [building_4, building_10, building_5, building_8],
)

slope_switch_1 = industry.add_slope_graphics_switch('coffee_estate_slope_switch_1',
                                                    slope_spritelayout_mapping={0: 'coffee_estate_597',
                                                                                1: 'coffee_estate_598',
                                                                                2: 'coffee_estate_599',
                                                                                3: 'coffee_estate_600',
                                                                                4: 'coffee_estate_601',
                                                                                5: 'coffee_estate_602',
                                                                                6: 'coffee_estate_603',
                                                                                7: 'coffee_estate_604',
                                                                                8: 'coffee_estate_605',
                                                                                9: 'coffee_estate_606',
                                                                                10: 'coffee_estate_607',
                                                                                11: 'coffee_estate_608',
                                                                                12: 'coffee_estate_609',
                                                                                13: 'coffee_estate_610',
                                                                                14: 'coffee_estate_611',
                                                                                29: 'coffee_estate_612',
                                                                                23: 'coffee_estate_613',
                                                                                27: 'coffee_estate_614',
                                                                                30: 'coffee_estate_615'},
                                                    default_result='coffee_estate_597')

industry.add_industry_layout(
    id = 'coffee_estate_layout_1',
    layout = [(0, 0, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (0, 1, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (0, 2, 'coffee_estate_tile_2', 'coffee_estate_shed_spritelayout'),
              (1, 0, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 1, 'coffee_estate_tile_2', 'coffee_estate_house_spritelayout'),
              (1, 2, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (2, 1, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (2, 2, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
    ]
)
industry.add_industry_layout(
    id = 'coffee_estate_layout_2',
    layout = [(0, 0, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (0, 1, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (0, 2, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (0, 3, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 1, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 2, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 3, 'coffee_estate_tile_2', 'coffee_estate_shed_spritelayout'),
              (1, 4, 'coffee_estate_tile_2', 'coffee_estate_house_spritelayout'),
    ]
)
industry.add_industry_layout(
    id = 'coffee_estate_layout_3',
    layout = [(0, 0, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (0, 1, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 0, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 1, 'coffee_estate_tile_2', 'coffee_estate_house_spritelayout'),
              (2, 0, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (2, 1, 'coffee_estate_tile_2', 'coffee_estate_shed_spritelayout'),
              (3, 0, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (3, 1, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
    ]
)
industry.add_industry_layout(
    id = 'coffee_estate_layout_4',
    layout = [(0, 0, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (0, 1, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (0, 3, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (0, 4, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 0, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 1, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 3, 'coffee_estate_tile_2', 'coffee_estate_house_spritelayout'),
              (1, 4, 'coffee_estate_tile_2', 'coffee_estate_shed_spritelayout'),
              (3, 0, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (3, 1, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (3, 3, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (3, 4, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (4, 0, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (4, 1, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (4, 3, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (4, 4, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
    ]
)
industry.add_industry_layout(
    id = 'coffee_estate_layout_5',
    layout = [(0, 1, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (0, 2, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (0, 3, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (0, 4, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 0, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 1, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 2, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 3, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 4, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (1, 5, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (2, 0, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (2, 1, 'coffee_estate_tile_2', 'coffee_estate_shed_spritelayout'),
              (2, 2, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (2, 3, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (2, 4, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (2, 5, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (3, 1, 'coffee_estate_tile_2', 'coffee_estate_house_spritelayout'),
              (3, 2, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (3, 3, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
              (3, 4, 'coffee_estate_tile_1', 'coffee_estate_slope_switch_1'),
    ]
)