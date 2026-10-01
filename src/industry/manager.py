"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

import importlib

import global_constants
import utils

class IndustryManager(list):
    """
    It's convenient to have a structure for working with industries.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def __init__(self):
        self.incompatible_industries = {}
        self.industries_per_accepted_cargo = {}
        self.industries_per_produced_cargo = {}

    def add_industry(self, industry_module_name):
        industry_module = importlib.import_module(
            "." + industry_module_name, package="industries"
        )
        industry_module.industry.validate()
        self.append(industry_module.industry)

    def post_init_actions(self, cargo_manager, economy_manager):
        self.provision_incompatible_industries()
        self.provision_industries_per_accepted_cargo(cargo_manager, economy_manager)
        self.provision_industries_per_produced_cargo(cargo_manager, economy_manager)
        self.validate_industry_ids()
        self.validate_industry_tile_ids()
        self.validate_object_ids()

    def get_industry_by_type(self, industry_id):
        # be aware that this shouldn't be called before all industries have been initialised
        for industry in self:
            if industry.id == industry_id:
                return industry
        # if none found, that's an error, don't handle the error, just blow up

    def provision_incompatible_industries(self):
        # this can't be called until all industries, economies and cargos are registered
        # this was tested as expensive if called repeatedly (9s vs 2s when cached), so it needs to to be called once during post init and cached
        for industry in self:
            incompatible = []
            # special case supplies, pax, mail to exclude them (not useful in checks)
            excluded_cargos = ["ENSP", "FMSP", "PASS", "MAIL"]
            for cargo, prod_industries in self.industries_per_produced_cargo.items():
                if cargo not in excluded_cargos:
                    if industry in prod_industries:
                        incompatible.extend(self.industries_per_accepted_cargo[cargo])
            for cargo, accept_industries in self.industries_per_accepted_cargo.items():
                # special case supplies, pax, mail to exclude them (not useful in checks)
                if cargo not in excluded_cargos:
                    if industry in accept_industries:
                        incompatible.extend(self.industries_per_produced_cargo[cargo])
            self.incompatible_industries[industry] = set(incompatible)

    def provision_industries_per_accepted_cargo(self, cargo_manager, economy_manager):
        # this can't be called until all industries, economies and cargos are registered
        for cargo in cargo_manager:
            self.industries_per_accepted_cargo[cargo.cargo_label] = []

        for industry in self:
            accepted = []
            for economy in economy_manager:
                for cargo_label in industry.get_accepted_cargo_labels_by_economy(
                    economy
                ):
                    accepted.append(cargo_label)
            for cargo_label in set(accepted):
                self.industries_per_accepted_cargo[cargo_label].append(industry)

    def provision_industries_per_produced_cargo(self, cargo_manager, economy_manager):
        # this can't be called until all industries, economies and cargos are registered
        for cargo in cargo_manager:
            self.industries_per_produced_cargo[cargo.cargo_label] = []

        for industry in self:
            produced = []
            for economy in economy_manager:
                for cargo_label, ratio in industry.get_prod_cargo_types(economy):
                    produced.append(cargo_label)
            for cargo_label in set(produced):
                self.industries_per_produced_cargo[cargo_label].append(industry)

    def validate_industry_ids(self):
        # guard against unused / wasted industry IDs
        # n.b. sometimes there are valid unused IDs during development
        # note also that tile ID should be cleaned up if removing an industry id
        for (
            industry_id,
            industry_numeric_id,
        ) in global_constants.industry_numeric_ids.items():
            found = False
            for industry in self:
                if industry_id == industry.id:
                    found = True
                    break
            if found == False:
                utils.echo_message(
                    "Not found: " + industry_id + " from global_constants"
                )

    def validate_industry_tile_ids(self):
        # guard against unused / wasted tile IDs
        # n.b. sometimes there are valid unused IDs during development
        for (
            tile_id,
            tile_numeric_id,
        ) in global_constants.tile_numeric_ids.items():
            found = False
            for industry in self:
                for tile in industry.tiles:
                    if tile_id == tile.id:
                        found = True
                        break
            if found == False:
                utils.echo_message(
                    "Tile ID not used: " + tile_id + " from global_constants"
                )

    def validate_object_ids(self):
        # guard against (1) too many objects (2) invalid objects
        counter = 0
        for industry in self:
            for grf_object in industry.objects.values():
                grf_object.validate()
                counter += 1
                if counter > 64000:
                    raise BaseException(
                        "Object ID limit exceeded", counter, grf_object.id
                    )  # yair, try harder

