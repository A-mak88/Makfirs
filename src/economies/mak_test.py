from economy import Economy
economy = Economy(id = "MAK_TEST",
                  numeric_id = 0,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers', #Firs
                            'coal', #Firs
                            'mail', #Firs
                            'electricity',
                            'water',
                            'goods', #Firs
                            'fish', #Firs
                            'steam',
                            'wood', #Firs
                            'grain', #Firs
                            'paper',
                            'food', #Firs
                            'plant_fibres', #Firs
                            'fruits',  #Firs
                            'sugar_beet', #Firs
                            'livestock', #Firs
                            'wool',
                            'clay', #Firs
                            'stone', #Firs
                            'sand',
                            'iron_ore', #Firs
                            'oil', #Firs
                            'peat', #Dunno
                            'recyclables', #Firs
                            'milk', #Firs
                            'plastics',
                            'textiles',
                            'cement',
                            'coke',
                            'chemicals', #Firs
                            #'bauxite', #Firs
                            'lumber', #Firs
                            'scrap_metal', #Firs
                            'metal',#Firs
                            'glass',
                            'alcohol', #Firs
                            'packaging', #Firs
                            'engineering_supplies', #firs
                            'farm_supplies',
                            'building_materials',
                            'petrol' #Firs
                            ])

