registered_economies = []

# specify economies in the order that they should appear in parameter list in-game (and also in docs)
# economies have a numeric ID which maps parameter values and avoids breaking savegames when this list changes

from economies import basic_temperate
basic_temperate.economy.register()

from economies import basic_arctic
basic_arctic.economy.register()

from economies import basic_tropic
basic_tropic.economy.register()

from economies import mistah_kurtz
mistah_kurtz.economy.register()

from economies import firs
firs.economy.register()
