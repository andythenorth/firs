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

industry = Industry(id='hardware_store')

industry.add_tile(id='hardware_store_tile')

hardware_store_spriteset_ground = industry.add_spriteset(
    id = 'hardware_store_spriteset_ground',
    type='slab',
)
hardware_store_spriteset_ground_overlay = industry.add_spriteset(
    id = 'hardware_store_spriteset_ground_overlay',
    type = 'empty',
)
hardware_store_spriteset = industry.add_spriteset(
    id = 'hardware_store_spriteset',
    sprites = [(0, 0, 64, 64, -31, -33)]
)

industry.add_spritelayout(
    id = 'hardware_store_spritelayout',
    ground_sprite = hardware_store_spriteset_ground,
    ground_overlay = hardware_store_spriteset_ground_overlay,
    building_sprites = [hardware_store_spriteset]
)
industry.add_industry_layout(
    id = 'hardware_store_industry_layout',
    default_spritelayout = 'hardware_store_spritelayout',
    layout = [(0, 0, 'hardware_store_tile', 'hardware_store_spritelayout')
    ]
)
# Templating
industry.render_and_save_pnml()
