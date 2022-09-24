from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="tinplate_works",
    accept_cargos_with_input_ratios=[
        ("STSH", 4),
        ("TIN_", 2),
        ("SUAC", 2),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("TINP", 8)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="160",
    name="string(STR_IND_TINPLATE_WORKS)",
    nearby_station_name="string(STR_STATION_HEAVY_INDUSTRY_2)",
    fund_cost_multiplier="120",
)

# Tinplate is *not* in Steeltown because it fragments the consumers of Acid too much.  Maybe Better Living Through Chemistry?

industry.add_tile(
    id="tinplate_works_tile_1",
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
    sprites=[(10, 60, 64, 70, -31, -35)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 70, -31, -35)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 51, -31, -20)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 51, -31, -23)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 60, 64, 51, -31, -20)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 60, 64, 31, -31, 0)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 60, 64, 31, -31, 0)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-5,
    yoffset=0,
    zoffset=26,
)

industry.add_spritelayout(
    id="tinplate_works_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tinplate_works_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tinplate_works_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tinplate_works_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tinplate_works_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tinplate_works_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="tinplate_works_spritelayout_7",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="tinplate_works_industry_layout_1",
    layout=[
        (0, 0, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (0, 1, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (0, 2, "tinplate_works_tile_1", "tinplate_works_spritelayout_4"),
        (0, 3, "tinplate_works_tile_1", "tinplate_works_spritelayout_6"),
        (0, 4, "tinplate_works_tile_1", "tinplate_works_spritelayout_5"),
        (1, 0, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (1, 1, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (1, 2, "tinplate_works_tile_1", "tinplate_works_spritelayout_7"),
        (1, 3, "tinplate_works_tile_1", "tinplate_works_spritelayout_6"),
        (1, 4, "tinplate_works_tile_1", "tinplate_works_spritelayout_5"),
        (2, 0, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (2, 1, "tinplate_works_tile_1", "tinplate_works_spritelayout_1"),
        (2, 2, "tinplate_works_tile_1", "tinplate_works_spritelayout_2"),
        (2, 3, "tinplate_works_tile_1", "tinplate_works_spritelayout_7"),
        (2, 4, "tinplate_works_tile_1", "tinplate_works_spritelayout_6"),
    ],
)
industry.add_industry_layout(
    id="tinplate_works_industry_layout_2",
    layout=[
        (0, 2, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (0, 3, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (1, 0, "tinplate_works_tile_1", "tinplate_works_spritelayout_1"),
        (1, 1, "tinplate_works_tile_1", "tinplate_works_spritelayout_2"),
        (1, 2, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (1, 3, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (2, 0, "tinplate_works_tile_1", "tinplate_works_spritelayout_7"),
        (2, 1, "tinplate_works_tile_1", "tinplate_works_spritelayout_7"),
        (2, 2, "tinplate_works_tile_1", "tinplate_works_spritelayout_6"),
        (2, 3, "tinplate_works_tile_1", "tinplate_works_spritelayout_6"),
        (3, 0, "tinplate_works_tile_1", "tinplate_works_spritelayout_4"),
        (3, 1, "tinplate_works_tile_1", "tinplate_works_spritelayout_5"),
        (3, 2, "tinplate_works_tile_1", "tinplate_works_spritelayout_5"),
        (3, 3, "tinplate_works_tile_1", "tinplate_works_spritelayout_5"),
    ],
)
industry.add_industry_layout(
    id="tinplate_works_industry_layout_3",
    layout=[
        (0, 0, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (0, 1, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (0, 2, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (0, 3, "tinplate_works_tile_1", "tinplate_works_spritelayout_5"),
        (1, 0, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (1, 1, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (1, 2, "tinplate_works_tile_1", "tinplate_works_spritelayout_3"),
        (1, 3, "tinplate_works_tile_1", "tinplate_works_spritelayout_6"),
        (2, 0, "tinplate_works_tile_1", "tinplate_works_spritelayout_5"),
        (2, 1, "tinplate_works_tile_1", "tinplate_works_spritelayout_1"),
        (2, 2, "tinplate_works_tile_1", "tinplate_works_spritelayout_2"),
        (2, 3, "tinplate_works_tile_1", "tinplate_works_spritelayout_7"),
        (3, 0, "tinplate_works_tile_1", "tinplate_works_spritelayout_5"),
        (3, 1, "tinplate_works_tile_1", "tinplate_works_spritelayout_4"),
        (3, 2, "tinplate_works_tile_1", "tinplate_works_spritelayout_7"),
        (3, 3, "tinplate_works_tile_1", "tinplate_works_spritelayout_6"),
    ],
)
