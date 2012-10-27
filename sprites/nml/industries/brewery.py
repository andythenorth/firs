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

industry = Industry(id='brewery')

industry.add_tile(id='brewery_tile')

spriteset_ground = industry.add_spriteset(
    id = 'brewery_spriteset_ground',
    type = 'cobble',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'brewery_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'brewery_spriteset_1',
    sprites = [(10, 60, 64, 91, -31, -60)],
    zextent = 48
)
spriteset_2 = industry.add_spriteset(
    id = 'brewery_spriteset_2',
    sprites = [(80, 60, 64, 91, -31, -60)],
    zextent = 48
)
spriteset_3 = industry.add_spriteset(
    id = 'brewery_spriteset_3',
    sprites = [(150, 60, 64, 91, -31, -60)],
    zextent = 48
)
sprite_smoke = industry.add_sprite(
    sprite_number = 'animation_frame <= 19 ? 3079 + (animation_frame / 4) : 3079',
    xoffset= 8,
    yoffset= 0,
    zoffset= '55 + animation_frame',
    xextent= 11,
    zextent= 7
)

industry.add_spritelayout(
    id = 'brewery_spritelayout_1_anim',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1, sprite_smoke],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'brewery_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'brewery_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'brewery_industry_layout_1',
    default_spritelayout = 'brewery_spritelayout_3',
    layout = [(0, 2, 'brewery_tile', 'brewery_spritelayout_3'),
              (1, 0, 'brewery_tile', 'brewery_spritelayout_1_anim'),
              (1, 2, 'brewery_tile', 'brewery_spritelayout_2')
    ]
)
industry.add_industry_layout(
    id = 'brewery_industry_layout_2',
    default_spritelayout = 'brewery_spritelayout_3',
    layout = [(0, 0, 'brewery_tile', 'brewery_spritelayout_3'),
              (1, 0, 'brewery_tile', 'brewery_spritelayout_2'),
              (2, 0, 'brewery_tile', 'brewery_spritelayout_1_anim')
    ]
)
industry.add_industry_layout(
    id = 'brewery_industry_layout_3',
    default_spritelayout = 'brewery_spritelayout_3',
    layout = [(0, 1, 'brewery_tile', 'brewery_spritelayout_3'),
              (1, 0, 'brewery_tile', 'brewery_spritelayout_1_anim'),
              (1, 1, 'brewery_tile', 'brewery_spritelayout_2')
    ]
)
industry.add_industry_layout(
    id = 'brewery_industry_layout_4',
    default_spritelayout = 'brewery_spritelayout_3',
    layout = [(0, 0, 'brewery_tile', 'brewery_spritelayout_1_anim'),
              (1, 0, 'brewery_tile', 'brewery_spritelayout_3'),
              (2, 0, 'brewery_tile', 'brewery_spritelayout_2')
    ]
)
industry.add_industry_layout(
    id = 'brewery_industry_layout_5',
    default_spritelayout = 'brewery_spritelayout_3',
    layout = [(0, 0, 'brewery_tile', 'brewery_spritelayout_3'),
              (0, 1, 'brewery_tile', 'brewery_spritelayout_3'),
              (1, 0, 'brewery_tile', 'brewery_spritelayout_2'),
              (1, 1, 'brewery_tile', 'brewery_spritelayout_2'),
              (2, 0, 'brewery_tile', 'brewery_spritelayout_1_anim')
    ]
)

# Templating
industry.render_and_save_pnml()
