from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='coke_oven',
                    processed_cargos_and_output_ratios=[('COAL', 8)],
                    prod_cargo_types=[('COKE', 6), ('SULP', 2)],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    map_colour='163',
                    name='string(STR_IND_COKE_OVEN)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_PIT))',
                    fund_cost_multiplier='120')

industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='coke_oven_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS' # ground tile same as overlay tile
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'coke_oven_spriteset_ground_overlay',
    type = 'empty'
)

spriteset_1 = industry.add_spriteset(
    id = 'coke_oven_spriteset_1',
    sprites = [(10, 10, 64, 110, -31, -70)],
)
spriteset_2 = industry.add_spriteset(
    id = 'coke_oven_spriteset_2',
    sprites = [(80, 10, 64, 110, -31, -70)],
)
spriteset_3 = industry.add_spriteset(
    id = 'coke_oven_spriteset_3',
    sprites = [(150, 10, 64, 64, -31, -31)],
)
spriteset_4 = industry.add_spriteset(
    id = 'coke_oven_spriteset_4',
    sprites = [(220, 10, 64, 92, -31, -60)],
)
spriteset_5 = industry.add_spriteset(
    id = 'coke_oven_spriteset_5',
    sprites = [(290, 10, 64, 64, -31, -31)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 10,
    yoffset= 5,
    zoffset= 73,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 10,
    yoffset= 10,
    zoffset= 73,
    animation_frame_offset = 1
)
sprite_smoke_3 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 10,
    yoffset= 15,
    zoffset= 73,
)

industry.add_spritelayout(
    id = 'coke_oven_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    smoke_sprites = [sprite_smoke_1, sprite_smoke_2, sprite_smoke_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'coke_oven_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'coke_oven_spritelayout_3',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'coke_oven_spritelayout_4',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'coke_oven_spritelayout_5',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'coke_oven_spritelayout_6',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'coke_oven_industry_layout_1',
    layout = [(0, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_2'),
              (0, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_1'),
              (1, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_6'),
              (1, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_6'),
              (2, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_6'),
              (2, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_4'),
              (3, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_5'),
              (3, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_3'),
              (4, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_5'),
              (4, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_3'),
              (5, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_5'),
              (5, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_3'),
    ]
)
industry.add_industry_layout(
    id = 'coke_oven_industry_layout_2',
    layout = [(0, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_2'),
              (0, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_1'),
              (0, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_1'),
              (0, 3, 'coke_oven_tile_1', 'coke_oven_spritelayout_1'),
              (1, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_6'),
              (1, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_6'),
              (1, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_6'),
              (1, 3, 'coke_oven_tile_1', 'coke_oven_spritelayout_6'),
              (2, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_6'),
              (2, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_4'),
              (2, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_6'),
              (2, 3, 'coke_oven_tile_1', 'coke_oven_spritelayout_6'),
    ]
)
