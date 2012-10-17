"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

import codecs # used for writing files - more unicode friendly than standard open() module

import os.path
currentdir = os.curdir

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir,'sprites','nml','templates'), format='text')
industry_templates = PageTemplateLoader(os.path.join(currentdir,'sprites','nml','industries'), format='text')


def unescape_chameleon_output(escaped_nml):
    # chameleon html-escapes some characters; that's sane and secure for chameleon's intended web use, but not wanted for nml
    # there is probably a standard module for unescaping html entities, but this will do for now
    escaped_nml = '>'.join(escaped_nml.split('&gt;'))
    escaped_nml = '<'.join(escaped_nml.split('&lt;'))
    escaped_nml = '&'.join(escaped_nml.split('&amp;'))
    return escaped_nml


class Tile(object):
    """ Base class to hold industry tiles"""
    def __init__(self, id):
        self.id = id


class Spriteset(object):
    """Base class to hold industry spritesets"""
    # !! arguably this should be two different classes, one for building/feature spritesets, and one for ground spritesets
    def __init__(self, id, sprites=[], type='', zextent=16, animation_rate = 0, num_sprites_to_autofill = 1):
        self.id = id
        self.sprites = sprites # a list of sprites 6-tuples in format (x, y, w, h, xoffs, yoffs)
        self.type = type # set to ground or other special types, or omit for default (building, greeble, foundations etc - graphics from png named same as industry)
        self.zextent = zextent # optional parameter, to use set this to z size of largest sprite in spriteset, or omit for default (16)
        self.animation_rate = animation_rate # optional multiplier to tile's animation rate, set to 1 for same as tile, >1 for faster; leave default (0) to disable animation
        self.num_sprites_to_autofill = num_sprites_to_autofill # create n sprites per sprite passed (optional convenience method for use where spriteset sizes must match; set value to same as size of largest spriteset)

    def get_ground_tile_x_start(self, type):
        return {'mud': 0, 'concrete': 80, 'cobble': 150, 'snow': 220, 'empty':290}[type]


class SpriteLayout(object):
    """Base class to hold spritelayouts for industry spritelayouts"""
    def __init__(self, id, ground_sprite, ground_overlay, building_sprites):
        self.id = id
        self.ground_sprite = ground_sprite
        self.ground_overlay = ground_overlay
        self.building_sprites = building_sprites


class IndustryLayout(object):
    """Base class to hold industry layouts"""
    def __init__(self, id, default_spritelayout, layout):
        self.id = id
        self.default_spritelayout = default_spritelayout
        self.layout = layout # a list of 4-tuples (SE offset from N tile, SW offset from N tile, tile identifier, identifier of spriteset or next nml switch)


class Industry(object):
    """Base class for all types of industry"""
    def __init__(self, id):
        self.id = id
        self.graphics_file = '"sprites/graphics/industries/' + id + '.png"' # don't use os.path.join here, this is for nml
        self.graphics_file_snow = '"sprites/graphics/industries/' + id + '_snow.png"' # don't use os.path.join here, this is for nml
        self.tiles = []
        self.spritesets = []
        self.spritelayouts = [] # by convention spritelayout is one word :P
        self.industry_layouts = []

    def add_tile(self, *args, **kwargs):
        new_tile = Tile(*args, **kwargs)
        self.tiles.append(new_tile)
        return new_tile

    def add_spriteset(self, *args, **kwargs):
        new_spriteset = Spriteset(*args, **kwargs)
        self.spritesets.append(new_spriteset)
        return new_spriteset # returning the new obj isn't essential, but permits the caller giving it a reference for use elsewhere

    def add_spritelayout(self, *args, **kwargs):
        new_spritelayout = SpriteLayout(*args, **kwargs)
        self.spritelayouts.append(new_spritelayout)
        return new_spritelayout # returning the new obj isn't essential, but permits the caller giving it a reference for use elsewhere

    def add_industry_layout(self, *args, **kwargs):
        new_industry_layout = IndustryLayout(*args, **kwargs)
        self.industry_layouts.append(new_industry_layout)
        return new_industry_layout # returning the new obj isn't essential, but permits the caller giving it a reference for use elsewhere

    def get_spritesets(self):
        template = templates['spritesets.pynml']
        return template(industry=industry)

    def get_spritelayouts(self):
        template = templates['spritelayouts.pynml']
        return template(industry=industry)

    def get_industry_layouts_as_tilelayouts(self):
        template = templates['industry_layout_tilelayouts.pynml']
        return template(industry=industry)

    def get_industry_layouts_as_property(self):
        template = templates['industry_layout_property.pynml']
        return template(industry=industry)

    def get_industry_layouts_as_graphic_switches(self):
        template = templates['industry_layout_graphics_switches.pynml']
        return template(industry=industry)

    def render_and_save_pnml(self):
        industry_template = industry_templates[self.id + '.pypnml']
        templated_pnml = industry_template(industry=self)
        templated_pnml = unescape_chameleon_output(templated_pnml)

        # save the results of templating
        pnml = codecs.open(os.path.join(currentdir,'sprites','nml','generated_pnml', self.id + '.pnml'), 'w','utf8')
        pnml.write(templated_pnml)
        pnml.close()

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry_id = 'grain_mill'
industry = Industry(id=industry_id)

