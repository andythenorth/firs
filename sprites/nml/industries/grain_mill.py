import codecs # used for writing files - more unicode friendly than standard open() module

import os.path
currentdir = os.curdir

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir,'sprites','nml','templates'), format='text')
industry_templates = PageTemplateLoader(os.path.join(currentdir,'sprites','nml','industries'), format='text')

class Tile(object):
    """Base class to hold industry tiles"""
    def __init__(self, id, ground_sprite, ground_overlay, building_sprites):
        self.id = id
        self.ground_sprite = ground_sprite
        self.ground_overlay = ground_overlay
        self.building_sprites = building_sprites

    def render(self, industry):
        template = templates['tile.pynml']
        return template(tile=self, industry=industry)


class Layout(object):
    """Base class to hold industry layouts"""
    def __init__(self, id, default_tile, tiles):
        self.id = id
        self.default_tile = default_tile
        self.tiles = tiles

    def render(self, industry):
        template = templates['layout.pynml']
        return template(layout=self, industry=industry)


class Industry(object):
    """Base class for all types of industry"""
    def __init__(self, name, tiles, layouts):
        self.name = name
        self.graphics_file = '"sprites/graphics/industries/' + name + '.png"' # don't use os.path.join here, this is for nml
        self.graphics_file_snow = '"sprites/graphics/industries/' + name + '_snow.png"' # don't use os.path.join here, this is for nml
        self.tiles = tiles
        self.layouts = layouts

tiles = []

brickbakery_tile_1 = Tile(
    id = 'brickbakery_tile_1',
    ground_sprite = 'grain_mill_spriteset_ground',
    ground_overlay = 'grain_mill_spriteset_ground_overlay_1',
    building_sprites = []
)
tiles.append(brickbakery_tile_1)
brickbakery_tile_2 = Tile(
    id = 'brickbakery_tile_2',
    ground_sprite = 'grain_mill_spriteset_ground',
    ground_overlay = 'grain_mill_spriteset_ground_overlay_2',
    building_sprites = []
)
tiles.append(brickbakery_tile_2)
brickbakery_tile_3 = Tile(
    id = 'brickbakery_tile_3',
    ground_sprite = 'grain_mill_spriteset_ground',
    ground_overlay = 'grain_mill_spriteset_ground_overlay_3',
    building_sprites = ['grain_mill_spriteset_3']
)
tiles.append(brickbakery_tile_3)
brickbakery_tile_4 = Tile(
    id = 'brickbakery_tile_4',
    ground_sprite = 'grain_mill_spriteset_ground',
    ground_overlay = 'grain_mill_spriteset_ground_overlay_4',
    building_sprites = ['grain_mill_spriteset_4']
)
tiles.append(brickbakery_tile_4)
"""
windmill_tile_anim = Tile(
    id = 'windmill_tile_anim',
    ground_sprite = 'windmill_spriteset_ground_windmill',
    ground_overlay = 'bar',
    building_sprites = ('ham','eggs')
)
"""
layouts = []

layout_1 = Layout('layout_1', default_tile = 'brickbakery_tile_3', tiles = (
    (0, 0, 'brickbakery_tile_3'),
    (0, 1, 'brickbakery_tile_4'),
    (1, 0, 'brickbakery_tile_1'),
    (1, 1, 'brickbakery_tile_2'),
))
layouts.append(layout_1)
layout_2 = Layout('layout_2', default_tile = 'brickbakery_tile_3', tiles = (
    (0, 0, 'brickbakery_tile_3'),
    (0, 1, 'brickbakery_tile_4'),
    (1, 0, 'brickbakery_tile_3'),
    (1, 1, 'brickbakery_tile_4'),
    (2, 0, 'brickbakery_tile_1'),
    (2, 1, 'brickbakery_tile_2'),

))
layouts.append(layout_2)
layout_3 = Layout('layout_3', default_tile = 'brickbakery_tile_3', tiles = (
    (0, 0, 'brickbakery_tile_3'),
    (0, 1, 'brickbakery_tile_4'),
    (0, 2, 'brickbakery_tile_3'),
    (0, 3, 'brickbakery_tile_4'),
    (1, 0, 'brickbakery_tile_1'),
    (1, 1, 'brickbakery_tile_2'),
    (1, 2, 'brickbakery_tile_1'),
    (1, 3, 'brickbakery_tile_2'),
))
layouts.append(layout_3)
layout_4 = Layout('layout_4', default_tile = 'windmill_tile_anim', tiles = (
    (0, 0, 'windmill_tile_anim'),
))
layouts.append(layout_4)

industry_name = 'grain_mill'
industry = Industry(name=industry_name, tiles=tiles, layouts=layouts)

# compile a single final nml file for the grf
industry_template = industry_templates[industry_name + '.pypnml']

templated_pnml = industry_template(industry = industry)
# an ugly hack here because chameleon html escapes some characters
templated_pnml = '>'.join(templated_pnml.split('&gt;'))
templated_pnml = '<'.join(templated_pnml.split('&lt;'))
templated_pnml = '&'.join(templated_pnml.split('&amp;'))

pnml = codecs.open(os.path.join(currentdir,'sprites','nml','generated_pnml','grain_mill.pnml'), 'w','utf8')
pnml.write(templated_pnml)
pnml.close()
