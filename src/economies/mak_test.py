from economy import Economy
economy = Economy(id = "MAK_TEST",
                  numeric_id = 0,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'coal',
                            'mail',
                            'coke',
                            'livestock',
                            'goods',
                            'engineering_supplies',
                            'farm_supplies',
                            'wood',
                            'fruits',  
                            'water',
                            'food',
                            'alcohol',
                            'chemicals',
                            'milk',
                            'fish',
                            'steam',
                            'electricity',
                            'lumber',
                            'recyclables',
                            'scrap_metal',
                            'paper'])

