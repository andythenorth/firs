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
    default_spritelayout = 'bauxite_mine_spritelayout_1',
    layout = [(0, 0, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_1'),
              (0, 1, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_1'),
              (0, 2, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_1'),
              (2, 0, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_5'),
              (2, 1, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_3'),
              (2, 2, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_4'),
              (3, 0, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_1'),
              (3, 1, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_1'),
              (3, 2, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_2'),
              (4, 1, 'bauxite_mine_tile', 'bauxite_mine_spritelayout_1'),
    ]
)
# Templating
industry.render_and_save_pnml()
