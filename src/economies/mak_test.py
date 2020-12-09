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
                            'clay', #Firs
                            'iron_ore', #Firs
                            'goods', #Firs
                            'wood', #Firs
                            'sand', #Firs
                            'stone', #Firs
                            'water',
                            'coke',
                            'food', #Firs
                            'plant_fibres', #Firs
                            'fruits',  #Firs
                            'grain', #Firs
                            'sugar_beet', #Firs
                            'livestock', #Firs
                            'wool',
                            'milk', #Firs
                            'oil', #Firs
                            'alcohol', #Firs
                            'chemicals', #Firs
                            'fish', #Firs
                            'steam',
                            'lumber', #Firs
                            'bauxite', #Firs
                            'recyclables', #Firs
                            'scrap_metal', #Firs
                            'metal',#Firs
                            'glass',
                            'paper',
                            'packaging', #Firs
                            'petrol', #Firs
                            'engineering_supplies', #firs
                            'farm_supplies',
                            'building_materials', #Firs
                            'electricity'])

