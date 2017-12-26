from industry import IndustryPrimaryTownProducer, TileLocationChecks

industry = IndustryPrimaryTownProducer(id='recycling_depot',
                                       accept_cargo_types=[],
                                       prod_cargo_types=['RCYC'],
                                       prob_in_game='20',
                                       prob_random='20',
                                       prod_multiplier='[0, 0]',
                                       map_colour='191',
                                       life_type='IND_LIFE_TYPE_EXTRACTIVE',
                                       location_checks=dict(same_type_distance=16,
                                                            town_industry_count=['recycling_depot', 0, 0],
                                                            prevent_player_founding=True),
                                       name='string(STR_IND_RECYCLING_DEPOT)',
                                       nearby_station_name='string(STR_STATION_TOWN_2)',
                                       fund_cost_multiplier='118',
                                       intro_year=1978)

industry.economy_variations['FIRS'].enabled = True

industry.add_tile(id='recycling_depot_tile_1',
                  location_checks=TileLocationChecks(always_allow_founder=False,
                                                     require_houses_nearby=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDTILE_SLABS',
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_hut = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)]
)
spriteset_no_hut = industry.add_spriteset(
    sprites=[(80, 10, 64, 31, -31, 0)]
)

industry.add_spritelayout(
    id='recycling_depot_spritelayout_hut',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_hut],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='recycling_depot_spritelayout_no_hut',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_no_hut],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_industry_layout(
    id='recycling_depot_industry_layout',
    layout=[(0, 0, 'recycling_depot_tile_1', 'recycling_depot_spritelayout_hut'),
            (0, 1, 'recycling_depot_tile_1', 'recycling_depot_spritelayout_no_hut'),
            (1, 0, 'recycling_depot_tile_1', 'recycling_depot_spritelayout_no_hut'),
            (1, 1, 'recycling_depot_tile_1', 'recycling_depot_spritelayout_no_hut')
            ]
)
