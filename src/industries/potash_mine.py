from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="potash_mine",
    prod_cargo_types_with_multipliers=[
        ("POTA", 20),
    ],
    prob_in_game="4",
    prob_map_gen="7",
    map_colour="196",
    location_checks=dict(require_cluster=[70, 3]),
    prospect_chance="0.75",
    name="string(STR_IND_POTASH_MINE)",
    nearby_station_name="string(STR_STATION_MINE)",
    fund_cost_multiplier="232",
    pollution_and_squalor_factor=1,
)

# exists in Steeltown primarily to give a direct cargo to Bulk Terminal
industry.enable_in_economy(
    "PLAINS_TRAINS_AND_STEEL",
    prod_cargo_types_with_multipliers=[
        ("POTA", 20)
    ],
    fund_cost_multiplier="72",
)

industry.add_tile(
    id="potash_mine_tile_1",
    animation_length=81,
    animation_looping=True,
    animation_speed=1,
    custom_animation_next_frame="((animation_frame == 80) ? CB_RESULT_STOP_ANIMATION : CB_RESULT_NEXT_FRAME)",
    custom_animation_control={
        "macro": "first_frame_is_0",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_TILE_LOOP)",
    },
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="potash_mine_tile_2",
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
    id="potash_mine_tile_3",
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
spriteset_small_mineral_pile = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
)
spriteset_containers = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
)
spriteset_mineral_pile = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -90)],
)
spriteset_hut_vents = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -90)],
)
spriteset_winding_house = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -90)],
)
spriteset_shed = industry.add_spriteset(
    sprites=[(570, 10, 64, 122, -31, -90)],
)
spriteset_pool_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -90)],
)
spriteset_pool_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -90)],
)
spriteset_pool_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_pool_4 = industry.add_spriteset(
    sprites=[(10, 160, 64, 122, -31, -90)],
)
spriteset_pool_5 = industry.add_spriteset(
    sprites=[(80, 160, 64, 122, -31, -90)],
)
spriteset_pool_6 = industry.add_spriteset(
    sprites=[(150, 160, 64, 122, -31, -90)],
)
spriteset_pool_7 = industry.add_spriteset(
    sprites=[(220, 160, 64, 122, -31, -90)],
)
spriteset_pool_8 = industry.add_spriteset(
    sprites=[(290, 160, 64, 122, -31, -90)],
)
spriteset_pool_9 = industry.add_spriteset(
    sprites=[(360, 160, 64, 122, -31, -90)],
)
spriteset_pool_10 = industry.add_spriteset(
    sprites=[(430, 160, 64, 122, -31, -90)],
)
spriteset_pool_11 = industry.add_spriteset(
    sprites=[(500, 160, 64, 122, -31, -90)],
)
spriteset_pool_12 = industry.add_spriteset(
    sprites=[(570, 160, 64, 122, -31, -90)],
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
    id="potash_mine_spritelayout_tile_empty",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_headgear_animated",
    tile="potash_mine_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_headgear_animated],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_small_mineral_pile",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_small_mineral_pile],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_mineral_pile",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_mineral_pile],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_hut_vents",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_hut_vents],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_winding_house",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_winding_house],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_shed_1",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_shed],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_containers",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_containers],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_pool_1",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_pool_1],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_pool_2",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_pool_2],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_pool_3",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_pool_3],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_pool_4",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_pool_4],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_pool_5",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_pool_5],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_pool_6",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_pool_6],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_pool_7",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_pool_7],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_pool_8",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_pool_8],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_pool_9",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_pool_9],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_pool_10",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_pool_10],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_pool_11",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_pool_11],
)
industry.add_spritelayout(
    id="potash_mine_spritelayout_pool_12",
    tile="potash_mine_tile_2",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_pool_12],
)
industry.add_industry_layout(
    id="potash_mine_industry_layout_1",
    layout=[
        (0, 0, "potash_mine_spritelayout_tile_empty"),
        (0, 1, "potash_mine_spritelayout_headgear_animated"),
        (0, 2, "potash_mine_spritelayout_winding_house"),
        (1, 0, "potash_mine_spritelayout_containers"),
        (1, 1, "potash_mine_spritelayout_mineral_pile"),
        (1, 2, "potash_mine_spritelayout_hut_vents"),
        (2, 0, "potash_mine_spritelayout_tile_empty"),
        (2, 1, "potash_mine_spritelayout_pool_1"),
        (2, 2, "potash_mine_spritelayout_pool_2"),
        (2, 3, "potash_mine_spritelayout_pool_3"),
        (3, 0, "potash_mine_spritelayout_shed_1"),
        (3, 1, "potash_mine_spritelayout_pool_4"),
        (3, 2, "potash_mine_spritelayout_pool_5"),
        (3, 3, "potash_mine_spritelayout_pool_6"),
        (4, 1, "potash_mine_spritelayout_pool_7"),
        (4, 2, "potash_mine_spritelayout_pool_8"),
        (4, 3, "potash_mine_spritelayout_pool_9"),
        (5, 1, "potash_mine_spritelayout_pool_10"),
        (5, 2, "potash_mine_spritelayout_pool_11"),
        (5, 3, "potash_mine_spritelayout_pool_12"),
    ],
)
industry.add_industry_layout(
    id="potash_mine_industry_layout_2",
    layout=[
        (0, 0, "potash_mine_spritelayout_tile_empty"),
        (0, 1, "potash_mine_spritelayout_tile_empty"),
        (0, 2, "potash_mine_spritelayout_tile_empty"),
        (0, 3, "potash_mine_spritelayout_shed_1"),
        (1, 0, "potash_mine_spritelayout_mineral_pile"),
        (1, 1, "potash_mine_spritelayout_tile_empty"),
        (1, 2, "potash_mine_spritelayout_headgear_animated"),
        (1, 3, "potash_mine_spritelayout_winding_house"),
        (1, 4, "potash_mine_spritelayout_tile_empty"),
        (1, 5, "potash_mine_spritelayout_small_mineral_pile"),
        (1, 6, "potash_mine_spritelayout_tile_empty"),
        (2, 0, "potash_mine_spritelayout_pool_1"),
        (2, 1, "potash_mine_spritelayout_pool_2"),
        (2, 2, "potash_mine_spritelayout_pool_3"),
        (2, 3, "potash_mine_spritelayout_tile_empty"),
        (2, 4, "potash_mine_spritelayout_mineral_pile"),
        (2, 5, "potash_mine_spritelayout_shed_1"),
        (2, 6, "potash_mine_spritelayout_tile_empty"),
        (3, 0, "potash_mine_spritelayout_pool_4"),
        (3, 1, "potash_mine_spritelayout_pool_5"),
        (3, 2, "potash_mine_spritelayout_pool_6"),
        (3, 3, "potash_mine_spritelayout_hut_vents"),
        (4, 0, "potash_mine_spritelayout_pool_7"),
        (4, 1, "potash_mine_spritelayout_pool_8"),
        (4, 2, "potash_mine_spritelayout_pool_9"),
        (5, 0, "potash_mine_spritelayout_pool_10"),
        (5, 1, "potash_mine_spritelayout_pool_11"),
        (5, 2, "potash_mine_spritelayout_pool_12"),
        (3, 4, "potash_mine_spritelayout_pool_1"),
        (3, 5, "potash_mine_spritelayout_pool_2"),
        (3, 6, "potash_mine_spritelayout_pool_3"),
        (4, 4, "potash_mine_spritelayout_pool_4"),
        (4, 5, "potash_mine_spritelayout_pool_5"),
        (4, 6, "potash_mine_spritelayout_pool_6"),
        (5, 4, "potash_mine_spritelayout_pool_7"),
        (5, 5, "potash_mine_spritelayout_pool_8"),
        (5, 6, "potash_mine_spritelayout_pool_9"),
        (6, 4, "potash_mine_spritelayout_pool_10"),
        (6, 5, "potash_mine_spritelayout_pool_11"),
        (6, 6, "potash_mine_spritelayout_pool_12"),
    ],
)
