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

class Spriteset(object):
    """Base class to hold industry spritesets"""
    # arguably this should be two different classes, one for building/feature spritesets, and one for ground spritesets
    def __init__(self, id, sprites=[], type='', zextent=16, animation_rate = 0, num_sprites_to_autofill = 1):
        self.id = id
        self.type = type # set to ground or other special types, or omit for default (building, greeble, foundations etc)
        self.sprites = sprites
        self.zextent = zextent # optional parameter, to use set this to value of largest sprite in spriteset, or omit for default (16)
        self.animation_rate = animation_rate # multiplier to tile's animation rate, set to 1 for same as tile, >1 for faster; leave default (0) to disable animation
        self.num_sprites_to_autofill = num_sprites_to_autofill # create n sprites per sprite passed (convenience method for use where spriteset sizes must match)

    def get_ground_tile_x_start(self, type):
        return {'mud': 0, 'concrete': 80, 'cobble': 150, 'snow': 220, 'empty':290}[type]

    def render(self, industry):
        template = templates['spriteset.pynml']
        return template(spriteset=self, industry=industry)


class SpriteLayout(object):
    """Base class to hold spritelayouts for industry spritelayouts"""
    def __init__(self, id, ground_sprite, ground_overlay, building_sprites):
        self.id = id
        self.ground_sprite = ground_sprite
        self.ground_overlay = ground_overlay
        self.building_sprites = building_sprites

    def render(self, industry):
        template = templates['spritelayout.pynml']
        return template(spritelayout=self, industry=industry)


class IndustryLayout(object):
    """Base class to hold industry layouts"""
    def __init__(self, id, default_tile, spritelayouts):
        self.id = id
        self.default_tile = default_tile
        self.spritelayouts = spritelayouts


class Industry(object):
    """Base class for all types of industry"""
    def __init__(self, id, spritesets, spritelayouts, industry_layouts):
        self.id = id
        self.graphics_file = '"sprites/graphics/industries/' + id + '.png"' # don't use os.path.join here, this is for nml
        self.graphics_file_snow = '"sprites/graphics/industries/' + id + '_snow.png"' # don't use os.path.join here, this is for nml
        self.spritesets = spritesets
        self.spritelayouts = spritelayouts # by convention spritelayout is one word :P
        self.industry_layouts = industry_layouts

    def get_industry_layouts_as_tilelayouts(self):
        template = templates['industry_layout_tilelayouts.pynml']
        return template(industry=industry)

    def get_industry_layouts_as_property(self):
        template = templates['industry_layout_property.pynml']
        return template(industry=industry)

    def get_industry_layouts_as_graphic_switches(self):
        template = templates['industry_layout_graphics_switches.pynml']
        return template(industry=industry)


""" by convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix """

spritesets = []
spriteset_ground_bakery = Spriteset(
    id = 'grain_mill_spriteset_ground_bakery',
	type='cobble',
)
spritesets.append(spriteset_ground_bakery)
spriteset_ground_overlay_1 = Spriteset(
    id = 'grain_mill_spriteset_ground_overlay_1',
	sprites = [(10, 10, 64, 31, -31, 0)],
)
spritesets.append(spriteset_ground_overlay_1)
spriteset_ground_overlay_2 = Spriteset(
    id = 'grain_mill_spriteset_ground_overlay_2',
	sprites = [(80, 10, 64, 31, -31, 0)]
)
spritesets.append(spriteset_ground_overlay_2)
spriteset_ground_overlay_3 = Spriteset(
    id = 'grain_mill_spriteset_ground_overlay_3',
	sprites = [(150, 10, 64, 31, -31, 0)]
)
spritesets.append(spriteset_ground_overlay_3)
spriteset_ground_overlay_4 = Spriteset(
    id = 'grain_mill_spriteset_ground_overlay_4',
	sprites = [(220, 10, 64, 31, -31, 0)]
)
spritesets.append(spriteset_ground_overlay_4)

spriteset_1 = Spriteset(
    id = 'grain_mill_spriteset_1',
	sprites = [(10, 10, 64, 31, -31, 0)]
)
spritesets.append(spriteset_1)
spriteset_2 = Spriteset(
    id = 'grain_mill_spriteset_2',
	sprites = [(80, 10, 64, 31, -31, 0)]
)
spritesets.append(spriteset_2)
spriteset_3 = Spriteset(
    id = 'grain_mill_spriteset_3',
	sprites = [(150, 60, 64, 82, -31, -51)],
	zextent = 48 # optional zextent value, will default to 16 if this param is omitted
)
spritesets.append(spriteset_3)
spriteset_4 = Spriteset(
    id = 'grain_mill_spriteset_4',
	sprites = [(220, 60, 64, 82, -31, -51)],
	zextent = 48 # optional zextent value, will default to 16 if this param is omitted
)
spritesets.append(spriteset_4)

