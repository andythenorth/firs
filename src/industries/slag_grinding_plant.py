from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='slag_grinding_plant',
                             accept_cargos_with_input_ratios=[('SLAG', 8)],
                             prod_cargo_types_with_output_ratios=[('CMNT', 4), ('FMSP', 4)],
                             prob_in_game='3',
                             prob_random='5',
                             map_colour='19',
                             special_flags=['IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE'],
                             # it's rare to force co-location of secondaries, but this one is near blast furnace by design
                             location_checks=dict(industry_max_distance=['blast_furnace', 72], same_type_distance=72),
                             name='string(STR_IND_SLAG_GRINDING_PLANT)',
                             nearby_station_name='string(STR_STATION_SILO)',
                             fund_cost_multiplier='100 ')

industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='slag_grinding_plant_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type='concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_silos = industry.add_spriteset(
    sprites=[(10, 10, 64, 120, -31, -89)],
)
spriteset_large_shed = industry.add_spriteset(
    sprites=[(80, 10, 64, 120, -31, -89)],
)
spriteset_grinding_tower = industry.add_spriteset(
    sprites=[(150, 10, 64, 120, -31, -89)],
)
spriteset_conveyors_1 = industry.add_spriteset(
    sprites=[(220, 10, 64, 120, -31, -89)],
)
spriteset_conveyors_2 = industry.add_spriteset(
    sprites=[(290, 10, 64, 120, -31, -89)],
)
spriteset_slag_dump_1 = industry.add_spriteset(
    sprites=[(360, 10, 64, 120, -31, -89)],
)
spriteset_slag_dump_2 = industry.add_spriteset(
    sprites=[(430, 10, 64, 120, -31, -89)],
)
# non-standard offsets to position crane over slag pit, may be regrettable
spriteset_crane = industry.add_spriteset(
    sprites=[(500, 10, 64, 120, -1, -89)],
)
spriteset_office = industry.add_spriteset(
    sprites=[(570, 10, 64, 120, -31, -89)],
)
spriteset_slag_dozer = industry.add_spriteset(
    sprites=[(10, 140, 64, 64, -31, -31)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=1,
    yoffset=0,
    zoffset=62,
    animation_frame_offset=1
)

industry.add_spritelayout(
    id='slag_grinding_plant_spritelayout_tile_empty',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
)
industry.add_spritelayout(
    id='slag_grinding_plant_spritelayout_large_silo',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_silos],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='slag_grinding_plant_spritelayout_large_shed',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_shed],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='slag_grinding_plant_spritelayout_grinding_tower',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_grinding_tower],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='slag_grinding_plant_spritelayout_conveyors_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_conveyors_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='slag_grinding_plant_spritelayout_conveyors_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_conveyors_2, spriteset_crane],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='slag_grinding_plant_spritelayout_slag_dump_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_slag_dump_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='slag_grinding_plant_spritelayout_slag_dump_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_slag_dump_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='slag_grinding_plant_spritelayout_slag_dump_3',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_slag_dump_1, spriteset_slag_dozer],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='slag_grinding_plant_spritelayout_office',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_office],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='slag_grinding_plant_industry_layout_1',
    layout=[(0, 0, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_slag_dump_3'),
            (0, 1, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_slag_dump_2'),
            (0, 2, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_slag_dump_1'),
            (0, 3, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_slag_dump_2'),
            (1, 0, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_tile_empty'),
            (1, 1, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_tile_empty'),
            (1, 2, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_tile_empty'),
            (1, 3, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_conveyors_2'),
            (2, 0, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_large_silo'),
            (2, 1, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_large_shed'),
            (2, 2, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_grinding_tower'),
            (2, 3, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_conveyors_1'),
            (3, 0, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_large_silo'),
            (3, 1, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_large_shed'),
            (3, 2, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_tile_empty'),
            (3, 3, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_office'),]
)
industry.add_industry_layout(
    id='slag_grinding_plant_industry_layout_2',
    layout=[(0, 0, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_slag_dump_3'),
            (0, 1, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_slag_dump_2'),
            (0, 2, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_slag_dump_1'),
            (0, 3, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_slag_dump_2'),
            (1, 0, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_tile_empty'),
            (1, 1, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_tile_empty'),
            (1, 2, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_tile_empty'),
            (1, 3, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_conveyors_2'),
            (2, 0, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_large_shed'),
            (2, 1, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_large_shed'),
            (2, 2, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_grinding_tower'),
            (2, 3, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_conveyors_1'),
            (3, 0, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_large_silo'),
            (3, 1, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_large_silo'),
            (3, 2, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_tile_empty'),
            (3, 3, 'slag_grinding_plant_tile_1', 'slag_grinding_plant_spritelayout_office'),]
)
