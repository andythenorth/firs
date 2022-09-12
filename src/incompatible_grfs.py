incompatible_grfs = []


class DwordGrfID(object):
    """
    grfids in game and bananas are presented as dwords, so it would be more convenient all round to use the dword
    however nml wants grfids as literals, so this class stores a dword, and converts it to an *nml* literal on demand
    """

    def __init__(self, grfid):
        self.grfid_as_dword = grfid  # keep the grfid around in case it's wanted for docs etc (as yet unknown)
        # split to bytes
        split = [
            self.grfid_as_dword[i : i + 2]
            for i in range(0, len(self.grfid_as_dword), 2)
        ]
        self.grfid = "\\" + "\\".join(
            split
        )  # note the leading '\' that nml requires (escaped as double \\ for python)


class LiteralGrfID(object):
    """
    store a literal grfid directly, which is convenient for nml
    but most grfids are found in the wild as dwords, in which case it's simpler to use the class for dword grfids instead ;)
    """

    def __init__(self, grfid):
        # grfid should be passed using r"literal", to avoid python interpreting \ chars as escapes
        self.grfid = grfid


class IncompatibleGRF(object):
    """ simple class to hold incompatible grfs, including optional properties for extended checks """

    def __init__(self, grfid, grfname):
        self._grfid = (
            grfid  # private var for this, we'll mangle it when called as a property
        )
        self.grfname = grfname
        incompatible_grfs.append(self)

    @property
    def grfid(self):
        return self._grfid.grfid


# add incompatible grfs here (note that some properties are optional, allowing simple or extended checks)
# IMPORTANT
# both forms of grfid string are supported: literal (per nfo) and dword (displayed in Bananas, in OpenTTD)

IncompatibleGRF(DwordGrfID("F1250005"), "FIRS v1")
IncompatibleGRF(DwordGrfID("F1250006"), "FIRS v2")
IncompatibleGRF(DwordGrfID("F1250007"), "FIRS v3")
IncompatibleGRF(LiteralGrfID(r"mb\07\00"), "Alpine Climate")
IncompatibleGRF(DwordGrfID("454E1501"), "Apollo Rocket Industry Set")
IncompatibleGRF(DwordGrfID("47470104"), "Australian Industries")
IncompatibleGRF(DwordGrfID("47472030"), "Australian Industries Set AuzIn")
IncompatibleGRF(DwordGrfID("47472031"), "Australian Industry AuzInd2")
IncompatibleGRF(DwordGrfID("47476001"), "Australian Industry AuzInd6")
IncompatibleGRF(DwordGrfID("42580002"), "BSPI")
IncompatibleGRF(DwordGrfID("4D490209"), "CZTR Engines-Diesel")
IncompatibleGRF(DwordGrfID("4D490208"), "CZTR Engines-Electric")
IncompatibleGRF(DwordGrfID("4D490210"), "CZTR Engines-EMU")
IncompatibleGRF(DwordGrfID("4D490207"), "CZTR Engines-Steam")
IncompatibleGRF(LiteralGrfID(r"Meo\97"), "ECS Agricultural Vector")
IncompatibleGRF(LiteralGrfID(r"Meo\98"), "ECS Basic for Arctic")
IncompatibleGRF(LiteralGrfID(r"Meo\99"), "ECS Basic for Tropic")
IncompatibleGRF(LiteralGrfID(r"Meo\92"), "ECS Basic Vector")
IncompatibleGRF(DwordGrfID("4d656f9f"), "ECS Basic Vector II")
IncompatibleGRF(LiteralGrfID(r"Meo\93"), "ECS Chemical Vector")
IncompatibleGRF(LiteralGrfID(r"Meo\9C"), "ECS Chemical Vector II")
IncompatibleGRF(LiteralGrfID(r"Meo\9B"), "ECS Construction Vector by Pikkabird")
IncompatibleGRF(LiteralGrfID(r"Meo\96"), "ECS Construction Vector")
IncompatibleGRF(LiteralGrfID(r"Meo\9A"), "ECS Machinery for Tropic")
IncompatibleGRF(LiteralGrfID(r"Meo\94"), "ECS Machinery Vector")
IncompatibleGRF(LiteralGrfID(r"Meo\91"), "ECS Town Vector")
IncompatibleGRF(LiteralGrfID(r"Meo\95"), "ECS Wood Vector")
IncompatibleGRF(LiteralGrfID(r"EX\01\02"), "Ex Citybuilder")
IncompatibleGRF(LiteralGrfID(r"EX\01\03"), "Ex Citybuilder")
IncompatibleGRF(LiteralGrfID(r"EH\01\01"), "Experts hard industries")
IncompatibleGRF(DwordGrfID("4a448807"), "Extreme Industry Set")
IncompatibleGRF(DwordGrfID("52530101"), "Improved Oil Rig Layout")
IncompatibleGRF(DwordGrfID("54540401"), "Improved Town Industries")
IncompatibleGRF(LiteralGrfID(r"TT20"), "Industries of the Caribbean")
IncompatibleGRF(LiteralGrfID(r"TT21"), "Lumberjack Industries")
IncompatibleGRF(LiteralGrfID(r"SK\05\01"), "Luukland Citybuilder")
IncompatibleGRF(LiteralGrfID(r"JS\0A\02"), "Luukland Citybuilder")
IncompatibleGRF(LiteralGrfID(r"JS\0A\03"), "Luukland Citybuilder")
IncompatibleGRF(LiteralGrfID(r"JS\0A\04"), "Luukland Citybuilder")
IncompatibleGRF(LiteralGrfID(r"JS\0A\05"), "Luukland Citybuilder")
IncompatibleGRF(LiteralGrfID(r"frMI"), "Manual Industries")
IncompatibleGRF(LiteralGrfID(r"TT22"), "Minimalist Industries")
IncompatibleGRF(LiteralGrfID(r"AL\01\01"), "Nearby Station Names")
IncompatibleGRF(LiteralGrfID(r"Meo\81"), "New Cargos")
IncompatibleGRF(LiteralGrfID(r"Meo\82"), "New Cargos Petrol + Tourists")
IncompatibleGRF(LiteralGrfID(r"mb\08\00"), "NewCargos by Michael Blunck")
IncompatibleGRF(DwordGrfID("4E4D1113"), "North American Industry Set")
IncompatibleGRF(LiteralGrfID(r"EN\31\01"), "North Korean Industry Set v1")
IncompatibleGRF(LiteralGrfID(r"EN\31\03"), "North Korean Industry Set v1 Fix")
IncompatibleGRF(LiteralGrfID(r"EN\31\02"), "North Korean Industry Set v2")
IncompatibleGRF(LiteralGrfID(r"SZ\13D"), "Oil well decrease neutralizer")
IncompatibleGRF(LiteralGrfID(r"OG+3"), "OpenGFX+ Industries")
IncompatibleGRF(LiteralGrfID(r"DD\06\02"), "Pikka Basic Industries")
IncompatibleGRF(DwordGrfID("31ff0503"), "Stock Piled industries 1.1")
IncompatibleGRF(DwordGrfID("31ff0504"), "Stock Piled industries 1.2")
IncompatibleGRF(DwordGrfID("31ff0505"), "Stock Piled industries 1.3")
IncompatibleGRF(LiteralGrfID(r"SLTU"), "Tourist Set")
IncompatibleGRF(LiteralGrfID(r"DD\06\03"), "UKRS Brick Chain")
IncompatibleGRF(LiteralGrfID(r"DD\06\01"), "UKRS Industries")
IncompatibleGRF(DwordGrfID("42580002"), "Vanilla Industries in Stockpiling mode")
