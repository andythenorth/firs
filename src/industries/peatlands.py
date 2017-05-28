from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(id='peatlands',
                    prod_cargo_types=['PEAT'],
                    prob_in_game='4',
                    prob_random='7',
                    prod_multiplier='[14, 14]',
                    map_colour='93',
                    # allow longer distance on clustering than usual, and more clusters, as industry is hard to locate
                    location_checks=dict(cluster=[90, 4]),
                    prospect_chance='0.75',
                    name='string(STR_IND_PEATLANDS)',
                    nearby_station_name='string(STR_IND_PEATLANDS)',
                    fund_cost_multiplier='210')

industry.economy_variations['BASIC_ARCTIC'].enabled = True

# 2 tiles for this industry: pit outer tile cannot be on slopes; pit inner tiles and processor tiles can be
# cases for both tiles ensure that tiles can only be built at same height as north tile
industry.add_tile(id='peatlands_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_desert=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = '4126'
)
spriteset_1 = industry.add_spriteset(
    sprites = [(10, 90, 64, 31, -31, 0)],
)
spriteset_2 = industry.add_spriteset(
    sprites = [(80, 90, 64, 31, -31, 0)],
)
industry.add_spritelayout(
    id = 'peatlands_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground,
    building_sprites = [],
    terrain_aware_ground = True,
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'peatlands_layout_1',
    layout = [(0, 1, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (0, 2, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (0, 3, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (1, 0, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (1, 1, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (1, 2, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (1, 3, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (2, 0, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (2, 1, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (2, 2, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (2, 3, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (3, 0, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (3, 1, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (3, 2, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (3, 3, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (4, 1, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (4, 2, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
              (4, 3, 'peatlands_tile_1', 'peatlands_spritelayout_1'),
    ]
)