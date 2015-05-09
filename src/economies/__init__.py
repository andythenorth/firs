registered_economies = []

# keep these alphabetised for ease of maintaining
#from industries import aluminium_plant
#aluminium_plant.industry.register()

# changing the order of items in economy list breaks savegames, don't do it.
# this could be solved by having the economy mapped to the parameter number it uses
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
