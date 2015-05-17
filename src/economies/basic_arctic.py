from economy import Economy
economy = Economy(id="BASIC_ARCTIC",
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'alcohol',
                            'mail',
                            'chemicals',
                            'goods',
                            'clay',
                            'engineering_supplies',
                            'farm_supplies',
                            'fish',
                            'grain',
                            'iron_ore',
                            'food',
                            'livestock',
                            'manufacturing_supplies',
                            'oil',
                            'paper',
                            'petrol',
                            'wood'])
