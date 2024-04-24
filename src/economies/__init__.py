import importlib

registered_economies = []

# specify economies in the order that they should appear in parameter list in-game (and also in docs)
# economies have a numeric ID which maps parameter values and avoids breaking savegames when this list changes
# !! ^ that doesn't appear to work, action 14 param doesn't seem to be able to abstract name value from name orde??

economy_module_names = [
    "basic_temperate",
    "basic_arctic",
    "basic_tropic",
    "steeltown",
    "in_a_hot_country",
]

package_name = "economies"
for economy_module_name in economy_module_names:
    economy_module = importlib.import_module("." + economy_module_name, package_name)
    economy_module.economy.register()
