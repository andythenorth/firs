from economy import Economy
economy = Economy(id="BASIC_ARCTIC",
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'bauxite',
                            'mail',
                            'chemicals',
                            'clay',
                            'goods',
                            'engineering_supplies',
                            'farm_supplies',
                            'fish',
                            'iron_ore',
                            'metal',
                            'food',
                            'oil',
                            'paper',
                            'petrol',
                            'rubber',
                            'sand',
                            'scrap_metal',
                            'vehicle_parts',
                            'vehicles',
                            'wood'])
