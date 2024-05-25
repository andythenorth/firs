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
        # high foundry output production is unwanted
        ("FOCA", 5),
        ("ENSP", 1),
    ],
    prob_in_game="2",
    prob_map_gen="5",
    map_colour="166",
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
    type="gravel",
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
    sprites=[(430, 10, 64, 70, -31, -39)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(500, 10, 64, 70, -31, -39)],
)
spriteset_iron_pigs_anim = industry.add_spriteset(
    sprites=[
        (220, 10, 64, 70, -31, -39),
        (290, 10, 64, 70, -31, -39),
        (360, 10, 64, 70, -31, -39),
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
)
industry.add_spritelayout(
    id="foundry_spritelayout_large_shed",
    tile="foundry_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=[],
)
industry.add_spritelayout(
    id="foundry_spritelayout_large_shed_clerestory_roof",
    tile="foundry_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=[],
)
industry.add_spritelayout(
    id="foundry_spritelayout_iron_pigs_anim",
    tile="foundry_tile_3",
    ground_sprite=spriteset_ground_pigs,
    ground_overlay=spriteset_ground_overlay_pigs,
    building_sprites=[spriteset_iron_pigs_anim],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="foundry_spritelayout_staithes",
    tile="foundry_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne"],
)
industry.add_spritelayout(
    id="foundry_spritelayout_logs",
    tile="foundry_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="foundry_spritelayout_empty",
    tile="foundry_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se"],
)
industry.add_industry_layout(
    id="foundry_industry_layout_1",
    layout=[
        (
            0,
            0,
            "foundry_spritelayout_large_shed_clerestory_roof",
        ),
        (0, 1, "foundry_spritelayout_furnace_anim"),
        (0, 2, "foundry_spritelayout_iron_pigs_anim"),
        (
            1,
            0,
            "foundry_spritelayout_large_shed_clerestory_roof",
        ),
        (1, 1, "foundry_spritelayout_furnace_anim"),
        (1, 2, "foundry_spritelayout_iron_pigs_anim"),
        (2, 0, "foundry_spritelayout_large_shed"),
        (2, 1, "foundry_spritelayout_staithes"),
        (2, 2, "foundry_spritelayout_logs"),
        (
            3,
            0,
            "foundry_spritelayout_large_shed_clerestory_roof",
        ),
        (3, 1, "foundry_spritelayout_furnace_anim"),
        (3, 2, "foundry_spritelayout_iron_pigs_anim"),
        (
            4,
            0,
            "foundry_spritelayout_large_shed_clerestory_roof",
        ),
        (4, 1, "foundry_spritelayout_furnace_anim"),
        (4, 2, "foundry_spritelayout_iron_pigs_anim"),
        (5, 0, "foundry_spritelayout_large_shed"),
        (5, 1, "foundry_spritelayout_staithes"),
        (5, 2, "foundry_spritelayout_logs"),
    ],
)
