from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(id='fruit_plantation',
                                  prod_cargo_types_with_multipliers=[('FRUT', 16)],
                                  prob_in_game='4',
                                  prob_map_gen='10',
                                  prospect_chance='0.75',
                                  map_colour='207',
                                  name='TTD_STR_INDUSTRY_NAME_FRUIT_PLANTATION',
                                  extra_text_fund='string(STR_FUND_FRUIT_PLANTATION)',
                                  nearby_station_name='string(STR_STATION_PLANTATION)',
                                  # fruit plantation doesn't cluster, by design - no industry location checks needed
                                  fund_cost_multiplier='54',
                                  override_default_construction_states=True)

###industry.economy_variations['BETTER_LIVING_THROUGH_CHEMISTRY'].enabled = True
industry.economy_variations['IN_A_HOT_COUNTRY'].enabled = True

industry.add_tile(id='fruit_plantation_tile_1',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  autoslope='return CB_RESULT_NO_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='fruit_plantation_tile_2',  # house
                  autoslope='return CB_RESULT_AUTOSLOPE',
                  location_checks=TileLocationChecks(disallow_above_snowline=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number=3962
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 59, -31, -28)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 59, -31, -28)],
)

industry.add_spritelayout(
    id='fruit_plantation_house_spritelayout',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id='fruit_plantation_shed_spritelayout',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)
industry.add_magic_spritelayout(
    type='slope_aware_trees',
    base_id='fruit_plantation_slope_aware_ground_with_trees_1',
    config={'ground_sprite': 4145,
            'trees_default': [1620, 1620, 1620, 1620],
            'trees_tropic': [1832, 1830, 1831, 1832]}
)
industry.add_magic_spritelayout(
    type='slope_aware_trees',
    base_id='fruit_plantation_slope_aware_ground_with_trees_2',
    config={'ground_sprite': 4145,
            'trees_default': [1621, 1622, 1623, 1620],
            'trees_tropic': [1832, 1830, 1831, 1832]}
)

industry.add_industry_layout(
    id='fruit_plantation_layout_1',
    layout=[(0, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (0, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (0, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_2'),
            (2, 1, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
            (2, 2, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
            ]
)
industry.add_industry_layout(
    id='fruit_plantation_layout_2',
    layout=[(0, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (0, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (0, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_2'),
            (0, 3, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
            (1, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 4, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
            ]
)
industry.add_industry_layout(
    id='fruit_plantation_layout_3',
    layout=[(0, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (0, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (2, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (2, 1, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
            (3, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_2'),
            (3, 1, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
            ]
)
industry.add_industry_layout(
    id='fruit_plantation_layout_4',
    layout=[(0, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (0, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (0, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (0, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (3, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_2'),
            (3, 1, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
            (3, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (3, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (4, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (4, 1, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
            (4, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (4, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            ]
)
industry.add_industry_layout(
    id='fruit_plantation_layout_5',
    layout=[(0, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (0, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (0, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (0, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (1, 5, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (3, 0, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (3, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (3, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (3, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (3, 4, 'fruit_plantation_tile_2', 'fruit_plantation_shed_spritelayout'),
            (3, 5, 'fruit_plantation_tile_2', 'fruit_plantation_house_spritelayout'),
            (4, 1, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (4, 2, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (4, 3, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_1'),
            (4, 4, 'fruit_plantation_tile_1', 'fruit_plantation_slope_aware_ground_with_trees_2'),
            ]
)
