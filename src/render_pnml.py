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
from multiprocessing import Pool
import subprocess

import global_constants as global_constants
import utils as utils
import firs
import cargos
from cargos import registered_cargos
import industries
from industries import registered_industries

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(src_path, 'templates'), format='text')
industry_templates = PageTemplateLoader(os.path.join(src_path, 'industries'), format='text')
header_item_templates = PageTemplateLoader(os.path.join(src_path, 'header_items'), format='text')

generated_pnml_path = os.path.join(firs.generated_files_path, 'pnml')
if not os.path.exists(generated_pnml_path):
    os.mkdir(generated_pnml_path)
generated_nml_path = os.path.join(firs.generated_files_path, 'nml')
if not os.path.exists(generated_nml_path):
    os.mkdir(generated_nml_path)

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)


def render_industry(industry):
    pnml_file = codecs.open(os.path.join(generated_pnml_path, industry.id + '.pnml'), 'w','utf8')
    only_build_test_industry = repo_vars.get('test_industry', None)
    if not only_build_test_industry or only_build_test_industry == industry.id:
        result = industry.render_pnml()
    else:
        result = ''
    pnml_file.write(result)
    pnml_file.close()

def main():
    header_items = ['checks','conditions','header','firs','parameters']
    for header_item in header_items:
        template = header_item_templates[header_item + '.pypnml']
        templated_pnml = utils.unescape_chameleon_output(template(registered_industries=registered_industries, global_constants=global_constants, utils=utils, sys=sys, generated_pnml_path=generated_pnml_path))
        # save the results of templating
        pnml_file_path = os.path.join(generated_pnml_path, header_item + '.pnml')
        pnml = codecs.open(pnml_file_path, 'w','utf8')
        pnml.write(templated_pnml)
        pnml.close()

    template = templates['defines.pypnml']
    templated_pnml = utils.unescape_chameleon_output(template(global_constants=global_constants))
    # save the results of templating
    pnml = codecs.open(os.path.join(generated_pnml_path, 'defines.pnml'), 'w','utf8')
    pnml.write(templated_pnml)
    pnml.close()

    template = templates['registered_cargos.pypnml']
    templated_pnml = utils.unescape_chameleon_output(template(registered_cargos=registered_cargos, global_constants=global_constants))
    # save the results of templating
    pnml = codecs.open(os.path.join(generated_pnml_path, 'registered_cargos.pnml'), 'w','utf8')
    pnml.write(templated_pnml)
    pnml.close()

    if repo_vars.get('no_mp', None) != 'False':
        utils.echo_message('Multiprocessing disabled: (use NO_MP=False to enable it)')
        for industry in industries.registered_industries:
            render_industry(industry)
    else:
        pool = Pool(processes=16) # 16 is an arbitrary amount that appears to be fast without blocking the system
        pool.map(render_industry, industries.registered_industries)
        pool.close()
        pool.join()

    # linker
    print "Linking"
    template = header_item_templates['firs.pypnml']
    firs_pnml = codecs.open(os.path.join(firs.generated_files_path, 'firs.pnml'), 'w','utf8')
    firs_pnml.write(utils.unescape_chameleon_output(template(registered_industries=registered_industries, global_constants=global_constants,
                                                utils=utils, sys=sys, generated_pnml_path=generated_pnml_path)))
    firs_pnml.close()


if __name__ == '__main__':
    main()
