from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(id='iron_ore_mine',
                                     map_colour='55',
                                     prob_in_game='4',
                                     prob_random='7',
                                     prospect_chance='0.75',
                                     name='TTD_STR_INDUSTRY_NAME_IRON_ORE_MINE',
                                     location_checks=dict(cluster=[70, 3]),
                                     prod_multiplier='[20]',
                                     prod_cargo_types=['IORE'],
                                     nearby_station_name='string(STR_STATION_IRONSTONE)',
                                     fund_cost_multiplier='232')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['STEELTOWN'].enabled = True
industry.economy_variations['STEELTOWN'].prob_random = '10'

industry.add_tile(id='iron_ore_mine_tile_1',
                  animation_length=81,
                  animation_looping=True,
                  animation_speed=1,
                  custom_animation_next_frame='((animation_frame == 80) ? CB_RESULT_STOP_ANIMATION : CB_RESULT_NEXT_FRAME)',
                  custom_animation_control={'macro': 'first_frame_is_0',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_TILE_LOOP)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

industry.add_tile(id='iron_ore_mine_tile_2',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  custom_animation_control={'macro': 'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

industry.add_tile(id='iron_ore_mine_tile_3',
                  animation_length=200,
                  animation_looping=True,
                  animation_speed=3,
                  custom_animation_next_frame='((animation_frame == 18) ? CB_RESULT_STOP_ANIMATION : CB_RESULT_NEXT_FRAME)',
                  custom_animation_control={'macro': 'first_frame_is_0',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_TILE_LOOP)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDTILE_MUD_TRACKS'
)
sprite_ground_overlay = industry.add_sprite(
    sprite_number='GROUNDTILE_MUD_TRACKS'
)

spriteset_headgear_animated = industry.add_spriteset(
    sprites=[(10, 310, 64, 122, -31, -88), (80, 310, 64, 122, -31, -88), (150, 310, 64, 122, -31, -88)],
    animation_rate=1,
    custom_sprite_selector='(animation_frame % 3)',
)
spriteset_exit_trestle_animated = industry.add_spriteset(
    sprites=[(10, 160, 64, 122, -31, -88), (80, 160, 64, 122, -31, -88), (150, 160, 64, 122, -31, -88),
             (220, 160, 64, 122, -31, -88), (290, 160, 64, 122, -31, -88), (360, 160, 64, 122, -31, -88),
             (430, 160, 64, 122, -31, -88), (500, 160, 64, 122, -31, -88), (500, 160, 64, 122, -31, -88),
             (570, 160, 64, 122, -31, -88), (570, 160, 64, 122, -31, -88), (640, 160, 64, 122, -31, -88),
             (640, 160, 64, 122, -31, -88), (710, 160, 64, 122, -31, -88), (780, 160, 64, 122, -31, -88),
             (850, 160, 64, 122, -31, -88), (920, 160, 64, 122, -31, -88), (990, 160, 64, 122, -31, -88),
             (1060, 160, 64, 122, -31, -88)],
    animation_rate=1,
)
spriteset_crusher_front_part = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -90)],
)
spriteset_crusher_rear_part = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -74)],
)
spriteset_ore_truck = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_joined_ore_front = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
)
spriteset_joined_ore_rear = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
)
spriteset_winding_house = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -90)],
)
spriteset_exit_shed_rear = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -90)],
)
spriteset_boiler_house = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -90)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=5,
    yoffset=6,
    zoffset=71,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=5,
    yoffset=11,
    zoffset=71,
    animation_frame_offset=1
)

industry.add_spritelayout(
    id='iron_ore_mine_spritelayout_tile_empty',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[],
)
industry.add_spritelayout(
    id='iron_ore_mine_spritelayout_headgear_animated',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_headgear_animated],
)
industry.add_spritelayout(
    id='iron_ore_mine_spritelayout_exit_trestle_animated',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_exit_trestle_animated],
)
industry.add_spritelayout(
    id='iron_ore_mine_spritelayout_crusher_front_part',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_crusher_front_part],
)
industry.add_spritelayout(
    id='iron_ore_mine_spritelayout_crusher_rear_part',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_crusher_rear_part],
)
industry.add_spritelayout(
    id='iron_ore_mine_spritelayout_ore_truck',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_ore_truck],
)
industry.add_spritelayout(
    id='iron_ore_mine_spritelayout_joined_ore_front',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_joined_ore_front],
)
industry.add_spritelayout(
    id='iron_ore_mine_spritelayout_joined_ore_rear',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_joined_ore_rear],
)
industry.add_spritelayout(
    id='iron_ore_mine_spritelayout_boiler_house',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_boiler_house],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
)
industry.add_spritelayout(
    id='iron_ore_mine_spritelayout_winding_house',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_winding_house],
)
industry.add_spritelayout(
    id='iron_ore_mine_spritelayout_exit_shed_rear',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_exit_shed_rear],
)

industry.add_industry_layout(
    id='iron_ore_mine_industry_layout_1',
    layout=[(0, 0, 'iron_ore_mine_tile_2', 'iron_ore_mine_spritelayout_winding_house'),
            (0, 1, 'iron_ore_mine_tile_1', 'iron_ore_mine_spritelayout_headgear_animated'),
            (0, 2, 'iron_ore_mine_tile_2', 'iron_ore_mine_spritelayout_crusher_rear_part'),
            (0, 3, 'iron_ore_mine_tile_2', 'iron_ore_mine_spritelayout_boiler_house'),
            (1, 0, 'iron_ore_mine_tile_2', 'iron_ore_mine_spritelayout_winding_house'),
            (1, 1, 'iron_ore_mine_tile_1', 'iron_ore_mine_spritelayout_headgear_animated'),
            (1, 2, 'iron_ore_mine_tile_2', 'iron_ore_mine_spritelayout_crusher_rear_part'),
            (1, 3, 'iron_ore_mine_tile_2', 'iron_ore_mine_spritelayout_ore_truck'),
            (2, 0, 'iron_ore_mine_tile_2', 'iron_ore_mine_spritelayout_joined_ore_rear'),
            (2, 1, 'iron_ore_mine_tile_2', 'iron_ore_mine_spritelayout_exit_shed_rear'),
            (2, 2, 'iron_ore_mine_tile_2', 'iron_ore_mine_spritelayout_tile_empty'),
            (2, 3, 'iron_ore_mine_tile_2', 'iron_ore_mine_spritelayout_joined_ore_rear'),
            (3, 0, 'iron_ore_mine_tile_2', 'iron_ore_mine_spritelayout_joined_ore_front'),
            (3, 1, 'iron_ore_mine_tile_3', 'iron_ore_mine_spritelayout_exit_trestle_animated'),
            (3, 2, 'iron_ore_mine_tile_2', 'iron_ore_mine_spritelayout_crusher_front_part'),
            (3, 3, 'iron_ore_mine_tile_2', 'iron_ore_mine_spritelayout_joined_ore_front'),
            ]
)
