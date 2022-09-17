from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="glass_works",
    accept_cargos_with_input_ratios=[
        ("SAND", 6),
        ("SASH", 2),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("GLAS", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="151",
    special_flags=["IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE"],
    name="string(STR_IND_GLASS_WORKS)",
    nearby_station_name="string(STR_STATION_SHARP_STREET)",
    fund_cost_multiplier="95",
    provides_snow=True,
)

industry.enable_in_economy(
    "BASIC_TEMPERATE",
    accept_cargos_with_input_ratios=[
        ("SAND", 6),
        ("RFPR", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("GOOD", 8),
    ],
)


industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
    accept_cargos_with_input_ratios=[
        ("SAND", 6),
        ("RFPR", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("BDMT", 4),
        ("GOOD", 4),
    ],
)

industry.enable_in_economy(
    "STEELTOWN",
    accept_cargos_with_input_ratios=[
        ("SAND", 6),
        ("SASH", 2),
    ],  # no limestone or dolomite, too much detail
    prob_in_game="1",  # low probability of build during gameplay
)

industry.add_tile(
    id="glass_works_tile_1",
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
    type="cobble",
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
    id="glass_works_spritelayout_1",
    tile="glass_works_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay_1,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="glass_works_spritelayout_2",
    tile="glass_works_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay_2,
    building_sprites=[spriteset_2, spriteset_4],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="glass_works_spritelayout_3",
    tile="glass_works_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay_3,
    building_sprites=[spriteset_3],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "sw"],
)
industry.add_spritelayout(
    id="glass_works_spritelayout_4",
    tile="glass_works_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay_4,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="glass_works_industry_layout_1",
    layout=[
        (0, 0, "glass_works_spritelayout_4"),
        (0, 1, "glass_works_spritelayout_3"),
        (0, 2, "glass_works_spritelayout_4"),
        (0, 3, "glass_works_spritelayout_3"),
        (1, 0, "glass_works_spritelayout_1"),
        (1, 1, "glass_works_spritelayout_2"),
        (1, 2, "glass_works_spritelayout_1"),
        (1, 3, "glass_works_spritelayout_2"),
        (2, 0, "glass_works_spritelayout_4"),
        (2, 1, "glass_works_spritelayout_3"),
        (2, 2, "glass_works_spritelayout_4"),
        (2, 3, "glass_works_spritelayout_3"),
        (3, 0, "glass_works_spritelayout_1"),
        (3, 1, "glass_works_spritelayout_2"),
        (3, 2, "glass_works_spritelayout_1"),
        (3, 3, "glass_works_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="glass_works_industry_layout_2",
    layout=[
        (0, 0, "glass_works_spritelayout_4"),
        (0, 1, "glass_works_spritelayout_3"),
        (1, 0, "glass_works_spritelayout_1"),
        (1, 1, "glass_works_spritelayout_2"),
        (1, 2, "glass_works_spritelayout_4"),
        (1, 3, "glass_works_spritelayout_3"),
        (2, 0, "glass_works_spritelayout_4"),
        (2, 1, "glass_works_spritelayout_3"),
        (2, 2, "glass_works_spritelayout_1"),
        (2, 3, "glass_works_spritelayout_2"),
        (3, 0, "glass_works_spritelayout_1"),
        (3, 1, "glass_works_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="glass_works_industry_layout_3",
    layout=[
        (0, 0, "glass_works_spritelayout_4"),
        (0, 1, "glass_works_spritelayout_3"),
        (0, 2, "glass_works_spritelayout_4"),
        (0, 3, "glass_works_spritelayout_3"),
        (1, 0, "glass_works_spritelayout_1"),
        (1, 1, "glass_works_spritelayout_2"),
        (1, 2, "glass_works_spritelayout_1"),
        (1, 3, "glass_works_spritelayout_2"),
        (2, 1, "glass_works_spritelayout_4"),
        (2, 2, "glass_works_spritelayout_3"),
        (3, 1, "glass_works_spritelayout_1"),
        (3, 2, "glass_works_spritelayout_2"),
    ],
)
