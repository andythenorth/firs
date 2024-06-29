# firs is imported, but main is not called in this module, this relies on firs already being present in the context
import firs

manufacturer_types = [
    "steelmaker",
    "automaker",
    "equipment_manufacturer",
    "chemicals_manufacturer",
    "building_materials_manufacturer",
]

def main():
    test_economy = firs.economy_manager.get_economy_by_id("STEELTOWN")
    print("CABBAGE manufacturers test_economy.detect_cargo_flow")
    print(test_economy.detect_cargo_flow("GOOD"))


class Manufacturer(object):
    # extend

    def __init__(self):
        pass
