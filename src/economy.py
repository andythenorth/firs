import utils
from economies import registered_economies


class Economy(object):
    """class to hold economies, this comment is pointless eh?"""

    def __init__(self, id, **kwargs):
        self.id = id
        self.numeric_id = kwargs.get("numeric_id")
        self.cargo_ids = kwargs.get("cargos")
        self.cargoflow_graph_tuning = kwargs.get("cargoflow_graph_tuning")
        self.biomes = []

    def register(self):
        # guard, duplicate numeric IDs don't work :P
        for economy in registered_economies:
            if self.numeric_id == economy.numeric_id:
                raise Exception(
                    "Economy "
                    + self.id
                    + " has same numeric ID as economy "
                    + economy.id
                )
        registered_economies.append(self)

    def add_biome(self, biome_id, **kwargs):
        self.biomes.append(Biome(biome_id, **kwargs))

    def forcibly_space_cargo_price_factors(self, registered_cargos):
        # check for overlapping price factors (and adjust if necessary) to ensure they're all unique per economy
        # prevents cargos overlapping on the payment curves chart in-game
        # designed to be called from template, easiest way to ensure registered_cargos is in scope and complete
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
