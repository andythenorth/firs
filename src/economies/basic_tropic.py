from economy import Economy
economy = Economy(id = "BASIC_TROPIC",
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'bauxite',
                            'mail',
                            'beans',
                            'chemicals',
                            'goods',
                            'coffee',
                            'engineering_supplies',
                            'farm_supplies',
                            'fruits',
                            'livestock',
                            'food',
                            'manufacturing_supplies',
                            'nitrates',
                            'oil',
                            'sugarcane',
                            'vehicle_parts',
                            'wool'])
