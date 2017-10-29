from economy import Economy
economy = Economy(id = "BRINE",
                  numeric_id = 6,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'vehicles',
                            'vehicle_bodies',
                            'vehicle_parts',
                            'engineering_supplies',
                            'goods',
                            'farm_supplies',
                            'rubber',
                            'sulphur',
                            'scrap_metal',
                            'sand',
                            'food',
                            'soda_ash',
                            'oil',
                            'chemicals',
                            'copper'])

