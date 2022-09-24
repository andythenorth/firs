from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="flour_mill",
    accept_cargos_with_input_ratios=[
        ("GRAI", 6),
    ],
    prod_cargo_types_with_output_ratios=[
        ("FOOD", 8),
    ],
    prob_map_gen="10",
    prob_in_game="10",
    map_colour="49",
    location_checks=dict(flour_mill_layouts_by_date=True),
    name="string(STR_IND_FLOUR_MILL)",
    nearby_station_name="string(STR_STATION_MILL)",
    fund_cost_multiplier="50",
    provides_snow=True,
)

industry.enable_in_economy("BASIC_TROPIC")
industry.economy_variations["BASIC_TROPIC"].accept_cargos_with_input_ratios = [
    ("GRAI", 6)
]


industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
    accept_cargos_with_input_ratios=[
        ("CASS", 6),
        ("MAIZ", 6),
    ],
)

industry.add_tile(
    id="flour_mill_tile_1",
    animation_length=6,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True,
        require_houses_nearby=True,
        disallow_industry_adjacent=True,
    ),
)

spriteset_ground_bakery = industry.add_spriteset(
    type="cobble",
)
spriteset_ground_overlay_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_ground_overlay_2 = industry.add_spriteset(sprites=[(80, 10, 64, 31, -31, 0)])
spriteset_ground_overlay_3 = industry.add_spriteset(sprites=[(150, 10, 64, 31, -31, 0)])
spriteset_ground_overlay_4 = industry.add_spriteset(sprites=[(220, 10, 64, 31, -31, 0)])
spriteset_1 = industry.add_spriteset(sprites=[(10, 10, 64, 31, -31, 0)])
spriteset_2 = industry.add_spriteset(sprites=[(80, 10, 64, 31, -31, 0)])
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 82, -31, -51)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 82, -31, -51)],
)
# animated spriteset defined first so others can copy num. frames
spriteset_windmill_anim = industry.add_spriteset(
    sprites=[
        (10, 200, 64, 82, -31, -52),
        (80, 200, 64, 82, -31, -52),
        (150, 200, 64, 82, -31, -52),
        (220, 200, 64, 82, -31, -52),
        (290, 200, 64, 82, -31, -52),
        (360, 200, 64, 82, -31, -52),
    ],
    animation_rate=1,
)
spriteset_ground_windmill = industry.add_spriteset(
    type="empty",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)
spriteset_ground_overlay_windmill = industry.add_spriteset(
    sprites=[(150, 160, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)
spriteset_ground_overlay_windmill_granary = industry.add_spriteset(
    sprites=[(80, 160, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)
spriteset_windmill_granary = industry.add_spriteset(
    sprites=[(80, 60, 64, 82, -31, -52)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)
spriteset_ground_overlay_windmill_shed = industry.add_spriteset(
    sprites=[(10, 160, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)
spriteset_windmill_shed = industry.add_spriteset(
    sprites=[(10, 60, 64, 82, -31, -52)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)
spriteset_ground_overlay_windmill_greeble = industry.add_spriteset(
    sprites=[(220, 160, 64, 31, -31, 0)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_windmill_anim.sprites),
)

industry.add_spritelayout(
    id="flour_mill_spritelayout_brickbakery_1",
    tile="flour_mill_tile_1",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_1,
    building_sprites=[],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_brickbakery_2",
    tile="flour_mill_tile_1",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_2,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_brickbakery_3",
    tile="flour_mill_tile_1",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_3,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_brickbakery_4",
    tile="flour_mill_tile_1",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_4,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_windmill_anim",
    tile="flour_mill_tile_1",
    ground_sprite=spriteset_ground_windmill,
    ground_overlay=spriteset_ground_overlay_windmill,
    building_sprites=[spriteset_windmill_anim],
    fences=["nw", "ne", "se", "sw"],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_windmill_granary",
    tile="flour_mill_tile_1",
    ground_sprite=spriteset_ground_windmill,
    ground_overlay=spriteset_ground_overlay_windmill_granary,
    building_sprites=[spriteset_windmill_granary],
    fences=["nw", "ne", "se", "sw"],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_windmill_shed",
    tile="flour_mill_tile_1",
    ground_sprite=spriteset_ground_windmill,
    ground_overlay=spriteset_ground_overlay_windmill_shed,
    building_sprites=[spriteset_windmill_shed],
    fences=["nw", "ne", "se", "sw"],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="flour_mill_spritelayout_windmill_greeble",
    tile="flour_mill_tile_1",
    ground_sprite=spriteset_ground_windmill,
    ground_overlay=spriteset_ground_overlay_windmill_greeble,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
    terrain_aware_ground=True,
)
industry.add_industry_layout(
    id="flour_mill_industry_layout_1",
    layout=[
        (0, 0, "flour_mill_spritelayout_brickbakery_3"),
        (0, 1, "flour_mill_spritelayout_brickbakery_4"),
        (1, 0, "flour_mill_spritelayout_brickbakery_1"),
        (1, 1, "flour_mill_spritelayout_brickbakery_2"),
    ],
)
industry.add_industry_layout(
    id="flour_mill_industry_layout_2",
    layout=[
        (0, 0, "flour_mill_spritelayout_brickbakery_3"),
        (0, 1, "flour_mill_spritelayout_brickbakery_4"),
        (1, 0, "flour_mill_spritelayout_brickbakery_3"),
        (1, 1, "flour_mill_spritelayout_brickbakery_4"),
        (2, 0, "flour_mill_spritelayout_brickbakery_1"),
        (2, 1, "flour_mill_spritelayout_brickbakery_2"),
    ],
)
industry.add_industry_layout(
    id="flour_mill_industry_layout_3",
    layout=[
        (0, 0, "flour_mill_spritelayout_brickbakery_3"),
        (0, 1, "flour_mill_spritelayout_brickbakery_4"),
        (0, 2, "flour_mill_spritelayout_brickbakery_3"),
        (0, 3, "flour_mill_spritelayout_brickbakery_4"),
        (1, 0, "flour_mill_spritelayout_brickbakery_1"),
        (1, 1, "flour_mill_spritelayout_brickbakery_2"),
        (1, 2, "flour_mill_spritelayout_brickbakery_1"),
        (1, 3, "flour_mill_spritelayout_brickbakery_2"),
    ],
)
industry.add_industry_layout(
    id="flour_mill_industry_layout_4",
    layout=[
        (0, 0, "flour_mill_spritelayout_windmill_shed"),
        (0, 1, "flour_mill_spritelayout_windmill_granary"),
        (1, 0, "flour_mill_spritelayout_windmill_anim"),
        (1, 1, "flour_mill_spritelayout_windmill_greeble"),
    ],
)
industry.add_industry_layout(
    id="flour_mill_industry_layout_5",
    layout=[
        (0, 0, "flour_mill_spritelayout_windmill_shed"),
        (0, 1, "flour_mill_spritelayout_windmill_anim"),
        (1, 0, "flour_mill_spritelayout_windmill_granary"),
        (1, 1, "flour_mill_spritelayout_windmill_greeble"),
    ],
)
industry.add_industry_layout(
    id="flour_mill_industry_layout_6",
    layout=[
        (0, 0, "flour_mill_spritelayout_windmill_granary"),
        (0, 1, "flour_mill_spritelayout_windmill_greeble"),
        (1, 0, "flour_mill_spritelayout_windmill_anim"),
        (1, 1, "flour_mill_spritelayout_windmill_shed"),
    ],
)
