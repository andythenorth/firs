import importlib

import os

currentdir = os.curdir

import global_constants
import utils

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ["CHAMELEON_CACHE"] = chameleon_cache_path

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)

import cargos
import economies
import industries

registered_cargos = cargos.registered_cargos


class CargoManager(list):
    """
    It's convenient to have a structure for working with cargos.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def add_cargo(self, cargo_module_name):
        cargo_module = importlib.import_module(
            "." + cargo_module_name, package="cargos"
        )
        self.append(cargo_module.cargo)


class EconomyManager(list):
    """
    It's convenient to have a structure for working with economies.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def add_economy(self, economy_module_name):
        economy_module = importlib.import_module(
            "." + economy_module_name, package="economies"
        )
        self.append(economy_module.economy)


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

    def post_init_actions(self):
        self.provision_incompatible_industries()
        self.provision_industries_per_accepted_cargo()
        self.provision_industries_per_produced_cargo()
        self.validate_industry_ids()
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

    def provision_industries_per_accepted_cargo(self):
        # this can't be called until all industries, economies and cargos are registered
        for cargo in cargo_manager:
            self.industries_per_accepted_cargo[cargo.cargo_label] = []

        for industry in self:
            accepted = []
            for economy in economy_manager:
                for cargo_label in industry.get_accept_cargo_types(economy):
                    accepted.append(cargo_label)
            for cargo_label in set(accepted):
                self.industries_per_accepted_cargo[cargo_label].append(industry)

    def provision_industries_per_produced_cargo(self):
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
            for industry in industry_manager:
                if industry_id == industry.id:
                    found = True
                    break
            if found == False:
                utils.echo_message(
                    "Not found: " + industry_id + " from global_constants"
                )

    def validate_object_ids(self):
        # guard against (1) too many objects (2) invalid objects
        counter = 0
        for industry in industry_manager:
            for grf_object in industry.objects.values():
                grf_object.validate()
                counter += 1
                if counter > 64000:
                    raise BaseException(
                        "Object ID limit exceeded", counter, grf_object.id
                    )  # yair, try harder


def main():
    if not os.path.exists(generated_files_path):
        os.mkdir(generated_files_path)

    # globals *within* this module so they can be accessed externally by other modules using iron_horse.foo
    globals()["economy_manager"] = EconomyManager()
    globals()["cargo_manager"] = CargoManager()
    globals()["industry_manager"] = IndustryManager()

    # economies
    for economy_module_name in economies.economy_module_names:
        economy_manager.add_economy(economy_module_name)

    # cargos
    for cargo_module_name in cargos.cargo_module_names:
        cargo_manager.add_cargo(cargo_module_name)

    # industries
    for industry_module_name in industries.industry_module_names:
        industry_manager.add_industry(industry_module_name)

    # post init actions called after all industries, cargos and economies are inited
    industry_manager.post_init_actions()

    # guard against mistakes with cargo ids in economies
    # !! CABBAGE - should this be directly on the economy - surely it should validate itself?
    known_cargo_ids = [cargo.id for cargo in cargo_manager]
    cargo_label_id_mapping = {
        cargo.cargo_label: cargo.id for cargo in cargo_manager
    }
    for economy in economy_manager:
        for cargo_id in economy.cargo_ids:
            if cargo_id not in known_cargo_ids:
                raise Exception(
                    economy.id
                    + ' economy includes cargo ID "'
                    + cargo_id
                    + '" which does not exist'
                )
        # guard against industries defining accepted / produced cargos that aren't available in the economy
        # - prevents callback failures
        # - prevents possibly incorrect combinatorial production maths
        for industry in industry_manager:
            if industry.economy_variations[economy.id].enabled:
                for cargo_label in industry.get_accept_cargo_types(economy):
                    if cargo_label_id_mapping[cargo_label] not in economy.cargo_ids:
                        utils.echo_message(
                            " ".join(
                                [
                                    "In economy",
                                    economy.id,
                                    "industry",
                                    industry.id,
                                    "accepts",
                                    cargo_label,
                                    "which is not available for that economy",
                                ]
                            )
                        )
                for cargo_label, amount in industry.get_prod_cargo_types(economy):
                    if cargo_label_id_mapping[cargo_label] not in economy.cargo_ids:
                        utils.echo_message(
                            " ".join(
                                [
                                    "In economy",
                                    economy.id,
                                    "industry",
                                    industry.id,
                                    "produces",
                                    cargo_label,
                                    "which is not available for that economy",
                                ]
                            )
                        )
