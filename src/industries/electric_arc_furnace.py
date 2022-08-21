from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="electric_arc_furnace",
    accept_cargos_with_input_ratios=[
        ("SCMT", 4),
        ("FECR", 2),
        ("QLME", 1),
        ("O2__", 1),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("STCB", 4), ("STST", 2), ("SLAG", 2)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="186",
    name="string(STR_IND_ELECTRIC_ARC_FURNACE)",
    nearby_station_name="string(STR_STATION_FURNACE)",
    fund_cost_multiplier="160",
    pollution_and_squalor_factor=2,
)

industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations[
    "STEELTOWN"
].prob_in_game = "1"  # low chance of build during gameplay

industry.add_tile(
    id="electric_arc_furnace_tile_1",
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
    type="hard_standing_dirt",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 76, -31, -45)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 76, -31, -45)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 63, -31, -32)],
)
spriteset_scrap_1 = industry.add_spriteset(
    sprites=[(220, 10, 64, 63, -31, -32)],
)
spriteset_scrap_2 = industry.add_spriteset(
    sprites=[(290, 10, 64, 63, -31, -32)],
)
spriteset_metal_1 = industry.add_spriteset(
    sprites=[(360, 10, 64, 63, -31, -32)],
)
spriteset_metal_2 = industry.add_spriteset(
    sprites=[(430, 10, 64, 63, -31, -32)],
)
spriteset_crane_1 = industry.add_spriteset(
    sprites=[(500, 10, 64, 63, -31, -32)],
)
spriteset_crane_2 = industry.add_spriteset(
    sprites=[(570, 10, 64, 63, -31, -32)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-5,
    yoffset=0,
    zoffset=40,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-5,
    yoffset=5,
    zoffset=40,
)

industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_empty",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_scrap_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_scrap_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_scrap_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_scrap_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_crane_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_crane_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_crane_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_crane_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_metal_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_metal_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_2],
    fences=["nw", "ne", "se", "sw"],
)

# min 6x4 or 5x5 as there are lots of output cargos
industry.add_industry_layout(
    id="electric_arc_furnace_industry_layout_1",
    layout=[
        # test outpost layout
        (4, 0, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_metal_2"),
        (4, 1, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_metal_1"),
        (5, 0, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_metal_2"),
        (5, 1, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_crane_2"),
        # main layout, shifted by 4 in y direction
        (0, 4, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_2"),
        (0, 5, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_2"),
        (0, 6, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_2"),
        (0, 7, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_2"),
        (0, 8, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_3"),
        (0, 9, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_3"),
        (1, 4, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_1"),
        (1, 5, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_1"),
        (1, 6, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_1"),
        (1, 7, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_1"),
        (
            1,
            8,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_scrap_1",
        ),
        (
            1,
            9,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_scrap_1",
        ),
        (
            2,
            4,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_metal_2",
        ),
        (
            2,
            5,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_metal_2",
        ),
        (
            2,
            6,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_metal_1",
        ),
        (
            2,
            7,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_empty",
        ),
        (
            2,
            8,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_crane_1",
        ),
        (
            2,
            9,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_scrap_1",
        ),
        (
            3,
            4,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_metal_2",
        ),
        (
            3,
            5,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_metal_2",
        ),
        (
            3,
            6,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_crane_2",
        ),
        (
            3,
            7,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_empty",
        ),
        (
            3,
            8,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_scrap_2",
        ),
        (
            3,
            9,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_crane_1",
        ),
    ],
)
