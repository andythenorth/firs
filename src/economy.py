import importlib

import utils

# firs is imported, but main is not called in this module, this relies on firs already being present in the context
import firs

logger = utils.get_logger(__file__)

class Economy(object):
    """class to hold economies, this comment is pointless eh?"""

    def __init__(self, id, **kwargs):
        self.id = id
        self.numeric_id = kwargs.get("numeric_id")
        self.cargo_ids = kwargs.get("cargos")
        self.cargoflow_graph_tuning = kwargs.get("cargoflow_graph_tuning")

    def validate_economy_cargo_ids(self):
        for cargo_id in self.cargo_ids:
            if cargo_id not in firs.cargo_manager.cargo_ids:
                raise Exception(
                    self.id
                    + ' economy includes cargo ID "'
                    + cargo_id
                    + '" which does not exist'
                )

    @property
    def cargos(self):
        result = []
        for cargo in firs.cargo_manager:
            if cargo.id in self.cargo_ids:
                result.append(cargo)
        return result

    @property
    def industries(self):
        result = []
        for industry in firs.industry_manager:
            if industry.economy_variations[self.id].enabled:
                result.append(industry)
        return result

    # CABBAGE stopped calling this in August 2026, was experimental only, consider moving to branch
    def detect_cargo_flow(self, cargo_label):
        """
        Intended for use with GS Manufacturers.
        - excludes certain cargos
        - won't recurse past IndustryPrimary (including port-type industries)
        """

        result = {"upstream": [], "downstream": []}

        def is_primary_industry(industry):
            return any(
                cls.__name__ == "IndustryPrimary" for cls in industry.__class__.__mro__
            )

        excluded_cargos = ["ENSP", "FMSP", "PASS", "MAIL"]

        def find_upstream(cargo, visited_industries, visited_cargos):
            for industry in self.industries:
                if industry not in visited_industries:
                    produced_cargos = industry.get_produced_cargo_labels_by_economy(
                        self
                    )
                    if cargo in produced_cargos:
                        if industry not in result["upstream"]:
                            result["upstream"].append(industry)
                        visited_industries.add(industry)
                        if not is_primary_industry(industry):
                            for (
                                input_cargo
                            ) in industry.get_accepted_cargo_labels_by_economy(self):
                                if (
                                    input_cargo not in visited_cargos
                                ):  # Avoid immediate recursion on the same cargo
                                    visited_cargos.add(input_cargo)
                                    find_upstream(
                                        input_cargo, visited_industries, visited_cargos
                                    )

        def find_downstream(cargo, visited_industries, visited_cargos):
            for industry in self.industries:
                if industry not in visited_industries:
                    accepted_cargos = industry.get_accepted_cargo_labels_by_economy(
                        self
                    )
                    if cargo in accepted_cargos and cargo not in excluded_cargos:
                        if industry not in result["downstream"]:
                            result["downstream"].append(industry)
                        visited_industries.add(industry)
                        if not is_primary_industry(industry):
                            for (
                                output_cargo
                            ) in industry.get_produced_cargo_labels_by_economy(self):
                                if (
                                    output_cargo not in visited_cargos
                                ):  # Avoid immediate recursion on the same cargo
                                    visited_cargos.add(output_cargo)
                                    find_downstream(
                                        output_cargo, visited_industries, visited_cargos
                                    )

        visited_upstream_industries = set()
        visited_downstream_industries = set()
        visited_upstream_cargos = set()
        visited_downstream_cargos = set()

        find_upstream(cargo_label, visited_upstream_industries, visited_upstream_cargos)
        find_downstream(
            cargo_label, visited_downstream_industries, visited_downstream_cargos
        )

        return result

    def get_cargo_price_factors(self, registered_cargos):
        cargos_by_price_factor = {}

        for cargo in registered_cargos:
            if cargo.id in self.cargo_ids:
                cargos_by_price_factor.setdefault(cargo.price_factor, []).append(cargo)

        for price_factor, cargos in sorted(cargos_by_price_factor.items()):
            # no more than 2 cargos on the same price factor in this economy
            # this is purely to space out the payment charts a bit in game
            # if there are more than 2, manual adjustment is needed
            # ...although this can lead to unfortunate tail-chasing across economies
            if len(cargos) > 2:
                message = (
                    f"Economy {self.id}: price_factor {price_factor} has "
                    f"{len(cargos)} cargos: "
                    + ", ".join(cargo.id for cargo in cargos)
                )

                utils.echo_message(message, "warning")
                logger.warning(message)
            # log but don't warn if there are 2 cargos, this just aids manual adjustment
            if len(cargos) == 2:
                message = (
                    f"Economy {self.id}: price_factor {price_factor} has "
                    f"{len(cargos)} cargos: "
                    + ", ".join(cargo.id for cargo in cargos)
                )

                logger.info(message)


        return {
            cargo.id: cargo.price_factor
            for cargo in registered_cargos
            if cargo.id in self.cargo_ids
        }


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

    def post_init_actions(self):
        self.validate_economy_ids()
        self.validate_economies_cargo_ids()

    def validate_economy_ids(self):
        # guard, duplicate numeric IDs don't work :P
        seen = {}
        for economy in self:
            if economy.numeric_id in seen.keys():
                raise Exception(
                    "Economy "
                    + economy.id
                    + " has same numeric ID as economy "
                    + seen[economy.numeric_id].id
                )
            seen[economy.numeric_id] = economy

    def validate_economies_cargo_ids(self):
        for economy in self:
            economy.validate_economy_cargo_ids()

    def get_economy_by_id(self, id):
        for economy in self:
            if economy.id == id:
                return economy


