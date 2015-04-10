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
economy_schemas = {}

class DocHelper(object):
    # dirty class to help do some doc formatting
    def get_economy_name(self, economy):
        string_id = "STR_PARAM_VALUE_ECONOMIES_" + economy
        name_string = base_lang_strings.get(string_id, 'NO_NAME ' + economy)
        return name_string.split(' Economy')[0] # name strings contain 'economy', I don't want that in docs

    def get_cargo_name(self, cargo):
        # cargos don't store the name directly as a python attr, but in lang - so look it up in base_lang using string id
        name = cargo.type_name
        string_id = utils.unwrap_nml_string_declaration(name)
        result = base_lang_strings.get(string_id, 'NO NAME ' + str(name) + ' ' + cargo.id)
        #!! KILL THE SUGAR STUFF IN V2 - not needed, make it less complex, fewer LOC
        if cargo.id == 'sugar_beet':
            result = result + " / " + base_lang_strings['STR_CARGO_NAME_SUGARCANE']
        if cargo.id == 'sugarcane':
            result = result + " / " + base_lang_strings['STR_CARGO_NAME_SUGAR_BEET']
        return result

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
        return sorted(global_constants.economies, key=lambda economy: self.get_economy_name(economy))

    def get_registered_cargo_sorted_by_name(self):
        # cargos don't store the name as a python attr, but we often need to iterate over their names in A-Z order
        result = dict((self.get_cargo_name(cargo), cargo) for cargo in registered_cargos if cargo.id is not 'sugarcane')
        return sorted(result.items())

    def get_registered_industries_sorted_by_name(self):
        # industries don't store the name as a python attr, but we often need to iterate over their names in A-Z order
        result = dict((self.get_industry_name(industry), industry) for industry in registered_industries)
        return sorted(result.items())

    def get_economy_extra_info(self, economy):
        return base_lang_strings.get('ECONOMY_INFO_' + economy, '')

    def get_cargo_extra_info(self, cargo):
        return base_lang_strings.get('CARGO_INFO_' + cargo.id.upper(), '')

    def get_industry_extra_info(self, industry):
        return base_lang_strings.get('INDUSTRY_INFO_' + industry.id.upper(), '')

    def industry_find_industries_active_in_economy_for_cargo(self, cargo, economy, accept_or_produce):
        result = set()
        # hmm, pretty certain this could be changed to use industry.get_prod_cargo_types or accept equivalent
        # needs to pass economy, AND climate (from list defined in global_constants)
        # climate is required for those functions, and can be used (note in brackets) to show when a cargo is climate special-cased (only SGBT/SGCN are)
        # for non-special-cased cargos, don't bother showing any extra info about climates
        #!! KILL THE CLIMATE STUFF IN V2 - not needed, make it less complex, fewer LOC
        if cargo in economy_schemas[economy]['enabled_cargos']:
            for industry in economy_schemas[economy]['enabled_industries']:
                    for cargo_label in industry.get_property(accept_or_produce, economy):
                        if cargo.cargo_label[1:-1] == cargo_label:
                            result.add(industry)
        return result

    def industries_using_cargo(self, cargo):
        # segmented by economy
        result = {}
        for economy in self.get_economies_sorted_by_name():
            accepted_by = self.industry_find_industries_active_in_economy_for_cargo(cargo, economy, 'accept_cargo_types')
            produced_by = self.industry_find_industries_active_in_economy_for_cargo(cargo, economy, 'prod_cargo_types')
            accepted_by = sorted(accepted_by, key=self.get_industry_name)
            produced_by = sorted(produced_by, key=self.get_industry_name)
            if len(list(accepted_by) + list(produced_by)) > 0:
                result[economy] = {'accepted_by':accepted_by, 'produced_by':produced_by}
        return result


    def industry_find_cargos_active_in_economy_for_industry(self, industry, economy, accept_or_produce):
        result = []
        if industry in economy_schemas[economy]['enabled_industries']:
            for cargo_label in industry.get_property(accept_or_produce, economy):
                for cargo in economy_schemas[economy]['enabled_cargos']:
                    if cargo_label == cargo.cargo_label[1:-1]:
                        result.append(cargo)
        return set(result)


    def cargos_used_by_industry(self, industry):
        # segmented by economy
        result = {}
        for economy in self.get_economies_sorted_by_name():
            accept_cargo_types = self.industry_find_cargos_active_in_economy_for_industry(industry, economy, 'accept_cargo_types')
            prod_cargo_types = self.industry_find_cargos_active_in_economy_for_industry(industry, economy, 'prod_cargo_types')
            accept_cargo_types = sorted(accept_cargo_types, key=self.get_cargo_name)
            prod_cargo_types = sorted(prod_cargo_types, key=self.get_cargo_name)
            if len(list(accept_cargo_types) + list(prod_cargo_types)) > 0:
                result[economy] = {'accept_cargo_types':accept_cargo_types, 'prod_cargo_types':prod_cargo_types}
        return result


    def industry_unique_cargo_combinations(self, industry):
        result = {}
        for economy in self.get_economies_sorted_by_name():
            economy_cargos = []
            accept_cargo_types = self.industry_find_cargos_active_in_economy_for_industry(industry, economy, 'accept_cargo_types')
            prod_cargo_types = self.industry_find_cargos_active_in_economy_for_industry(industry, economy, 'prod_cargo_types')
            for cargo in accept_cargo_types:
                economy_cargos.append(cargo)
            for cargo in prod_cargo_types:
                economy_cargos.append(cargo)
            if len(economy_cargos) > 0:
                cargo_key = tuple(sorted(economy_cargos))
                result.setdefault(cargo_key, {'accept_cargo_types': accept_cargo_types, 'prod_cargo_types': prod_cargo_types})
                result[cargo_key].setdefault('economies',[]).append(economy)
                 # convenient to have items sorted
                result[cargo_key]['economies'] = sorted(result[cargo_key]['economies'], key=lambda economy: self.get_economy_name(economy))
        # return a list, sorted by economies (only need first economy entry in each list of economies)
        return sorted(result.values(), key = lambda combo: self.get_economy_name(combo['economies'][0]))


    def get_active_nav(self, doc_name, nav_link):
        return ('','active')[doc_name == nav_link]


