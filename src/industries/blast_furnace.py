from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='blast_furnace',
                             processed_cargos_and_output_ratios=[('IORE', 3), ('COAL', 2), ('SCMT', 3)],
                             combined_cargos_boost_prod=True,
                             prod_cargo_types=['METL'],
                             prob_in_game='3',
                             prob_random='5',
                             prod_multiplier='[0, 0]',
                             map_colour='10',
                             spec_flags='bitmask()',
                             name='TTD_STR_INDUSTRY_NAME_STEEL_MILL',  # default to steel mill
                             nearby_station_name='string(STR_STATION_FURNACE)',
                             fund_cost_multiplier='190',
                             intro_year=1850)


industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].intro_year = 1800
industry.economy_variations['BASIC_TEMPERATE'].prod_cargo_types = ['STEL']
industry.economy_variations['STEELTOWN'].enabled = True
industry.economy_variations['STEELTOWN'].name = 'string(STR_IND_BLAST_FURNACE)'
industry.economy_variations['STEELTOWN'].processed_cargos_and_output_ratios = [('IORE', 3), ('COKE', 3), ('LIME', 2)]
industry.economy_variations['STEELTOWN'].prod_cargo_types = [('IRON', 6), ('SLAG', 2)]
industry.economy_variations['STEELTOWN'].prob_random = '3'

industry.add_tile(id='blast_furnace_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  custom_animation_control={'macro': 'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

industry.add_tile(id='blast_furnace_tile_2',
                  animation_length=30,
                  animation_looping=True,
                  animation_speed=4,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDTILE_MUD_TRACKS'  # ground tile same as overlay tile
)
sprite_ground_overlay = industry.add_spriteset(
    type='empty',
)
spriteset_ground_tile_dark = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -91)],
)
spriteset_greeble = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -91)],
)
spriteset_blast_furnace_2 = industry.add_spriteset(
    sprites=[(10, 10, 64, 144, -31, -114)],
)
spriteset_blast_furnace_1 = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -91)],
)
spriteset_small_shed = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -91)],
)
spriteset_ladle_transporter = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -91)],
)
spriteset_brick_building = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -91)],
)
spriteset_small_tanks = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -91)],
)
spriteset_large_shed_rear_part = industry.add_spriteset(
    sprites=[(570, 10, 64, 122, -31, -91)],
)
spriteset_large_shed_front_part_animated = industry.add_spriteset(
    sprites=[(10, 160, 64, 122, -31, -91), (80, 160, 64, 122, -31, -91), (150, 160, 64, 122, -31, -91),
             (220, 160, 64, 122, -31, -91), (290, 160, 64, 122, -31, -91), (360, 160, 64, 122, -31, -91),
             (430, 160, 64, 122, -31, -91), (500, 160, 64, 122, -31, -91), (570, 160, 64, 122, -31, -91),
             (640, 160, 64, 122, -31, -91)],
    animation_rate=1,
    custom_sprite_selector='(animation_frame < 10) ? (animation_frame % 10) : 0',
)
spriteset_ground_tile_dark_animated = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -91)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_large_shed_front_part_animated.sprites),
)
spriteset_casting_shed_animated = industry.add_spriteset(
    sprites=[(10, 310, 64, 122, -31, -91), (80, 310, 64, 122, -31, -91), (150, 310, 64, 122, -31, -91),
             (220, 310, 64, 122, -31, -91), (290, 310, 64, 122, -31, -91), (360, 310, 64, 122, -31, -91),
             (430, 310, 64, 122, -31, -91), (500, 310, 64, 122, -31, -91), (570, 310, 64, 122, -31, -91),
             (640, 310, 64, 122, -31, -91)],
    animation_rate=1,
    custom_sprite_selector='(animation_frame < 10) ? (animation_frame % 10) : 0',
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=5,
    yoffset=6,
    zoffset=68,
)

