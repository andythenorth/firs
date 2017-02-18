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