def render_docs(doc_list, file_type, use_markdown=False):
    for doc_name in doc_list:
        template = docs_templates[doc_name + '.pt'] # .pt is the conventional extension for chameleon page templates
        doc = template(registered_cargos=registered_cargos, registered_industries=registered_industries,
                              economy_schemas=economy_schemas, global_constants=global_constants, repo_vars=repo_vars,
                              metadata=metadata, utils=utils, doc_helper=DocHelper(), doc_name=doc_name)
        if use_markdown:
            # the doc might be in markdown format, if so we need to render markdown to html, and wrap the result in some boilerplate html
            markdown_wrapper = docs_templates['markdown_wrapper.pt']
            doc = markdown_wrapper(content=markdown.markdown(doc), global_constants=global_constants, repo_vars=repo_vars,
                              metadata=metadata, utils=utils, doc_helper=DocHelper(), doc_name=doc_name)
        if file_type == 'html':
            subdir = 'html'
        else:
            subdir = ''
        # save the results of templating
        doc_file = codecs.open(os.path.join(docs_output_path, subdir, doc_name + '.' + file_type), 'w','utf8')
        doc_file.write(doc)
        doc_file.close()


def main():
    for economy in global_constants.economies:
        # !! KILL THE SUGARCANE STUFF IN V2 - not needed, make it less complex, fewer LOC
        enabled_cargos = [cargo for cargo in registered_cargos if not cargo.economy_variations[economy].get('disabled') and cargo.id is not 'sugarcane']
        enabled_industries = [industry for industry in registered_industries if industry.economy_variations[economy].enabled]
        economy_schemas[economy] = {'enabled_cargos':enabled_cargos, 'enabled_industries':enabled_industries}

    # render standard docs from a list
    html_docs = ['get_started', 'code_reference','economies', 'cargos', 'industries', 'translations']
    txt_docs = ['license', 'readme', 'test_docs']
    markdown_docs = ['changelog']

    render_docs(html_docs, 'html')
    render_docs(txt_docs, 'txt')
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(markdown_docs, 'txt')
    render_docs(markdown_docs, 'html', use_markdown=True)

if __name__ == '__main__':
    main()
