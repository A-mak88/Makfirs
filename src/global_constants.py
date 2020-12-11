# Definition of numeric IDs for industries
industry_numeric_ids = dict(sawmill = 0,
                            forest  = 1,
                            lumber_yard = 2,
                            paper_mill = 3,
                            supply_yard = 4,
                            arable_farm = 5,
                            orchard_piggery = 6,
                            sheep_farm = 7,
                            coal_mine = 8,
                            fish_farm = 9,
                            fishing_harbour = 10,
                            fishing_grounds = 11,
                            stockyard = 12,
                            textile_mill = 13,
                            brewery = 14,
                            bulk_terminal = 15,
                            junk_yard = 16,
                            dairy_farm = 17,
                            dairy = 18,
                            recycling_plant = 19,
                            recycling_depot = 20,
                            hotel = 21,
                            general_store = 22,
                            power_plant = 23,
                            coke_oven = 24,
                            coal_pit = 25, 
                            basic_oxygen_furnace = 26
                            #!steel_mill = 2,
                            #cryo_plant = 3,
                            #!iron_ore_mine = 4,
                            #!peatlands = 5,
                            #!smithy_forge = 6,
                            #!blast_furnace = 7,
                            #!aluminium_plant = 8,
                            #!metal_workshop = 9,
                            #!quarry = 10,= 11,
                            #!furniture_factory = 13,
                            #!oil_wells = 15,
                            #!oil_rig = 16,
                            #!oil_refinery = 17,
                            #!plastics_plant = 18,
                            #!sugar_refinery = 19,
                            #!dredging_site = 20,
                            #!iron_works = 21,
                            #!glass_works = 22,
                            #farm = 29,
                            #!fruit_plantation = 30,
                            #vehicle_distributor = 33,
                            #!flour_mill = 34,
                            #machine_shop = 38,
                            #port = 39,
                            #ammonia_plant = 40,
                            #!cement_plant = 43,
                            #!clay_pit = 44,
                            #!brick_works = 45,
                            #biorefinery = 46,
                            #ranch = 48,
                            #!chemical_plant = 49,
                            #coffee_estate = 50,
                            #trading_post = 52,
                            #rubber_plantation = 53,
                            #limestone_mine = 54,
                            #diamond_mine = 55,
                            #food_processor = 56,
                            #!hardware_store = 57,
                            #!food_market = 59,
                            #!petrol_pump = 60,
                            #assembly_plant = 62,
                            #!builders_yard = 63,
                            #copper_mine = 64,
                            #nitrate_mine = 65,
                            #copper_refinery = 67,
                            #vineyard = 68,
                            #tyre_plant = 70,
                            #pyrite_mine = 71,
                            #pyrite_smelter = 72,
                            #phosphate_mine = 73,
                            #liquids_terminal = 74,
                            #manganese_mine = 75,
                            #potash_mine = 76,
                            #!lime_kiln = 77,
                            #electric_arc_furnace = 79,
                            #slag_grinding_plant = 80,
                            #engine_plant = 81,
                            #wharf = 82,
                            #machine_works = 83,
                            #carbon_black_plant = 84,
                            #herding_coop = 85,
                            #soda_ash_mine = 86,
                            #chlor_alkali_plant = 87,
                            #component_factory = 88,
                            #ferrochrome_smelter = 89,
                            #chromite_mine = 90,
                            #copper_concentrator = 91,
                            #fischer_tropsch_plant = 92,
                            #latex_processor = 93,
                            #= 94,
                            #wire_and_section_mill = 95,
                            #body_plant = 96,
                            #tinplate_works = 97,
                            #ethylene_cracker = 99,
                            #factory_1 = 100,
                            #factory_2 = 101,
                            #factory_3 = 102,
                            #sheet_and_pipe_mill = 103,
                            #solvay_plant = 104,
                            #salt_mine = 105,
                            #fertiliser_plant = 106,
                            #civil_explosives_facility = 107,
                            #phosphoric_acid_plant = 108,
                            #sulphuric_acid_plant = 109,
                            #polypropylene_plant = 110,
                            #polyethylene_plant = 111,
                            )
