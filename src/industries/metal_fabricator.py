from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="metal_fabricator",
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
    colour_scheme_name="scheme_3_hendrix",
    name="string(STR_IND_METAL_FABRICATOR)",
    nearby_station_name="string(STR_STATION_HARDWARE_FACTORY)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
    sprites_complete=True,
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
        ("HWAR", 3),
        ("GOOD", 3),
        ("ENSP", 2),
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
spriteset_shed_1_with_chimneys = industry.add_spriteset(
    sprites=[(10, 10, 64, 80, -31, -50)],
)
spriteset_shed_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 80, -31, -50)],
)
spriteset_shed_3_half = industry.add_spriteset(
    sprites=[(150, 10, 64, 80, -31, -50)],
)
spriteset_shed_4_half_with_chimneys = industry.add_spriteset(
    sprites=[(220, 10, 64, 80, -31, -50)],
)
spriteset_shed_tall = industry.add_spriteset(
    sprites=[(290, 10, 64, 80, -31, -50)],
)
spriteset_small_building = industry.add_spriteset(
    sprites=[(360, 10, 64, 80, -31, -50)],
)
spriteset_greeble_1 = industry.add_spriteset(
    sprites=[(430, 10, 64, 80, -31, -50)],
)
spriteset_greeble_2 = industry.add_spriteset(
    sprites=[(500, 10, 64, 80, -31, -50)],
)

industry.add_spritelayout(
    id="hardware_factory_spritelayout_shed_1_with_chimneys",
    tile="hardware_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_1_with_chimneys],
    fences=["ne"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="hardware_factory_spritelayout_shed_2",
    tile="hardware_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_2],
    fences=["ne"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="hardware_factory_spritelayout_shed_3_half",
    tile="hardware_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_3_half],
    fences=["nw", "ne"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="hardware_factory_spritelayout_shed_4_half_with_chimneys",
    tile="hardware_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_4_half_with_chimneys],
    fences=["nw", "ne"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="hardware_factory_spritelayout_shed_tall",
    tile="hardware_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_tall],
    fences=["ne"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="hardware_factory_spritelayout_small_building",
    tile="hardware_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_small_building],
    fences=["nw", "ne", "sw"],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="hardware_factory_spritelayout_greeble_1",
    tile="hardware_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_greeble_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="hardware_factory_spritelayout_greeble_2",
    tile="hardware_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_greeble_2],
    fences=["nw", "ne"],
    add_to_object_num=8,
)

# this industry needs outpost layout as there are lots of cargos
industry.add_industry_outpost_layout(
    id="hardware_factory_industry_outpost_layout_1",
    layout=[
        # test outpost layout
        (0, 0, "hardware_factory_spritelayout_shed_4_half_with_chimneys"),
        (0, 1, "hardware_factory_spritelayout_shed_1_with_chimneys"),
        (0, 2, "hardware_factory_spritelayout_small_building"),
        (1, 0, "hardware_factory_spritelayout_shed_3_half"),
        (1, 1, "hardware_factory_spritelayout_shed_tall"),
        (1, 2, "hardware_factory_spritelayout_greeble_1"),
    ],
)
industry.add_industry_outpost_layout(
    id="hardware_factory_industry_outpost_layout_2",
    layout=[
        # test outpost layout
        (0, 0, "hardware_factory_spritelayout_shed_4_half_with_chimneys"),
        (0, 1, "hardware_factory_spritelayout_shed_1_with_chimneys"),
        (1, 0, "hardware_factory_spritelayout_shed_3_half"),
        (1, 1, "hardware_factory_spritelayout_shed_tall"),
        (2, 0, "hardware_factory_spritelayout_greeble_1"),
        (2, 1, "hardware_factory_spritelayout_small_building"),
    ],
)

industry.add_industry_layout(
    id="hardware_factory_industry_layout_1",
    layout=[
        (0, 0, "hardware_factory_spritelayout_shed_4_half_with_chimneys"),
        (0, 1, "hardware_factory_spritelayout_shed_1_with_chimneys"),
        (0, 2, "hardware_factory_spritelayout_shed_1_with_chimneys"),
        (0, 3, "hardware_factory_spritelayout_shed_tall"),
        (0, 4, "hardware_factory_spritelayout_shed_4_half_with_chimneys"),
        (0, 5, "hardware_factory_spritelayout_shed_1_with_chimneys"),
        (1, 0, "hardware_factory_spritelayout_shed_3_half"),
        (1, 1, "hardware_factory_spritelayout_shed_1_with_chimneys"),
        (1, 2, "hardware_factory_spritelayout_greeble_1"),
        (1, 3, "hardware_factory_spritelayout_greeble_1"),
        (1, 4, "hardware_factory_spritelayout_shed_3_half"),
        (1, 5, "hardware_factory_spritelayout_shed_tall"),
        (2, 0, "hardware_factory_spritelayout_shed_3_half"),
        (2, 1, "hardware_factory_spritelayout_shed_1_with_chimneys"),
        (2, 2, "hardware_factory_spritelayout_shed_tall"),
        (2, 3, "hardware_factory_spritelayout_greeble_2"),
        (2, 4, "hardware_factory_spritelayout_greeble_1"),
        (2, 5, "hardware_factory_spritelayout_small_building"),
    ],
)
industry.add_industry_layout(
    id="hardware_factory_industry_layout_2",
    layout=[
        (0, 0, "hardware_factory_spritelayout_shed_4_half_with_chimneys"),
        (0, 1, "hardware_factory_spritelayout_shed_1_with_chimneys"),
        (0, 2, "hardware_factory_spritelayout_shed_1_with_chimneys"),
        (1, 0, "hardware_factory_spritelayout_shed_3_half"),
        (1, 1, "hardware_factory_spritelayout_shed_1_with_chimneys"),
        (1, 2, "hardware_factory_spritelayout_shed_tall"),
        (2, 0, "hardware_factory_spritelayout_greeble_2"),
        (2, 1, "hardware_factory_spritelayout_greeble_1"),
        (2, 2, "hardware_factory_spritelayout_small_building"),
        (3, 0, "hardware_factory_spritelayout_shed_4_half_with_chimneys"),
        (3, 1, "hardware_factory_spritelayout_shed_1_with_chimneys"),
        (3, 2, "hardware_factory_spritelayout_greeble_1"),
        (4, 0, "hardware_factory_spritelayout_shed_3_half"),
        (4, 1, "hardware_factory_spritelayout_shed_1_with_chimneys"),
        (4, 2, "hardware_factory_spritelayout_shed_tall"),
    ],
)
