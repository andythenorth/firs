from economy import Economy
economy = Economy(id = "BASIC_TEMPERATE",
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'alcohol',
                            'mail',
                            'chemicals',
                            'clay',
                            'goods',
                            'coal',
                            'engineering_supplies',
                            'farm_supplies',
                            'fish',
                            'fruits',
                            'food',
                            'iron_ore',
                            'livestock',
                            'manufacturing_supplies',
                            'metal',
                            'milk',
                            'sand',
                            'scrap_metal'])
