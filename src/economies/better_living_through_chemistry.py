from economy import Economy
economy = Economy(id = "BETTER_LIVING_THROUGH_CHEMISTRY",
                  numeric_id = 2,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'acid',
                            'mail',
                            'alcohol',
                            'aluminia',
                            'aluminium',
                            'ammonia',
                            'cement',
                            'chlorine',
                            'clay',
                            'cleaning_agents',
                            'food', # must be in slot 11
                            'coffee',
                            'coal',
                            'coal_tar',
                            'copper',
                            'electrical_parts',
                            'engineering_supplies',
                            'ethylene',
                            'farm_supplies',
                            'fertiliser',
                            'fish',
                            'food_additives',
                            'furniture',
                            'glass',
                            'grain',
                            'iron_ore',
                            'limestone',
                            'livestock',
                            'lumber',
                            'lye',
                            'oil',
                            'oxygen',
                            'packaging',
                            'paints_and_coatings',
                            'petrol',
                            'pig_iron',
                            'plant_fibres', # should be cotton?
                            'plastics',
                            'quicklime',
                            'rubber', # includes synthetic rubber, export only
                            'salt',
                            'sand',
                            'soda_ash',
                            'steel_sections',
                            'steel_sheet',
                            'steel_wire_rod',
                            'sugar_beet',
                            #'sugar',
                            'sulphur',
                            'textiles',
                            'tinplate',
                            'vehicles',
                            'wood',
])
