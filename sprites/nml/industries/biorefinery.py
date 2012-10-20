"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from firs import Industry, Tile, Sprite, Spriteset, SpriteLayout, IndustryLayout

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='biorefinery')

industry.add_tile(id='biorefinery_tile')

spriteset_ground = industry.add_spriteset(
    id = 'biorefinery_spriteset_ground',
    type = 'concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'biorefinery_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'biorefinery_spriteset_1',
    sprites = [(500, 10, 64, 66, -31, -35)]
)
spriteset_2 = industry.add_spriteset(
    id = 'biorefinery_spriteset_2',
    sprites = [(570, 10, 64, 66, -31, -35)]
)
spriteset_3 = industry.add_spriteset(
    id = 'biorefinery_spriteset_3',
    sprites = [(710, 10, 64, 66, -31, -35)]
)
spriteset_4 = industry.add_spriteset(
    id = 'biorefinery_spriteset_4',
    sprites = [(80, 10, 64, 88, -31, -58)]
)
spriteset_5 = industry.add_spriteset(
    id = 'biorefinery_spriteset_5',
    sprites = [(150, 10, 64, 88, -31, -59)]
)
spriteset_6 = industry.add_spriteset(
    id = 'biorefinery_spriteset_6',
    sprites = [(220, 10, 64, 88, -31, -64)]
)
spriteset_7 = industry.add_spriteset(
    id = 'biorefinery_spriteset_7',
    sprites = [(360, 10, 64, 73, -31, -45)]
)
spriteset_8 = industry.add_spriteset(
    id = 'biorefinery_spriteset_8',
    sprites = [(430, 10, 64, 66, -31, -38)]
)
"""
industry.add_spritelayout(
    id = 'food_market_spritelayout',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1, sprite_tree_1, sprite_tree_2]
)
industry.add_industry_layout(
    id = 'food_market_industry_layout',
    default_spritelayout = 'food_market_spritelayout',
    layout = [(0, 0, 'food_market_tile', 'food_market_spritelayout')
    ]
)"""
# Templating
industry.render_and_save_pnml()
