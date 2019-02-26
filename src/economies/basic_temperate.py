from economy import Economy
economy = Economy(id = "BASIC_TEMPERATE",
                  numeric_id = 0,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'alcohol',
                            'mail',
                            'chemicals',
                            'coal',
                            'goods',
                            'engineering_supplies',
                            'farm_supplies',
                            'fish',
                            'fruits',
                            'iron_ore',
                            'food',
                            'kaolin',
                            'livestock',
                            'milk',
                            'sand',
                            'scrap_metal',
                            'steel'])
