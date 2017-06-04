import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

property_to_delete = 'station_list_colour'
#property_to_move = 'sea_capable'
#property_to_insert_after = 'gross_tonnage'
#line_to_insert = "            property_name = 'example',"

filenames = ['alcohol', 'alcohol', 'bauxite', 'beans', 'building_materials', 'cassava', 'cement', 'chemicals', 'clay', 'coal', 'coffee', 'coke', 'copper_ore', 'copper', 'diamonds', 'edible_oil', 'engineering_supplies', 'explosives', 'farm_supplies', 'fertiliser', 'fish', 'food', 'fruits', 'gold', 'goods', 'grain', 'iron_ore', 'kaolin', 'livestock', 'lumber', 'mail', 'maize', 'manganese', 'manufacturing_supplies', 'metal', 'milk', 'nickel', 'nitrates', 'nuts', 'oil', 'paper', 'passengers', 'peat', 'petrol', 'phosphate', 'pig_iron', 'pipe', 'plant_fibres', 'potash', 'pyrite_ore', 'quicklime', 'recyclables', 'rubber', 'sand', 'scrap_metal', 'slag', 'soda_ash', 'steel', 'stone', 'sugar_beet', 'sugar', 'sugarcane', 'sulphur', 'vehicle_bodies', 'vehicle_parts', 'vehicles', 'wood', 'wool', 'zinc']

def delete_property(filename):
    file = open(os.path.join('src','cargos',filename + '.py'),'r')
    content = file.readlines()

    for line in content:
        if property_to_delete in line:
            content.remove(line)

    file = open(os.path.join('src','cargos',filename + '.py'),'w')
    file.write(''.join(content))
    file.close

"""
def move_property(filename):
    file = open(os.path.join('src','vehicles',filename),'r')
    content = file.readlines()

    for line in content:
        if property_to_move in line:
            cut_line = line
    content.remove(cut_line)
    for line in content:
        if property_to_insert_after in line:
            line_to_insert_after = line
    insert_position = content.index(line_to_insert_after)
    content.insert(insert_position+1, cut_line)
    #print ''.join(content)

    file = open(os.path.join('src','vehicles',filename),'w')
    file.write(''.join(content))
    file.close

def insert_property(filename):
    file = open(os.path.join('src','vehicles',filename),'r')
    content = file.readlines()

    for line in content:
        if property_to_insert_after in line:
            line_to_insert_after = line
    insert_position = content.index(line_to_insert_after)
    content.insert(insert_position+1, line_to_insert)
    #print ''.join(content)

    file = open(os.path.join('src','vehicles',filename),'w')
    file.write(''.join(content))
    file.close
"""

for filename in filenames:
    delete_property(filename)
    #move_property(filename)
    #insert_property(filename)
