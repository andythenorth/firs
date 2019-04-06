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
    sprites=[(80, 10, 64, 64, -31, -32)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -31)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -31)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -31)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -31)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 64, -31, -31)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 64, -31, -31)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 64, -31, -31)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=8,
    yoffset=2,
    zoffset=70,
)

industry.add_spritelayout(
    id='cryo_plant_spritelayout_chimney',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='cryo_plant_spritelayout_large_shed',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='cryo_plant_spritelayout_conveyors',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='cryo_plant_spritelayout_processor',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='cryo_plant_spritelayout_raised_tanks',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='cryo_plant_spritelayout_raised_shed',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='cryo_plant_spritelayout_machinery',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='cryo_plant_spritelayout_hut',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='cryo_plant_spritelayout_empty',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='cryo_plant_industry_layout_1',
    layout=[(0, 0, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_chimney'),
            (0, 1, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_raised_shed'),
            (0, 2, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_hut'),
            (1, 0, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_raised_tanks'),
            (1, 1, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_raised_tanks'),
            (1, 2, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_empty'),
            (2, 0, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_processor'),
            (2, 1, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_processor'),
            (2, 2, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_empty'),
            (3, 0, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_conveyors'),
            (3, 1, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_conveyors'),
            (3, 2, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_empty'),
            (4, 0, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_large_shed'),
            (4, 1, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_large_shed'),
            (4, 2, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_machinery'),
            ]
)
industry.add_industry_layout(
    id='cryo_plant_industry_layout_2',
    layout=[(0, 0, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_raised_tanks'),
            (0, 1, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_processor'),
            (0, 2, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_processor'),
            (0, 3, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_raised_shed'),
            (1, 0, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_chimney'),
            (1, 1, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_conveyors'),
            (1, 2, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_conveyors'),
            (1, 3, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_empty'),
            (2, 0, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_machinery'),
            (2, 1, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_large_shed'),
            (2, 2, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_large_shed'),
            (2, 3, 'cryo_plant_tile_1', 'cryo_plant_spritelayout_hut'),
            ]
)
