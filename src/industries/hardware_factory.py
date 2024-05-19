from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="hardware_factory",
    accept_cargos_with_input_ratios=[
        ("STEL", 6),
        ("RFPR", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("GOOD", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="209",
    name="string(STR_IND_HARDWARE_FACTORY)",
    nearby_station_name="string(STR_STATION_HARDWARE_FACTORY)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
    sprites_complete=False,
)

industry.enable_in_economy(
    "BASIC_TEMPERATE",
)

industry.enable_in_economy(
    "STEELTOWN",
    # two-cargo production boost - combined ratios of any two cargos must always be at least 8
    accept_cargos_with_input_ratios=[
        ("STSH", 6),
        ("STWR", 6),
        ("STBR", 6),
        ("FOCA", 6),
        ("CSTI", 6),
        ("ALUM", 6),
    ],
    prod_cargo_types_with_output_ratios=[
        ("HWAR", 4),
        ("GOOD", 4),
    ],
)

industry.add_tile(
    id="hardware_factory_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_shed_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 80, -31, -50)],
)
spriteset_shed_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 80, -31, -50)],
)
spriteset_tanks = industry.add_spriteset(
    sprites=[(220, 10, 64, 80, -31, -50)],
)
spriteset_office = industry.add_spriteset(
    sprites=[(290, 10, 64, 80, -31, -50)],
)

industry.add_spritelayout(
    id="hardware_factory_spritelayout_empty",
    tile="hardware_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=[],
)
industry.add_spritelayout(
    id="hardware_factory_spritelayout_shed_1",
    tile="hardware_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_1],
    fences=["nw", "ne"],
    # add_to_object_num=5,
)
industry.add_spritelayout(
    id="hardware_factory_spritelayout_shed_2",
    tile="hardware_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_2],
    fences=["ne"],
    # add_to_object_num=5,
)
industry.add_spritelayout(
    id="hardware_factory_spritelayout_office",
    tile="hardware_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_office],
    fences=["nw", "ne", "se", "sw"],
    # add_to_object_num=5,
)
industry.add_spritelayout(
    id="hardware_factory_spritelayout_tanks",
    tile="hardware_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_tanks],
    fences=["nw", "ne", "se", "sw"],
    # add_to_object_num=5,
)
industry.add_industry_layout(
    id="hardware_factory_industry_layout_1",
    layout=[
        (0, 0, "hardware_factory_spritelayout_shed_1"),
        (0, 1, "hardware_factory_spritelayout_shed_1"),
        (0, 2, "hardware_factory_spritelayout_shed_1"),
        (0, 3, "hardware_factory_spritelayout_shed_2"),
        (1, 0, "hardware_factory_spritelayout_shed_1"),
        (1, 1, "hardware_factory_spritelayout_shed_1"),
        (1, 2, "hardware_factory_spritelayout_empty"),
        (1, 3, "hardware_factory_spritelayout_office"),
        (2, 0, "hardware_factory_spritelayout_shed_1"),
        (2, 1, "hardware_factory_spritelayout_shed_1"),
        (2, 2, "hardware_factory_spritelayout_shed_2"),
        (2, 3, "hardware_factory_spritelayout_tanks"),
    ],
)
