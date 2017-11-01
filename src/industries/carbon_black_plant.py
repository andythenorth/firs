from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='carbon_black_plant',
                    processed_cargos_and_output_ratios=[('PETR', 8)],
                    prod_cargo_types=['CBLK'],
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    map_colour='209',
                    spec_flags='bitmask(IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE)',
                    name='string(STR_IND_CARBON_BLACK_PLANT)',
                    nearby_station_name='string(STR_STATION_STACKS)',
                    fund_cost_multiplier='120')

industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='carbon_black_plant_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  custom_animation_control={'macro':'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type='cobble',
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty',
)

spriteset_1 = industry.add_spriteset(
    sprites = [(10, 10, 64, 101, -31, -64)],
)
spriteset_2 = industry.add_spriteset(
    sprites = [(80, 10, 64, 101, -31, -59)],
)
spriteset_3 = industry.add_spriteset(
    sprites = [(150, 10, 64, 101, -31, -71)],
)
spriteset_4 = industry.add_spriteset(
    sprites = [(220, 10, 64, 101, -31, -69)],
)
spriteset_sand_staithe = industry.add_spriteset(
    sprites = [(290, 10, 64, 31, -31, 0)],
)
spriteset_clay_staithe = industry.add_spriteset(
    sprites = [(360, 10, 64, 31, -31, 0)],
)
sprite_smoke_boilerhouse = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 8,
    yoffset= 0,
    zoffset= 70,
)
sprite_smoke_kiln = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 0,
    yoffset= 8,
    zoffset= 58,
)

industry.add_spritelayout(
    id = 'carbon_black_plant_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    smoke_sprites = [sprite_smoke_boilerhouse],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'carbon_black_plant_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'carbon_black_plant_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    smoke_sprites = [sprite_smoke_kiln],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'carbon_black_plant_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'carbon_black_plant_spritelayout_sand_staithe',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_sand_staithe],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'carbon_black_plant_spritelayout_clay_staithe',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_clay_staithe],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'carbon_black_plant_industry_layout_1',
    layout = [(0, 0, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_4'),
              (0, 1, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_4'),
              (1, 0, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_3'),
              (1, 1, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_3'),
              (2, 0, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_2'),
              (2, 1, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_1'),
              (3, 0, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_clay_staithe'),
              (3, 1, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_sand_staithe'),
    ]
)
industry.add_industry_layout(
    id = 'carbon_black_plant_industry_layout_2',
    layout = [(0, 0, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_4'),
              (0, 1, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_4'),
              (1, 0, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_3'),
              (1, 1, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_3'),
              (2, 0, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_2'),
              (2, 1, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_clay_staithe'),
              (3, 0, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_1'),
              (3, 1, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_sand_staithe'),
    ]
)
industry.add_industry_layout(
    id = 'carbon_black_plant_industry_layout_3',
    layout = [(0, 0, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_4'),
              (0, 1, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_4'),
              (0, 2, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_1'),
              (0, 3, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_clay_staithe'),
              (1, 0, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_3'),
              (1, 1, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_3'),
              (1, 2, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_2'),
              (1, 3, 'carbon_black_plant_tile_1', 'carbon_black_plant_spritelayout_sand_staithe'),
    ]
)
