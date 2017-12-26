from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='textile_mill',
                             processed_cargos_and_output_ratios=[('WOOL', 6), ('FICR', 6)],
                             prod_cargo_types=['GOOD'],
                             prob_in_game='3',
                             prob_random='5',
                             prod_multiplier='[0, 0]',
                             map_colour='37',
                             name='string(STR_IND_TEXTILE_MILL)',
                             nearby_station_name='string(STR_STATION_WEAVE_AND_DYE)',
                             fund_cost_multiplier='120')

industry.economy_variations['FIRS'].enabled = True

industry.add_tile(id='textile_mill_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type='cobble'
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_large_chimney = industry.add_spriteset(
    sprites=[(10, 60, 64, 103, -31, -74)],
)
spriteset_large_building_lh_part = industry.add_spriteset(
    sprites=[(80, 60, 64, 103, -31, -72)],
)
spriteset_large_building_rh_part = industry.add_spriteset(
    sprites=[(150, 60, 64, 103, -31, -72)],
)
spriteset_crates_greeble = industry.add_spriteset(
    sprites=[(220, 60, 64, 103, -31, -72)],
)
spriteset_small_warehouse = industry.add_spriteset(
    sprites=[(290, 60, 64, 103, -31, -72)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=0,
    yoffset=9,
    zoffset=78,
)

industry.add_spritelayout(
    id='textile_mill_spritelayout_1_anim',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_chimney],
    smoke_sprites=[sprite_smoke],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='textile_mill_spritelayout_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_building_lh_part],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='textile_mill_spritelayout_3',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_building_rh_part],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='textile_mill_spritelayout_4',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_crates_greeble],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='textile_mill_spritelayout_5',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_small_warehouse],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='textile_mill_spritelayout_6',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='textile_mill_industry_layout_1',
    layout=[(0, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_3'),
            (0, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_1_anim'),
            (1, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_2'),
            (1, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_5'),
            (2, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_3'),
            (2, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_3'),
            (3, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_2'),
            (3, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_2'),
            (4, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_5'),
            (4, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_4')
            ]
)
industry.add_industry_layout(
    id='textile_mill_industry_layout_2',
    layout=[(0, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_3'),
            (0, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_4'),
            (0, 2, 'textile_mill_tile_1', 'textile_mill_spritelayout_1_anim'),
            (1, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_2'),
            (1, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_6'),
            (1, 2, 'textile_mill_tile_1', 'textile_mill_spritelayout_5'),
            (2, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_5'),
            (2, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_6'),
            ]
)
industry.add_industry_layout(
    id='textile_mill_industry_layout_3',
    layout=[(0, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_3'),
            (0, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_5'),
            (1, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_2'),
            (1, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_4'),
            (2, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_1_anim'),
            ]
)
industry.add_industry_layout(
    id='textile_mill_industry_layout_4',
    layout=[(0, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_3'),
            (0, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_3'),
            (1, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_2'),
            (1, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_2'),
            (2, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_5'),
            (2, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_4'),
            (3, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_3'),
            (3, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_5'),
            (4, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_2'),
            (4, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_1_anim')
            ]
)
industry.add_industry_layout(
    id='textile_mill_industry_layout_5',
    layout=[(0, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_3'),
            (0, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_3'),
            (0, 2, 'textile_mill_tile_1', 'textile_mill_spritelayout_5'),
            (0, 3, 'textile_mill_tile_1', 'textile_mill_spritelayout_5'),
            (1, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_2'),
            (1, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_2'),
            (1, 2, 'textile_mill_tile_1', 'textile_mill_spritelayout_4'),
            (1, 3, 'textile_mill_tile_1', 'textile_mill_spritelayout_1_anim')
            ]
)
industry.add_industry_layout(
    id='textile_mill_industry_layout_6',
    layout=[(0, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_5'),
            (0, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_3'),
            (0, 2, 'textile_mill_tile_1', 'textile_mill_spritelayout_3'),
            (1, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_5'),
            (1, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_2'),
            (1, 2, 'textile_mill_tile_1', 'textile_mill_spritelayout_2'),
            (2, 0, 'textile_mill_tile_1', 'textile_mill_spritelayout_5'),
            (2, 1, 'textile_mill_tile_1', 'textile_mill_spritelayout_1_anim'),
            (2, 2, 'textile_mill_tile_1', 'textile_mill_spritelayout_4')
            ]
)
