import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

property_to_delete = 'cargo_payment_list_colour'
#property_to_move = 'sea_capable'
#property_to_insert_after = 'gross_tonnage'
#line_to_insert = "            property_name = 'example',"

filenames = ['acid', 'alcohol', 'alloy_steel', 'aluminia', 'aluminium', 'ammonia', 'ammonium_nitrate', 'bauxite', 'beans', 'building_materials', 'carbon_black', 'carbon_steel', 'cassava', 'cast_iron', 'cement', 'chemicals', 'chlorine', 'chromite_ore', 'clay', 'cleaning_agents', 'coal_tar', 'coal', 'coffee', 'coke', 'copper_concentrate', 'copper_ore', 'copper', 'diamonds', 'edible_oil', 'electrical_parts', 'engineering_supplies', 'ethylene', 'explosives', 'farm_supplies', 'ferrochrome', 'fertiliser', 'fish', 'food_additives', 'food', 'formic_acid', 'fruits', 'furniture', 'glass', 'gold', 'goods', 'grain', 'hydrochloric_acid', 'iron_ore', 'kaolin', 'limestone', 'livestock', 'lumber', 'lye', 'mail', 'maize', 'manganese', 'metal', 'methanol', 'milk', 'naphtha', 'nickel', 'nitrates', 'nitrogen', 'nuts', 'oil', 'oxygen', 'packaging', 'paints_and_coatings', 'paper', 'passengers', 'peat', 'petrol', 'pharmaceuticals', 'phosphate', 'phosphoric_acid', 'pig_iron', 'pipe', 'plant_fibres', 'plastics', 'potash', 'propylene', 'pyrite_ore', 'quicklime', 'raw_latex', 'rebar', 'recyclables', 'rubber', 'salt', 'sand', 'scrap_metal', 'slag', 'soda_ash', 'stainless_steel', 'steel_sections', 'steel_sheet', 'steel_wire_rod', 'steel', 'stone', 'sugar_beet', 'sugarcane', 'sulphur', 'sulphuric_acid', 'textiles', 'tin', 'tinplate', 'tyres', 'urea', 'vehicle_bodies', 'vehicle_engines', 'vehicle_parts', 'vehicles', 'wood', 'wool', 'yarn', 'zinc']

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
