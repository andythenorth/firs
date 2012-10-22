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

industry = Industry(id='plastics_plant')

industry.add_tile(id='plastics_plant_tile')

spriteset_ground = industry.add_spriteset(
    id = 'plastics_plant_spriteset_ground',
    type = 'concrete'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'plastics_plant_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'plastics_plant_spriteset_1',
    sprites = [(10, 10, 64, 62, -31, -31)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'plastics_plant_spriteset_2',
    sprites = [(80, 10, 64, 62, -31, -31)],
    zextent = 32
)
spriteset_3 = industry.add_spriteset(
    id = 'plastics_plant_spriteset_3',
    sprites = [(150, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'plastics_plant_spriteset_4',
    sprites = [(220, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_5 = industry.add_spriteset(
    id = 'plastics_plant_spriteset_5',
    sprites = [(290, 10, 64, 55, -31, -24)],
    zextent = 32
)
spriteset_6 = industry.add_spriteset(
    id = 'plastics_plant_spriteset_6',
    sprites = [(360, 10, 64, 87, -31, -56)],
    zextent = 52
)
spriteset_7 = industry.add_spriteset(
    id = 'plastics_plant_spriteset_7',
    sprites = [(430, 10, 64, 87, -31, -56)],
    zextent = 52
)
spriteset_8 = industry.add_spriteset(
    id = 'plastics_plant_spriteset_8',
    sprites = [(500, 10, 64, 87, -31, -56)],
    zextent = 52
)
spriteset_9 = industry.add_spriteset(
    id = 'plastics_plant_spriteset_9',
    sprites = [(570, 10, 64, 55, -31, -24)],
    zextent = 32
)

industry.add_spritelayout(
    id = 'plastics_plant_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'plastics_plant_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'plastics_plant_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'plastics_plant_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'plastics_plant_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'plastics_plant_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'plastics_plant_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'plastics_plant_spritelayout_8',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'plastics_plant_spritelayout_9',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_9],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'plastics_plant_spritelayout_10',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'plastics_plant_industry_layout_1',
    default_spritelayout = 'plastics_plant_spritelayout_8',
    layout = [(0, 0, 'plastics_plant_tile', 'plastics_plant_spritelayout_2'),
              (0, 1, 'plastics_plant_tile', 'plastics_plant_spritelayout_1'),
              (0, 2, 'plastics_plant_tile', 'plastics_plant_spritelayout_10'),
              (1, 0, 'plastics_plant_tile', 'plastics_plant_spritelayout_2'),
              (1, 1, 'plastics_plant_tile', 'plastics_plant_spritelayout_1'),
              (1, 2, 'plastics_plant_tile', 'plastics_plant_spritelayout_10'),
              (2, 0, 'plastics_plant_tile', 'plastics_plant_spritelayout_10'),
              (2, 1, 'plastics_plant_tile', 'plastics_plant_spritelayout_7'),
              (2, 2, 'plastics_plant_tile', 'plastics_plant_spritelayout_9'),
              (3, 0, 'plastics_plant_tile', 'plastics_plant_spritelayout_8'),
              (3, 1, 'plastics_plant_tile', 'plastics_plant_spritelayout_6'),
              (3, 2, 'plastics_plant_tile', 'plastics_plant_spritelayout_10'),
              (4, 0, 'plastics_plant_tile', 'plastics_plant_spritelayout_5'),
              (4, 1, 'plastics_plant_tile', 'plastics_plant_spritelayout_4'),
              (4, 2, 'plastics_plant_tile', 'plastics_plant_spritelayout_3')
    ]
)
industry.add_industry_layout(
    id = 'plastics_plant_industry_layout_2',
    default_spritelayout = 'plastics_plant_spritelayout_8',
    layout = [(0, 0, 'plastics_plant_tile', 'plastics_plant_spritelayout_8'),
              (0, 1, 'plastics_plant_tile', 'plastics_plant_spritelayout_7'),
              (0, 2, 'plastics_plant_tile', 'plastics_plant_spritelayout_9'),
              (1, 0, 'plastics_plant_tile', 'plastics_plant_spritelayout_8'),
              (1, 1, 'plastics_plant_tile', 'plastics_plant_spritelayout_6'),
              (1, 2, 'plastics_plant_tile', 'plastics_plant_spritelayout_10'),
              (2, 0, 'plastics_plant_tile', 'plastics_plant_spritelayout_5'),
              (2, 1, 'plastics_plant_tile', 'plastics_plant_spritelayout_4'),
              (2, 2, 'plastics_plant_tile', 'plastics_plant_spritelayout_3'),
              (3, 0, 'plastics_plant_tile', 'plastics_plant_spritelayout_2'),
              (3, 1, 'plastics_plant_tile', 'plastics_plant_spritelayout_1'),
              (3, 2, 'plastics_plant_tile', 'plastics_plant_spritelayout_10')
    ]
)
industry.add_industry_layout(
    id = 'plastics_plant_industry_layout_3',
    default_spritelayout = 'plastics_plant_spritelayout_8',
    layout = [(0, 0, 'plastics_plant_tile', 'plastics_plant_spritelayout_2'),
              (0, 1, 'plastics_plant_tile', 'plastics_plant_spritelayout_1'),
              (0, 2, 'plastics_plant_tile', 'plastics_plant_spritelayout_10'),
              (0, 3, 'plastics_plant_tile', 'plastics_plant_spritelayout_7'),
              (0, 4, 'plastics_plant_tile', 'plastics_plant_spritelayout_9'),
              (1, 0, 'plastics_plant_tile', 'plastics_plant_spritelayout_2'),
              (1, 1, 'plastics_plant_tile', 'plastics_plant_spritelayout_1'),
              (1, 2, 'plastics_plant_tile', 'plastics_plant_spritelayout_8'),
              (1, 3, 'plastics_plant_tile', 'plastics_plant_spritelayout_6'),
              (1, 4, 'plastics_plant_tile', 'plastics_plant_spritelayout_10'),
              (2, 0, 'plastics_plant_tile', 'plastics_plant_spritelayout_2'),
              (2, 1, 'plastics_plant_tile', 'plastics_plant_spritelayout_1'),
              (2, 2, 'plastics_plant_tile', 'plastics_plant_spritelayout_5'),
              (2, 3, 'plastics_plant_tile', 'plastics_plant_spritelayout_4'),
              (2, 4, 'plastics_plant_tile', 'plastics_plant_spritelayout_3')
    ]
)

# Templating
industry.render_and_save_pnml()
