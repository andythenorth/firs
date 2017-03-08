"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

print("[PYTHON] render pnml")

import codecs # used for writing files - more unicode friendly than standard open() module

import sys
import os
currentdir = os.curdir
src_path = os.path.join(currentdir, 'src')
from multiprocessing import Pool
from time import time

import global_constants
import utils
import firs
registered_cargos = firs.registered_cargos
registered_industries = firs.registered_industries
registered_economies = firs.registered_economies

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(src_path, 'templates'), format='text')
industry_templates = PageTemplateLoader(os.path.join(src_path, 'industries'), format='text')

generated_nml_path = os.path.join(firs.generated_files_path, 'nml')
if not os.path.exists(generated_nml_path):
    os.mkdir(generated_nml_path)

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

def render_header_item_nml(header_item):
    template = templates[header_item]
    templated_nml = utils.unescape_chameleon_output(template(registered_industries=registered_industries,
                                                              registered_cargos=registered_cargos,
                                                              economies=registered_economies,
                                                              global_constants=global_constants,
                                                              repo_vars=repo_vars,
                                                              utils=utils,
                                                              sys=sys))
    # save the results of templating
    # ! clunky split to get rid of the extension - temporary artefact of migrating away from CPP
    header_item_name = header_item.split('.')[0]
    nml_file_path = os.path.join(generated_nml_path, header_item_name + '.nml')
    nml = codecs.open(nml_file_path, 'w','utf8')
    nml.write(templated_nml)
    nml.close()

def render_industry_nml(industry):
    nml_file = codecs.open(os.path.join(generated_nml_path, industry.id + '.nml'), 'w','utf8')
    only_build_test_industry = repo_vars.get('test_industry', None)
    if not only_build_test_industry or only_build_test_industry == industry.id:
        result = industry.render_pnml()
    else:
        result = ''
    nml_file.write(result)
    nml_file.close()

def main():
    start = time()
    # ! extension is included due to partial migration from pypnaml to pynml; it should ideally be standard and concatenated within the repeat
    header_items = ['defines.pypnml', 'checks.pypnml','header.pynml','parameters.pynml','cargos.pynml']
    for header_item in header_items:
        render_header_item_nml(header_item)

    # multiprocessing was tried here and removed as it was empirically slower in testing (due to overhead of starting extra pythons probably)
    for industry in registered_industries:
        render_industry_nml(industry)

    template = templates['firs.pypnml']
    grf_nml = codecs.open(os.path.join(firs.generated_files_path, 'firs.pnml'),'w','utf8')
    grf_nml.write(utils.unescape_chameleon_output(template(registered_industries=registered_industries, global_constants=global_constants,
                                                  utils=utils, sys=sys)))
    grf_nml.close()
    # eh, how long does this take anyway?
    print(format((time() - start), '.2f')+'s')

if __name__ == '__main__':
    main()
