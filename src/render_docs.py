"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""
print("[PYTHON] render docs")

import codecs # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os
currentdir = os.curdir

docs_src = os.path.join(currentdir, 'src', 'docs_templates')
docs_output_path = os.path.join(currentdir, 'docs')
if os.path.exists(docs_output_path):
    shutil.rmtree(docs_output_path)
os.mkdir(docs_output_path)

shutil.copy(os.path.join(docs_src,'index.html'), docs_output_path)

static_dir_src = os.path.join(docs_src, 'html', 'static')
static_dir_dst = os.path.join(docs_output_path, 'html', 'static')
shutil.copytree(static_dir_src, static_dir_dst)

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
docs_templates = PageTemplateLoader(docs_src, format='text')

import global_constants as global_constants
import utils as utils
import markdown

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

# get the strings from base lang file so they can be used in docs
base_lang_strings = utils.parse_base_lang()

metadata = {}
metadata['dev_thread_url'] = 'http://www.tt-forums.net/viewtopic.php?t=41607'
metadata['repo_url'] = 'http://dev.openttdcoop.org/projects/firs/repository'
metadata['issue_tracker'] = 'http://dev.openttdcoop.org/projects/firs/issues'

import firs
# default sort for docs is by id
registered_cargos = sorted(firs.registered_cargos, key=lambda registered_cargos: registered_cargos.id)
registered_industries = sorted(firs.registered_industries, key=lambda registered_industries: registered_industries.id)
registered_economies = firs.registered_economies
economy_schemas = {}

class DocHelper(object):
    # dirty class to help do some doc formatting
    def get_economy_name(self, economy):
        string_id = "STR_PARAM_VALUE_ECONOMIES_" + economy.id
        name_string = base_lang_strings.get(string_id, 'NO_NAME ' + economy.id)
        return name_string.split(' Economy')[0] # name strings contain 'economy', I don't want that in docs

    def get_economy_name_char_safe(self, economy):
        # this uses _ not -, because it's also used in graphviz which chokes on -
        return self.get_economy_name(economy).replace(' ', '_').lower()

    def get_cargo_name(self, cargo):
        # cargos don't store the name directly as a python attr, but in lang - so look it up in base_lang using string id
        name = cargo.type_name
        string_id = utils.unwrap_nml_string_declaration(name)
        return base_lang_strings.get(string_id, 'NO NAME ' + str(name) + ' ' + cargo.id)

    def get_industry_name(self, industry, economy=None):
        # industries don't store the name directly as a python attr, but in lang - so look it up in base_lang using string id
        name = industry.get_property('name', economy)
        string_id = utils.unwrap_nml_string_declaration(name)
        if string_id not in base_lang_strings:
            utils.echo_message('Warning: string ' + string_id + ' missing for docs')
        return base_lang_strings.get(string_id, 'NO NAME ' + str(name) + ' ' + industry.id)

    def get_industry_all_name_strings(self, industry):
        # names can vary in each economy
        result = []
        for economy in economy_schemas:
            name = industry.get_property('name', economy)
            result.append(utils.unwrap_nml_string_declaration(name))
        return set(result)

    def get_industry_all_names(self, industry):
        # names can vary in each economy
        result = []
        for name_string in self.get_industry_all_name_strings(industry):
            result.append(base_lang_strings.get(name_string, 'NO NAME ' + name_string + ' ' + industry.id))
        return set(result)

    def get_economies_sorted_by_name(self):
        return sorted(registered_economies, key=lambda economy: self.get_economy_name(economy))

    def get_registered_cargo_sorted_by_name(self):
        # cargos don't store the name as a python attr, but we often need to iterate over their names in A-Z order
        result = dict((self.get_cargo_name(cargo), cargo) for cargo in registered_cargos)
        return sorted(result.items())

    def get_registered_industries_sorted_by_name(self):
        # industries don't store the name as a python attr, but we often need to iterate over their names in A-Z order
        result = dict((self.get_industry_name(industry), industry) for industry in registered_industries)
        return sorted(result.items())

    def get_economy_extra_info(self, economy):
        return base_lang_strings.get('ECONOMY_INFO_' + economy.id, '')

    def get_cargo_extra_info(self, cargo):
        return base_lang_strings.get('CARGO_INFO_' + cargo.id.upper(), '')

    def get_industry_extra_info(self, industry):
        return base_lang_strings.get('INDUSTRY_INFO_' + industry.id.upper(), '')

    def industry_is_unused(self, industry, economy):
        if industry in economy_schemas[economy]['enabled_industries']:
            return False
        else:
            return True

    def industries_producing_cargo(self, cargo, economy):
        result = set()
        if cargo in economy_schemas[economy]['enabled_cargos']:
            for industry in economy_schemas[economy]['enabled_industries']:
                cargo_list = industry.get_prod_cargo_types(economy)
                for cargo_label in cargo_list:
                    if cargo.cargo_label == cargo_label:
                        result.add(industry)
        result = sorted(result, key=self.get_industry_name)
        return result

    def industries_accepting_cargo(self, cargo, economy):
        result = set()
        if cargo in economy_schemas[economy]['enabled_cargos']:
            for industry in economy_schemas[economy]['enabled_industries']:
                cargo_list = industry.get_accept_cargo_types(economy)
                for cargo_label in cargo_list:
                    if cargo.cargo_label == cargo_label:
                        result.add(industry)
        result = sorted(result, key=self.get_industry_name)
        return result

    def cargo_is_unused_in_any_economy(self, cargo):
        result = 0
        for economy in self.get_economies_sorted_by_name():
            result += len(self.industries_accepting_cargo(cargo, economy))
            result += len(self.industries_producing_cargo(cargo, economy))
        if result == 0:
            return True
        else:
            return False

    def cargo_is_unused(self, cargo, economy):
        result = 0
        result += len(self.industries_accepting_cargo(cargo, economy))
        result += len(self.industries_producing_cargo(cargo, economy))
        if result == 0:
            return True
        else:
            return False

    def get_cargo_objects_from_labels(self, cargo_list):
        result = []
        for cargo_label in cargo_list:
            for cargo in registered_cargos:
                if cargo_label == cargo.cargo_label:
                    result.append(cargo)
        return result

    def cargos_produced_by_industry(self, industry, economy):
        result = self.get_cargo_objects_from_labels(industry.get_prod_cargo_types(economy))
        result = sorted(result, key=self.get_cargo_name)
        return result

    def cargos_accepted_by_industry(self, industry, economy):
        result = self.get_cargo_objects_from_labels(industry.get_accept_cargo_types(economy))
        result = sorted(result, key=self.get_cargo_name)
        return result

    def get_cargoflow_banned_cargos(self):
        return ['mail', 'passengers']

    def get_cargoflow_supply_cargos(self):
        return ['farm_supplies', 'engineering_supplies', 'manufacturing_supplies']

    def get_active_nav(self, doc_name, nav_link):
        return ('','active')[doc_name == nav_link]


