from economy import Economy
economy = Economy(id = "STEELTOWN",
                  numeric_id = 5,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'acid',
                            'mail',
                            'cement',
                            'chlorine',
                            'vehicles', # no goods?
                            'coal',
                            'coke',
                            'copper',
                            'electrical_machines',
                            'engineering_supplies',
                            'food',
                            'farm_supplies',
                            'iron_ore',
                            'limestone',
                            'manganese',
                            #'nickel',
                            'pig_iron',
                            'petrol',
                            'pipe',
                            'quicklime',
                            'rubber',
                            'salt',
                            'sand',
                            'scrap_metal',
                            'slag',
                            'soda_ash',
                            'steel',
                            'sulphur',
                            'vehicle_parts',
                            'vehicle_bodies',
                            'zinc'])
