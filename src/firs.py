"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

import os
currentdir = os.curdir
# add to the module search path
src_path = os.path.join(currentdir, 'src')

import global_constants

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)
if not os.path.exists(generated_files_path):
    os.mkdir(generated_files_path)

import cargos
registered_cargos = cargos.registered_cargos
import industries
registered_industries = industries.registered_industries
import economies
registered_economies = economies.registered_economies

# guard against mistakes with cargo ids in economies
known_cargo_ids = [cargo.id for cargo in registered_cargos]
for economy in registered_economies:
    for cargo_id in economy.cargos:
         if cargo_id not in known_cargo_ids:
            raise Exception(economy.id + ' economy includes cargo ID "' + cargo_id + '" which does not exist')

# cargo production and incompatibility lists have to be done after all industries, economies and cargos are registered
# this means they have to live here, which isn't ideal, but eh
industries_producing_cargo = {}
for cargo in registered_cargos:
    industries_producing_cargo[cargo.cargo_label] = []

for industry in registered_industries:
    produced = []
    for economy in registered_economies:
        for cargo_label, ratio in industry.get_prod_cargo_types(economy):
            produced.append(cargo_label)
    for cargo_label in set(produced):
        industries_producing_cargo[cargo_label].append(industry)

industries_accepting_cargo = {}
for cargo in registered_cargos:
    industries_accepting_cargo[cargo.cargo_label] = []

for industry in registered_industries:
    accepted = []
    for economy in registered_economies:
        for cargo_label in industry.get_accept_cargo_types(economy):
            accepted.append(cargo_label)
    for cargo_label in set(accepted):
        industries_accepting_cargo[cargo_label].append(industry)

incompatible_industries = {}
for industry in registered_industries:
    incompatible = []
    # special case supplies, pax, mail to exclude them (not useful in checks)
    excluded_cargos = ["ENSP", "FMSP", "PASS", "MAIL"]
    for cargo, prod_industries in industries_producing_cargo.items():
        if cargo not in excluded_cargos:
            if industry in prod_industries:
                incompatible.extend(industries_accepting_cargo[cargo])
    for cargo, accept_industries in industries_accepting_cargo.items():
        # special case supplies, pax, mail to exclude them (not useful in checks)
        if cargo not in excluded_cargos:
            if industry in accept_industries:
                incompatible.extend(industries_producing_cargo[cargo])
    incompatible_industries[industry] = set(incompatible)
