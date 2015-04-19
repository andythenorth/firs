"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryExtractive, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryExtractive(id='coal_mine',
                    input_multiplier_1='[0, 0]',
                    prob_in_game='3',
                    prob_random='8',
                    prod_multiplier='[20, 0]',
                    prod_cargo_types=['COAL'],
                    substitute='0',
                    map_colour='1',
                    prospect_chance='0.75',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_MINE))',
                    name='TTD_STR_INDUSTRY_NAME_COAL_MINE',
                    fund_cost_multiplier='252',
                    override='0',
                    )

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS' # ground tile same as overlay tile
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'coal_mine_spriteset_ground_overlay',
    type = 'empty'
)

spriteset_1a = industry.add_spriteset(
    id = 'coal_mine_spriteset_1a',
    sprites = [(10, 10, 64, 110, -31, -70)],
    zextent = 48
)
spriteset_1b = industry.add_spriteset(
    id = 'coal_mine_spriteset_1b',
    sprites = [(10, 130, 64, 110, -31, -70)],
    zextent = 48
)
spriteset_1c = industry.add_spriteset(
    id = 'coal_mine_spriteset_1c',
    sprites = [(10, 250, 64, 110, -31, -70)],
    zextent = 48
)

spriteset_2 = industry.add_spriteset(
    id = 'coal_mine_spriteset_2',
    sprites = [(80, 10, 64, 110, -31, -70)],
    zextent = 48
)
spriteset_3 = industry.add_spriteset(
    id = 'coal_mine_spriteset_3',
    sprites = [(150, 10, 64, 64, -31, -30)],
    zextent = 48
)

industry.add_spritelayout(
    id = 'coal_mine_spritelayout_1a',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1a],
)
industry.add_spritelayout(
    id = 'coal_mine_spritelayout_1b',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1b],
)
industry.add_spritelayout(
    id = 'coal_mine_spritelayout_1c',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1c],
)
industry.add_spritelayout(
    id = 'coal_mine_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
)
industry.add_spritelayout(
    id = 'coal_mine_spritelayout_3',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
)
