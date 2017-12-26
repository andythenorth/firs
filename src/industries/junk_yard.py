from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(id='junk_yard',
                                     prod_cargo_types=['SCMT'],
                                     prob_in_game='3',
                                     prob_random='7',
                                     prod_multiplier='[12, 0]',
                                     map_colour='64',
                                     # no industry location checks for junk yard, by design
                                     prospect_chance='0.75',
                                     name='string(STR_IND_JUNKYARD)',
                                     nearby_station_name='string(STR_STATION_BONEYARD)',
                                     fund_cost_multiplier='101',
                                     graphics_change_dates=[1949, 1960, 1980, 2000],
                                     intro_year=1850)

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['STEELTOWN'].enabled = True
industry.economy_variations['STEELTOWN'].prob_random = '14'

industry.add_tile(id='junk_yard_tile_1',
                  location_checks=TileLocationChecks(disallow_steep_slopes=True,
                                                     require_houses_nearby=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 55, -31, -24)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 55, -31, -24)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 55, -31, -24)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 55, -31, -24)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 55, -31, -24)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 55, -31, -24)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 55, -31, -24)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 55, -31, -24)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 55, -31, -24)],
)

industry.add_spritelayout(
    id='junk_yard_spritelayout_1',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id='junk_yard_spritelayout_2',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id='junk_yard_spritelayout_3',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id='junk_yard_spritelayout_4',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id='junk_yard_spritelayout_5',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
)
industry.add_spritelayout(
    id='junk_yard_spritelayout_6',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
)
industry.add_spritelayout(
    id='junk_yard_spritelayout_7',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
)
industry.add_spritelayout(
    id='junk_yard_spritelayout_8',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
)
industry.add_spritelayout(
    id='junk_yard_spritelayout_9',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
)

industry.add_industry_layout(
    id='junk_yard_industry_layout_1',
    layout=[(0, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_2'),
            (1, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_2'),
            (1, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_9'),
            (2, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_1'),
            (2, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_8'),
            (3, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_4'),
            (3, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_7'),
            (4, 0, 'junk_yard_tile_1', 'junk_yard_spritelayout_5'),
            (4, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_3'),
            (4, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_6'),
            ]
)
industry.add_industry_layout(
    id='junk_yard_industry_layout_2',
    layout=[(0, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_7'),
            (1, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_1'),
            (1, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_8'),
            (2, 0, 'junk_yard_tile_1', 'junk_yard_spritelayout_5'),
            (2, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_3'),
            (2, 2, 'junk_yard_tile_1', 'junk_yard_spritelayout_6'),
            ]
)
industry.add_industry_layout(
    id='junk_yard_industry_layout_3',
    layout=[(0, 3, 'junk_yard_tile_1', 'junk_yard_spritelayout_2'),
            (1, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_2'),
            (1, 3, 'junk_yard_tile_1', 'junk_yard_spritelayout_9'),
            (2, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_1'),
            (2, 3, 'junk_yard_tile_1', 'junk_yard_spritelayout_8'),
            (3, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_4'),
            (3, 3, 'junk_yard_tile_1', 'junk_yard_spritelayout_7'),
            (4, 0, 'junk_yard_tile_1', 'junk_yard_spritelayout_5'),
            (4, 1, 'junk_yard_tile_1', 'junk_yard_spritelayout_3'),
            (4, 3, 'junk_yard_tile_1', 'junk_yard_spritelayout_6'),
            ]
)