#127 is last ID to be used (128 industry limit, zero-based)
# see also why 128 is a hard limit as of 2020 http://webster.openttdcoop.org/?channel=openttd&date=1586563200#1586641232
# if 128 is hit, will have to manually assign IDs per economy
# possibly auto-assignment, but non-alphabetised and with a placeholder option for removals, i.e. a system of 64 slots, and slots are occupied or not
# a pure alphabetised list for auto-IDs will constantly wreck savegames, does that matter?

# Definition of industry tile numeric IDs
# tiles 0-xxx currently vacant
tile_numeric_ids = dict(coal_pit_tile_1 = 89,
                        polyethylene_plant_tile_1 = 90,
                        polypropylene_plant_tile_1 = 91,
                        sulphuric_acid_plant_tile_1 = 92,
                        sulphuric_acid_plant_tile_2 = 93,
                        phosphoric_acid_plant_tile_1 = 94,
                        phosphoric_acid_plant_tile_2 = 95,
                        civil_explosives_facility_tile_1 = 96,
                        civil_explosives_facility_tile_2 = 97,
                        fertiliser_plant_tile_2 = 98,
                        fertiliser_plant_tile_1 = 99,
                        salt_mine_tile_1 = 100,
                        salt_mine_tile_2 = 101,
                        solvay_plant_tile_1 = 102,
                        solvay_plant_tile_2 = 103,
                        steel_mill_tile_1 = 104,
                        factory_1_tile_1 = 105,
                        factory_2_tile_1 = 106,
                        factory_3_tile_1 = 107,
                        ethylene_cracker_tile_1 = 108,
                        ethylene_cracker_tile_2 = 109,
                        coal_pit_tile_2 = 110,
                        tinplate_works_tile_1 = 111,
                        wire_and_section_mill_tile_1 = 112,
                        slag_grinding_plant_tile_1 = 113,
                        slag_grinding_plant_tile_2 = 114,
                        wharf_tile_3 = 115,
                        fish_farm_tile_1 = 116,
                        fish_farm_tile_2 = 117,
                        latex_processor_tile_1 = 118,
                        fischer_tropsch_plant_tile_1 = 119,
                        copper_concentrator_tile_1 = 120,
                        chromite_mine_tile_1 = 121,
                        chromite_mine_tile_2 = 122,
                        chromite_mine_tile_3 = 123,
                        ferrochrome_smelter_tile_1 = 124,
                        component_factory_tile_1 = 125,
                        chlor_alkali_plant_tile_1 = 126,
                        chlor_alkali_plant_tile_2 = 127,
                        carbon_black_plant_tile_1 = 128,
                        machine_works_tile_1 = 129,
                        cryo_plant_tile_1=130,
                        wharf_tile_1 = 131,
                        wharf_tile_2 = 132,
                        vehicle_distributor_tile_1 = 133,
                        limestone_mine_tile_1 = 134,
                        limestone_mine_tile_2 = 135,
                        limestone_mine_tile_3 = 136,
                        engine_plant_tile_1 = 137,
                        paper_mill_tile_1 = 138,
                        potash_mine_tile_1 = 139,
                        potash_mine_tile_2 = 140,
                        potash_mine_tile_3 = 141,
                        soda_ash_mine_tile_1 = 142,
                        soda_ash_mine_tile_2 = 143,
                        herding_coop_tile_1 = 144,
                        diamond_mine_tile_1 = 145,
                        diamond_mine_tile_2 = 146,
                        peatlands_tile_1 = 147,
                        peatlands_tile_2 = 148,
                        phosphate_mine_tile_1 = 149,
                        phosphate_mine_tile_2 = 150,
                        body_plant_tile_1 = 151,
                        electric_arc_furnace_tile_1 = 152,
                        coal_mine_tile_1 = 153,
                        basic_oxygen_furnace_tile_1 = 154,
                        manganese_mine_tile_1 = 155,
                        manganese_mine_tile_2 = 156,
                        manganese_mine_tile_3 = 157,
                        blast_furnace_tile_1 = 158,
                        blast_furnace_tile_2 = 159,
                        arable_farm_tile_1 = 160,
                        brewery_tile_1 = 161,
                        brewery_tile_2 = 162,
                        ammonia_plant_tile_1 = 163,
                        builders_yard_tile_1 = 164,
                        brick_works_tile_1 = 165,
                        biorefinery_tile_1 = 166,
                        coke_oven_tile_1 = 167,
                        coke_oven_tile_2 = 168,
                        port_tile_1 = 169,
                        port_tile_2 = 170,
                        orchard_piggery_tile_1 = 171,
                        orchard_piggery_tile_2 = 172,
                        ranch_tile_1 = 173,
                        copper_mine_tile_1 = 174,
                        dairy_tile_1 = 175,
                        dairy_tile_2 = 176,
                        copper_refinery_tile_1 = 177,
                        glass_works_tile_1 = 178,
                        stockyard_tile_1 = 179,
                        dairy_farm_tile_1 = 180,
                        plastics_plant_tile_1 = 181,
                        flour_mill_tile_1 = 182,
                        textile_mill_tile_1 = 183,
                        furniture_factory_tile_1 = 184,
                        aluminium_plant_tile_1 = 185,
                        machine_shop_tile_1 = 186,
                        lumber_yard_tile_1 = 187,
                        lumber_yard_tile_2 = 188,
                        power_plant_tile_1 = 189,
                        farm_tile_1 = 190,
                        lime_kiln_tile_1 = 191,
                        sheep_farm_tile_1 = 192,
                        junk_yard_tile_1 = 193,
                        food_market_tile_1 = 194,
                        fishing_harbour_tile_1 = 195,
                        fishing_harbour_tile_2 = 196,
                        tyre_plant_tile_1 = 197,
                        dredging_site_tile_1 = 198,
                        metal_workshop_tile_1 = 199,
                        sheet_and_pipe_mill_tile_1 = 200,
                        recycling_plant_tile_1 = 201,
                        recycling_depot_tile_1 = 202,
                        petrol_pump_tile_1 = 203,
                        fishing_grounds_tile_1 = 204,
                        forest_tile_1 = 205,
                        forest_tile_2 = 206,
                        fruit_plantation_tile_1 = 207,
                        fruit_plantation_tile_2 = 208,
                        smithy_forge_tile_1 = 209,
                        iron_works_tile_1 = 210,
                        iron_works_tile_2 = 211,
                        iron_works_tile_3 = 212,
                        oil_rig_tile_1 = 213,
                        sugar_refinery_tile_1 = 214,
                        oil_wells_tile_1 = 215,
                        oil_wells_tile_2 = 216,
                        hotel_tile_1 = 217,
                        hardware_store_tile_1 = 218,
                        general_store_tile_1 = 219,
                        coffee_estate_tile_1 = 220,
                        coffee_estate_tile_2 = 221,
                        bulk_terminal_tile_1 = 222,
                        bulk_terminal_tile_2 = 223,
                        supply_yard_tile_1 = 224,
                        trading_post_tile_1 = 225,
                        trading_post_tile_2 = 226,
                        rubber_plantation_tile_1 = 227,
                        rubber_plantation_tile_2 = 228,
                        food_processor_tile_1 = 229,
                        nitrate_mine_tile_1 = 230,
                        chemical_plant_tile_1 = 231,
                        assembly_plant_tile_1 = 232,
                        cement_plant_tile_1 = 233,
                        sawmill_tile_1 = 234,
                        oil_refinery_tile_1 = 235,
                        iron_ore_mine_tile_1 = 236,
                        iron_ore_mine_tile_2 = 237,
                        iron_ore_mine_tile_3 = 238,
                        clay_pit_tile_1 = 239,
                        clay_pit_tile_2 = 240,
                        quarry_tile_1 = 241,
                        quarry_tile_2 = 242,
                        vineyard_tile_1 = 243,
                        vineyard_tile_2 = 244,
                        vineyard_tile_3 = 245,
                        pyrite_mine_tile_1 = 246,
                        pyrite_mine_tile_2 = 247,
                        pyrite_mine_tile_3 = 248,
                        pyrite_smelter_tile_1 = 249,
                        liquids_terminal_tile_1 = 250,
                        liquids_terminal_tile_2 = 251,
                        fishing_village_tile_1 = 252,
                        fishing_village_tile_2 = 253,
                        chemical_plant_tile_2 = 254
                         )

