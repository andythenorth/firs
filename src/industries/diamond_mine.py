from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(id='diamond_mine',
                                     prod_cargo_types_with_multipliers=[('DIAM', 12)],
                                     map_colour='69',
                                     prospect_chance='0.75',
                                     prob_map_gen='4',
                                     prob_in_game='7',
                                     layouts="AUTO",
                                     override='INDUSTRYTYPE_DIAMOND_MINE',
                                     # diamond mine doesn't cluster, by design - no industry location checks needed
                                     substitute='INDUSTRYTYPE_DIAMOND_MINE',
                                     name='TTD_STR_INDUSTRY_NAME_DIAMOND_MINE',
                                     nearby_station_name='string(STR_STATION_KIMBERLITE_DEPOSITS)',
                                     fund_cost_multiplier='232')

#industry.economy_variations['IN_A_HOT_COUNTRY'].enabled = True

industry.add_tile(id='diamond_mine_tile_1',
                  animation_length=81,
                  animation_looping=True,
                  animation_speed=1,
                  custom_animation_next_frame='((animation_frame == 80) ? CB_RESULT_STOP_ANIMATION : CB_RESULT_NEXT_FRAME)',
                  custom_animation_control={'macro': 'first_frame_is_0',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_TILE_LOOP)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

industry.add_tile(id='diamond_mine_tile_2',
                  animation_length=71,
                  animation_looping=True,
                  animation_speed=2,
                  custom_animation_control={'macro': 'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDTILE_MUD_TRACKS'
)
sprite_ground_overlay = industry.add_sprite(
    sprite_number='GROUNDTILE_MUD_TRACKS'
)

spriteset_headgear_animated = industry.add_spriteset(
    sprites=[(10, 160, 64, 122, -31, -88), (80, 160, 64, 122, -31, -88), (150, 160, 64, 122, -31, -88)],
    animation_rate=1,
    custom_sprite_selector='(animation_frame % 3)',
)
spriteset_crusher_front_part = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -90)],
)
spriteset_crusher_rear_part = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -74)],
)
spriteset_misc_building = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_vents_shed = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
)
spriteset_winding_house = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type='white_smoke_small',
    xoffset=-5,
    yoffset=3,
    zoffset=16,
)

industry.add_spritelayout(
    id='diamond_mine_spritelayout_tile_empty',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='diamond_mine_spritelayout_headgear_animated',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_headgear_animated],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='diamond_mine_spritelayout_crusher_front_part',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_crusher_front_part],
    smoke_sprites=[sprite_smoke_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='diamond_mine_spritelayout_crusher_rear_part',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_crusher_rear_part],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='diamond_mine_spritelayout_misc_building',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_misc_building],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='diamond_mine_spritelayout_vents_shed',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_vents_shed],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='diamond_mine_spritelayout_winding_house',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_winding_house],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='diamond_mine_industry_layout_1',
    layout=[(0, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_rear_part'),
            (0, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_headgear_animated'),
            (0, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_winding_house'),
            (1, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
            (1, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_misc_building'),
            (1, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_misc_building'),
            (2, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_front_part'),
            (2, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_vents_shed'),
            (2, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
            ]
)

industry.add_industry_layout(
    id='diamond_mine_industry_layout_2',
    layout=[(0, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_rear_part'),
            (0, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_headgear_animated'),
            (0, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_winding_house'),
            (0, 3, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_vents_shed'),
            (1, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
            (1, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_misc_building'),
            (1, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_headgear_animated'),
            (1, 3, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_winding_house'),
            (2, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_front_part'),
            (2, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_vents_shed'),
            (2, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
            (2, 3, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_misc_building')
            ]
)

industry.add_industry_layout(
    id='diamond_mine_industry_layout_3',
    layout=[(0, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_misc_building'),
            (0, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_headgear_animated'),
            (0, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_winding_house'),
            (1, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_rear_part'),
            (1, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_rear_part'),
            (1, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_misc_building'),
            (2, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
            (2, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
            (2, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_vents_shed'),
            (3, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_front_part'),
            (3, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_front_part'),
            (3, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
            ]
)

industry.add_industry_layout(
    id='diamond_mine_industry_layout_4',
    layout=[(0, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_headgear_animated'),
            (0, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_winding_house'),
            (0, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_rear_part'),
            (0, 3, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_rear_part'),
            (0, 4, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_misc_building'),
            (1, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_headgear_animated'),
            (1, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_winding_house'),
            (1, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
            (1, 3, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
            (1, 4, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_tile_empty'),
            (2, 0, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_misc_building'),
            (2, 1, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_vents_shed'),
            (2, 2, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_front_part'),
            (2, 3, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_crusher_front_part'),
            (2, 4, 'diamond_mine_tile_2', 'diamond_mine_spritelayout_vents_shed'),
            ]
)
