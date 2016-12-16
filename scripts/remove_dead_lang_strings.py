import os.path
currentdir = os.curdir

import codecs

import sys
sys.path.append(os.path.join('src')) # add to the module search path

# Sometimes strings are deprecated and need removing from all lang files
# this script removes dead strings - adjust the 'dead_strings' list to suit

dead_strings = ["STR_EXTRA_ALUMINUM_PLANT",
                "STR_EXTRA_BASIC_OXYGEN_FURNACE",
                "STR_EXTRA_BIOREFINERY",
                "STR_EXTRA_BREWERY",
                "STR_EXTRA_BREWERY_FRUIT_SUBSTR",
                "STR_EXTRA_BREWERY_GRAIN_SUBSTR",
                "STR_EXTRA_BREWERY_MAIZE_SUBSTR",
                "STR_EXTRA_BRICKWORKS",
                "STR_EXTRA_CEMENT_PLANT",
                "STR_EXTRA_CEMENT_PLANT_COAL_SUBSTR",
                "STR_EXTRA_CHEMICAL_PLANT",
                "STR_EXTRA_COKE_OVEN",
                "STR_EXTRA_COPPER_REFINERY",
                "STR_EXTRA_DAIRY",
                "STR_EXTRA_ELECTRIC_ARC_FURNACE",
                "STR_EXTRA_FACTORY",
                "STR_EXTRA_FERTILIZER_PLANT",
                "STR_EXTRA_FISHING_HARBOUR",
                "STR_EXTRA_FLOUR_MILL",
                "STR_EXTRA_FLOUR_MILL_GRAIN_SUBSTR",
                "STR_EXTRA_FOOD_PROCESSING_PLANT_NUTS_SUBSTR",
                "STR_EXTRA_FOOD_PROCESSING_PLANT_BEANS_SUBSTR",
                "STR_EXTRA_FOOD_PROCESSING_PLANT",
                "STR_EXTRA_FURNITURE_FACTORY",
                "STR_EXTRA_GALVANISING_PLANT",
                "STR_EXTRA_IRON_WORKS",
                "STR_EXTRA_LIME_KILN",
                "STR_EXTRA_MEAT_PACKER",
                "STR_EXTRA_PIPE_MILL",
                "STR_EXTRA_PLASTICS_PLANT_CHEMICALS_SUBSTR",
                "STR_EXTRA_PLASTICS_PLANT_PLANT_FIBRES_SUBSTR",
                "STR_EXTRA_SHIPYARD",
                "STR_EXTRA_SLAG_GRINDING_PLANT",
                "STR_EXTRA_STEELMILL",
                "STR_EXTRA_SUGAR_REFINERY",
                "STR_EXTRA_SUPPLY_YARD",
                "STR_EXTRA_SUPPLY_YARD_VEHICLES_SUBSTR",
                "STR_EXTRA_SUPPLY_YARD_BUILDING_MATERIALS_SUBSTR",
                "STR_EXTRA_TEXTILE_MILL",
                "STR_EXTRA_TEXTILE_MILL_PLANT_FIBRES_SUBSTR",
                "STR_EXTRA_TEXTILE_MILL_WOOL_SUBSTR",
                "STR_EXTRA_TYRE_PLANT",
                "STR_EXTRA_VEHICLE_FACTORY"]

def delete_string(dead_string):
    for filename in os.listdir(os.path.join('lang')):
        print(filename)
        if filename is not '.DS_Store':
            file = codecs.open(os.path.join('lang', filename),'r', encoding='utf-8')
            content = file.readlines()
            result = []

            for line in content:
                if dead_string not in line:
                    result.append(line)

            file = open(os.path.join('lang',filename),'w')
            for line in result:
                file.write(line)
            file.close

for dead_string in dead_strings:
    #pass
    delete_string(dead_string)
    #insert_property(filename)
