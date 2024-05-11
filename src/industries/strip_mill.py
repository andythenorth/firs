from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="strip_mill",
    accept_cargos_with_input_ratios=[
        ("STSL", 5),
        ("ACID", 1),
        ("ZINC", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        # high strip mill production is unwanted as there is only one output cargo
        ("STSH", 6),
    ],
    # do not build during gameplay
    prob_in_game="0",
    prob_map_gen="5",
    map_colour="160",
    name="string(STR_IND_STRIP_MILL)",
    nearby_station_name="string(STR_STATION_STRIP_MILL)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
    sprites_complete=True,
)


industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="strip_mill_tile_1",
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


spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_boilerhouse = industry.add_spriteset(
    sprites=[(10, 10, 64, 101, -31, -71)],
)
spriteset_shed_1 = industry.add_spriteset(
    sprites=[(80, 10, 64, 101, -31, -70)],
)
spriteset_shed_2 = industry.add_spriteset(
    sprites=[(150, 10, 64, 101, -31, -70)],
)
spriteset_shed_3 = industry.add_spriteset(
    sprites=[(220, 10, 64, 101, -31, -70)],
)
spriteset_shed_4 = industry.add_spriteset(
    sprites=[(290, 10, 64, 101, -31, -70)],
)
spriteset_open_shed_coils = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -33)],
)
spriteset_tanks = industry.add_spriteset(
    sprites=[(500, 10, 64, 64, -31, -33)],
)
spriteset_small_office = industry.add_spriteset(
    sprites=[(570, 10, 64, 64, -31, -33)],
)
spriteset_coils_1 = industry.add_spriteset(
    sprites=[(360, 80, 64, 31, -31, 0)],
)
spriteset_coils_2 = industry.add_spriteset(
    sprites=[(430, 80, 64, 31, -31, 0)],
)
spriteset_forklift_1 = industry.add_spriteset(
    sprites=[(500, 80, 64, 31, -31, -10)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-5,
    yoffset=0,
    zoffset=39,
)

industry.add_spritelayout(
    id="strip_mill_spritelayout_boilerhouse",
    tile="strip_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_boilerhouse],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="strip_mill_spritelayout_shed_1",
    tile="strip_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_1],
    fences=[],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="strip_mill_spritelayout_shed_2",
    tile="strip_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_2],
    fences=[],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="strip_mill_spritelayout_shed_3",
    tile="strip_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_3],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="strip_mill_spritelayout_shed_4",
    tile="strip_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_4],
    fences=[],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="strip_mill_spritelayout_open_shed_coils",
    tile="strip_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_open_shed_coils],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="strip_mill_spritelayout_tanks",
    tile="strip_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_tanks],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="strip_mill_spritelayout_office",
    tile="strip_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_small_office],
    fences=["nw", "ne", "sw"],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="strip_mill_spritelayout_coils_1",
    tile="strip_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_coils_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="strip_mill_spritelayout_coils_2",
    tile="strip_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_coils_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="strip_mill_spritelayout_forklift_1",
    tile="strip_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_forklift_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="strip_mill_spritelayout_small_office",
    tile="strip_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_small_office],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="strip_mill_spritelayout_empty",
    tile="strip_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=[],
)

# this industry needs outpost layout as there are lots of cargos
industry.add_industry_outpost_layout(
    id="strip_mill_industry_outpost_layout_1",
    layout=[
        # test outpost layout
        (
            0,
            0,
            "strip_mill_spritelayout_shed_1",
        ),
        (
            0,
            1,
            "strip_mill_spritelayout_coils_2",
        ),
        (
            1,
            0,
            "strip_mill_spritelayout_shed_4",
        ),
        (
            1,
            1,
            "strip_mill_spritelayout_coils_1",
        ),
        (
            2,
            0,
            "strip_mill_spritelayout_tanks",
        ),
        (
            2,
            1,
            "strip_mill_spritelayout_boilerhouse",
        ),
    ],
)

industry.add_industry_layout(
    id="strip_mill_industry_layout_1",
    layout=[
        (
            0,
            0,
            "strip_mill_spritelayout_shed_1",
        ),
        (
            0,
            1,
            "strip_mill_spritelayout_shed_1",
        ),
        (
            0,
            2,
            "strip_mill_spritelayout_shed_4",
        ),
        (
            1,
            0,
            "strip_mill_spritelayout_shed_3",
        ),
        (
            1,
            1,
            "strip_mill_spritelayout_shed_1",
        ),
        (
            1,
            2,
            "strip_mill_spritelayout_shed_4",
        ),
        (
            2,
            0,
            "strip_mill_spritelayout_shed_1",
        ),
        (
            2,
            1,
            "strip_mill_spritelayout_boilerhouse",
        ),
        (
            2,
            2,
            "strip_mill_spritelayout_forklift_1",
        ),
        (
            3,
            0,
            "strip_mill_spritelayout_shed_1",
        ),
        (
            3,
            1,
            "strip_mill_spritelayout_tanks",
        ),
        (
            3,
            2,
            "strip_mill_spritelayout_small_office",
        ),
        (
            4,
            0,
            "strip_mill_spritelayout_shed_1",
        ),
        (
            4,
            1,
            "strip_mill_spritelayout_coils_2",
        ),
        (
            4,
            2,
            "strip_mill_spritelayout_empty",
        ),
        (5, 0, "strip_mill_spritelayout_shed_2"),
        (
            5,
            1,
            "strip_mill_spritelayout_coils_1",
        ),
        (
            5,
            2,
            "strip_mill_spritelayout_open_shed_coils",
        ),
    ],
)