chameleon_cache_dir =  '.chameleon_cache'

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir =  'generated'

# this is for nml or grfcodec, don't need to use python path module here
graphics_path =  'generated/graphics/'

# OpenTTD's max date
max_game_date = 5000000

# amount of cargo required to trigger 'enhanced' production at primary industries
FARM_MINE_SUPPLY_REQUIREMENT = 16

# time window (days) for delivery of combinatory cargos to secondary industries
secondary_production_span = 90

graphics_temp_storage = dict(var_terrain_sprite = 0, # ID of terrain sprite (from baseset) for the tile
                           var_fencesprite_ne = 1, # fence sprite to use on the NE border
                           var_fencesprite_nw = 2, # fence sprite to use on the NW border
                           var_fencesprite_se = 3, # fence sprite to use on the SE border
                           var_fencesprite_sw = 4, # fence sprite to use on the SW border
                           var_fence_offset_ne = 5, # y-offset for fence sprite to use on the NE border
                           var_fence_offset_nw = 6, # y-offset for fence sprite to use on the NW border
                           var_fence_offset_se = 7, # y-offset for fence sprite to use on the SE border
                           var_fence_offset_sw = 8, # y-offset for fence sprite to use on the SW border
                           var_use_fence_ne = 9, # draw fence in the NE
                           var_use_fence_nw = 10, # draw fence in the NW
                           var_use_fence_se = 11, # draw fence in the SE
                           var_use_fence_sw = 12, # draw fence in the SW
                           var_terrain_is_snow = 13, # must be set to 1 (true) or 0 (false)
                           var_random_bits = 14, # some random bits to use as required
                        )  # max register number must be 235; registers 236-255 are reserved for building sprite hide/show values

