import os.path
currentdir = os.curdir

import codecs

import sys
sys.path.append(os.path.join('src')) # add to the module search path

# Sometimes strings are deprecated and need removing from all lang files
# this script removes dead strings - adjust the 'dead_strings' list to suit

# never leave empty strings or strings with only spaces in this list, that will strip everything from a lang file
dead_strings = ["STR_GRF_NAME", "STR_EMPTY"]

def delete_string(dead_string):
    for filename in os.listdir(os.path.join('src','lang')):
        print(filename)
        if filename is not '.DS_Store':
            file = codecs.open(os.path.join('src','lang', filename),'r', encoding='utf-8')
            content = file.readlines()
            result = []

            for line in content:
                if dead_string not in line:
                    result.append(line)

            file = open(os.path.join('src','lang',filename),'w')
            for line in result:
                file.write(line)
            file.close

for dead_string in dead_strings:
    #pass
    delete_string(dead_string)
    #insert_property(filename)
