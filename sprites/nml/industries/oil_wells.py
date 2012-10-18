from firs import Industry, Tile, Sprite, Spriteset, SpriteLayout, IndustryLayout

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='oil_wells')

industry.add_tile(id='oil_wells_tile_pump')

spriteset_ground = industry.add_spriteset(
    id = 'oil_wells_spriteset_ground',
    type='empty',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'oil_wells_spriteset_ground_overlay',
    sprites = [(0, 0, 1, 1, 0, 0)], # no ground overlay needed, use a 1px sprite of blue
)
spriteset_1 = industry.add_spriteset(
    id = 'oil_wells_spriteset',
    sprites = [(10, 60, 64, 36, -31, -4)]
)
sprite_pump = industry.add_sprite(
    sprite_number = '2174 + (((animation_frame % 11) < 6) ? (animation_frame % 11) : 10 - (animation_frame % 11))',
    xoffset= 1,
    yoffset= 2,
    xextent= 15,
    yextent= 14
)

industry.add_spritelayout(
    id = 'oil_wells_spritelayout_pump',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1]
)

industry.add_industry_layout(
    id = 'oil_wells_industry_layout_1',
    default_spritelayout = 'oil_wells_spritelayout_pump',
    layout = [(0, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (0, 7, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (1, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (2, 1, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (3, 5, 'oil_wells_tile_building', 'oil_wells_spritelayout_pump'), #tile_building
              (4, 8, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (5, 1, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (5, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
    ]
)
industry.add_industry_layout(
    id = 'oil_wells_industry_layout_2',
    default_spritelayout = 'oil_wells_spritelayout_pump',
    layout = [(0, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (0, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (1, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (2, 8, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (4, 4, 'oil_wells_tile_building', 'oil_wells_spritelayout_pump'), #tile_building
              (4, 8, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (5, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (6, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (6, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
    ]
)
industry.add_industry_layout(
    id = 'oil_wells_industry_layout_3',
    default_spritelayout = 'oil_wells_spritelayout_pump',
    layout = [(0, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (0, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (1, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (1, 6, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (2, 0, 'oil_wells_tile_building', 'oil_wells_spritelayout_pump'), #tile_building
              (3, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (3, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
    ]
)
industry.add_industry_layout(
    id = 'oil_wells_industry_layout_4',
    default_spritelayout = 'oil_wells_spritelayout_pump',
    layout = [(0, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (0, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (0, 6, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (1, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (1, 8, 'oil_wells_tile_building', 'oil_wells_spritelayout_pump'), #tile_building
              (2, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (2, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (3, 1, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (5, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (5, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (6, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
    ]
)
# Templating
industry.render_and_save_pnml()
