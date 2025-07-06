from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="foundry",
    # runs both casting line (sand) and forging line (soap)
    # cleaning agents also stand in for shot-blasting etc
    accept_cargos_with_input_ratios=[
        ("STIG", 6),
        ("SAND", 1),
        ("SOAP", 1),
    ],
    prod_cargo_types_with_output_ratios=[
        ("FOCA", 6),
        ("ENSP", 2),
    ],
    prob_in_game="2",
    prob_map_gen="5",
    map_colour="166",
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[
            ["basic_oxygen_furnace", "electric_arc_furnace"],
            56,
        ],
    ),
    name="string(STR_IND_FORGE_AND_FOUNDRY)",
    nearby_station_name="string(STR_STATION_FORGE)",
    fund_cost_multiplier="63",
    sprites_complete=True,
)

industry.enable_in_economy(
    "STEELTOWN",
)

# not animated tiles
industry.add_tile(
    id="foundry_tile_1",
    location_checks=TileLocationChecks(disallow_industry_adjacent=True),
)
# animated tiles
industry.add_tile(
    id="foundry_tile_2",
    animation_length=180,
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
    id="foundry_tile_3",
    animation_length=3,
    animation_looping=True,
    animation_speed=8,
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
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 70, -31, -40)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 70, -31, -39)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 70, -31, -39)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 70, -31, -39)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 70, -31, -39)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 70, -31, -39)],
)
spriteset_iron_pigs_anim = industry.add_spriteset(
    sprites=[
        (10, 90, 64, 70, -31, -39),
        (80, 90, 64, 70, -31, -39),
        (150, 90, 64, 70, -31, -39),
    ],
    animation_rate=1,
)
spriteset_ground_pigs = industry.add_spriteset(
    type="asphalt",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_iron_pigs_anim.sprites),
)
spriteset_ground_overlay_pigs = industry.add_spriteset(
    type="empty",
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_iron_pigs_anim.sprites),
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=0,
    yoffset=4,
    zoffset=23,
)

industry.add_spritelayout(
    id="foundry_spritelayout_furnace_anim",
    tile="foundry_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="foundry_spritelayout_iron_pigs_anim",
    tile="foundry_tile_3",
    ground_sprite=spriteset_ground_pigs,
    ground_overlay=spriteset_ground_overlay_pigs,
    building_sprites=[spriteset_iron_pigs_anim],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="foundry_spritelayout_large_chimney",
    tile="foundry_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="foundry_spritelayout_large_shed",
    tile="foundry_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=[],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="foundry_spritelayout_large_shed_alt",
    tile="foundry_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=[],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="foundry_spritelayout_silos",
    tile="foundry_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=[],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="foundry_spritelayout_store_shed",
    tile="foundry_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne"],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="foundry_spritelayout_empty",
    tile="foundry_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=[],
    add_to_object_num=8,
)

# this industry needs outpost layout as there are lots of cargos
industry.add_industry_outpost_layout(
    id="foundry_industry_outpost_layout_1",
    layout=[
        # test outpost layout
        (
            0,
            0,
            "foundry_spritelayout_large_shed",
        ),
        (
            0,
            1,
            "foundry_spritelayout_furnace_anim",
        ),
        (
            0,
            2,
            "foundry_spritelayout_iron_pigs_anim",
        ),
        (
            1,
            0,
            "foundry_spritelayout_large_chimney",
        ),
        (
            1,
            1,
            "foundry_spritelayout_silos",
        ),
        (
            1,
            2,
            "foundry_spritelayout_store_shed",
        ),
    ],
)

industry.add_industry_layout(
    id="foundry_industry_layout_1",
    layout=[
        (
            0,
            0,
            "foundry_spritelayout_large_shed",
        ),
        (0, 1, "foundry_spritelayout_furnace_anim"),
        (0, 2, "foundry_spritelayout_iron_pigs_anim"),
        (
            1,
            0,
            "foundry_spritelayout_large_shed",
        ),
        (1, 1, "foundry_spritelayout_furnace_anim"),
        (1, 2, "foundry_spritelayout_iron_pigs_anim"),
        (2, 0, "foundry_spritelayout_large_chimney"),
        (2, 1, "foundry_spritelayout_silos"),
        (2, 2, "foundry_spritelayout_store_shed"),
        (
            3,
            0,
            "foundry_spritelayout_large_shed",
        ),
        (3, 1, "foundry_spritelayout_furnace_anim"),
        (3, 2, "foundry_spritelayout_iron_pigs_anim"),
        (
            4,
            0,
            "foundry_spritelayout_large_shed",
        ),
        (4, 1, "foundry_spritelayout_furnace_anim"),
        (4, 2, "foundry_spritelayout_iron_pigs_anim"),
        (5, 0, "foundry_spritelayout_large_chimney"),
        (5, 1, "foundry_spritelayout_silos"),
        (5, 2, "foundry_spritelayout_empty"),
    ],
)

industry.add_industry_layout(
    id="foundry_industry_layout_2",
    layout=[
        (
            0,
            0,
            "foundry_spritelayout_large_shed",
        ),
        (0, 1, "foundry_spritelayout_furnace_anim"),
        (0, 2, "foundry_spritelayout_iron_pigs_anim"),
        (
            0,
            3,
            "foundry_spritelayout_large_shed",
        ),
        (0, 4, "foundry_spritelayout_furnace_anim"),
        (0, 5, "foundry_spritelayout_iron_pigs_anim"),
        (
            1,
            0,
            "foundry_spritelayout_large_shed",
        ),
        (1, 1, "foundry_spritelayout_furnace_anim"),
        (1, 2, "foundry_spritelayout_iron_pigs_anim"),
        (
            1,
            3,
            "foundry_spritelayout_large_shed",
        ),
        (1, 4, "foundry_spritelayout_furnace_anim"),
        (1, 5, "foundry_spritelayout_iron_pigs_anim"),
        (2, 0, "foundry_spritelayout_large_chimney"),
        (2, 1, "foundry_spritelayout_silos"),
        (2, 2, "foundry_spritelayout_empty"),
        (2, 3, "foundry_spritelayout_large_chimney"),
        (2, 4, "foundry_spritelayout_silos"),
        (2, 5, "foundry_spritelayout_store_shed"),
    ],
)

industry.add_industry_layout(
    id="foundry_industry_layout_3",
    layout=[
        (
            0,
            0,
            "foundry_spritelayout_large_shed",
        ),
        (
            0,
            1,
            "foundry_spritelayout_large_shed",
        ),
        (0, 2, "foundry_spritelayout_furnace_anim"),
        (0, 3, "foundry_spritelayout_iron_pigs_anim"),
        (
            1,
            0,
            "foundry_spritelayout_large_shed",
        ),
        (
            1,
            1,
            "foundry_spritelayout_large_shed",
        ),
        (1, 2, "foundry_spritelayout_furnace_anim"),
        (1, 3, "foundry_spritelayout_iron_pigs_anim"),
        (2, 0, "foundry_spritelayout_large_chimney"),
        (2, 1, "foundry_spritelayout_large_chimney"),
        (2, 2, "foundry_spritelayout_silos"),
        (2, 3, "foundry_spritelayout_store_shed"),
    ],
)