industry.add_tile(id='grain_mill_tile')

spriteset_ground_bakery = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_bakery',
    type='cobble',
)
spriteset_ground_overlay_1 = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_1',
    sprites = [(10, 10, 64, 31, -31, 0)],
)
spriteset_ground_overlay_2 = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_2',
    sprites = [(80, 10, 64, 31, -31, 0)]
)
spriteset_ground_overlay_3 = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_3',
    sprites = [(150, 10, 64, 31, -31, 0)]
)
spriteset_ground_overlay_4 = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_4',
    sprites = [(220, 10, 64, 31, -31, 0)]
)
spriteset_1 = industry.add_spriteset(
    id = 'grain_mill_spriteset_1',
    sprites = [(10, 10, 64, 31, -31, 0)]
)
spriteset_2 = industry.add_spriteset(
    id = 'grain_mill_spriteset_2',
    sprites = [(80, 10, 64, 31, -31, 0)]
)
spriteset_3 = industry.add_spriteset(
    id = 'grain_mill_spriteset_3',
    sprites = [(150, 60, 64, 82, -31, -51)],
    zextent = 48 # optional zextent value, will default to 16 if this param is omitted
)
spriteset_4 = industry.add_spriteset(
    id = 'grain_mill_spriteset_4',
    sprites = [(220, 60, 64, 82, -31, -51)],
    zextent = 48 # optional zextent value, will default to 16 if this param is omitted
)
spriteset_windmill_anim = industry.add_spriteset(
    id = 'grain_mill_spriteset_windmill_anim',
    sprites = [(10, 200, 64, 82, -31, -52), (80, 200, 64, 82, -31, -52), (150, 200, 64, 82, -31, -52),
               (220, 200, 64, 82, -31, -52), (290, 200, 64, 82, -31, -52), (360, 200, 64, 82, -31, -52)],
    zextent = 24, # optional zextent value, will default to 16 if this param is omitted
    animation_rate = 1
)
spriteset_ground_windmill = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_windmill',
    type = 'empty',
    num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of animated frames (can get count from another spriteset if defined already)
)
spriteset_ground_overlay_windmill = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_windmill',
    sprites = [(10, 160, 64, 31, -31, 0)],
    num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of animated frames (can get count from another spriteset if defined already)
)

industry.add_spritelayout(
    id = 'grain_mill_spritelayout_brickbakery_1',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_1,
    building_sprites = []
)
industry.add_spritelayout(
    id = 'grain_mill_spritelayout_brickbakery_2',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_2,
    building_sprites = []
)
industry.add_spritelayout(
    id = 'grain_mill_spritelayout_brickbakery_3',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_3,
    building_sprites = [spriteset_3]
)
industry.add_spritelayout(
    id = 'grain_mill_spritelayout_brickbakery_4',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_4,
    building_sprites = [spriteset_4]
)
industry.add_spritelayout(
    id = 'grain_mill_spritelayout_windmill_anim',
    ground_sprite = spriteset_ground_windmill,
    ground_overlay = spriteset_ground_overlay_windmill,
    building_sprites = [spriteset_windmill_anim]
)

industry.add_industry_layout(
    id = 'grain_mill_industry_layout_1',
    default_spritelayout = 'grain_mill_spritelayout_brickbakery_3',
    layout = [(0, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (0, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (1, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_1'),
              (1, 1, 'grain_mill_tile','grain_mill_spritelayout_brickbakery_2')
    ]
)
industry.add_industry_layout(
    id = 'grain_mill_industry_layout_2',
    default_spritelayout = 'grain_mill_spritelayout_brickbakery_3',
    layout = [(0, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (0, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (1, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (1, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (2, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_1'),
              (2, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_2')
    ]
)
industry.add_industry_layout(
    id = 'grain_mill_industry_layout_3',
    default_spritelayout = 'grain_mill_spritelayout_brickbakery_3',
    layout = [(0, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (0, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (0, 2, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (0, 3, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (1, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_1'),
              (1, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_2'),
              (1, 2, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_1'),
              (1, 3, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_2')
    ]
)
industry.add_industry_layout(
    id = 'grain_mill_industry_layout_4',
    default_spritelayout = 'grain_mill_spritelayout_windmill_anim',
    layout = [(0, 0, 'grain_mill_tile', 'grain_mill_spritelayout_windmill_anim')]
)

# Templating
industry.render_and_save_pnml()
