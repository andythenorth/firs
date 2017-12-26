from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='lumber_yard',
                             processed_cargos_and_output_ratios=[('WDPR', 6), ('RFPR', 2)],
                             combined_cargos_boost_prod=True,
                             prod_cargo_types=['ENSP', 'BDMT'],
                             prob_in_game='3',
                             prob_random='5',
                             prod_multiplier='[0, 0]',
                             map_colour='43',
                             name='string(STR_IND_LUMBER_YARD)',
                             nearby_station_name='string(STR_STATION_CREOSOTING)',
                             fund_cost_multiplier='35')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].prod_cargo_types = ['BDMT']

# non-animated tile, allowed on slopes
industry.add_tile(id='lumber_yard_tile_1',
                  location_checks=TileLocationChecks(disallow_industry_adjacent=True))

# animated kiln-building tile, graphics break if built on slopes
industry.add_tile(id='lumber_yard_tile_2',
                  animation_length=71,
                  animation_looping=True,
                  animation_speed=2,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -40)]
)
spriteset_2 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -34)]
)
# no spriteset 3 for this industry, historical reasons
spriteset_4 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -35)]
)
spriteset_5 = industry.add_spriteset(
    sprites=[(10, 10, 64, 64, -31, -26)]
)
spriteset_6 = industry.add_spriteset(
    sprites=[(150, 90, 64, 31, -31, -4)]
)
spriteset_7 = industry.add_spriteset(
    sprites=[(220, 90, 64, 31, -31, -4)]
)
spriteset_8 = industry.add_spriteset(
    sprites=[(290, 90, 64, 31, -31, -4)]
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type='white_smoke_small',
    xoffset=0,
    yoffset=3,
    zoffset=12,
)

industry.add_spritelayout(
    id='lumber_yard_spritelayout_1',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='lumber_yard_spritelayout_2',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    smoke_sprites=[sprite_smoke],
    fences=['nw', 'ne', 'se', 'sw']
)
# no spritelayout 3 for this industry, historical reasons
industry.add_spritelayout(
    id='lumber_yard_spritelayout_4',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='lumber_yard_spritelayout_5',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='lumber_yard_spritelayout_6',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='lumber_yard_spritelayout_7',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='lumber_yard_spritelayout_8',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='lumber_yard_industry_layout_1',
    layout=[(0, 0, 'lumber_yard_tile_2', 'lumber_yard_spritelayout_2'),
            (0, 1, 'lumber_yard_tile_2', 'lumber_yard_spritelayout_1'),
            (0, 2, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_5'),
            (1, 0, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_6'),
            (1, 1, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_4'),
            (1, 2, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_8'),
            (2, 0, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_8'),
            (2, 1, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_4'),
            (2, 2, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_7'),
            (3, 0, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_6'),
            (3, 1, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_5'),
            (3, 2, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_6')
            ]
)
industry.add_industry_layout(
    id='lumber_yard_industry_layout_2',
    layout=[(0, 0, 'lumber_yard_tile_2', 'lumber_yard_spritelayout_2'),
            (0, 1, 'lumber_yard_tile_2', 'lumber_yard_spritelayout_1'),
            (0, 2, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_5'),
            (0, 3, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_6'),
            (1, 0, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_8'),
            (1, 1, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_8'),
            (1, 2, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_4'),
            (1, 3, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_6'),
            (2, 0, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_5'),
            (2, 1, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_6'),
            (2, 2, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_4'),
            (2, 3, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_7')
            ]
)
industry.add_industry_layout(
    id='lumber_yard_industry_layout_3',
    layout=[(0, 0, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_6'),
            (0, 1, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_4'),
            (0, 2, 'lumber_yard_tile_2', 'lumber_yard_spritelayout_2'),
            (0, 3, 'lumber_yard_tile_2', 'lumber_yard_spritelayout_1'),
            (0, 4, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_8'),
            (1, 0, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_8'),
            (1, 1, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_4'),
            (1, 2, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_6'),
            (1, 3, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_5'),
            (1, 4, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_7')
            ]
)
industry.add_industry_layout(
    id='lumber_yard_industry_layout_4',
    layout=[(0, 0, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_4'),
            (0, 1, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_7'),
            (1, 0, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_4'),
            (1, 1, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_6'),
            (2, 0, 'lumber_yard_tile_2', 'lumber_yard_spritelayout_2'),
            (2, 1, 'lumber_yard_tile_2', 'lumber_yard_spritelayout_1'),
            (3, 0, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_8'),
            (3, 1, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_6'),
            (4, 0, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_5'),
            (4, 1, 'lumber_yard_tile_1', 'lumber_yard_spritelayout_6')
            ]
)
