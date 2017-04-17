from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='coke_oven',
                    processed_cargos_and_output_ratios=[('COAL', 8)],
                    prod_cargo_types=[('COKE', 6), ('SULP', 2)],
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

sprite_ground = industry.add_spriteset(
    type='concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    type = 'empty'
)

spriteset_oven_battery_rear = industry.add_spriteset(
    sprites = [(10, 10, 64, 122, -31, -91)],
)
spriteset_oven_battery_front = industry.add_spriteset(
    sprites = [(80, 10, 64, 122, -31, -91)],
)
spriteset_quench_tower = industry.add_spriteset(
    sprites = [(150, 10, 64, 122, -31, -91)],
)
spriteset_chimney = industry.add_spriteset(
    sprites = [(220, 10, 64, 136, -31, -109)],
)
spriteset_gas_plant_1 = industry.add_spriteset(
    sprites = [(290, 10, 64, 122, -31, -91)],
)
spriteset_silo = industry.add_spriteset(
    sprites = [(360, 10, 64, 122, -31, -91)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 9,
    yoffset= 5,
    zoffset= 123,
)

industry.add_spritelayout(
    id = 'coke_oven_spritelayout_empty',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'coke_oven_spritelayout_oven_battery_rear',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_oven_battery_rear],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'coke_oven_spritelayout_oven_battery_front',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_oven_battery_front],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'coke_oven_spritelayout_quench_tower',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_quench_tower],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'coke_oven_spritelayout_chimney',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_chimney],
    smoke_sprites = [sprite_smoke_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'coke_oven_spritelayout_gas_plant_1',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_gas_plant_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'coke_oven_spritelayout_silo',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_silo],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'coke_oven_industry_layout_1',
    layout = [(0, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_silo'),
              (0, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_chimney'),
              (0, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_empty'),
              (1, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_oven_battery_rear'),
              (1, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_oven_battery_front'),
              (1, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_empty'),
              (2, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_oven_battery_rear'),
              (2, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_oven_battery_front'),
              (2, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_gas_plant_1'),
              (3, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_oven_battery_rear'),
              (3, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_oven_battery_front'),
              (3, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_empty'),
              (4, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_quench_tower'),
              (4, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_empty'),
              (4, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_empty'),
    ]
)