industry.add_spritelayout(
    id='blast_furnace_spritelayout_empty',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[],
)
industry.add_spritelayout(
    id='blast_furnace_spritelayout_greeble',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_greeble],
)
industry.add_spritelayout(
    id='blast_furnace_spritelayout_blast_furnace_1',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_blast_furnace_1],
    smoke_sprites=[sprite_smoke],
)
industry.add_spritelayout(
    id='blast_furnace_spritelayout_blast_furnace_2',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_blast_furnace_2],
)
industry.add_spritelayout(
    id='blast_furnace_spritelayout_small_shed',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_small_shed],
)
industry.add_spritelayout(
    id='blast_furnace_spritelayout_ladle_transporter',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_ladle_transporter],
)
industry.add_spritelayout(
    id='blast_furnace_spritelayout_brick_building',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_brick_building],
)
industry.add_spritelayout(
    id='blast_furnace_spritelayout_small_tanks',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_small_tanks],
)
industry.add_spritelayout(
    id='blast_furnace_spritelayout_large_shed_rear_part',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_large_shed_rear_part],
)
industry.add_spritelayout(
    id='blast_furnace_spritelayout_large_shed_front_part',
    ground_sprite=spriteset_ground_tile_dark_animated,
    ground_overlay=spriteset_ground_tile_dark_animated,
    building_sprites=[spriteset_large_shed_front_part_animated],
)
industry.add_spritelayout(
    id='blast_furnace_spritelayout_casting_shed',
    ground_sprite=spriteset_ground_tile_dark_animated,
    ground_overlay=spriteset_ground_tile_dark_animated,
    building_sprites=[spriteset_casting_shed_animated],
)
industry.add_industry_layout(
    id='blast_furnace_industry_layout_1',
    layout=[(0, 0, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_small_shed'),
            (0, 1, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_empty'),
            (0, 2, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_large_shed_rear_part'),
            (1, 0, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_small_tanks'),
            (1, 1, 'blast_furnace_tile_2', 'blast_furnace_spritelayout_casting_shed'),
            (1, 2, 'blast_furnace_tile_2', 'blast_furnace_spritelayout_large_shed_front_part'),
            (2, 0, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_blast_furnace_1'),
            (2, 1, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_blast_furnace_2'),
            (2, 2, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_ladle_transporter'),
            (3, 0, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_blast_furnace_1'),
            (3, 1, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_blast_furnace_2'),
            (3, 2, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_small_shed'),
            (4, 0, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_small_tanks'),
            (4, 1, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_brick_building'),
            (4, 2, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_greeble'),
            ]
)
industry.add_industry_layout(
    id='blast_furnace_industry_layout_2',
    layout=[(0, 0, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_small_tanks'),
            (0, 1, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_large_shed_rear_part'),
            (0, 2, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_small_shed'),
            (0, 3, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_blast_furnace_1'),
            (0, 4, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_blast_furnace_2'),
            (1, 0, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_casting_shed'),
            (1, 1, 'blast_furnace_tile_2', 'blast_furnace_spritelayout_large_shed_front_part'),
            (1, 2, 'blast_furnace_tile_2', 'blast_furnace_spritelayout_blast_furnace_1'),
            (1, 3, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_blast_furnace_2'),
            (1, 4, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_brick_building'),
            (2, 0, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_empty'),
            (2, 1, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_large_shed_rear_part'),
            (2, 2, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_blast_furnace_1'),
            (2, 3, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_blast_furnace_2'),
            (2, 4, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_small_shed'),
            (3, 0, 'blast_furnace_tile_2', 'blast_furnace_spritelayout_casting_shed'),
            (3, 1, 'blast_furnace_tile_2', 'blast_furnace_spritelayout_large_shed_front_part'),
            (3, 2, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_ladle_transporter'),
            (3, 3, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_empty'),
            (3, 4, 'blast_furnace_tile_1', 'blast_furnace_spritelayout_greeble'),
            ]
)
