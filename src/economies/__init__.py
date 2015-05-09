registered_economies = []

# keep these alphabetised for ease of maintaining
#from industries import aluminium_plant
#aluminium_plant.industry.register()

# changing the order of items in econmy list breaks savegames, don't do it.
from economy import Economy
registered_economies = [Economy("FIRS"),
             Economy("BASIC_TEMPERATE"),
             Economy("BASIC_ARCTIC"),
             Economy("BASIC_TROPIC"),
             Economy("MISTAH_KURTZ")]


