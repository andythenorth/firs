incompatible_grfs = []

class IncompatibleGRF(object):
    def __init__(self, grfid, grfname):
        self.grfid = grfid
        self.grfname = grfname
        print(self.grfid)

        incompatible_grfs.append(self)

# add incompatible grfs here (note that some properties are optional, allowing simple or extended checks)

IncompatibleGRF(r"Meo\81", "New Cargos")
IncompatibleGRF(r"Meo\82", "New Cargos Petrol + Tourists")
IncompatibleGRF(r"Meo\91", "ECS Town Vector")
IncompatibleGRF(r"Meo\92", "ECS Basic Vector")
IncompatibleGRF(r"Meo\93", "ECS Chemical Vector")
IncompatibleGRF(r"Meo\94", "ECS Machinery Vector")
IncompatibleGRF(r"Meo\95", "ECS Wood Vector")
IncompatibleGRF(r"Meo\96", "ECS Construction Vector")
IncompatibleGRF(r"Meo\97", "ECS Agricultural Vector")
IncompatibleGRF(r"Meo\98", "ECS Basic for Arctic")
IncompatibleGRF(r"Meo\99", "ECS Basic for Tropic")
IncompatibleGRF(r"Meo\9A", "ECS Machinery for Tropic")
IncompatibleGRF(r"Meo\9B", "ECS Construction Vector by Pikkabird")
IncompatibleGRF(r"Meo\9C", "ECS Chemical Vector II")

IncompatibleGRF("\\F1\\25\\00\\05", "FIRS v1")

IncompatibleGRF(r"SK\05\01", "Luukland Citybuilder")
IncompatibleGRF(r"JS\0A\02", "Luukland Citybuilder")
IncompatibleGRF(r"JS\0A\03", "Luukland Citybuilder")
IncompatibleGRF(r"JS\0A\04", "Luukland Citybuilder")
IncompatibleGRF(r"JS\0A\05", "Luukland Citybuilder")
IncompatibleGRF(r"EX\01\02", "Ex Citybuilder")
IncompatibleGRF(r"EX\01\03", "Ex Citybuilder")
IncompatibleGRF(r"DD\06\01", "UKRS Industries")
IncompatibleGRF(r"frMI", "Manual Industries")
IncompatibleGRF(r"SLTU", "Tourist Set")
IncompatibleGRF(r"SZ\13D", "Oil well decrease neutralizer")
IncompatibleGRF(r"EH\01\01", "Experts hard industries")
IncompatibleGRF(r"DD\06\03", "UKRS Brick Chain")
IncompatibleGRF(r"DD\06\02", "Pikka Basic Industries")
IncompatibleGRF(r"mb\08\00", "NewCargos by Michael Blunck")
IncompatibleGRF(r"AL\01\01", "Nearby Station Names")
