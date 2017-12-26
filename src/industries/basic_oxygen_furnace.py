from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='basic_oxygen_furnace',
                             processed_cargos_and_output_ratios=[('IRON', 4), ('MNO2', 2), ('QLME', 2)],
                             combined_cargos_boost_prod=True,
                             prod_cargo_types=[('STEL', 6), ('SLAG', 2)],
                             prob_in_game='3',
                             prob_random='5',
                             prod_multiplier='[0, 0]',
                             map_colour='49',
                             spec_flags='bitmask(IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE)',
                             # it's rare to force co-location of secondaries, but this one is near blast furnace by design
                             location_checks=dict(industry_max_distance=['blast_furnace', 72], same_type_distance=72),
                             name='string(STR_IND_BASIC_OXYGEN_FURNACE)',
                             nearby_station_name='string(STR_STATION_FURNACE)',
                             fund_cost_multiplier='160',
                             intro_year=1850)  # intro year needs to >= Blast Furnace intro year, otherwise location restriction means no BOFs are built

industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='basic_oxygen_furnace_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  custom_animation_control={'macro': 'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDTILE_MUD_TRACKS'  # ground tile same as overlay tile
)
sprite_ground_overlay = industry.add_spriteset(
    type='empty',
)
# unused
"""
spriteset_roaster_1 = industry.add_spriteset(
    sprites = [(80, 10, 64, 122, -31, -90)],
)
spriteset_chimney = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
"""
spriteset_crane = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
)
spriteset_manganese_1 = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
)
spriteset_air_plant_2 = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -90)],
)
spriteset_furnace_1 = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -90)],
)
spriteset_metal_1 = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -90)],
)
spriteset_metal_2 = industry.add_spriteset(
    sprites=[(570, 10, 64, 122, -31, -90)],
)
spriteset_office = industry.add_spriteset(
    sprites=[(640, 10, 64, 122, -31, -90)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=1,
    yoffset=0,
    zoffset=64,
)

industry.add_spritelayout(
    id='basic_oxygen_furnace_spritelayout_empty',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='basic_oxygen_furnace_spritelayout_metal_2',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_metal_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='basic_oxygen_furnace_spritelayout_crane',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_crane],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='basic_oxygen_furnace_spritelayout_manganese_1',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_manganese_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='basic_oxygen_furnace_spritelayout_air_plant_2',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_air_plant_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='basic_oxygen_furnace_spritelayout_furnace_1',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_furnace_1],
    smoke_sprites=[sprite_smoke],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='basic_oxygen_furnace_spritelayout_metal_1',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_metal_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='basic_oxygen_furnace_spritelayout_office',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_office],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='basic_oxygen_furnace_industry_layout_1',
    layout=[(0, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (0, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (0, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (0, 3, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (0, 4, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (1, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_crane'),
            (1, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (1, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (1, 3, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (1, 4, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_air_plant_2'),
            (2, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_office'),
            (2, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_metal_2'),
            (2, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_metal_1'),
            (2, 3, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (2, 4, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_manganese_1'),
            ]
)
industry.add_industry_layout(
    id='basic_oxygen_furnace_industry_layout_2',
    layout=[(0, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (0, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (0, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (0, 3, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_air_plant_2'),
            (1, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (1, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (1, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (1, 3, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_manganese_1'),
            (2, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (2, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_crane'),
            (2, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (2, 3, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (3, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_metal_2'),
            (3, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_metal_1'),
            (3, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (3, 3, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_office'),
            ]
)
industry.add_industry_layout(
    id='basic_oxygen_furnace_industry_layout_3',
    layout=[(0, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (0, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (0, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (1, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (1, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (1, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (2, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_crane'),
            (2, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (2, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (3, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_air_plant_2'),
            (3, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_metal_2'),
            (3, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_metal_1'),
            (4, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_manganese_1'),
            (4, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (4, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_office'),
            ]
)
industry.add_industry_layout(
    id='basic_oxygen_furnace_industry_layout_4',
    layout=[(0, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (0, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (0, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_crane'),
            (1, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (1, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (1, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_manganese_1'),
            (2, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (2, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (2, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_air_plant_2'),
            (3, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_furnace_1'),
            (3, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            (3, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_office'),
            (4, 0, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_metal_1'),
            (4, 1, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_metal_2'),
            (4, 2, 'basic_oxygen_furnace_tile_1', 'basic_oxygen_furnace_spritelayout_empty'),
            ]
)
