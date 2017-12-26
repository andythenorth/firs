from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(id='arable_farm',
                                  prod_cargo_types=['GRAI', 'SGBT'],
                                  prob_in_game='4',
                                  prob_random='11',
                                  prod_multiplier='[14, 14]',
                                  map_colour='209',
                                  spec_flags='bitmask(IND_FLAG_PLANT_FIELDS_PERIODICALLY, IND_FLAG_PLANT_FIELDS_WHEN_BUILT)',
                                  location_checks=dict(cluster=[72, 4]),
                                  prospect_chance='0.75',
                                  name='string(STR_IND_ARABLE_FARM)',
                                  extra_text_fund='string(STR_FUND_ARABLE_FARM)',
                                  nearby_station_name='string(STR_STATION_FARM_1)',
                                  fund_cost_multiplier='55',
                                  graphics_change_dates=[1928])

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['BASIC_TROPIC'].prod_cargo_types = ['GRAI', 'BEAN']
industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].prod_cargo_types = ['CASS', 'NUTS']

industry.add_tile(id='arable_farm_tile_1',
                  location_checks=TileLocationChecks(disallow_slopes=True,
                                                     disallow_above_snowline=True,
                                                     disallow_desert=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_empty = industry.add_spriteset(
    type='empty'
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
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 59, -31, -28)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 59, -31, -28)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 59, -31, -28)],
)

industry.add_spritelayout(
    id='arable_farm_spritelayout_1',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1]
)
industry.add_spritelayout(
    id='arable_farm_spritelayout_2',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='arable_farm_spritelayout_3',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    terrain_aware_ground=True
)
industry.add_spritelayout(
    id='arable_farm_spritelayout_4',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id='arable_farm_spritelayout_5',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
)

industry.add_industry_layout(
    id='arable_farm_industry_layout_1',
    layout=[(0, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_5'),
            (0, 2, 'arable_farm_tile_1', 'arable_farm_spritelayout_3'),
            (1, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_1'),
            (1, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_2'),
            (2, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_4'),
            ]
)
industry.add_industry_layout(
    id='arable_farm_industry_layout_2',
    layout=[(0, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_5'),
            (0, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_4'),
            (1, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_1'),
            (1, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_2'),
            (2, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_3'),
            ]
)
industry.add_industry_layout(
    id='arable_farm_industry_layout_3',
    layout=[(0, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_1'),
            (0, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_2'),
            (1, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_5'),
            (2, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_4'),
            (2, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_3'),
            ]
)
