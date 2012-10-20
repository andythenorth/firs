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

industry.add_tile(id='food_market_tile')

spriteset_ground = industry.add_spriteset(
    id = 'food_market_spriteset_ground',
    type='slab',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'food_market_spriteset_ground_overlay',
    sprites = [(10, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(
    id = 'food_market_spriteset',
    sprites = [(10, 60, 64, 36, -31, -4)]
)
sprite_tree_1 = industry.add_sprite(
    sprite_number = 'nearby_tile_terrain_type(0, 0) != TILETYPE_SNOW ? market_tree : MARKET_TREE_SNOW', # defined in defines.pnml, to permit possibility of selecting a different sprite if a tree grf is loaded
    xoffset= 11,
    yoffset= 1,
    xextent= 6,
    yextent= 6
)
sprite_tree_2 = industry.add_sprite(
    sprite_number = 'nearby_tile_terrain_type(0, 0) != TILETYPE_SNOW ? market_tree : MARKET_TREE_SNOW', # defined in defines.pnml, to permit possibility of selecting a different sprite if a tree grf is loaded
    xoffset= 11,
    yoffset= 6,
    xextent= 6,
    yextent= 6
)

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
)
# Templating
industry.render_and_save_pnml()
