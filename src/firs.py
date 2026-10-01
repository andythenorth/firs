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

from cargo import CargoManager
import cargos
from economy import EconomyManager
import economies
from industry.manager import IndustryManager
import industries
from badges.badge import BadgeManager

def main():
    # exist_ok=True is used for case with parallel make (`make -j 2` or similar), don't fail with error if dir already exists
    os.makedirs(generated_files_path, exist_ok=True)

    # globals *within* this module so they can be accessed externally by other modules using iron_horse.foo
    globals()["economy_manager"] = EconomyManager()
    globals()["cargo_manager"] = CargoManager()
    globals()["industry_manager"] = IndustryManager()
    globals()["badge_manager"] = BadgeManager()

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
    economy_manager.post_init_actions()
    cargo_manager.post_init_actions()
    industry_manager.post_init_actions(cargo_manager, economy_manager)
