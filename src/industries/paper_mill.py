from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='paper_mill',
                             processed_cargos_and_output_ratios=[('CLAY', 2), ('WOOD', 4), ('RFPR', 2)],
                             combined_cargos_boost_prod=True,
                             prod_cargo_types=['GOOD', 'MNSP'],
                             prob_in_game='3',
                             prob_random='5',
                             prod_multiplier='[0, 0]',
                             substitute='14',
                             map_colour='164',
                             fund_cost_multiplier='120',
                             nearby_station_name='string(STR_STATION_MILL)',
                             name='TTD_STR_INDUSTRY_NAME_PAPER_MILL',
                             override='14')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].prod_cargo_types = ['PAPR']
industry.economy_variations['BASIC_ARCTIC'].processed_cargos_and_output_ratios = [('KAOL', 2), ('WOOD', 4), ('SULP', 2)]

# industry uses layouts and sprites from default game, no custom layouts etc

industry.add_tile(id='paper_mill_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type='concrete'
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
# spriteset_1 deprecated
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -33)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -33)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -33)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -33)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -33)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(10, 84, 64, 120, -31, -89)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(80, 84, 64, 120, -31, -89)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(150, 84, 64, 120, -31, -89)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(220, 84, 64, 120, -31, -89)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=10,
    yoffset=0,
    zoffset=93,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type='white_smoke_big',
    xoffset=6,
    yoffset=0,
    zoffset=79,
    animation_frame_offset=1
)

industry.add_spritelayout(
    id='paper_mill_spritelayout_paper_store_empty',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id='paper_mill_spritelayout_paper_store_full',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id='paper_mill_spritelayout_wood_store_forklift',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id='paper_mill_spritelayout_wood_store_full',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
)
industry.add_spritelayout(
    id='paper_mill_spritelayout_chemical_tanks',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
)
industry.add_spritelayout(
    id='paper_mill_spritelayout_tall_building_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
)
industry.add_spritelayout(
    id='paper_mill_spritelayout_tall_building_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
)
industry.add_spritelayout(
    id='paper_mill_spritelayout_pulp_processor',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
)
industry.add_spritelayout(
    id='paper_mill_spritelayout_boilerhouse',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2]
)

industry.add_industry_layout(
    id='paper_mill_industry_layout_1',
    layout=[(0, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_1'),
            (0, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_1'),
            (0, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_paper_store_full'),
            (1, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_2'),
            (1, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_pulp_processor'),
            (1, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_paper_store_empty'),
            (2, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_1'),
            (2, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_chemical_tanks'),
            (2, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_paper_store_full'),
            (3, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_2'),
            (3, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_forklift'),
            (3, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_full'),
            (4, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_boilerhouse'),
            (4, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_full'),
            (4, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_forklift')
            ]
)
industry.add_industry_layout(
    id='paper_mill_industry_layout_2',
    layout=[(0, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_1'),
            (0, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_1'),
            (0, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_chemical_tanks'),
            (1, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_2'),
            (1, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_2'),
            (1, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_paper_store_empty'),
            (2, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_boilerhouse'),
            (2, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_pulp_processor'),
            (2, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_paper_store_full'),
            (3, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_forklift'),
            (3, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_full'),
            (3, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_full'),
            ]
)
industry.add_industry_layout(
    id='paper_mill_industry_layout_3',
    layout=[(0, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_1'),
            (0, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_1'),
            (0, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_pulp_processor'),
            (0, 3, 'paper_mill_tile_1', 'paper_mill_spritelayout_chemical_tanks'),
            (1, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_2'),
            (1, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_2'),
            (1, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_boilerhouse'),
            (1, 3, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_forklift'),
            (2, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_paper_store_full'),
            (2, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_paper_store_empty'),
            (2, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_forklift'),
            (2, 3, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_full'),
            ]
)
industry.add_industry_layout(
    id='paper_mill_industry_layout_4',
    layout=[(0, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_1'),
            (0, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_1'),
            (0, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_2'),
            (0, 3, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_forklift'),
            (1, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_2'),
            (1, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_tall_building_2'),
            (1, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_boilerhouse'),
            (1, 3, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_full'),
            (2, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_pulp_processor'),
            (2, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_paper_store_full'),
            (2, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_forklift'),
            (2, 3, 'paper_mill_tile_1', 'paper_mill_spritelayout_wood_store_full'),
            (3, 0, 'paper_mill_tile_1', 'paper_mill_spritelayout_chemical_tanks'),
            (3, 1, 'paper_mill_tile_1', 'paper_mill_spritelayout_paper_store_empty'),
            (3, 2, 'paper_mill_tile_1', 'paper_mill_spritelayout_paper_store_full'),
            ]
)
