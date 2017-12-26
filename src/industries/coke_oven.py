from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='coke_oven',
                             processed_cargos_and_output_ratios=[('COAL', 8)],
                             prod_cargo_types=[('COKE', 6), ('SULP', 2)],
                             prob_in_game='3',
                             prob_random='5',
                             prod_multiplier='[0, 0]',
                             map_colour='183',
                             # it's rare to force co-location of secondaries, but this one is near blast furnace by design
                             location_checks=dict(industry_max_distance=['blast_furnace', 72], same_type_distance=72),
                             name='string(STR_IND_COKE_OVEN)',
                             nearby_station_name='string(STR_STATION_BANK_TOP)',
                             fund_cost_multiplier='120')

industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='coke_oven_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  custom_animation_control={'macro': 'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

industry.add_tile(id='coke_oven_tile_2',
                  animation_length=47,
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

spriteset_silo = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -91)],
)
spriteset_oven_battery = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -91)],
)
spriteset_larry_car = industry.add_spriteset(
    sprites=[(10, 150, 64, 64, -31, -56)],
)
spriteset_pusher_rails_base = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -91)],
    yextent=8  # prevents gantry flickering
)
spriteset_pusher_car = industry.add_spriteset(
    sprites=[(10, 234, 64, 64, -31, -32)],
)
spriteset_pipe_gantry = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -91)],
)
spriteset_pipe_gantry_house = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -91)],
    yextent=32
)
spriteset_coal_handling_front = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -91)],
)
spriteset_coal_handling_rear = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -91)],
)
spriteset_quench_tower = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -91)],
)
spriteset_gas_plant_1 = industry.add_spriteset(
    sprites=[(570, 10, 64, 122, -31, -91)],
)
sprite_smoke_big_1 = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=8,
    yoffset=5,
    zoffset=104,
)
sprite_smoke_big_2 = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=0,
    yoffset=7,
    zoffset=76,
)
sprite_smoke_small_1 = industry.add_smoke_sprite(
    smoke_type='white_smoke_small',
    xoffset=0,
    yoffset=0,
    zoffset=16,
)
sprite_smoke_small_2 = industry.add_smoke_sprite(
    smoke_type='white_smoke_small',
    xoffset=0,
    yoffset=5,
    zoffset=16,
    animation_frame_offset=4,
)

industry.add_spritelayout(
    id='coke_oven_spritelayout_oven_battery_empty',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_oven_battery],
)
industry.add_spritelayout(
    id='coke_oven_spritelayout_oven_battery_animated',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_oven_battery, spriteset_larry_car],
    smoke_sprites=[sprite_smoke_small_1, sprite_smoke_small_2]
)
industry.add_spritelayout(
    id='coke_oven_spritelayout_silo',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_silo],
    smoke_sprites=[sprite_smoke_big_1],
)
industry.add_spritelayout(
    id='coke_oven_spritelayout_pusher_rails_empty',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_pusher_rails_base, spriteset_pipe_gantry],
)
industry.add_spritelayout(
    id='coke_oven_spritelayout_pusher_rails_animated',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_pusher_rails_base, spriteset_pusher_car, spriteset_pipe_gantry],
)
industry.add_spritelayout(
    id='coke_oven_spritelayout_pusher_rails_with_house',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_pusher_rails_base, spriteset_pipe_gantry, spriteset_pipe_gantry_house],
)
industry.add_spritelayout(
    id='coke_oven_spritelayout_quench_tower',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_quench_tower],
    smoke_sprites=[sprite_smoke_big_2]
)
industry.add_spritelayout(
    id='coke_oven_spritelayout_gas_plant_1',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_gas_plant_1],
)
industry.add_spritelayout(
    id='coke_oven_spritelayout_coal_handling_front',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_coal_handling_front],
)
industry.add_spritelayout(
    id='coke_oven_spritelayout_coal_handling_rear',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_coal_handling_rear],
)

industry.add_industry_layout(
    id='coke_oven_industry_layout_1',
    layout=[(0, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_quench_tower'),
            (0, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_silo'),
            (0, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_pusher_rails_empty'),
            (1, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_gas_plant_1'),
            (1, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_oven_battery_empty'),
            (1, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_pusher_rails_with_house'),
            (2, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_coal_handling_rear'),
            (2, 1, 'coke_oven_tile_2', 'coke_oven_spritelayout_oven_battery_animated'),
            (2, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_pusher_rails_animated'),
            (3, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_coal_handling_front'),
            (3, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_oven_battery_empty'),
            (3, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_pusher_rails_with_house'),
            ]
)
industry.add_industry_layout(
    id='coke_oven_industry_layout_2',
    layout=[(0, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_quench_tower'),
            (0, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_oven_battery_empty'),
            (0, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_pusher_rails_with_house'),
            (1, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_gas_plant_1'),
            (1, 1, 'coke_oven_tile_2', 'coke_oven_spritelayout_oven_battery_animated'),
            (1, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_pusher_rails_empty'),
            (2, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_coal_handling_rear'),
            (2, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_oven_battery_empty'),
            (2, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_pusher_rails_with_house'),
            (3, 0, 'coke_oven_tile_1', 'coke_oven_spritelayout_coal_handling_front'),
            (3, 1, 'coke_oven_tile_1', 'coke_oven_spritelayout_silo'),
            (3, 2, 'coke_oven_tile_1', 'coke_oven_spritelayout_pusher_rails_animated'),
            ]
)
