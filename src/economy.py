import utils

# firs is imported, but main is not called in this module, this relies on firs already being present in the context
import firs


class Economy(object):
    """class to hold economies, this comment is pointless eh?"""

    def __init__(self, id, **kwargs):
        self.id = id
        self.numeric_id = kwargs.get("numeric_id")
        self.cargo_ids = kwargs.get("cargos")
        self.cargoflow_graph_tuning = kwargs.get("cargoflow_graph_tuning")
        self.biomes = []

    def add_biome(self, biome_id, **kwargs):
        self.biomes.append(Biome(biome_id, **kwargs))

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

    def forcibly_space_cargo_price_factors(self, registered_cargos):
        # check for overlapping price factors (and adjust if necessary) to ensure they're all unique per economy
        # prevents cargos overlapping on the payment curves chart in-game
        cargos_by_price_factor = []
        for cargo_id in self.cargo_ids:
            for cargo in registered_cargos:
                if cargo_id == cargo.id:
                    cargos_by_price_factor.append(cargo)
        cargos_by_price_factor = sorted(
            cargos_by_price_factor, key=lambda cargo: cargo.price_factor
        )

        result = {}
        for counter, cargo in enumerate(cargos_by_price_factor):
            if counter > 0:
                previous_cargo = cargos_by_price_factor[counter - 1]
                if result[previous_cargo.id] >= cargo.price_factor:
                    # if this is seen, usually just one cargo needs a different price factor set
                    # however be aware that it could produce ping-pong where changes for one economy trigger warnings in another
                    # also the message might cascade as it checks the *adjusted* prices, not the base
                    utils.echo_message(
                        "Cargo "
                        + cargo.id
                        + " has overlapping price_factor with "
                        + previous_cargo.id
                        + " in economy "
                        + self.id
                        + "; automatically adjusting (this may or not need changing).",
                        "info",
                    )
                    result[cargo.id] = result[previous_cargo.id] + 1
                else:
                    result[cargo.id] = cargo.price_factor
            else:
                result[cargo.id] = cargo.price_factor
        return result


class Biome(object):
    """
    class to hold definitions of map biomes, optionally used for cases like industry location rules
    they're not really 'biomes', but it's an easy way to avoid clash with 'regions' for other purposes
    """

    def __init__(self, id, **kwargs):
        self.id = id
        self.min_x_percent = kwargs["min_x_percent"]
        self.max_x_percent = kwargs["max_x_percent"]
        self.min_y_percent = kwargs["min_y_percent"]
        self.max_y_percent = kwargs["max_y_percent"]
