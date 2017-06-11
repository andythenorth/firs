import os.path
currentdir = os.curdir

import codecs

# this script is a one-off to mass-remove ids from spritesets, they're deprecated
ignore_files = ['.DS_Store', '__init__.py', '__pycache__']

for filename in os.listdir(os.path.join('src','industries')):
    if filename not in ignore_files:
        print(filename)
        file = codecs.open(os.path.join('src','industries', filename),'r', encoding='utf-8')
        content = file.readlines()
        result = []
        id_exepected_in_next_line = False
        for line in content:
            if id_exepected_in_next_line:
                # contains id so don't copy this line to result
                id_exepected_in_next_line = False
            else:
                result.append(line)
            if 'add_spriteset' in line:
                id_exepected_in_next_line = True
        file_new = open(os.path.join('src','industries_new',filename),'w')
        for line in result:
            file_new.write(line)
        file_new.close