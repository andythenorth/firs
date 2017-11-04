from economy import Economy
economy = Economy(id = "STEELTOWN",
                  numeric_id = 5,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'cement',
                            'mail',
                            'quicklime',
                            'engineering_supplies',
                            'vehicles', # no goods?
                            'farm_supplies',
                            'steel',
                            'slag',
                            'limestone',
                            'sand',
                            'food',
                            'manganese',
                            'coal',
                            'iron_ore',
                            'pig_iron',
                            'coke',
                            'petrol',
                            'sulphur',
                            'scrap_metal',
                            'soda_ash',
                            'zinc',
                            'copper',
                            'rubber',
                            'pipe',
                            'salt',
                            'acid',
                            'chlorine',
                            'electrical_machines',
                            'vehicle_parts',
                            'vehicle_bodies'])
