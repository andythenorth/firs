from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='factory',
                             processed_cargos_and_output_ratios=[('MNSP', 8)],
                             prod_cargo_types=['GOOD'],
                             prob_in_game='7',
                             prob_random='8',
                             prod_multiplier='[0, 0]',
                             map_colour='186',
                             prospect_chance='0.75',
                             name='string(STR_IND_FACTORY)',
                             nearby_station_name='string(STR_STATION_INDUSTRY_ESTATE_1)',
                             fund_cost_multiplier='95')

industry.add_tile(id='factory_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))


spriteset_ground = industry.add_spriteset(
    type='cobble',
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty',
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 88, -31, -42)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 88, -31, -44)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 88, -31, -42)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 88, -31, -42)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 60, 64, 88, -31, -42)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 60, 64, 88, -31, -41)],
)

industry.add_spritelayout(
    id='factory_spritelayout_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='factory_spritelayout_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='factory_spritelayout_3',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='factory_spritelayout_4',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='factory_spritelayout_5',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='factory_spritelayout_6',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='factory_industry_layout_1',
    layout=[(0, 1, 'factory_tile_1', 'factory_spritelayout_3'),
            (1, 0, 'factory_tile_1', 'factory_spritelayout_5'),
            (1, 1, 'factory_tile_1', 'factory_spritelayout_2'),
            (2, 0, 'factory_tile_1', 'factory_spritelayout_4'),
            (2, 1, 'factory_tile_1', 'factory_spritelayout_1'),
            ]
)
industry.add_industry_layout(
    id='factory_industry_layout_2',
    layout=[(0, 0, 'factory_tile_1', 'factory_spritelayout_5'),
            (0, 1, 'factory_tile_1', 'factory_spritelayout_3'),
            (1, 0, 'factory_tile_1', 'factory_spritelayout_4'),
            (1, 1, 'factory_tile_1', 'factory_spritelayout_2'),
            (2, 0, 'factory_tile_1', 'factory_spritelayout_6'),
            (2, 1, 'factory_tile_1', 'factory_spritelayout_1'),
            ]
)
industry.add_industry_layout(
    id='factory_industry_layout_3',
    layout=[(0, 0, 'factory_tile_1', 'factory_spritelayout_3'),
            (0, 1, 'factory_tile_1', 'factory_spritelayout_6'),
            (1, 0, 'factory_tile_1', 'factory_spritelayout_2'),
            (1, 1, 'factory_tile_1', 'factory_spritelayout_3'),
            (2, 0, 'factory_tile_1', 'factory_spritelayout_1'),
            (2, 1, 'factory_tile_1', 'factory_spritelayout_2'),
            (3, 0, 'factory_tile_1', 'factory_spritelayout_5'),
            (3, 1, 'factory_tile_1', 'factory_spritelayout_1'),
            (4, 0, 'factory_tile_1', 'factory_spritelayout_4'),
            (4, 1, 'factory_tile_1', 'factory_spritelayout_6'),
            ]
)
industry.add_industry_layout(
    id='factory_industry_layout_4',
    layout=[(0, 0, 'factory_tile_1', 'factory_spritelayout_5'),
            (0, 1, 'factory_tile_1', 'factory_spritelayout_6'),
            (1, 0, 'factory_tile_1', 'factory_spritelayout_4'),
            (1, 1, 'factory_tile_1', 'factory_spritelayout_6'),
            (2, 0, 'factory_tile_1', 'factory_spritelayout_3'),
            (2, 1, 'factory_tile_1', 'factory_spritelayout_3'),
            (3, 0, 'factory_tile_1', 'factory_spritelayout_2'),
            (3, 1, 'factory_tile_1', 'factory_spritelayout_2'),
            (4, 0, 'factory_tile_1', 'factory_spritelayout_1'),
            (4, 1, 'factory_tile_1', 'factory_spritelayout_1'),
            ]
)
industry.add_industry_layout(
    id='factory_industry_layout_5',
    layout=[(0, 0, 'factory_tile_1', 'factory_spritelayout_5'),
            (0, 1, 'factory_tile_1', 'factory_spritelayout_3'),
            (0, 2, 'factory_tile_1', 'factory_spritelayout_3'),
            (1, 0, 'factory_tile_1', 'factory_spritelayout_4'),
            (1, 1, 'factory_tile_1', 'factory_spritelayout_2'),
            (1, 2, 'factory_tile_1', 'factory_spritelayout_2'),
            (2, 0, 'factory_tile_1', 'factory_spritelayout_6'),
            (2, 1, 'factory_tile_1', 'factory_spritelayout_1'),
            (2, 2, 'factory_tile_1', 'factory_spritelayout_1'),
            ]
)