def render_docs(doc_list, file_type, use_markdown=False):
    for doc_name in doc_list:
        template = docs_templates[doc_name + '.pt'] # .pt is the conventional extension for chameleon page templates
        doc = template(registered_cargos=registered_cargos,
                       registered_industries=registered_industries,
                       economies=registered_economies,
                       economy_schemas=economy_schemas,
                       global_constants=global_constants,
                       repo_vars=repo_vars,
                       metadata=metadata,
                       utils=utils,
                       doc_helper=DocHelper(),
                       doc_name=doc_name)
        if use_markdown:
            # the doc might be in markdown format, if so we need to render markdown to html, and wrap the result in some boilerplate html
            markdown_wrapper = docs_templates['markdown_wrapper.pt']
            doc = markdown_wrapper(content=markdown.markdown(doc),
                                   global_constants=global_constants,
                                   repo_vars=repo_vars,
                                   metadata=metadata,
                                   utils=utils,
                                   doc_helper=DocHelper(),
                                   doc_name=doc_name)
        if file_type == 'html':
            subdir = 'html'
        elif file_type == 'css':
            subdir = 'html' # don't put generated files into static dir, it's a bit confusing, dump them in with the html
        else:
            subdir = ''
        # save the results of templating
        doc_file = codecs.open(os.path.join(docs_output_path, subdir, doc_name + '.' + file_type), 'w','utf8')
        doc_file.write(doc)
        doc_file.close()


def main():
    for economy in registered_economies:
        enabled_cargos = [cargo for cargo in registered_cargos if cargo.id in economy.cargos]
        enabled_industries = [industry for industry in registered_industries if industry.economy_variations[economy.id].enabled]
        economy_schemas[economy] = {'enabled_cargos':enabled_cargos, 'enabled_industries':enabled_industries}

    # render standard docs from a list
    html_docs = ['get_started', 'code_reference','economies', 'cargos', 'industries', 'translations']
    txt_docs = ['license', 'readme', 'test_docs']
    markdown_docs = ['changelog']
    graph_docs = ['cargoflow']
    stylesheets = ['cargoflow_styles']

    render_docs(html_docs, 'html')
    render_docs(txt_docs, 'txt')
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(markdown_docs, 'txt')
    render_docs(markdown_docs, 'html', use_markdown=True)
    render_docs(graph_docs, 'dotall')
    render_docs(stylesheets, 'css')

if __name__ == '__main__':
    main()
