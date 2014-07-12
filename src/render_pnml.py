"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

print "[PYTHON] render pnml"

import codecs # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import global_constants
import os
currentdir = os.curdir
src_path = os.path.join(currentdir, 'src')

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

# set output path for generated_pnml, clean it if it exists, create it if it doesn't
pnml_output_path = os.path.join(currentdir, 'generated_pnml')
if os.path.exists(pnml_output_path):
    shutil.rmtree(pnml_output_path)
os.mkdir(pnml_output_path)

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(src_path, 'templates'), format='text')
industry_templates = PageTemplateLoader(os.path.join(src_path, 'industries'), format='text')
header_item_templates = PageTemplateLoader(os.path.join(src_path, 'header_items'), format='text')

import global_constants as global_constants
import utils as utils
import firs
import cargos
from cargos import registered_cargos
import industries
from industries import registered_industries


def render_industry_nml(industry):
    # save the results of templating
    pnml_file = codecs.open(os.path.join(pnml_output_path, industry.id + '.pnml'), 'w','utf8')
    pnml_file.write(industry.render_pnml())
    pnml_file.close()


def main():
    header_items = ['checks','conditions','header','firs','parameters']
    for header_item in header_items:
        template = header_item_templates[header_item + '.pypnml']
        templated_pnml = utils.unescape_chameleon_output(template(registered_industries=registered_industries, global_constants=global_constants, utils=utils, sys=sys))
        # save the results of templating
        pnml = codecs.open(os.path.join(pnml_output_path, header_item + '.pnml'), 'w','utf8')
        pnml.write(templated_pnml)
        pnml.close()

    template = templates['registered_cargos.pypnml']
    templated_pnml = utils.unescape_chameleon_output(template(registered_cargos=registered_cargos, global_constants=global_constants))
    # save the results of templating
    pnml = codecs.open(os.path.join(pnml_output_path, 'registered_cargos.pnml'), 'w','utf8')
    pnml.write(templated_pnml)
    pnml.close()

    for industry in industries.registered_industries:
        render_industry_nml(industry)

if __name__ == '__main__':
    main()
