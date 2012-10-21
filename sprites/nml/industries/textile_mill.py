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

industry = Industry(id='textile_mill')

industry.add_tile(id='textile_mill_tile')

spriteset_ground = industry.add_spriteset(
    id = 'textile_mill_spriteset_ground',
    type = 'concrete'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'textile_mill_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'textile_mill_spriteset_1',
    sprites = [(10, 10, 64, 76, -31, -45)],
    zextent = 48
)
spriteset_2 = industry.add_spriteset(
    id = 'textile_mill_spriteset_2',
    sprites = [(80, 10, 64, 76, -31, -45)],
    zextent = 48
)
spriteset_3 = industry.add_spriteset(
    id = 'textile_mill_spriteset_3',
    sprites = [(150, 10, 64, 63, -31, -32)],
    zextent = 48
)
spriteset_4 = industry.add_spriteset(
    id = 'textile_mill_spriteset_4',
    sprites = [(220, 10, 64, 63, -31, -32)],
    zextent = 48
)
spriteset_5 = industry.add_spriteset(
    id = 'textile_mill_spriteset_5',
    sprites = [(290, 10, 64, 63, -31, -32)],
    zextent = 48
)
spriteset_6 = industry.add_spriteset(
    id = 'textile_mill_spriteset_6',
    sprites = [(360, 10, 64, 63, -31, -32)],
    zextent = 48
)

industry.add_spritelayout(
    id = 'textile_mill_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'textile_mill_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'textile_mill_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'textile_mill_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'textile_mill_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'textile_mill_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'textile_mill_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'textile_mill_industry_layout',
    default_spritelayout = 'textile_mill_spritelayout_7',
    layout = [(0, 0, 'textile_mill_tile', 'textile_mill_spritelayout_2'),
              (0, 1, 'textile_mill_tile', 'textile_mill_spritelayout_3'),
              (1, 0, 'textile_mill_tile', 'textile_mill_spritelayout_1'),
              (1, 1, 'textile_mill_tile', 'textile_mill_spritelayout_4'),
              (2, 0, 'textile_mill_tile', 'textile_mill_spritelayout_5'),
              (2, 1, 'textile_mill_tile', 'textile_mill_spritelayout_6')
    ]
)

# Templating
industry.render_and_save_pnml()
