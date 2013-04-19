"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import Industry, Tile, Sprite, Spriteset, SpriteLayout, IndustryLayout

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='coal_mine',
                    accept_cargo_types=['ENSP'],
                    input_multiplier_1='[0, 0]',
                    prob_in_game='3',
                    prob_random='8',
                    prod_multiplier='[20, 0]',
                    prod_cargo_types=['COAL'],
                    substitute='0',
                    map_colour='1',
                    prospect_chance='0.75',
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

spriteset_1 = industry.add_spriteset(
    id = 'coal_mine_spriteset_1',
    sprites = [(10, 10, 64, 110, -31, -70)],
    zextent = 48
)
spriteset_2 = industry.add_spriteset(
    id = 'coal_mine_spriteset_2',
    sprites = [(80, 10, 64, 110, -31, -70)],
    zextent = 48
)
spriteset_3 = industry.add_spriteset(
    id = 'coal_mine_spriteset_3',
    sprites = [(150, 10, 64, 64, -31, -70)],
    zextent = 48
)

industry.add_spritelayout(
    id = 'coal_mine_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'coal_mine_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'coal_mine_spritelayout_3',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
