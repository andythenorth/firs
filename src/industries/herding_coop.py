from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(id='herding_coop',
                    prod_cargo_types=['FOOD'],
                    prob_in_game='14',
                    prob_random='14',
                    prod_multiplier='[5, 0]',
                    map_colour='86',
                    spec_flags='bitmask(IND_FLAG_NO_PRODUCTION_INCREASE)',
                    # herding_coop doesn't cluster, by design - no industry location checks needed
                    prospect_chance='0.75',
                    name='string(STR_IND_HERDING_COOP)',
                    extra_text_fund='string(STR_FUND_HERDING_COOP)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_HERDING_COOP))',
                    fund_cost_multiplier='88')

industry.economy_variations['BASIC_ARCTIC'].enabled = True

industry.add_tile(id='herding_coop_tile_1',
                  location_checks=TileLocationChecks(disallow_desert=True,
                                                     disallow_coast=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    type = 'empty'
)
sprite_ground_mud = industry.add_sprite(
    sprite_number = 'GROUNDSPRITE_CLEARED'
)
spriteset_ground_overlay = industry.add_spriteset(
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    sprites = [(10, 10, 64, 52, -31, -21)],
)
spriteset_1_ground = industry.add_spriteset(
    sprites = [(10, 70, 64, 52, -31, -21)],
)
spriteset_2 = industry.add_spriteset(
    sprites = [(80, 10, 64, 52, -31, -21)],
)
spriteset_2_ground = industry.add_spriteset(
    sprites = [(80, 70, 64, 52, -31, -21)],
)

industry.add_spritelayout(
    id = 'herding_coop_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_1_ground,
    building_sprites = [spriteset_1],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'herding_coop_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_2_ground,
    building_sprites = [spriteset_2],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'herding_coop_spritelayout_3',
    ground_sprite = sprite_ground_mud,
    ground_overlay = sprite_ground_mud,
    building_sprites = [],
    terrain_aware_ground = True
)

industry.add_industry_layout(
    id = 'herding_coop_industry_layout_1',
    layout = [(0, 1, 'herding_coop_tile_1', 'herding_coop_spritelayout_3'),
              (0, 2, 'herding_coop_tile_1', 'herding_coop_spritelayout_1'),
              (1, 0, 'herding_coop_tile_1', 'herding_coop_spritelayout_2'),
              (1, 2, 'herding_coop_tile_1', 'herding_coop_spritelayout_2'),
    ]
)
industry.add_industry_layout(
    id = 'herding_coop_industry_layout_2',
    layout = [(0, 0, 'herding_coop_tile_1', 'herding_coop_spritelayout_2'),
              (0, 1, 'herding_coop_tile_1', 'herding_coop_spritelayout_2'),
              (0, 2, 'herding_coop_tile_1', 'herding_coop_spritelayout_1'),
              (1, 0, 'herding_coop_tile_1', 'herding_coop_spritelayout_3'),
    ]
)
industry.add_industry_layout(
    id = 'herding_coop_industry_layout_3',
    layout = [(0, 0, 'herding_coop_tile_1', 'herding_coop_spritelayout_2'),
              (0, 1, 'herding_coop_tile_1', 'herding_coop_spritelayout_1'),
              (1, 0, 'herding_coop_tile_1', 'herding_coop_spritelayout_2'),
              (1, 2, 'herding_coop_tile_1', 'herding_coop_spritelayout_3'),
    ]
)
