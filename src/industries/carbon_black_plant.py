from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="carbon_black_plant",
    # amount of output is unrealistic 8:8 but input is usually small, so give a decent amount out eh?
    accept_cargos_with_input_ratios=[
        ("CTAR", 8),
    ],
    prod_cargo_types_with_output_ratios=[
        ("CBLK", 8),
    ],
    prob_in_game="0",  # do not build during gameplay
    prob_map_gen="5",
    map_colour="178",
    special_flags=["IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE"],
    # it's rare to force co-location of secondaries, but this one is near coke oven by design
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[["coke_oven"], 72],
        same_type_distance=72,
    ),
    name="string(STR_IND_CARBON_BLACK_PLANT)",
    nearby_station_name="string(STR_STATION_SOOT_FURNACE)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=2,
)

industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="carbon_black_plant_tile_1",
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

spriteset_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)

spriteset_boiler = industry.add_spriteset(
    sprites=[(10, 10, 64, 114, -31, -83)],
)
spriteset_chimneys = industry.add_spriteset(
    sprites=[(80, 10, 64, 114, -31, -83)],
)
spriteset_tanks_group = industry.add_spriteset(
    sprites=[(150, 10, 64, 114, -31, -83)],
)
spriteset_silos = industry.add_spriteset(
    sprites=[(220, 10, 64, 114, -31, -83)],
)
spriteset_silos_with_office = industry.add_spriteset(
    sprites=[(290, 10, 64, 114, -31, -83)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=9,
    yoffset=0,
    zoffset=87,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=2,
    yoffset=6,
    zoffset=71,
)
sprite_smoke_3 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=5,
    yoffset=6,
    zoffset=71,
)

industry.add_spritelayout(
    id="carbon_black_plant_spritelayout_empty",
    tile="carbon_black_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
)
industry.add_spritelayout(
    id="carbon_black_plant_spritelayout_boiler",
    tile="carbon_black_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_boiler],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="carbon_black_plant_spritelayout_chimneys",
    tile="carbon_black_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_chimneys],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2, sprite_smoke_3],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="carbon_black_plant_spritelayout_tanks_group",
    tile="carbon_black_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_tanks_group],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="carbon_black_plant_spritelayout_silos",
    tile="carbon_black_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_silos],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="carbon_black_plant_spritelayout_silos_with_office",
    tile="carbon_black_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_silos_with_office],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)

industry.add_industry_layout(
    id="carbon_black_plant_industry_layout_1",
    layout=[
        (0, 0, "carbon_black_plant_spritelayout_chimneys"),
        (0, 1, "carbon_black_plant_spritelayout_boiler"),
        (
            0,
            2,
            "carbon_black_plant_spritelayout_tanks_group",
        ),
        (1, 0, "carbon_black_plant_spritelayout_chimneys"),
        (1, 1, "carbon_black_plant_spritelayout_boiler"),
        (
            1,
            2,
            "carbon_black_plant_spritelayout_tanks_group",
        ),
        (
            2,
            0,
            "carbon_black_plant_spritelayout_silos_with_office",
        ),
        (2, 1, "carbon_black_plant_spritelayout_silos"),
        (2, 2, "carbon_black_plant_spritelayout_empty"),
    ],
)
industry.add_industry_layout(
    id="carbon_black_plant_industry_layout_2",
    layout=[
        (0, 0, "carbon_black_plant_spritelayout_boiler"),
        (
            0,
            1,
            "carbon_black_plant_spritelayout_tanks_group",
        ),
        (1, 0, "carbon_black_plant_spritelayout_boiler"),
        (
            1,
            1,
            "carbon_black_plant_spritelayout_tanks_group",
        ),
        (2, 0, "carbon_black_plant_spritelayout_chimneys"),
        (2, 1, "carbon_black_plant_spritelayout_silos"),
        (
            3,
            0,
            "carbon_black_plant_spritelayout_silos_with_office",
        ),
        (3, 1, "carbon_black_plant_spritelayout_empty"),
    ],
)
industry.add_industry_layout(
    id="carbon_black_plant_industry_layout_3",
    layout=[
        (0, 0, "carbon_black_plant_spritelayout_boiler"),
        (
            0,
            1,
            "carbon_black_plant_spritelayout_tanks_group",
        ),
        (0, 2, "carbon_black_plant_spritelayout_chimneys"),
        (0, 3, "carbon_black_plant_spritelayout_silos"),
        (1, 0, "carbon_black_plant_spritelayout_boiler"),
        (
            1,
            1,
            "carbon_black_plant_spritelayout_tanks_group",
        ),
        (
            1,
            2,
            "carbon_black_plant_spritelayout_silos_with_office",
        ),
        (1, 3, "carbon_black_plant_spritelayout_empty"),
    ],
)
