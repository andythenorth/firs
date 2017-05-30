from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(id='diamond_mine',
                    map_colour='69',
                    prospect_chance='0.75',
                    prob_random='3',
                    prob_in_game='5',
                    layouts="AUTO",
                    override='INDUSTRYTYPE_DIAMOND_MINE',
                    prod_multiplier='[8]',
                    location_checks=dict(cluster=[70, 3]),
                    prod_cargo_types=['DIAM'],
                    substitute='INDUSTRYTYPE_DIAMOND_MINE',
                    name='TTD_STR_INDUSTRY_NAME_DIAMOND_MINE',
                    nearby_station_name='string(STR_STATION_KIMBERLITE_DEPOSITS)',
                    fund_cost_multiplier='232')

industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.add_tile(id='diamond_mine_tile_1',
                  animation_length=81,
                  animation_looping=True,
                  animation_speed=1,
                  custom_animation_next_frame='((animation_frame == 80) ? CB_RESULT_STOP_ANIMATION : CB_RESULT_NEXT_FRAME)',
                  custom_animation_control={'macro':'first_frame_is_0',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_TILE_LOOP)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

industry.add_tile(id='diamond_mine_tile_2',
                  animation_length=71,
                  animation_looping=True,
                  animation_speed=2,
                  custom_animation_control={'macro':'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
sprite_ground_overlay = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)

spriteset_headgear_animated = industry.add_spriteset(
    sprites = [(10, 160, 64, 122, -31, -88), (80, 160, 64, 122, -31, -88), (150, 160, 64, 122, -31, -88)],
    animation_rate = 1,
    custom_sprite_selector = '(animation_frame % 3)',
)
spriteset_crusher_front_part = industry.add_spriteset(
    sprites = [(10, 10, 64, 122, -31, -90)],
)
spriteset_crusher_rear_part = industry.add_spriteset(
    sprites = [(80, 10, 64, 122, -31, -74)],
)
spriteset_misc_building_tanks = industry.add_spriteset(
    sprites = [(150, 10, 64, 122, -31, -90)],
)
spriteset_ore_1 = industry.add_spriteset(
    sprites = [(220, 10, 64, 122, -31, -90)],
)
spriteset_ore_2 = industry.add_spriteset(
    sprites = [(290, 10, 64, 122, -31, -90)],
)
spriteset_winding_house = industry.add_spriteset(
    sprites = [(360, 10, 64, 122, -31, -90)],
)
spriteset_exit_trestle = industry.add_spriteset(
    sprites = [(430, 10, 64, 122, -31, -88)],
)
spriteset_exit_silo_conveyor = industry.add_spriteset(
    sprites = [(500, 10, 64, 122, -31, -90)],
)
spriteset_truck = industry.add_spriteset(
    sprites = [(570, 10, 64, 122, -31, -90)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_small',
    xoffset= -5,
    yoffset= 3,
    zoffset= 16,
)

industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_tile_empty',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_headgear_animated',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_headgear_animated],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_silos',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_exit_trestle],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_crusher_front_part',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_crusher_front_part],
    smoke_sprites = [sprite_smoke_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_crusher_rear_part',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_crusher_rear_part],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_misc_building_tanks',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_misc_building_tanks],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_ore_1',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_ore_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_ore_2',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_ore_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_winding_house',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_winding_house],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_silo_conveyor',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_exit_silo_conveyor],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_truck',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_truck],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'diamond_mine_industry_layout_1',
    layout = [(0, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_rear_part'),
              (0, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_headgear_animated'),
              (0, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_winding_house'),
              (1, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
              (1, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_ore_2'),
              (1, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_misc_building_tanks'),
              (2, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_front_part'),
              (2, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_ore_1'),
              (2, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
              (3, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_silos'),
              (3, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_silo_conveyor'),
              (3, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_truck'),
    ]
)

industry.add_industry_layout(
    id = 'diamond_mine_industry_layout_2',
    layout = [(0, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_rear_part'),
              (0, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_headgear_animated'),
              (0, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_winding_house'),
              (0, 3, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_headgear_animated'),
              (0, 4, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_winding_house'),
              (1, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
              (1, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_ore_2'),
              (1, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_misc_building_tanks'),
              (1, 3, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_truck'),
              (1, 4, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_ore_2'),
              (2, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_front_part'),
              (2, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_ore_1'),
              (2, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_silos'),
              (2, 3, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_silo_conveyor'),
              (2, 4, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_ore_1')
    ]
)

industry.add_industry_layout(
    id = 'diamond_mine_industry_layout_3',
    layout = [(0, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_headgear_animated'),
              (0, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_winding_house'),
              (1, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_silos'),
              (1, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_silo_conveyor'),
              (1, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_misc_building_tanks'),
              (2, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_misc_building_tanks'),
              (2, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_headgear_animated'),
              (2, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_winding_house'),
              (3, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_rear_part'),
              (3, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_rear_part'),
              (3, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_ore_2'),
              (4, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
              (4, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
              (4, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_ore_1'),
              (5, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_front_part'),
              (5, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_front_part'),
              (5, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_truck')
    ]
)

industry.add_industry_layout(
    id = 'diamond_mine_industry_layout_4',
    layout = [(0, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_headgear_animated'),
              (0, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_winding_house'),
              (0, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_rear_part'),
              (0, 3, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_rear_part'),
              (0, 4, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_ore_2'),
              (1, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_misc_building_tanks'),
              (1, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
              (1, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
              (1, 3, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
              (1, 4, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_ore_1'),
              (2, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_silos'),
              (2, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_silo_conveyor'),
              (2, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_front_part'),
              (2, 3, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_front_part'),
              (2, 4, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_truck')
    ]
)

