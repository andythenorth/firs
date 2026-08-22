from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="convenience_foods_factory",
    accept_cargos_with_input_ratios=[
        ("MEAT", 2),
        ("VEG_", 2),
        ("BAKE", 2),
        ("ENUM", 1),
        ("PACK", 1),
    ],
    prod_cargo_types_with_output_ratios=[
        ("FOOD", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="151",
    colour_scheme_name="scheme_3_hendrix",
    name="string(STR_IND_CONVENIENCE_FOODS_FACTORY)",
    nearby_station_name="string(STR_STATION_SOUPS)",
    fund_cost_multiplier="95",
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "MILD_MILD_WEST",
)

industry.add_tile(
    id="convenience_foods_factory_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="convenience_foods_factory_tile_2",
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
spriteset_ground_overlay_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_ground_overlay_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 31, -31, 0)],
)
spriteset_ground_overlay_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 31, -31, 0)],
)
spriteset_ground_overlay_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 90, -31, -59)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 90, -31, -71)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 90, -31, -59)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 90, -31, -59)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=13,
    yoffset=0,
    zoffset=54,
)

industry.add_spritelayout(
    id="convenience_foods_factory_spritelayout_1",
    tile="convenience_foods_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay_1,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="convenience_foods_factory_spritelayout_2",
    tile="convenience_foods_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay_2,
    building_sprites=[spriteset_2, spriteset_4],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="convenience_foods_factory_spritelayout_3",
    tile="convenience_foods_factory_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay_3,
    building_sprites=[spriteset_3],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "sw"],
)
industry.add_spritelayout(
    id="convenience_foods_factory_spritelayout_4",
    tile="convenience_foods_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay_4,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

# this industry needs outpost layout as there are lots of cargos
industry.add_industry_outpost_layout(
    id="convenience_foods_factory_industry_outpost_layout_1",
    layout=[
        # test outpost layout
        (
            0,
            0,
            "convenience_foods_factory_spritelayout_4",
        ),
        (
            0,
            1,
            "convenience_foods_factory_spritelayout_3",
        ),
        (
            1,
            0,
            "convenience_foods_factory_spritelayout_1",
        ),
        (
            1,
            1,
            "convenience_foods_factory_spritelayout_2",
        ),
    ],
)

industry.add_industry_layout(
    id="convenience_foods_factory_industry_layout_1",
    layout=[
        (0, 0, "convenience_foods_factory_spritelayout_4"),
        (0, 1, "convenience_foods_factory_spritelayout_3"),
        (0, 2, "convenience_foods_factory_spritelayout_4"),
        (0, 3, "convenience_foods_factory_spritelayout_3"),
        (1, 0, "convenience_foods_factory_spritelayout_1"),
        (1, 1, "convenience_foods_factory_spritelayout_2"),
        (1, 2, "convenience_foods_factory_spritelayout_1"),
        (1, 3, "convenience_foods_factory_spritelayout_2"),
        (2, 0, "convenience_foods_factory_spritelayout_4"),
        (2, 1, "convenience_foods_factory_spritelayout_3"),
        (2, 2, "convenience_foods_factory_spritelayout_4"),
        (2, 3, "convenience_foods_factory_spritelayout_3"),
        (3, 0, "convenience_foods_factory_spritelayout_1"),
        (3, 1, "convenience_foods_factory_spritelayout_2"),
        (3, 2, "convenience_foods_factory_spritelayout_1"),
        (3, 3, "convenience_foods_factory_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="convenience_foods_factory_industry_layout_2",
    layout=[
        (0, 0, "convenience_foods_factory_spritelayout_4"),
        (0, 1, "convenience_foods_factory_spritelayout_3"),
        (1, 0, "convenience_foods_factory_spritelayout_1"),
        (1, 1, "convenience_foods_factory_spritelayout_2"),
        (1, 2, "convenience_foods_factory_spritelayout_4"),
        (1, 3, "convenience_foods_factory_spritelayout_3"),
        (2, 0, "convenience_foods_factory_spritelayout_4"),
        (2, 1, "convenience_foods_factory_spritelayout_3"),
        (2, 2, "convenience_foods_factory_spritelayout_1"),
        (2, 3, "convenience_foods_factory_spritelayout_2"),
        (3, 0, "convenience_foods_factory_spritelayout_1"),
        (3, 1, "convenience_foods_factory_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="convenience_foods_factory_industry_layout_3",
    layout=[
        (0, 0, "convenience_foods_factory_spritelayout_4"),
        (0, 1, "convenience_foods_factory_spritelayout_3"),
        (0, 2, "convenience_foods_factory_spritelayout_4"),
        (0, 3, "convenience_foods_factory_spritelayout_3"),
        (1, 0, "convenience_foods_factory_spritelayout_1"),
        (1, 1, "convenience_foods_factory_spritelayout_2"),
        (1, 2, "convenience_foods_factory_spritelayout_1"),
        (1, 3, "convenience_foods_factory_spritelayout_2"),
        (2, 1, "convenience_foods_factory_spritelayout_4"),
        (2, 2, "convenience_foods_factory_spritelayout_3"),
        (3, 1, "convenience_foods_factory_spritelayout_1"),
        (3, 2, "convenience_foods_factory_spritelayout_2"),
    ],
)
