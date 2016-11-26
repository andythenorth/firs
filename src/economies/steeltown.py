from economy import Economy
economy = Economy(id = "STEELTOWN",
                  numeric_id = 5,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'copper',
                            'mail',
                            'chemicals',
                            'engineering_supplies',
                            'goods',
                            'farm_supplies',
                            'steel',
                            'oil',
                            'rubber',
                            'sand',
                            'food',
                            'petrol',
                            'manganese',
                            'nickel',
                            'stone',
                            'coal',
                            'iron_ore',
                            'pig_iron',
                            'coke',
                            'quicklime',
                            'building_materials',
                            'scrap_metal',
                            'alcohol',
                            'vehicle_parts',
                            'vehicles'])
