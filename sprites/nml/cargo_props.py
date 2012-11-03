from firs import unescape_chameleon_output as unescape_chameleon_output

import codecs # used for writing files - more unicode friendly than standard open() module

import os.path
currentdir = os.curdir

import global_constants as global_constants

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
cargo_templates = PageTemplateLoader(os.path.join(currentdir,'sprites','nml'), format='text')

templated_pnml = unescape_chameleon_output(cargo_templates['cargo_props.pypnml']())

# save the results of templating
pnml = codecs.open(os.path.join(currentdir,'sprites','nml','generated_pnml', 'cargo_props.pnml'), 'w','utf8')
pnml.write(templated_pnml)
pnml.close()
