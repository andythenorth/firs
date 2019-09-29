from economy import Economy
economy = Economy(id = "BASIC_TROPIC",
                  numeric_id = 4,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'alcohol',
                            'mail',
                            'beans',
                            'chemicals',
                            'goods',
                            'coffee',
                            'copper',
                            'copper_ore',
                            'engineering_supplies',
                            'farm_supplies',
                            'food', # has to be out of order for compatibility
                            'fish',
                            'fruits',
                            'grain',
                            'livestock',
                            'nitrates',
                            'oil',
                            'wool'])
