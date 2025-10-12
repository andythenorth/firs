from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="pyrite_mine",
    prod_cargo_types_with_multipliers=[
        ("PORE", 20),
    ],
    prob_in_game="4",
    prob_map_gen="7",
    map_colour="181",
    colour_scheme_name="scheme_13_whitney",
    location_checks=dict(require_cluster=[70, 3]),
    prospect_chance="0.75",
    name="string(STR_IND_PYRITE_MINE)",
    nearby_station_name="string(STR_STATION_PYRITES)",
    fund_cost_multiplier="252",
    pollution_and_squalor_factor=1,
    primary_production_random_factor_set="wide_range",
    sprites_complete=True,
)

industry.enable_in_economy(
    "BASIC_ARCTIC",
)

industry.add_tile(
    id="pyrite_mine_tile_1",
    animation_length=81,
    animation_looping=True,
    animation_speed=1,
    custom_animation_next_frame="((animation_frame == 80) ? CB_RESULT_STOP_ANIMATION : CB_RESULT_NEXT_FRAME)",
    custom_animation_control={
        "macro": "first_frame_is_0",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_TILE_LOOP)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

industry.add_tile(
    id="pyrite_mine_tile_2",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

industry.add_tile(
    id="pyrite_mine_tile_3",
    animation_length=200,
    animation_looping=True,
    animation_speed=3,
    custom_animation_next_frame="((animation_frame == 18) ? CB_RESULT_STOP_ANIMATION : CB_RESULT_NEXT_FRAME)",
    custom_animation_control={
        "macro": "first_frame_is_0",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_TILE_LOOP)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

sprite_ground = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")
sprite_ground_overlay = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")

spriteset_headgear_animated = industry.add_spriteset(
    sprites=[
        (10, 310, 64, 122, -31, -88),
        (80, 310, 64, 122, -31, -88),
        (150, 310, 64, 122, -31, -88),
    ],
    animation_rate=1,
    custom_sprite_selector="(animation_frame % 3)",
)
spriteset_exit_trestle_animated = industry.add_spriteset(
    sprites=[
        (10, 160, 64, 122, -31, -88),
        (80, 160, 64, 122, -31, -88),
        (150, 160, 64, 122, -31, -88),
        (220, 160, 64, 122, -31, -88),
        (290, 160, 64, 122, -31, -88),
        (360, 160, 64, 122, -31, -88),
        (430, 160, 64, 122, -31, -88),
        (500, 160, 64, 122, -31, -88),
        (500, 160, 64, 122, -31, -88),
        (570, 160, 64, 122, -31, -88),
        (570, 160, 64, 122, -31, -88),
        (640, 160, 64, 122, -31, -88),
        (640, 160, 64, 122, -31, -88),
        (710, 160, 64, 122, -31, -88),
        (780, 160, 64, 122, -31, -88),
        (850, 160, 64, 122, -31, -88),
        (920, 160, 64, 122, -31, -88),
        (990, 160, 64, 122, -31, -88),
        (1060, 160, 64, 122, -31, -88),
    ],
    animation_rate=1,
)
spriteset_crusher_front_part = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -90)],
)
spriteset_crusher_rear_part = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -74)],
)
spriteset_hut_vents = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_ore_1 = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
)
spriteset_ore_2 = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
)
spriteset_winding_house = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -90)],
)
spriteset_exit_shed_rear = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -90)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=-1,
    yoffset=2,
    zoffset=38,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=-1,
    yoffset=6,
    zoffset=38,
)

industry.add_spritelayout(
    id="pyrite_mine_spritelayout_tile_empty",
    tile="pyrite_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[],
    add_to_object_num=8,
)
industry.add_spritelayout(
    id="pyrite_mine_spritelayout_headgear_animated",
    tile="pyrite_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_headgear_animated],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="pyrite_mine_spritelayout_exit_trestle_animated",
    tile="pyrite_mine_tile_3",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_exit_trestle_animated],
)
industry.add_spritelayout(
    id="pyrite_mine_spritelayout_crusher_front_part",
    tile="pyrite_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_crusher_front_part],
)
industry.add_spritelayout(
    id="pyrite_mine_spritelayout_crusher_rear_part",
    tile="pyrite_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_crusher_rear_part],
)
industry.add_spritelayout(
    id="pyrite_mine_spritelayout_hut_vents",
    tile="pyrite_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_hut_vents],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="pyrite_mine_spritelayout_ore_1",
    tile="pyrite_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_ore_1],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="pyrite_mine_spritelayout_ore_2",
    tile="pyrite_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_ore_2],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="pyrite_mine_spritelayout_winding_house",
    tile="pyrite_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_winding_house],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="pyrite_mine_spritelayout_exit_shed_rear",
    # tile has to match trestle for multi-tile object case
    tile="pyrite_mine_tile_3",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_exit_shed_rear],
)

industry.add_multi_tile_object(
    add_to_object_num=2,
    view_layout=[
        (0, 0, "pyrite_mine_spritelayout_exit_shed_rear"),
        (1, 0, "pyrite_mine_spritelayout_exit_trestle_animated"),
    ],
)
industry.add_multi_tile_object(
    add_to_object_num=3,
    view_layout=[
        (0, 0, "pyrite_mine_spritelayout_crusher_rear_part"),
        (1, 0, "pyrite_mine_spritelayout_tile_empty"),
        (2, 0, "pyrite_mine_spritelayout_crusher_front_part"),
    ],
)

