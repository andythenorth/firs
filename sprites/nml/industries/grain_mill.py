import codecs # used for writing files - more unicode friendly than standard open() module

import os.path
currentdir = os.curdir

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir,'sprites','nml','templates'))
industry_templates = PageTemplateLoader(os.path.join(currentdir,'sprites','nml','industries'))

class Industry(object):
    """Base class for all types of industry"""
    def __init__(self, name, layouts):
        self.name = name
        self.graphics_file = '"sprites/graphics/industries/' + name + '.png"' # don't use os.path.join here, this is for nml
        self.graphics_file_snow = '"sprites/graphics/industries/' + name + '_snow.png"' # don't use os.path.join here, this is for nml
        self.layouts = layouts

class Layout(object):
    """Base class to hold industry layouts"""
    def __init__(self, id, default_tile, tiles):
        self.id = id
        self.default_tile = default_tile
        self.tiles = tiles

    def render(self, industry):
        template = templates['layout.pynml']
        return template(layout=self, industry=industry)

layout_1 = Layout('layout_1', default_tile = 'brickbakery_tile_3', tiles = (
    (0, 0, 'brickbakery_tile_4'),
    (1, 0, 'brickbakery_tile_1'),
    (1, 1, 'brickbakery_tile_2'),
))
layout_2 = Layout('layout_2', default_tile = 'brickbakery_tile_3', tiles = (
    (0, 0, 'brickbakery_tile_3'),
    (0, 1, 'brickbakery_tile_4'),
    (1, 0, 'brickbakery_tile_3'),
    (1, 1, 'brickbakery_tile_4'),
    (2, 0, 'brickbakery_tile_1'),
    (2, 1, 'brickbakery_tile_2'),

))
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

industry_name = 'grain_mill'
industry = Industry(name=industry_name, layouts=(layout_1, layout_2, layout_3))

# compile a single final nml file for the grf
industry_template = industry_templates[industry_name + '.pypnml']

templated_pnml = industry_template(industry = industry)

pnml = codecs.open(os.path.join(currentdir,'sprites','nml','industries','grain_mill.pnml'), 'w','utf8')
pnml.write(templated_pnml)
pnml.close()
