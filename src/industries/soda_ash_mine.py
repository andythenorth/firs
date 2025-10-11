from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="soda_ash_mine",
    prod_cargo_types_with_multipliers=[
        ("SASH", 16),
        ("SALT", 18),
    ],
    prob_in_game="4",
    prob_map_gen="7",
    map_colour="169",
    colour_scheme_name="scheme_3_hendrix",
    location_checks=dict(require_cluster=[70, 3]),
    prospect_chance="0.75",
    name="string(STR_IND_SODA_ASH_MINE)",
    nearby_station_name="string(STR_STATION_TRONA_BEDS)",
    fund_cost_multiplier="180",
    pollution_and_squalor_factor=1,
    primary_production_random_factor_set="wide_range",
    sprites_complete=True,
)

industry.enable_in_economy(
    "STEELTOWN",
    vulcan_config={
        "map_curator": {
            "curation_function": "MinimumRatioToCompanionIndustryTypes",
            "companion_industries": ["glass_works"],
            "companion_industries_ratio": 1,
        }
    },
)

industry.add_tile(
    id="soda_ash_mine_tile_1",
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
    id="soda_ash_mine_tile_2",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

sprite_ground = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")
sprite_ground_overlay = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")

spriteset_headgear_animated = industry.add_spriteset(
    sprites=[
        (10, 160, 64, 122, -31, -88),
        (80, 160, 64, 122, -31, -88),
        (150, 160, 64, 122, -31, -88),
    ],
    animation_rate=1,
    custom_sprite_selector="(animation_frame % 3)",
)
spriteset_crusher_front_part = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -90)],
)
spriteset_crusher_rear_part = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -74)],
)
spriteset_misc_building_tanks = industry.add_spriteset(
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
spriteset_exit_trestle = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -88)],
)
spriteset_exit_silo_conveyor = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -90)],
)
spriteset_truck = industry.add_spriteset(
    sprites=[(570, 10, 64, 122, -31, -90)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=3,
    yoffset=0,
    zoffset=73,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=12,
    yoffset=20,
    zoffset=45,
    animation_frame_offset=1,
)
sprite_smoke_3 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=9,
    yoffset=0,
    zoffset=67,
)
sprite_smoke_4 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=12,
    yoffset=0,
    zoffset=67,
    animation_frame_offset=1,
)


industry.add_spritelayout(
    id="soda_ash_mine_spritelayout_tile_empty",
    tile="soda_ash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[],
)
industry.add_spritelayout(
    id="soda_ash_mine_spritelayout_headgear_animated",
    tile="soda_ash_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_headgear_animated],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="soda_ash_mine_spritelayout_silos",
    tile="soda_ash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_exit_trestle],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="soda_ash_mine_spritelayout_crusher_front_part",
    tile="soda_ash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_crusher_front_part],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
)
industry.add_spritelayout(
    id="soda_ash_mine_spritelayout_crusher_rear_part",
    tile="soda_ash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_crusher_rear_part],
    smoke_sprites=[sprite_smoke_3, sprite_smoke_4],
)
industry.add_spritelayout(
    id="soda_ash_mine_spritelayout_misc_building_tanks",
    tile="soda_ash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_misc_building_tanks],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="soda_ash_mine_spritelayout_ore_1",
    tile="soda_ash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_ore_1],
)
industry.add_spritelayout(
    id="soda_ash_mine_spritelayout_ore_2",
    tile="soda_ash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_ore_2],
)
industry.add_spritelayout(
    id="soda_ash_mine_spritelayout_winding_house",
    tile="soda_ash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_winding_house],
)
industry.add_spritelayout(
    id="soda_ash_mine_spritelayout_silo_conveyor",
    tile="soda_ash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_exit_silo_conveyor],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="soda_ash_mine_spritelayout_truck",
    tile="soda_ash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_truck],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="soda_ash_mine_spritelayout_empty",
    tile="soda_ash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[],
    add_to_object_num=8,
)

industry.add_multi_tile_object(
    add_to_object_num=2,
    view_layout=[
        (0, 0, "soda_ash_mine_spritelayout_crusher_rear_part"),
        (1, 0, "soda_ash_mine_spritelayout_tile_empty"),
        (2, 0, "soda_ash_mine_spritelayout_crusher_front_part"),
    ],
)
industry.add_multi_tile_object(
    add_to_object_num=6,
    view_layout=[
        (0, 0, "soda_ash_mine_spritelayout_ore_2"),
        (1, 0, "soda_ash_mine_spritelayout_ore_1"),
    ],
)