industry.add_industry_layout(
    id="pyrite_mine_industry_layout_1",
    layout=[
        (0, 1, "pyrite_mine_spritelayout_headgear_animated"),
        (0, 2, "pyrite_mine_spritelayout_winding_house"),
        (1, 0, "pyrite_mine_spritelayout_crusher_rear_part"),
        (1, 1, "pyrite_mine_spritelayout_exit_shed_rear"),
        (1, 2, "pyrite_mine_spritelayout_hut_vents"),
        (2, 0, "pyrite_mine_spritelayout_tile_empty"),
        (2, 1, "pyrite_mine_spritelayout_exit_trestle_animated"),
        (2, 2, "pyrite_mine_spritelayout_tile_empty"),
        (3, 0, "pyrite_mine_spritelayout_crusher_front_part"),
        (3, 1, "pyrite_mine_spritelayout_ore_1"),
        (3, 2, "pyrite_mine_spritelayout_ore_2"),
    ],
)

industry.add_industry_layout(
    id="pyrite_mine_industry_layout_2",
    layout=[
        (0, 0, "pyrite_mine_spritelayout_crusher_rear_part"),
        (0, 1, "pyrite_mine_spritelayout_headgear_animated"),
        (0, 2, "pyrite_mine_spritelayout_winding_house"),
        (0, 3, "pyrite_mine_spritelayout_headgear_animated"),
        (0, 4, "pyrite_mine_spritelayout_winding_house"),
        (1, 0, "pyrite_mine_spritelayout_tile_empty"),
        (1, 1, "pyrite_mine_spritelayout_exit_shed_rear"),
        (1, 2, "pyrite_mine_spritelayout_tile_empty"),
        (1, 3, "pyrite_mine_spritelayout_exit_shed_rear"),
        (1, 4, "pyrite_mine_spritelayout_hut_vents"),
        (2, 0, "pyrite_mine_spritelayout_crusher_front_part"),
        (2, 1, "pyrite_mine_spritelayout_exit_trestle_animated"),
        (2, 2, "pyrite_mine_spritelayout_ore_1"),
        (2, 3, "pyrite_mine_spritelayout_exit_trestle_animated"),
        (2, 4, "pyrite_mine_spritelayout_ore_2"),
    ],
)

industry.add_industry_layout(
    id="pyrite_mine_industry_layout_3",
    layout=[
        (0, 0, "pyrite_mine_spritelayout_headgear_animated"),
        (0, 1, "pyrite_mine_spritelayout_winding_house"),
        (1, 0, "pyrite_mine_spritelayout_exit_shed_rear"),
        (1, 1, "pyrite_mine_spritelayout_ore_2"),
        (1, 2, "pyrite_mine_spritelayout_tile_empty"),
        (2, 0, "pyrite_mine_spritelayout_exit_trestle_animated"),
        (2, 1, "pyrite_mine_spritelayout_headgear_animated"),
        (2, 2, "pyrite_mine_spritelayout_winding_house"),
        (3, 2, "pyrite_mine_spritelayout_hut_vents"),
        (3, 1, "pyrite_mine_spritelayout_exit_shed_rear"),
        (3, 0, "pyrite_mine_spritelayout_crusher_rear_part"),
        (4, 0, "pyrite_mine_spritelayout_tile_empty"),
        (4, 1, "pyrite_mine_spritelayout_exit_trestle_animated"),
        (4, 2, "pyrite_mine_spritelayout_ore_2"),
        (5, 0, "pyrite_mine_spritelayout_crusher_front_part"),
        (5, 1, "pyrite_mine_spritelayout_ore_1"),
    ],
)

industry.add_industry_layout(
    id="pyrite_mine_industry_layout_4",
    layout=[
        (0, 0, "pyrite_mine_spritelayout_headgear_animated"),
        (0, 1, "pyrite_mine_spritelayout_winding_house"),
        (0, 2, "pyrite_mine_spritelayout_headgear_animated"),
        (0, 3, "pyrite_mine_spritelayout_winding_house"),
        (0, 4, "pyrite_mine_spritelayout_crusher_rear_part"),
        (1, 0, "pyrite_mine_spritelayout_exit_shed_rear"),
        (1, 1, "pyrite_mine_spritelayout_ore_2"),
        (1, 2, "pyrite_mine_spritelayout_exit_shed_rear"),
        (1, 3, "pyrite_mine_spritelayout_tile_empty"),
        (1, 4, "pyrite_mine_spritelayout_tile_empty"),
        (2, 0, "pyrite_mine_spritelayout_exit_trestle_animated"),
        (2, 1, "pyrite_mine_spritelayout_hut_vents"),
        (2, 2, "pyrite_mine_spritelayout_exit_trestle_animated"),
        (2, 3, "pyrite_mine_spritelayout_ore_1"),
        (2, 4, "pyrite_mine_spritelayout_crusher_front_part"),
    ],
)
