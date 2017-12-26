from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(id='hotel',
                            accept_cargo_types=['FOOD', 'BEER', 'PASS'],
                            prod_cargo_types=['PASS'],
                            prob_in_game='15',
                            prob_random='10',
                            prod_multiplier='[17, 0]',
                            map_colour='189',
                            life_type='IND_LIFE_TYPE_BLACK_HOLE',
                            location_checks=dict(same_type_distance=16),
                            prospect_chance='0.75',
                            name='string(STR_IND_HOTEL)',
                            nearby_station_name='string(STR_STATION_BAR_GRILL_AND_ROOMS)',
                            fund_cost_multiplier='101')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.add_tile(id='hotel_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     require_houses_nearby=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDSPRITE_CLEARED'
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty',
)
sprite_building_1 = industry.add_sprite(
    sprite_number='(terrain_type == TILETYPE_SNOW) ? 4583 : 4475'
)
sprite_building_2 = industry.add_sprite(
    sprite_number='(terrain_type == TILETYPE_SNOW) ? 4584 : 4476'
)

industry.add_spritelayout(
    id='hotel_spritelayout_1',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_building_1]
)
industry.add_spritelayout(
    id='hotel_spritelayout_2',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_building_2]
)

industry.add_industry_layout(
    id='hotel_industry_layout',
    layout=[(0, 0, 'hotel_tile_1', 'hotel_spritelayout_1'),
            (1, 0, 'hotel_tile_1', 'hotel_spritelayout_1'),
            (0, 1, 'hotel_tile_1', 'hotel_spritelayout_2'),
            (1, 1, 'hotel_tile_1', 'hotel_spritelayout_2')
            ]
)