industry.add_industry_layout(
    id="soda_ash_mine_industry_layout_1",
    layout=[
        (0, 0, "soda_ash_mine_spritelayout_crusher_rear_part"),
        (0, 1, "soda_ash_mine_spritelayout_headgear_animated"),
        (0, 2, "soda_ash_mine_spritelayout_winding_house"),
        (1, 0, "soda_ash_mine_spritelayout_tile_empty"),
        (1, 1, "soda_ash_mine_spritelayout_ore_2"),
        (
            1,
            2,
            "soda_ash_mine_spritelayout_misc_building_tanks",
        ),
        (2, 0, "soda_ash_mine_spritelayout_crusher_front_part"),
        (2, 1, "soda_ash_mine_spritelayout_ore_1"),
        (2, 2, "soda_ash_mine_spritelayout_tile_empty"),
        (3, 0, "soda_ash_mine_spritelayout_silos"),
        (3, 1, "soda_ash_mine_spritelayout_silo_conveyor"),
        (3, 2, "soda_ash_mine_spritelayout_truck"),
    ],
)

industry.add_industry_layout(
    id="soda_ash_mine_industry_layout_2",
    layout=[
        (0, 0, "soda_ash_mine_spritelayout_crusher_rear_part"),
        (0, 1, "soda_ash_mine_spritelayout_headgear_animated"),
        (0, 2, "soda_ash_mine_spritelayout_winding_house"),
        (0, 3, "soda_ash_mine_spritelayout_headgear_animated"),
        (0, 4, "soda_ash_mine_spritelayout_winding_house"),
        (1, 0, "soda_ash_mine_spritelayout_tile_empty"),
        (1, 1, "soda_ash_mine_spritelayout_ore_2"),
        (
            1,
            2,
            "soda_ash_mine_spritelayout_misc_building_tanks",
        ),
        (1, 3, "soda_ash_mine_spritelayout_truck"),
        (1, 4, "soda_ash_mine_spritelayout_ore_2"),
        (2, 0, "soda_ash_mine_spritelayout_crusher_front_part"),
        (2, 1, "soda_ash_mine_spritelayout_ore_1"),
        (2, 2, "soda_ash_mine_spritelayout_silos"),
        (2, 3, "soda_ash_mine_spritelayout_silo_conveyor"),
        (2, 4, "soda_ash_mine_spritelayout_ore_1"),
    ],
)

industry.add_industry_layout(
    id="soda_ash_mine_industry_layout_3",
    layout=[
        (0, 0, "soda_ash_mine_spritelayout_headgear_animated"),
        (0, 1, "soda_ash_mine_spritelayout_winding_house"),
        (1, 0, "soda_ash_mine_spritelayout_silos"),
        (1, 1, "soda_ash_mine_spritelayout_silo_conveyor"),
        (
            1,
            2,
            "soda_ash_mine_spritelayout_misc_building_tanks",
        ),
        (
            2,
            0,
            "soda_ash_mine_spritelayout_misc_building_tanks",
        ),
        (2, 1, "soda_ash_mine_spritelayout_headgear_animated"),
        (2, 2, "soda_ash_mine_spritelayout_winding_house"),
        (3, 0, "soda_ash_mine_spritelayout_crusher_rear_part"),
        (3, 1, "soda_ash_mine_spritelayout_crusher_rear_part"),
        (3, 2, "soda_ash_mine_spritelayout_ore_2"),
        (4, 0, "soda_ash_mine_spritelayout_tile_empty"),
        (4, 1, "soda_ash_mine_spritelayout_tile_empty"),
        (4, 2, "soda_ash_mine_spritelayout_ore_1"),
        (5, 0, "soda_ash_mine_spritelayout_crusher_front_part"),
        (5, 1, "soda_ash_mine_spritelayout_crusher_front_part"),
        (5, 2, "soda_ash_mine_spritelayout_truck"),
    ],
)

industry.add_industry_layout(
    id="soda_ash_mine_industry_layout_4",
    layout=[
        (0, 0, "soda_ash_mine_spritelayout_headgear_animated"),
        (0, 1, "soda_ash_mine_spritelayout_winding_house"),
        (0, 2, "soda_ash_mine_spritelayout_crusher_rear_part"),
        (0, 3, "soda_ash_mine_spritelayout_crusher_rear_part"),
        (0, 4, "soda_ash_mine_spritelayout_ore_2"),
        (
            1,
            0,
            "soda_ash_mine_spritelayout_misc_building_tanks",
        ),
        (1, 1, "soda_ash_mine_spritelayout_tile_empty"),
        (1, 2, "soda_ash_mine_spritelayout_tile_empty"),
        (1, 3, "soda_ash_mine_spritelayout_tile_empty"),
        (1, 4, "soda_ash_mine_spritelayout_ore_1"),
        (2, 0, "soda_ash_mine_spritelayout_silos"),
        (2, 1, "soda_ash_mine_spritelayout_silo_conveyor"),
        (2, 2, "soda_ash_mine_spritelayout_crusher_front_part"),
        (2, 3, "soda_ash_mine_spritelayout_crusher_front_part"),
        (2, 4, "soda_ash_mine_spritelayout_truck"),
    ],
)