spriteset_windmill_anim = Spriteset(
    id = 'grain_mill_spriteset_windmill_anim',
	sprites = [(10, 200, 64, 82, -31, -52), (80, 200, 64, 82, -31, -52), (150, 200, 64, 82, -31, -52),
               (220, 200, 64, 82, -31, -52), (290, 200, 64, 82, -31, -52), (360, 200, 64, 82, -31, -52)],
	zextent = 24, # optional zextent value, will default to 16 if this param is omitted
	animation_rate = 1
)
spritesets.append(spriteset_windmill_anim)
spriteset_ground_windmill = Spriteset(
    id = 'grain_mill_spriteset_ground_windmill',
	type = 'empty',
	num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of animated frames (can get count from another spriteset if defined already)
)
spritesets.append(spriteset_ground_windmill)
spriteset_ground_overlay_windmill = Spriteset(
    id = 'grain_mill_spriteset_ground_overlay_windmill',
	sprites = [(10, 160, 64, 31, -31, 0)],
	num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of animated frames (can get count from another spriteset if defined already)
)
spritesets.append(spriteset_ground_overlay_windmill)


spritelayouts = []
spritelayout_brickbakery_1 = SpriteLayout(
    id = 'grain_mill_spritelayout_brickbakery_1',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_1,
    building_sprites = []
)
spritelayouts.append(spritelayout_brickbakery_1)
spritelayout_brickbakery_2 = SpriteLayout(
    id = 'grain_mill_spritelayout_brickbakery_2',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_2,
    building_sprites = []
)
spritelayouts.append(spritelayout_brickbakery_2)
spritelayout_brickbakery_3 = SpriteLayout(
    id = 'grain_mill_spritelayout_brickbakery_3',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_3,
    building_sprites = [spriteset_3]
)
spritelayouts.append(spritelayout_brickbakery_3)
spritelayout_brickbakery_4 = SpriteLayout(
    id = 'grain_mill_spritelayout_brickbakery_4',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_4,
    building_sprites = [spriteset_4]
)
spritelayouts.append(spritelayout_brickbakery_4)
spritelayout_windmill_anim = SpriteLayout(
    id = 'grain_mill_spritelayout_windmill_anim',
    ground_sprite = spriteset_ground_windmill,
    ground_overlay = spriteset_ground_overlay_windmill,
    building_sprites = [spriteset_windmill_anim]
)
spritelayouts.append(spritelayout_windmill_anim)


industry_layouts = []
industry_layout_1 = IndustryLayout(
    id = 'grain_mill_industry_layout_1',
    default_tile = 'grain_mill_spritelayout_brickbakery_3',
    spritelayouts = [(0, 0, 'grain_mill_spritelayout_brickbakery_3'),
            (0, 1, 'grain_mill_spritelayout_brickbakery_4'),
            (1, 0, 'grain_mill_spritelayout_brickbakery_1'),
            (1, 1, 'grain_mill_spritelayout_brickbakery_2')
    ]
)
industry_layouts.append(industry_layout_1)
industry_layout_2 = IndustryLayout(
    id = 'grain_mill_industry_layout_2',
    default_tile = 'grain_mill_spritelayout_brickbakery_3',
    spritelayouts = [(0, 0, 'grain_mill_spritelayout_brickbakery_3'),
             (0, 1, 'grain_mill_spritelayout_brickbakery_4'),
             (1, 0, 'grain_mill_spritelayout_brickbakery_3'),
             (1, 1, 'grain_mill_spritelayout_brickbakery_4'),
             (2, 0, 'grain_mill_spritelayout_brickbakery_1'),
             (2, 1, 'grain_mill_spritelayout_brickbakery_2')
    ]
)
industry_layouts.append(industry_layout_2)
industry_layout_3 = IndustryLayout(
    id = 'grain_mill_industry_layout_3',
    default_tile = 'grain_mill_spritelayout_brickbakery_3',
    spritelayouts = [(0, 0, 'grain_mill_spritelayout_brickbakery_3'),
             (0, 1, 'grain_mill_spritelayout_brickbakery_4'),
             (0, 2, 'grain_mill_spritelayout_brickbakery_3'),
             (0, 3, 'grain_mill_spritelayout_brickbakery_4'),
             (1, 0, 'grain_mill_spritelayout_brickbakery_1'),
             (1, 1, 'grain_mill_spritelayout_brickbakery_2'),
             (1, 2, 'grain_mill_spritelayout_brickbakery_1'),
             (1, 3, 'grain_mill_spritelayout_brickbakery_2')
    ]
)
industry_layouts.append(industry_layout_3)
industry_layout_4 = IndustryLayout(
    id = 'grain_mill_industry_layout_4',
    default_tile = 'grain_mill_spritelayout_windmill_anim',
    spritelayouts = [(0, 0, 'grain_mill_spritelayout_windmill_anim')]
)
industry_layouts.append(industry_layout_4)

industry_id = 'grain_mill'
industry = Industry(id=industry_id, spritesets=spritesets, spritelayouts=spritelayouts, industry_layouts=industry_layouts)

# compile a single final nml file for the grf
industry_template = industry_templates[industry_id + '.pypnml']

templated_pnml = industry_template(industry = industry)
# an ugly hack here because chameleon html escapes some characters
templated_pnml = '>'.join(templated_pnml.split('&gt;'))
templated_pnml = '<'.join(templated_pnml.split('&lt;'))
templated_pnml = '&'.join(templated_pnml.split('&amp;'))

pnml = codecs.open(os.path.join(currentdir,'sprites','nml','generated_pnml','grain_mill.pnml'), 'w','utf8')
pnml.write(templated_pnml)
pnml.close()
