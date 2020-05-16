from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='methanol_plant',
                             accept_cargos_with_input_ratios=[('METH', 8)],
                             prod_cargo_types_with_output_ratios=[('MEOH', 6)],
                             prob_in_game='3',
                             prob_map_gen='5',
                             map_colour='191',
                             special_flags=['IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE'],
                             fund_cost_multiplier='200',
                             name='string(STR_IND_METHANOL_PLANT)',
                             nearby_station_name='string(STR_STATION_REFINERY)')

#industry.economy_variations['BETTER_LIVING_THROUGH_CHEMISTRY'].enabled = True

industry.add_tile(id='methanol_plant_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type='concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 66, -31, -35)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 128, -31, -96)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 128, -31, -96)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 128, -31, -96)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 66, -31, -35)],
)

industry.add_spritelayout(
    id='methanol_plant_spritelayout_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='methanol_plant_spritelayout_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='methanol_plant_spritelayout_3',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='methanol_plant_spritelayout_4',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='methanol_plant_spritelayout_5',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='methanol_plant_industry_layout_1',
    layout=[(0, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (0, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (0, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (0, 3, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (0, 4, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_2'),
            (1, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (1, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (1, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_4'),
            (1, 3, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_2'),
            (1, 4, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_5'),
            (2, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (2, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (2, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_4'),
            (2, 3, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (2, 4, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_5'),
            ]
)
industry.add_industry_layout(
    id='methanol_plant_industry_layout_2',
    layout=[(0, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_2'),
            (0, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (0, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (0, 3, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_4'),
            (1, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_2'),
            (1, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_4'),
            (1, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (1, 3, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_2'),
            (2, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_5'),
            (2, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (2, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (2, 3, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (3, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_5'),
            (3, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (3, 3, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            ]
)
industry.add_industry_layout(
    id='methanol_plant_industry_layout_3',
    layout=[(0, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_2'),
            (0, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (0, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (0, 3, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_4'),
            (0, 4, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (0, 5, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (1, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (1, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_4'),
            (1, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (1, 3, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_2'),
            (1, 4, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_5'),
            (1, 5, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (2, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_4'),
            (2, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (2, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (2, 3, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (2, 4, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (2, 5, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (3, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_5'),
            (3, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (3, 3, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (3, 4, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (3, 5, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            ]
)
industry.add_industry_layout(
    id='methanol_plant_industry_layout_4',
    layout=[(0, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (0, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (0, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (1, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (1, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (1, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (2, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (2, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (2, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (3, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_4'),
            (3, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_1'),
            (3, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_5'),
            (4, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_4'),
            (4, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (4, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_5'),
            (5, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_2'),
            (5, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (5, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_4'),
            (6, 0, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_5'),
            (6, 1, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_3'),
            (6, 2, 'methanol_plant_tile_1', 'methanol_plant_spritelayout_2'),
            ]
)