# valid industry map colours, derived from an algorithm to ensure contrast against green / dark green / purple minimaps
# based on work by frosch, https://devs.openttd.org/~frosch/texts/industrymap_green_darkgreen_violet.html
valid_industry_map_colours = [183, 64, 61, 166, 45, 151, 157, 191, 141, 178, 189, 55, 186, 43, 148, 5, 116, 160, 127, 143, 170,
                              49, 37, 146, 214, 8, 172, 177, 181, 194, 24, 168, 155, 210, 169, 70, 119, 26, 69, 85, 56, 19, 121,
                              105, 125, 144, 209, 164, 16, 63, 111, 65, 10, 126, 62, 104, 207, 190, 83, 142, 72, 33, 162, 173]
# we also know that some colours are safe, whatever the algorithm thinks
valid_industry_map_colours.extend([1, 15])

# valid cargo colours, derived from the valid map colours, adjusted for:
# - 191 replaced by 51 as 191 is the edge colour for cargo flow diagram
# - 8 is removed, it's a grey, invisible on cargo payment chart, 149 appended at end to replace
# - 19 replaced by 18 for legibility on grey
# - 141 replaced by 139 for legibility on grey
# - first entry is 152, traditional colour for pax (assumes pax will always be cargo 0)
# - third entry is 15, traditional colour for mail (assumes mail will always be cargo 2)
valid_cargo_colours = [152, 183, 15, 61, 166, 45, 157, 51, 139, 178, 189, 55, 186, 43, 148, 5, 116, 160, 127, 143, 170,
                       49, 37, 146, 214, 172, 177, 181, 194, 24, 168, 155, 210, 169, 70, 119, 26, 69, 85, 56, 18, 121, 105,
                       125, 144, 209, 164, 16, 63, 111, 65, 10, 126, 62, 104, 207, 190, 83, 142, 72, 33, 162, 173, 149]
