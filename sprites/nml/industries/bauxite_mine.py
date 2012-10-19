from firs import Industry, Tile, Sprite, Spriteset, SpriteLayout, IndustryLayout

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='bauxite_mine')

industry.add_tile(id='bauxite_mine_tile_pump')
industry.add_tile(id='bauxite_mine_tile_building')

spriteset_ground_pump = industry.add_spriteset(
    id = 'bauxite_mine_spriteset_ground_overlay_pump',
    type='empty',
)
sprite_ground_overlay_pump = industry.add_sprite(
    sprite_number = 2173
)
sprite_pump = industry.add_sprite(
    sprite_number = '2174 + (((animation_frame % 11) < 6) ? (animation_frame % 11) : 10 - (animation_frame % 11))',
    xoffset= 1,
    yoffset= 2,
    xextent= 15,
    yextent= 14
)
industry.add_spritelayout(
    id = 'bauxite_mine_spritelayout_pump',
    ground_sprite = spriteset_ground_pump,
    ground_overlay = sprite_ground_overlay_pump,
    building_sprites = [sprite_pump]
)

spriteset_ground_building = industry.add_spriteset(
    id = 'bauxite_mine_spriteset_ground_overlay_building',
    type='empty',
)
sprite_ground_overlay_building = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS',
)
spriteset_building = industry.add_spriteset(
    id = 'bauxite_mine_spriteset_building',
    sprites = [(10, 10, 64, 38, -31, -9)],
    xoffset= 1,
    yoffset= 2,
    xextent= 15,
    yextent= 14
)
industry.add_spritelayout(
    id = 'bauxite_mine_spritelayout_building',
    ground_sprite = spriteset_ground_building,
    ground_overlay = sprite_ground_overlay_building,
    building_sprites = [spriteset_building]
)


industry.add_industry_layout(
    id = 'bauxite_mine_industry_layout_1',
    default_spritelayout = 'bauxite_mine_spritelayout_pump',
    layout = [(0, 0, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (0, 7, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (1, 4, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (2, 1, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (3, 5, 'bauxite_mine_tile_building', 'bauxite_mine_spritelayout_building'),
              (4, 8, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (5, 1, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (5, 4, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
    ]
)
industry.add_industry_layout(
    id = 'bauxite_mine_industry_layout_2',
    default_spritelayout = 'bauxite_mine_spritelayout_pump',
    layout = [(0, 0, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (0, 4, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (1, 4, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (2, 8, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (4, 4, 'bauxite_mine_tile_building', 'bauxite_mine_spritelayout_building'),
              (4, 8, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (5, 2, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (6, 2, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (6, 4, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
    ]
)
industry.add_industry_layout(
    id = 'bauxite_mine_industry_layout_3',
    default_spritelayout = 'bauxite_mine_spritelayout_pump',
    layout = [(0, 0, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (0, 2, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (1, 4, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (1, 6, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (2, 0, 'bauxite_mine_tile_building', 'bauxite_mine_spritelayout_building'),
              (3, 2, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (3, 4, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
    ]
)
industry.add_industry_layout(
    id = 'bauxite_mine_industry_layout_4',
    default_spritelayout = 'bauxite_mine_spritelayout_pump',
    layout = [(0, 0, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (0, 4, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (0, 6, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (1, 2, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (1, 8, 'bauxite_mine_tile_building', 'bauxite_mine_spritelayout_building'),
              (2, 0, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (2, 2, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (3, 1, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (5, 0, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (5, 2, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
              (6, 0, 'bauxite_mine_tile_pump', 'bauxite_mine_spritelayout_pump'),
    ]
)
# Templating
industry.render_and_save_pnml()
