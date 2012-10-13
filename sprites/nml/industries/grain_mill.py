import codecs # used for writing files - more unicode friendly than standard open() module

import os.path
currentdir = os.curdir

industry_name = 'grain_mill'

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir,'sprites','nml','templates'))
industry_templates = PageTemplateLoader(os.path.join(currentdir,'sprites','nml','industries'))

# compile a single final nml file for the grf
industry_template = industry_templates[industry_name + '.pypnml']

templated_pnml = industry_template(industry_name = industry_name)

pnml = codecs.open(os.path.join(currentdir,'sprites','nml','industries','grain_mill.pnml'), 'w','utf8')
pnml.write(templated_pnml)
pnml.close()
