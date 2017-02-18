import os.path
currentdir = os.curdir

import codecs

import sys
sys.path.append(os.path.join('src')) # add to the module search path

# Sometimes strings are deprecated and need removing from all lang files
# this script removes dead strings - adjust the 'dead_strings' list to suit

# never leave empty strings or strings with only spaces in this list, that will strip everything from a lang file
dead_strings = ["STR_EXTRA_GLASS_WORKS",
                "STR_EXTRA_LUMBER_YARD",
                "STR_EXTRA_MACHINE_SHOP",
                "STR_EXTRA_METAL_WORKSHOP",
                "STR_EXTRA_OIL_REFINERY",
                "STR_EXTRA_RECYCLING_PLANT",
                "STR_EXTRA_PAPER_MILL",
                "STR_EXTRA_SMITHY_FORGE",
                "STR_EXTRA_SAWMILL",
                "STR_EXTRA_MAX_PRODUCTION",
                "STR_EXTRA_PYRITE_SMELTER",
                "STR_EXTRA_PLASTICS_PLANT",
                "STR_EXTRA_METAL_FABRICATION_PLANT"]

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
