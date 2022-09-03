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
spriteset_large_shed_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -90)],
)
spriteset_large_shed_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -90)],
)
spriteset_large_shed_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_tanks = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
)
spriteset_air_plant = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
)
spriteset_metal_1 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -33)],
)
spriteset_extra_shed_1 = industry.add_spriteset(
    sprites=[(430, 10, 64, 64, -31, -33)],
)
spriteset_casting_shed_1 = industry.add_spriteset(
    sprites=[(10, 160, 64, 64, -31, -33)],
)
spriteset_casting_shed_2 = industry.add_spriteset(
    sprites=[(80, 160, 64, 64, -31, -33)],
)
spriteset_casting_shed_3 = industry.add_spriteset(
    sprites=[(150, 160, 64, 64, -31, -33)],
)
spriteset_caster_line_roof_animated = industry.add_spriteset(
    sprites=[(80, 160, 64, 64, -31, -33)],
)
spriteset_caster_line_1_animated = industry.add_spriteset(
    sprites=[(10, 250, 64, 64, -31, -33)],
)
spriteset_caster_line_metal_animated = industry.add_spriteset(
    sprites=[(10, 340, 64, 64, -31, -33)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=2,
    yoffset=0,
    zoffset=56,
)

industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_empty",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_large_furnace_shed_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_shed_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_large_furnace_shed_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_shed_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_large_furnace_shed_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_shed_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_casting_shed_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_casting_shed_1],
    fences=["nw", "ne"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_casting_shed_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_casting_shed_2],
    fences=["nw", "ne"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_casting_shed_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_casting_shed_3],
    fences=["nw", "ne"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_caster_line_animated",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_caster_line_1_animated, spriteset_caster_line_metal_animated],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_tanks",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_tanks],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_air_plant",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_air_plant],
    fences=["nw", "ne", "se", "sw"],
    smoke_sprites=[sprite_smoke_1,],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_metal_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="electric_arc_furnace_spritelayout_extra_shed_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_extra_shed_1],
    fences=["nw", "ne", "se", "sw"],
)
# this industry needs outpost layout as there are lots of cargos
industry.add_industry_outpost_layout(
    id="electric_arc_furnace_industry_outpost_layout_1",
    layout=[
        # test outpost layout
        (0, 0, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_casting_shed_1"),
        (0, 1, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_casting_shed_2"),
        (0, 2, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_casting_shed_3"),
        (1, 0, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_air_plant"),
        (1, 1, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_tanks"),
        (1, 2, "electric_arc_furnace_tile_1", "electric_arc_furnace_spritelayout_metal_1"),
    ],
)
# core layouts are roughly 6x4 or 5x5
industry.add_industry_layout(
    id="electric_arc_furnace_industry_layout_1",
    layout=[
        (
            0,
            0,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            1,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            2,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            0,
            3,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            0,
            4,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            1,
            0,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_large_furnace_shed_1",
        ),
        (
            1,
            1,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_large_furnace_shed_3",
        ),
        (
            1,
            2,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_caster_line_animated",
        ),
        (
            1,
            3,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            1,
            4,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_casting_shed_3",
        ),
        (
            2,
            0,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_tanks",
        ),
        (
            2,
            1,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_air_plant",
        ),
        (
            2,
            2,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_metal_1",
        ),
        (
            2,
            3,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_metal_1",
        ),
        (
            2,
            4,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_extra_shed_1",
        ),
    ],
)
# just a swap of the air plant and tanks to test...
industry.add_industry_layout(
    id="electric_arc_furnace_industry_layout_2",
    layout=[
        (
            0,
            0,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            1,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_large_furnace_shed_2",
        ),
        (
            0,
            2,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            0,
            3,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            0,
            4,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_casting_shed_1",
        ),
        (
            1,
            0,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_large_furnace_shed_1",
        ),
        (
            1,
            1,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_large_furnace_shed_3",
        ),
        (
            1,
            2,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_caster_line_animated",
        ),
        (
            1,
            3,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_casting_shed_2",
        ),
        (
            1,
            4,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_casting_shed_3",
        ),
        (
            2,
            0,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_air_plant",
        ),
        (
            2,
            1,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_tanks",
        ),
        (
            2,
            2,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_metal_1",
        ),
        (
            2,
            3,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_metal_1",
        ),
        (
            2,
            4,
            "electric_arc_furnace_tile_1",
            "electric_arc_furnace_spritelayout_extra_shed_1",
        ),
    ],
)
