"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryExtractive, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryExtractive(id='junk_yard',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['SCMT'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='7',
                    prod_multiplier='[12, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='36',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(town_distance=(0, 144)),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_JUNKYARD)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_INDUSTRY_ESTATE))',
                    fund_cost_multiplier='101',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    graphics_change_dates = [1949, 1960, 1980, 2000],
                    intro_year=1850,
                    snakebite=True)

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True

industry.add_tile(id='junk_yard_tile_1',
                  location_checks=TileLocationChecks(disallow_steep_slopes=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'junk_yard_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'junk_yard_spriteset_1',
    sprites = [(10, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'junk_yard_spriteset_2',
    sprites = [(80, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_3 = industry.add_spriteset(
    id = 'junk_yard_spriteset_3',
    sprites = [(150, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'junk_yard_spriteset_4',
    sprites = [(220, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_5 = industry.add_spriteset(
    id = 'junk_yard_spriteset_5',
    sprites = [(290, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_6 = industry.add_spriteset(
    id = 'junk_yard_spriteset_6',
    sprites = [(360, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_7 = industry.add_spriteset(
    id = 'junk_yard_spriteset_7',
    sprites = [(430, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_8 = industry.add_spriteset(
    id = 'junk_yard_spriteset_8',
    sprites = [(500, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_9 = industry.add_spriteset(
    id = 'junk_yard_spriteset_9',
    sprites = [(570, 10, 64, 55, -31, -24)],
    zextent = 32
)

industry.add_spritelayout(
    id = 'junk_yard_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
)
industry.add_spritelayout(
    id = 'junk_yard_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
)
industry.add_spritelayout(
    id = 'junk_yard_spritelayout_3',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
)
industry.add_spritelayout(
    id = 'junk_yard_spritelayout_4',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
)
industry.add_spritelayout(
    id = 'junk_yard_spritelayout_5',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
)
industry.add_spritelayout(
    id = 'junk_yard_spritelayout_6',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
)
industry.add_spritelayout(
    id = 'junk_yard_spritelayout_7',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
)
industry.add_spritelayout(
    id = 'junk_yard_spritelayout_8',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
)
industry.add_spritelayout(
    id = 'junk_yard_spritelayout_9',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_9],
)

industry.add_industry_layout(
    id = 'junk_yard_industry_layout_1',
    layout = [(0, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_2'),
              (1, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_2'),
              (1, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_9'),
              (2, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_1'),
              (2, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_8'),
              (3, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_4'),
              (3, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_7'),
              (4, 0, 'junk_yard_tile_1', 'junk_yard_spritelayout_5'),
              (4, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_3'),
              (4, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_6'),
    ]
)
industry.add_industry_layout(
    id = 'junk_yard_industry_layout_2',
    layout = [(0, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_7'),
              (1, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_1'),
              (1, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_8'),
              (2, 0, 'junk_yard_tile_1', 'junk_yard_spritelayout_5'),
              (2, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_3'),
              (2, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_6'),
    ]
)
industry.add_industry_layout(
    id = 'junk_yard_industry_layout_3',
    layout = [(0, 3, 'junk_yard_tile_1', 'junk_yard_spritelayout_2'),
              (1, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_2'),
              (1, 3, 'junk_yard_tile_1', 'junk_yard_spritelayout_9'),
              (2, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_1'),
              (2, 3, 'junk_yard_tile_1', 'junk_yard_spritelayout_8'),
              (3, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_4'),
              (3, 3, 'junk_yard_tile_1', 'junk_yard_spritelayout_7'),
              (4, 0, 'junk_yard_tile_1', 'junk_yard_spritelayout_5'),
              (4, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_3'),
              (4, 3, 'junk_yard_tile_1', 'junk_yard_spritelayout_6'),
    ]
)

