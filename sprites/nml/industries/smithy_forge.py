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

industry = Industry(id='smithy_forge')

industry.add_tile(id='smithy_forge_tile')

spriteset_ground = industry.add_spriteset(
    id = 'smithy_forge_spriteset_ground',
    type = 'slab'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'smithy_forge_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_hut = industry.add_spriteset(
    id = 'smithy_forge_spriteset_hut',
    sprites = [(10, 10, 64, 31, -31, 0)]
)
spriteset_no_hut = industry.add_spriteset(
    id = 'smithy_forge_spriteset_no_hut',
    sprites = [(80, 10, 64, 31, -31, 0)]
)

industry.add_spritelayout(
    id = 'smithy_forge_spritelayout_hut',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_hut],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'smithy_forge_spritelayout_no_hut',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_no_hut],
    fences = ['nw','ne','se','sw']
)
industry.add_industry_layout(
    id = 'smithy_forge_industry_layout',
    default_spritelayout = 'smithy_forge_spritelayout_no_hut',
    layout = [(0, 0, 'smithy_forge_tile', 'smithy_forge_spritelayout_hut'),
              (0, 1, 'smithy_forge_tile', 'smithy_forge_spritelayout_no_hut'),
              (1, 0, 'smithy_forge_tile', 'smithy_forge_spritelayout_no_hut'),
              (1, 1, 'smithy_forge_tile', 'smithy_forge_spritelayout_no_hut')
    ]
)

# Templating
industry.render_and_save_pnml()
