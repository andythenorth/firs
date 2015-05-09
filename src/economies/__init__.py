registered_economies = []

# changing the order of items in economy list breaks savegames, don't do it.
# this could be solved by having the economy mapped to the parameter number it uses
# would be better to be able to alphabetise these for ease of maintaining
from economies import firs
firs.economy.register()

from economies import basic_temperate
basic_temperate.economy.register()

from economies import basic_arctic
basic_arctic.economy.register()

from economies import basic_tropic
basic_tropic.economy.register()

from economies import mistah_kurtz
mistah_kurtz.economy.register()
