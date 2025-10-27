from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="zinc_smelter",
    accept_cargos_with_input_ratios=[
        ("ZORE", 4),
        ("COKE", 4),
    ],
    prod_cargo_types_with_output_ratios=[
        ("ZINC", 4),
        ("SUAC", 4),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="19",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[
            [
                "wharf",
            ],  # assumes zinc ore from wharf in MMW
            56,
        ],
        same_type_distance=100,
    ),
    special_flags=["IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE"],
    name="string(STR_IND_ZINC_SMELTER)",
    nearby_station_name="string(STR_STATION_SMELTER)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=2,
    sprites_complete=False,
    animated_tiles_fixed=False,
)

industry.add_tile(
    id="zinc_smelter_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="gravel")
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)
spriteset_greeble = industry.add_spriteset(
    sprites=[(570, 10, 64, 122, -31, -90)],
)
spriteset_roaster_1 = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -90)],
)
spriteset_roaster_2 = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_chimney = industry.add_spriteset(
    sprites=[(220, 10, 64, 130, -31, -110)],
)
spriteset_acid_plant_1 = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
)
spriteset_acid_plant_2 = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -90)],
)
spriteset_metal_1 = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -90)],
)
spriteset_metal_2 = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -90)],
)
spriteset_office = industry.add_spriteset(
    sprites=[(640, 10, 64, 122, -31, -90)],
)
sprite_smoke_big_chimney = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=7,
    yoffset=0,
    zoffset=116,
)
sprite_smoke_roaster = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=0,
    zoffset=86,
)

industry.add_spritelayout(
    id="zinc_smelter_spritelayout_empty",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="zinc_smelter_spritelayout_greeble",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_greeble],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="zinc_smelter_spritelayout_roaster_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_roaster_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="zinc_smelter_spritelayout_roaster_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_roaster_2],
    smoke_sprites=[sprite_smoke_roaster],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="zinc_smelter_spritelayout_chimney",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_chimney],
    smoke_sprites=[sprite_smoke_big_chimney],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="zinc_smelter_spritelayout_acid_plant_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_acid_plant_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="zinc_smelter_spritelayout_acid_plant_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_acid_plant_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="zinc_smelter_spritelayout_metal_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="zinc_smelter_spritelayout_metal_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="zinc_smelter_spritelayout_office",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_office],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="zinc_smelter_industry_layout_1",
    layout=[
        (0, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (0, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_2"),
        (0, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (0, 3, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_2"),
        (0, 4, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_1"),
        (1, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_chimney"),
        (1, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (1, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (1, 3, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_1"),
        (1, 4, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_acid_plant_2"),
        (2, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_office"),
        (2, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_greeble"),
        (2, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_2"),
        (2, 3, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_empty"),
        (2, 4, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_acid_plant_1"),
    ],
)
industry.add_industry_layout(
    id="zinc_smelter_industry_layout_2",
    layout=[
        (0, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (0, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_2"),
        (0, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_1"),
        (0, 3, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_acid_plant_2"),
        (1, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (1, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (1, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_2"),
        (1, 3, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_acid_plant_1"),
        (2, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (2, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_chimney"),
        (2, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_1"),
        (2, 3, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_empty"),
        (3, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_greeble"),
        (3, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_2"),
        (3, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_empty"),
        (3, 3, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_office"),
    ],
)
industry.add_industry_layout(
    id="zinc_smelter_industry_layout_3",
    layout=[
        (0, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_2"),
        (0, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_2"),
        (0, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_1"),
        (1, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_1"),
        (1, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (1, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (2, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_chimney"),
        (2, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (2, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (3, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_acid_plant_2"),
        (3, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_greeble"),
        (3, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_2"),
        (4, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_acid_plant_1"),
        (4, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_empty"),
        (4, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_office"),
    ],
)
industry.add_industry_layout(
    id="zinc_smelter_industry_layout_4",
    layout=[
        (0, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_2"),
        (0, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_1"),
        (0, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_chimney"),
        (1, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_2"),
        (1, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (1, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_acid_plant_1"),
        (2, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (2, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (2, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_acid_plant_2"),
        (3, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_1"),
        (3, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_roaster_1"),
        (3, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_office"),
        (4, 0, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_metal_2"),
        (4, 1, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_greeble"),
        (4, 2, "zinc_smelter_tile_1", "zinc_smelter_spritelayout_empty"),
    ],
)
