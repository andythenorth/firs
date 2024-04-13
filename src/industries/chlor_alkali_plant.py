from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="chlor_alkali_plant",
    accept_cargos_with_input_ratios=[("SALT", 8)],
    prod_cargo_types_with_output_ratios=[("ACID", 4), ("CHLO", 2), ("LYE_", 2)],
    prob_in_game="0",  # do not build during gameplay
    prob_map_gen="5",
    prod_multiplier="[0, 0]",
    map_colour="191",
    name="string(STR_IND_CHLOR_ALKALI_PLANT)",
    nearby_station_name="string(STR_STATION_BRINE_WORKS)",
    fund_cost_multiplier="170",
    pollution_and_squalor_factor=2,
    sprites_complete=True,
)

industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="chlor_alkali_plant_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="chlor_alkali_plant_tile_2",
    animation_length=47,
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

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)

spriteset_horizontal_tanks = industry.add_spriteset(
    sprites=[(150, 10, 64, 114, -31, -83)],
)
spriteset_frac_columns = industry.add_spriteset(
    sprites=[(220, 10, 64, 114, -31, -83)],
)
spriteset_drop_tower_and_thin_chimney = industry.add_spriteset(
    sprites=[(290, 10, 64, 114, -31, -83)],
)
spriteset_large_building = industry.add_spriteset(
    sprites=[(360, 10, 64, 114, -31, -83)],
)
spriteset_fat_chimney = industry.add_spriteset(
    sprites=[(430, 10, 64, 114, -31, -83)],
)
spriteset_spherical_tanks = industry.add_spriteset(
    sprites=[(500, 10, 64, 66, -31, -35)],
)
spriteset_vertical_tanks = industry.add_spriteset(
    sprites=[(570, 10, 64, 66, -31, -35)],
)
spriteset_barrels = industry.add_spriteset(
    sprites=[(710, 10, 64, 66, -31, -35)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=0,
    zoffset=81,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=6,
    yoffset=-1,
    zoffset=45,
)
sprite_smoke_3 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=6,
    yoffset=3,
    zoffset=45,
)
sprite_smoke_4 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=2,
    yoffset=-1,
    zoffset=45,
)
sprite_smoke_5 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=2,
    yoffset=3,
    zoffset=45,
)
sprite_smoke_6 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=6,
    yoffset=0,
    zoffset=60,
)
sprite_smoke_7 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=6,
    yoffset=3,
    zoffset=60,
)
sprite_smoke_8 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=3,
    yoffset=0,
    zoffset=60,
)
sprite_smoke_9 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=3,
    yoffset=3,
    zoffset=60,
)
industry.add_spritelayout(
    id="chlor_alkali_plant_spritelayout_horizontal_tanks",
    tile="chlor_alkali_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_horizontal_tanks],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="chlor_alkali_plant_spritelayout_frac_columns",
    tile="chlor_alkali_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_frac_columns],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="chlor_alkali_plant_spritelayout_drop_tower_and_thin_chimney",
    tile="chlor_alkali_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_drop_tower_and_thin_chimney],
    smoke_sprites=[sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="chlor_alkali_plant_spritelayout_large_building",
    tile="chlor_alkali_plant_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_building],
    smoke_sprites=[sprite_smoke_2, sprite_smoke_3, sprite_smoke_4, sprite_smoke_5],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="chlor_alkali_plant_spritelayout_fat_chimney",
    tile="chlor_alkali_plant_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_fat_chimney],
    smoke_sprites=[sprite_smoke_6, sprite_smoke_7, sprite_smoke_8, sprite_smoke_9],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="chlor_alkali_plant_spritelayout_spherical_tanks",
    tile="chlor_alkali_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_spherical_tanks],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="chlor_alkali_plant_spritelayout_vertical_tanks",
    tile="chlor_alkali_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_vertical_tanks],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="chlor_alkali_plant_spritelayout_barrels",
    tile="chlor_alkali_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_barrels],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=8,
)

# this industry needs outpost layout as there are lots of cargos
# generally outposts are 2x2, but this industry uses 3x2 or so as the sprites seem to work better with it
industry.add_industry_outpost_layout(
    id="chlor_alkali_plant_industry_outpost_layout_1",
    layout=[
        (
            0,
            0,
            "chlor_alkali_plant_spritelayout_fat_chimney",
        ),
        (
            0,
            1,
            "chlor_alkali_plant_spritelayout_drop_tower_and_thin_chimney",
        ),
        (
            0,
            2,
            "chlor_alkali_plant_spritelayout_spherical_tanks",
        ),
        (
            1,
            0,
            "chlor_alkali_plant_spritelayout_large_building",
        ),
        (
            1,
            1,
            "chlor_alkali_plant_spritelayout_frac_columns",
        ),
        (
            1,
            2,
            "chlor_alkali_plant_spritelayout_horizontal_tanks",
        ),
    ],
)
industry.add_industry_outpost_layout(
    id="chlor_alkali_plant_industry_outpost_layout_2",
    layout=[
        (
            0,
            0,
            "chlor_alkali_plant_spritelayout_horizontal_tanks",
        ),
        (
            0,
            1,
            "chlor_alkali_plant_spritelayout_fat_chimney",
        ),
        (
            1,
            0,
            "chlor_alkali_plant_spritelayout_frac_columns",
        ),
        (
            1,
            1,
            "chlor_alkali_plant_spritelayout_large_building",
        ),
        (
            2,
            0,
            "chlor_alkali_plant_spritelayout_drop_tower_and_thin_chimney",
        ),
        (
            2,
            1,
            "chlor_alkali_plant_spritelayout_spherical_tanks",
        ),
    ],
)
# core layouts are roughly 3x4 or 3x3
industry.add_industry_layout(
    id="chlor_alkali_plant_industry_layout_1",
    layout=[
        (
            0,
            0,
            "chlor_alkali_plant_spritelayout_fat_chimney",
        ),
        (
            0,
            1,
            "chlor_alkali_plant_spritelayout_fat_chimney",
        ),
        (
            0,
            2,
            "chlor_alkali_plant_spritelayout_spherical_tanks",
        ),
        (
            1,
            0,
            "chlor_alkali_plant_spritelayout_large_building",
        ),
        (
            1,
            1,
            "chlor_alkali_plant_spritelayout_large_building",
        ),
        (1, 2, "chlor_alkali_plant_spritelayout_barrels"),
        (
            2,
            0,
            "chlor_alkali_plant_spritelayout_frac_columns",
        ),
        (
            2,
            1,
            "chlor_alkali_plant_spritelayout_frac_columns",
        ),
        (
            2,
            2,
            "chlor_alkali_plant_spritelayout_vertical_tanks",
        ),
        (
            3,
            0,
            "chlor_alkali_plant_spritelayout_drop_tower_and_thin_chimney",
        ),
        (
            3,
            1,
            "chlor_alkali_plant_spritelayout_horizontal_tanks",
        ),
        (
            3,
            2,
            "chlor_alkali_plant_spritelayout_vertical_tanks",
        ),
    ],
)
industry.add_industry_layout(
    id="chlor_alkali_plant_industry_layout_2",
    layout=[
        (
            0,
            0,
            "chlor_alkali_plant_spritelayout_drop_tower_and_thin_chimney",
        ),
        (
            0,
            1,
            "chlor_alkali_plant_spritelayout_horizontal_tanks",
        ),
        (
            0,
            2,
            "chlor_alkali_plant_spritelayout_fat_chimney",
        ),
        (
            0,
            3,
            "chlor_alkali_plant_spritelayout_fat_chimney",
        ),
        (
            1,
            0,
            "chlor_alkali_plant_spritelayout_frac_columns",
        ),
        (
            1,
            1,
            "chlor_alkali_plant_spritelayout_horizontal_tanks",
        ),
        (
            1,
            2,
            "chlor_alkali_plant_spritelayout_large_building",
        ),
        (
            1,
            3,
            "chlor_alkali_plant_spritelayout_large_building",
        ),
        (
            2,
            0,
            "chlor_alkali_plant_spritelayout_vertical_tanks",
        ),
        (2, 1, "chlor_alkali_plant_spritelayout_barrels"),
        (
            2,
            2,
            "chlor_alkali_plant_spritelayout_spherical_tanks",
        ),
        (
            2,
            3,
            "chlor_alkali_plant_spritelayout_spherical_tanks",
        ),
    ],
)
industry.add_industry_layout(
    id="chlor_alkali_plant_industry_layout_3",
    layout=[
        (
            0,
            0,
            "chlor_alkali_plant_spritelayout_fat_chimney",
        ),
        (
            0,
            1,
            "chlor_alkali_plant_spritelayout_fat_chimney",
        ),
        (
            0,
            2,
            "chlor_alkali_plant_spritelayout_frac_columns",
        ),
        (
            0,
            3,
            "chlor_alkali_plant_spritelayout_horizontal_tanks",
        ),
        (
            1,
            0,
            "chlor_alkali_plant_spritelayout_large_building",
        ),
        (
            1,
            1,
            "chlor_alkali_plant_spritelayout_large_building",
        ),
        (
            1,
            2,
            "chlor_alkali_plant_spritelayout_frac_columns",
        ),
        (
            1,
            3,
            "chlor_alkali_plant_spritelayout_drop_tower_and_thin_chimney",
        ),
        (
            2,
            0,
            "chlor_alkali_plant_spritelayout_spherical_tanks",
        ),
        (2, 1, "chlor_alkali_plant_spritelayout_barrels"),
        (
            2,
            2,
            "chlor_alkali_plant_spritelayout_vertical_tanks",
        ),
        (
            2,
            3,
            "chlor_alkali_plant_spritelayout_vertical_tanks",
        ),
    ],
)
industry.add_industry_layout(
    id="chlor_alkali_plant_industry_layout_4",
    layout=[
        (
            0,
            0,
            "chlor_alkali_plant_spritelayout_horizontal_tanks",
        ),
        (
            0,
            1,
            "chlor_alkali_plant_spritelayout_fat_chimney",
        ),
        (
            0,
            2,
            "chlor_alkali_plant_spritelayout_fat_chimney",
        ),
        (
            1,
            0,
            "chlor_alkali_plant_spritelayout_frac_columns",
        ),
        (
            1,
            1,
            "chlor_alkali_plant_spritelayout_large_building",
        ),
        (
            1,
            2,
            "chlor_alkali_plant_spritelayout_large_building",
        ),
        (
            2,
            0,
            "chlor_alkali_plant_spritelayout_drop_tower_and_thin_chimney",
        ),
        (
            2,
            1,
            "chlor_alkali_plant_spritelayout_vertical_tanks",
        ),
        (
            2,
            2,
            "chlor_alkali_plant_spritelayout_spherical_tanks",
        ),
    ],
)
industry.add_industry_layout(
    id="chlor_alkali_plant_industry_layout_5",
    layout=[
        (
            0,
            0,
            "chlor_alkali_plant_spritelayout_fat_chimney",
        ),
        (
            0,
            1,
            "chlor_alkali_plant_spritelayout_frac_columns",
        ),
        (
            0,
            2,
            "chlor_alkali_plant_spritelayout_vertical_tanks",
        ),
        (
            1,
            0,
            "chlor_alkali_plant_spritelayout_large_building",
        ),
        (
            1,
            1,
            "chlor_alkali_plant_spritelayout_horizontal_tanks",
        ),
        (
            1,
            2,
            "chlor_alkali_plant_spritelayout_drop_tower_and_thin_chimney",
        ),
        (
            2,
            0,
            "chlor_alkali_plant_spritelayout_fat_chimney",
        ),
        (
            2,
            1,
            "chlor_alkali_plant_spritelayout_horizontal_tanks",
        ),
        (
            2,
            2,
            "chlor_alkali_plant_spritelayout_frac_columns",
        ),
        (
            3,
            0,
            "chlor_alkali_plant_spritelayout_large_building",
        ),
        (3, 1, "chlor_alkali_plant_spritelayout_barrels"),
        (
            3,
            2,
            "chlor_alkali_plant_spritelayout_spherical_tanks",
        ),
    ],
)
