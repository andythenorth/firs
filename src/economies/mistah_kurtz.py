from economy import Economy
economy = Economy(id = "MISTAH_KURTZ",
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'alcohol',
                            'mail',
                            'building_materials',
                            'chemicals',
                            'goods',
                            'coffee',
                            'copper_ore',
                            'diamonds',
                            'engineering_supplies',
                            'farm_supplies',
                            'food',
                            'fish',
                            'fruits',
                            'grain',
                            'lumber',
                            'manufacturing_supplies',
                            'oil',
                            'plant_fibres',
                            'rubber',
                            'sugar',
                            'sugarcane',
                            'wood',
                            'clay', # adding to end, fix later
                            'coal',
                            'stone'])
