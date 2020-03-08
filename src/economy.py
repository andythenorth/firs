from economies import registered_economies

class Economy(object):
    """ class to hold economies, this comment is pointless eh? """
    def __init__(self, id, **kwargs):
        self.id = id
        self.numeric_id = kwargs.get('numeric_id')
        self.cargos = kwargs.get('cargos')

    def register(self):
        # guard, duplicate numeric IDs don't work :P
        for economy in registered_economies:
            if self.numeric_id == economy.numeric_id:
                raise Exception("Economy " + self.id + " has same numeric ID as economy " + economy.id)
        registered_economies.append(self)

    def forcibly_space_cargo_price_factors(self, registered_cargos):
        # registered_cargos has to be passed, can't rely on importing it, couldn't be bothered to find and fix why
        # means this might get calculated repeatedly but eh
        result = []
        for cargo_id in self.cargos:
            for cargo in registered_cargos:
                if cargo_id == cargo.id:
                    # store a 2 tuple eh
                    result.append((cargo.id, int(cargo.price_factor)))
        result = sorted(result, key=lambda c: c[1])
        return result
