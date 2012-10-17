from firs import Industry, Tile, Spriteset, SpriteLayout, IndustryLayout

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='grain_mill')

industry.add_tile(id='grain_mill_tile')

spriteset_ground_bakery = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_bakery',
    type='cobble',
)
spriteset_ground_overlay_1 = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_1',
    sprites = [(10, 10, 64, 31, -31, 0)],
)
spriteset_ground_overlay_2 = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_2',
    sprites = [(80, 10, 64, 31, -31, 0)]
)
spriteset_ground_overlay_3 = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_3',
    sprites = [(150, 10, 64, 31, -31, 0)]
)
spriteset_ground_overlay_4 = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_4',
    sprites = [(220, 10, 64, 31, -31, 0)]
)
spriteset_1 = industry.add_spriteset(
    id = 'grain_mill_spriteset_1',
    sprites = [(10, 10, 64, 31, -31, 0)]
)
spriteset_2 = industry.add_spriteset(
    id = 'grain_mill_spriteset_2',
    sprites = [(80, 10, 64, 31, -31, 0)]
)
spriteset_3 = industry.add_spriteset(
    id = 'grain_mill_spriteset_3',
    sprites = [(150, 60, 64, 82, -31, -51)],
    zextent = 48 # optional zextent value, will default to 16 if this param is omitted
)
spriteset_4 = industry.add_spriteset(
    id = 'grain_mill_spriteset_4',
    sprites = [(220, 60, 64, 82, -31, -51)],
    zextent = 48 # optional zextent value, will default to 16 if this param is omitted
)
spriteset_windmill_anim = industry.add_spriteset(
    id = 'grain_mill_spriteset_windmill_anim',
    sprites = [(10, 200, 64, 82, -31, -52), (80, 200, 64, 82, -31, -52), (150, 200, 64, 82, -31, -52),
               (220, 200, 64, 82, -31, -52), (290, 200, 64, 82, -31, -52), (360, 200, 64, 82, -31, -52)],
    zextent = 24, # optional zextent value, will default to 16 if this param is omitted
    animation_rate = 1
)
spriteset_ground_windmill = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_windmill',
    type = 'empty',
    num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)
spriteset_ground_overlay_windmill = industry.add_spriteset(
    id = 'grain_mill_spriteset_ground_overlay_windmill',
    sprites = [(10, 160, 64, 31, -31, 0)],
    num_sprites_to_autofill = len(spriteset_windmill_anim.sprites), # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
)

industry.add_spritelayout(
    id = 'grain_mill_spritelayout_brickbakery_1',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_1,
    building_sprites = []
)
industry.add_spritelayout(
    id = 'grain_mill_spritelayout_brickbakery_2',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_2,
    building_sprites = []
)
industry.add_spritelayout(
    id = 'grain_mill_spritelayout_brickbakery_3',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_3,
    building_sprites = [spriteset_3]
)
industry.add_spritelayout(
    id = 'grain_mill_spritelayout_brickbakery_4',
    ground_sprite = spriteset_ground_bakery,
    ground_overlay = spriteset_ground_overlay_4,
    building_sprites = [spriteset_4]
)
industry.add_spritelayout(
    id = 'grain_mill_spritelayout_windmill_anim',
    ground_sprite = spriteset_ground_windmill,
    ground_overlay = spriteset_ground_overlay_windmill,
    building_sprites = [spriteset_windmill_anim]
)

industry.add_industry_layout(
    id = 'grain_mill_industry_layout_1',
    default_spritelayout = 'grain_mill_spritelayout_brickbakery_3',
    layout = [(0, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (0, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (1, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_1'),
              (1, 1, 'grain_mill_tile','grain_mill_spritelayout_brickbakery_2')
    ]
)
industry.add_industry_layout(
    id = 'grain_mill_industry_layout_2',
    default_spritelayout = 'grain_mill_spritelayout_brickbakery_3',
    layout = [(0, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (0, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (1, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (1, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (2, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_1'),
              (2, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_2')
    ]
)
industry.add_industry_layout(
    id = 'grain_mill_industry_layout_3',
    default_spritelayout = 'grain_mill_spritelayout_brickbakery_3',
    layout = [(0, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (0, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (0, 2, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_3'),
              (0, 3, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_4'),
              (1, 0, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_1'),
              (1, 1, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_2'),
              (1, 2, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_1'),
              (1, 3, 'grain_mill_tile', 'grain_mill_spritelayout_brickbakery_2')
    ]
)
industry.add_industry_layout(
    id = 'grain_mill_industry_layout_4',
    default_spritelayout = 'grain_mill_spritelayout_windmill_anim',
    layout = [(0, 0, 'grain_mill_tile', 'grain_mill_spritelayout_windmill_anim')]
)

# Templating
industry.render_and_save_pnml()
