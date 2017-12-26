from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='lime_kiln',
                             processed_cargos_and_output_ratios=[('GRVL', 4), ('COAL', 4)],
                             combined_cargos_boost_prod=True,
                             prod_cargo_types=['RFPR', 'FMSP'],
                             prob_in_game='3',
                             prob_random='5',
                             prod_multiplier='[0, 0]',
                             map_colour='119',
                             name='string(STR_IND_LIME_KILN)',
                             nearby_station_name='string(STR_STATION_KILNS)',
                             fund_cost_multiplier='45',
                             graphics_change_dates=[1952, 1978])

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['STEELTOWN'].enabled = True
industry.economy_variations['STEELTOWN'].prod_cargo_types = ['QLME']
industry.economy_variations['STEELTOWN'].processed_cargos_and_output_ratios = [('LIME', 4), ('PETR', 4)]

industry.add_tile(id='lime_kiln_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDTILE_MUD_TRACKS'  # ground tile same as overlay tile
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)

spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 110, -31, -70)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 110, -31, -70)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -31)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 92, -31, -60)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -31)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=10,
    yoffset=5,
    zoffset=73,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=10,
    yoffset=10,
    zoffset=73,
    animation_frame_offset=1
)
sprite_smoke_3 = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=10,
    yoffset=15,
    zoffset=73,
)

industry.add_spritelayout(
    id='lime_kiln_spritelayout_1',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2, sprite_smoke_3],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='lime_kiln_spritelayout_2',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='lime_kiln_spritelayout_3',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='lime_kiln_spritelayout_4',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='lime_kiln_spritelayout_5',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='lime_kiln_spritelayout_6',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='lime_kiln_industry_layout_1',
    layout=[(0, 0, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_2'),
            (0, 1, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_1'),
            (0, 2, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_6'),
            (1, 0, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_4'),
            (1, 1, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_5'),
            (1, 2, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_3'),
            ]
)
industry.add_industry_layout(
    id='lime_kiln_industry_layout_2',
    layout=[(0, 0, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_2'),
            (0, 1, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_1'),
            (1, 0, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_4'),
            (1, 1, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_5'),
            (2, 0, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_6'),
            (2, 1, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_3'),
            ]
)
industry.add_industry_layout(
    id='lime_kiln_industry_layout_3',
    layout=[(0, 0, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_2'),
            (0, 1, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_1'),
            (0, 2, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_6'),
            (0, 3, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_6'),
            (1, 0, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_4'),
            (1, 1, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_5'),
            (1, 2, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_3'),
            (1, 3, 'lime_kiln_tile_1', 'lime_kiln_spritelayout_6'),
            ]
)
