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
                    nearby_station_name='string(STR_STATION_MINE)',
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

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
sprite_ground_overlay = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)

spriteset_1 = industry.add_spriteset(
    sprites = [(10, 10, 64, 110, -31, -70), (10, 130, 64, 110, -31, -70), (10, 250, 64, 110, -31, -70)],
    animation_rate = 1,
    custom_sprite_selector = '(animation_frame % 3)',
)
spriteset_2 = industry.add_spriteset(
    sprites = [(80, 10, 64, 110, -31, -70)],
    num_sprites_to_autofill = len(spriteset_1.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_3 = industry.add_spriteset(
    sprites = [(150, 10, 64, 64, -31, -30)],
    num_sprites_to_autofill = len(spriteset_1.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_4 = industry.add_spriteset(
    sprites = [(220, 10, 64, 64, -31, -33)],
    num_sprites_to_autofill = len(spriteset_1.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_5 = industry.add_spriteset(
    sprites = [(290, 10, 64, 64, -31, -33)],
    num_sprites_to_autofill = len(spriteset_1.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_6 = industry.add_spriteset(
    sprites = [(360, 10, 64, 64, -31, -33)],
    num_sprites_to_autofill = len(spriteset_1.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)

industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_1],
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_2],
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_3',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_3],
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_4',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_4],
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_5',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_5],
)
industry.add_spritelayout(
    id = 'diamond_mine_spritelayout_6',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground_overlay,
    building_sprites = [spriteset_6],
)

industry.add_industry_layout(
    id = 'diamond_mine_industry_layout_1',
    layout = [(0, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_1'),
              (0, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_2'),
              (0, 3, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_4'),
              (1, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_6'),
              (1, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_1'),
              (1, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_2'),
              (1, 3, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_3'),
              (2, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_5'),
              (2, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_4'),
              (2, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_3')
    ]
)
industry.add_industry_layout(
    id = 'diamond_mine_industry_layout_2',
    layout = [(0, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_1'),
              (0, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_2'),
              (0, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_6'),
              (1, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_3'),
              (1, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_3'),
              (1, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_5')
    ]
)
industry.add_industry_layout(
    id = 'diamond_mine_industry_layout_3',
    layout = [(0, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_4'),
              (1, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_4'),
              (1, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_1'),
              (1, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_2'),
              (2, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_6'),
              (2, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_5')
    ]
)
industry.add_industry_layout(
    id = 'diamond_mine_industry_layout_4',
    layout = [(0, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_3'),
              (0, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_4'),
              (0, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_4'),
              (1, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_3'),
              (1, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_1'),
              (1, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_2'),
              (2, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_1'),
              (2, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_2'),
              (2, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_6'),
              (3, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_3'),
              (3, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_4'),
              (3, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_5')
    ]
)
industry.add_industry_layout(
    id = 'diamond_mine_industry_layout_5',
    layout = [(0, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_4'),
              (0, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_6'),
              (1, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_3'),
              (1, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_5'),
              (2, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_1'),
              (2, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_2'),
              (3, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_1'),
              (3, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_2'),
              (4, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_3'),
              (4, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_4'),
    ]
)
industry.add_industry_layout(
    id = 'diamond_mine_industry_layout_6',
    layout = [(0, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_1'),
              (0, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_2'),
              (0, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_1'),
              (0, 3, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_2'),
              (0, 4, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_6'),
              (1, 0, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_3'),
              (1, 1, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_4'),
              (1, 2, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_3'),
              (1, 3, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_4'),
              (1, 4, 'diamond_mine_tile_1', 'diamond_mine_spritelayout_5')
    ]
)
