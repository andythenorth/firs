#!/usr/bin/env python

"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""
print "[PYTHON] render docs"

import codecs # used for writing files - more unicode friendly than standard open() module

import os.path
currentdir = os.curdir
docs_output_path = os.path.join(currentdir, 'docs')
src_path = os.path.join(currentdir, 'src')

import global_constants as global_constants
import utils as utils

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
docs_templates = PageTemplateLoader(os.path.join(currentdir, 'docs_src'), format='text')

from cargos import registered_cargos
from industries import registered_industries


template = docs_templates['test_docs.pytxt']
economy_schemas = {}
for economy in global_constants.economies:
    enabled_cargos = [cargo for cargo in registered_cargos if not cargo.economy_variations[economy].get('disabled')]
    enabled_industries = [industry for industry in registered_industries if industry.economy_variations[economy].enabled]
    economy_schemas[economy] = {'enabled_cargos':enabled_cargos, 'enabled_industries':enabled_industries}

templated_docs = template(registered_cargos=registered_cargos, registered_industries=registered_industries,
                          economy_schemas=economy_schemas, global_constants=global_constants)
# save the results of templating
docs = codecs.open(os.path.join(docs_output_path, 'test_docs.txt'), 'w','utf8')
docs.write(templated_docs)
docs.close()
