from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(id='ranch',
                                  prod_cargo_types=['LVST', 'WOOL'],
                                  prob_in_game='4',
                                  prob_random='11',
                                  prod_multiplier='[14, 13]',
                                  map_colour='168',
                                  location_checks=dict(cluster=[72, 4]),
                                  prospect_chance='0.75',
                                  name='string(STR_IND_RANCH)',
                                  nearby_station_name='string(STR_STATION_FARM_3)',
                                  fund_cost_multiplier='45')

industry.economy_variations['BASIC_TROPIC'].enabled = True

industry.add_tile(id='ranch_tile_1',
                  location_checks=TileLocationChecks(disallow_coast=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type='empty'
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 52, -31, -21)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 52, -31, -19)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 52, -31, -21)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 52, -31, -21)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 52, -31, -21)],
)

industry.add_spritelayout(
    id='ranch_spritelayout_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='ranch_spritelayout_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='ranch_spritelayout_3',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='ranch_spritelayout_4',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='ranch_spritelayout_5',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    terrain_aware_ground=True
)

industry.add_industry_layout(
    id='ranch_industry_layout_1',
    layout=[(0, 0, 'ranch_tile_1', 'ranch_spritelayout_3'),
            (1, 0, 'ranch_tile_1', 'ranch_spritelayout_2'),
            (1, 2, 'ranch_tile_1', 'ranch_spritelayout_4'),
            (3, 0, 'ranch_tile_1', 'ranch_spritelayout_1'),
            (3, 1, 'ranch_tile_1', 'ranch_spritelayout_5'),
            ]
)
industry.add_industry_layout(
    id='ranch_industry_layout_2',
    layout=[(0, 0, 'ranch_tile_1', 'ranch_spritelayout_2'),
            (0, 1, 'ranch_tile_1', 'ranch_spritelayout_1'),
            (0, 2, 'ranch_tile_1', 'ranch_spritelayout_4'),
            (2, 0, 'ranch_tile_1', 'ranch_spritelayout_3'),
            (2, 2, 'ranch_tile_1', 'ranch_spritelayout_5'),
            ]
)
