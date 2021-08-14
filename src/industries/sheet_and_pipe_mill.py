from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="sheet_and_pipe_mill",
    accept_cargos_with_input_ratios=[("STCB", 4), ("ZINC", 2), ("ACID", 2)],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("STSH", 4), ("PIPE", 3), ("ENSP", 1)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="160",
    name="string(STR_IND_SHEET_AND_PIPE_MILL)",
    nearby_station_name="string(STR_STATION_PIPE_MILL)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
)


industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations[
    "STEELTOWN"
].prob_in_game = "0"  # do not build during gameplay

industry.add_tile(
    id="sheet_and_pipe_mill_tile_1",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)


spriteset_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 64, -31, -34)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -33)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -33)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -33)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -33)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -33)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 64, -31, -33)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 64, -31, -33)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 64, -31, -33)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(360, 80, 64, 31, -31, 0)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(430, 80, 64, 31, -31, 0)],
)
spriteset_12 = industry.add_spriteset(
    sprites=[(500, 80, 64, 31, -31, -10)],
)
spriteset_13 = industry.add_spriteset(
    sprites=[(570, 80, 64, 31, -31, 0)],
)
spriteset_14 = industry.add_spriteset(
    sprites=[(640, 80, 64, 31, -31, 0)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-5,
    yoffset=0,
    zoffset=39,
)

industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_boilerhouse",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_shed_sw_ne_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_shed_sw_ne_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_shed_se_nw_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_shed_se_nw_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_open_shed_coils",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_open_shed_slabs",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_tanks",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_office",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "sw"],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_steel_pile_sw_ne",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_steel_pile_se_nw",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_11],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_greeble",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_12],
    fences=[],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_pipe_stack_sw_ne",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_13],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_pipe_stack_se_nw",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_14],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="sheet_and_pipe_mill_spritelayout_empty",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=[],
)

# long products mill uses non-standard layouts where some sprites only used for some orientiations (sw_ne or se_nw)
# this is to achieve the appearance of 'long'
# min 6x4 as there are lots of output cargos
industry.add_industry_layout(
    id="sheet_and_pipe_mill_industry_layout_1",
    layout=[
        (
            0,
            0,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            0,
            1,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            0,
            2,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_boilerhouse",
        ),
        (
            0,
            3,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_open_shed_coils",
        ),
        (
            1,
            0,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            1,
            1,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            1,
            2,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_steel_pile_se_nw",
        ),
        (
            1,
            3,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_steel_pile_sw_ne",
        ),
        (
            2,
            0,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            2,
            1,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            2,
            2,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (2, 3, "sheet_and_pipe_mill_tile_1", "sheet_and_pipe_mill_spritelayout_empty"),
        (
            3,
            0,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            3,
            1,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            3,
            2,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_sw_ne_1",
        ),
        (
            3,
            3,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_pipe_stack_sw_ne",
        ),
        (
            4,
            0,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_open_shed_slabs",
        ),
        (
            4,
            1,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_open_shed_slabs",
        ),
        (
            4,
            2,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_sw_ne_2",
        ),
        (
            4,
            3,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_pipe_stack_sw_ne",
        ),
        (5, 0, "sheet_and_pipe_mill_tile_1", "sheet_and_pipe_mill_spritelayout_tanks"),
        (5, 1, "sheet_and_pipe_mill_tile_1", "sheet_and_pipe_mill_spritelayout_empty"),
        (
            5,
            2,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_greeble",
        ),
        (5, 3, "sheet_and_pipe_mill_tile_1", "sheet_and_pipe_mill_spritelayout_office"),
    ],
)
industry.add_industry_layout(
    id="sheet_and_pipe_mill_industry_layout_2",
    layout=[
        (
            0,
            0,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_se_nw_1",
        ),
        (
            0,
            1,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_se_nw_2",
        ),
        (
            0,
            2,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_se_nw_2",
        ),
        (
            0,
            3,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_se_nw_1",
        ),
        (
            0,
            4,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_open_shed_slabs",
        ),
        (0, 5, "sheet_and_pipe_mill_tile_1", "sheet_and_pipe_mill_spritelayout_tanks"),
        (
            1,
            0,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_se_nw_1",
        ),
        (
            1,
            1,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_se_nw_2",
        ),
        (
            1,
            2,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_se_nw_2",
        ),
        (
            1,
            3,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_se_nw_1",
        ),
        (
            1,
            4,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_open_shed_slabs",
        ),
        (1, 5, "sheet_and_pipe_mill_tile_1", "sheet_and_pipe_mill_spritelayout_empty"),
        (
            2,
            0,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_boilerhouse",
        ),
        (
            2,
            1,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_steel_pile_sw_ne",
        ),
        (
            2,
            2,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_se_nw_2",
        ),
        (
            2,
            3,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_se_nw_1",
        ),
        (
            2,
            4,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_shed_se_nw_2",
        ),
        (
            2,
            5,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_greeble",
        ),
        (
            3,
            0,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_open_shed_coils",
        ),
        (
            3,
            1,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_steel_pile_se_nw",
        ),
        (3, 2, "sheet_and_pipe_mill_tile_1", "sheet_and_pipe_mill_spritelayout_empty"),
        (
            3,
            3,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_pipe_stack_se_nw",
        ),
        (
            3,
            4,
            "sheet_and_pipe_mill_tile_1",
            "sheet_and_pipe_mill_spritelayout_pipe_stack_se_nw",
        ),
        (3, 5, "sheet_and_pipe_mill_tile_1", "sheet_and_pipe_mill_spritelayout_office"),
    ],
)
