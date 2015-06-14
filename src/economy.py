from economies import registered_economies

class Economy(object):
    """ class to hold economies, this comment is pointless eh? """
    def __init__(self, id, **kwargs):
        self.id = id
        self.cargos = kwargs.get('cargos')

    def register(self):
        registered_economies.append(self)
