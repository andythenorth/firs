import codecs # used for writing files - more unicode friendly than standard open() module

import os.path
currentdir = os.curdir

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir,'sprites','nml','templates'))
industry_templates = PageTemplateLoader(os.path.join(currentdir,'sprites','nml','industries'))

class Industry(object):
    """Base class for all types of industry"""
    def __init__(self, name):
        self.name = name
        self.graphics_file = '"sprites/graphics/industries/' + name + '.png"' # don't use os.path.join here, this is for nml
        self.graphics_file_snow = '"sprites/graphics/industries/' + name + '_snow.png"' # don't use os.path.join here, this is for nml

industry_name = 'grain_mill'
industry = Industry(name=industry_name)

# compile a single final nml file for the grf
industry_template = industry_templates[industry_name + '.pypnml']

templated_pnml = industry_template(industry = industry)

pnml = codecs.open(os.path.join(currentdir,'sprites','nml','industries','grain_mill.pnml'), 'w','utf8')
pnml.write(templated_pnml)
pnml.close()
