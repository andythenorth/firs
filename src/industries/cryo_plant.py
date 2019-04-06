from industry import IndustryPrimaryNoSupplies, TileLocationChecks

industry = IndustryPrimaryNoSupplies(id='cryo_plant',
                                     accept_cargo_types=[],
                                     prod_cargo_types_with_multipliers=[('O2__', 14)],
                                     prob_in_game='4',
                                     prob_random='7',
                                     map_colour='189',
                                     location_checks=dict(same_type_distance=72),
                                     prospect_chance='0.75',
                                     name='string(STR_IND_CRYO_PLANT)',
                                     nearby_station_name='string(STR_STATION_CRYO_PLANT)',
                                     fund_cost_multiplier='180')

industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='cryo_plant_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type='concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)

spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 106, -31, -73)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -31)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 74, -31, -42)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -32)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -31)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -31)],
)

industry.add_spritelayout(
    id='cryo_plant_spritelayout_separation_tower',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='cryo_plant_spritelayout_large_shed',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=[]
)
industry.add_spritelayout(
    id='cryo_plant_spritelayout_horizontal_tanks',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='cryo_plant_spritelayout_vertical_tanks',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='cryo_plant_spritelayout_office',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=[]
)
industry.add_spritelayout(
    id='cryo_plant_spritelayout_empty',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='cryo_plant_industry_layout_1',
    layout=[(0, 0, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_separation_tower'),
            (0, 1, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_large_shed'),
            (1, 0, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_horizontal_tanks'),
            (1, 1, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_vertical_tanks'),
            (2, 0, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_office'),
            (2, 1, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_empty'),
            ]
)
industry.add_industry_layout(
    id='cryo_plant_industry_layout_2',
    layout=[(0, 0, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_separation_tower'),
            (0, 1, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_horizontal_tanks'),
            (0, 2, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_vertical_tanks'),
            (1, 0, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_large_shed'),
            (1, 1, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_office'),
            (1, 2, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_empty'),
            ]
)
