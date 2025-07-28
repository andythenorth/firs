from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="plate_mill",
    accept_cargos_with_input_ratios=[
        # this is a Quarto type plate mill + on-site processing for rolling, forming
        # water-jet descaling, no pickling, https://spartan.metinvestholding.com/en/activities/manufacturing
        # uses gas and burn bars for plate cutting / heat treatment, might be weird, but eh we'll see, it's more weird to remove it
        ("STSL", 6),
        ("WELD", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        # structural steel being a composite also covering rolled sections, but applied here to:
        # heavy plate, cut/treated plate, chequer plate, floor plate, and minor fab such as flanging parts or large beam fabrication
        ("STPL", 5),
        ("STSW", 3),
    ],
    # do not build during gameplay
    prob_in_game="0",
    prob_map_gen="5",
    map_colour="157",
    colour_scheme_name="scheme_12_mariah",
    name="string(STR_IND_PLATE_MILL)",
    nearby_station_name="string(STR_STATION_PLATE_MILL)",
    fund_cost_multiplier="200",
    pollution_and_squalor_factor=2,
    sprites_complete=True,
)

industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="plate_mill_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="gravel",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)
spriteset_shed_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 64, -31, -35)],
)
spriteset_shed_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -35)],
)
spriteset_shed_metal_1 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -35)],
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_shed_1",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_shed_2",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_metal_1",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_metal_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="plate_mill_spritelayout_empty",
    tile="plate_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=[],
    add_to_object_num=4,
)

# this industry needs outpost layout
industry.add_industry_outpost_layout(
    id="plate_mill_industry_outpost_layout_1",
    layout=[
        # test outpost layout
        (
            0,
            0,
            "plate_mill_spritelayout_shed_2",
        ),
        (
            0,
            1,
            "plate_mill_spritelayout_shed_2",
        ),
        (
            0,
            2,
            "plate_mill_spritelayout_metal_1",
        ),
        (
            1,
            0,
            "plate_mill_spritelayout_shed_1",
        ),
        (
            1,
            1,
            "plate_mill_spritelayout_metal_1",
        ),
        (
            1,
            2,
            "plate_mill_spritelayout_empty",
        ),
    ],
)

industry.add_industry_layout(
    id="plate_mill_industry_layout_1",
    layout=[
        (0, 0, "plate_mill_spritelayout_shed_2"),
        (0, 1, "plate_mill_spritelayout_shed_2"),
        (0, 2, "plate_mill_spritelayout_shed_2"),
        (0, 3, "plate_mill_spritelayout_shed_2"),
        (0, 4, "plate_mill_spritelayout_metal_1"),
        (1, 0, "plate_mill_spritelayout_shed_2"),
        (1, 1, "plate_mill_spritelayout_shed_2"),
        (1, 2, "plate_mill_spritelayout_shed_2"),
        (1, 3, "plate_mill_spritelayout_shed_2"),
        (1, 4, "plate_mill_spritelayout_empty"),
        (2, 0, "plate_mill_spritelayout_shed_1"),
        (2, 1, "plate_mill_spritelayout_shed_1"),
        (2, 2, "plate_mill_spritelayout_shed_1"),
        (2, 3, "plate_mill_spritelayout_empty"),
        (2, 4, "plate_mill_spritelayout_empty"),
        (3, 1, "plate_mill_spritelayout_shed_1"),
        (3, 2, "plate_mill_spritelayout_shed_1"),
        (3, 3, "plate_mill_spritelayout_empty"),
        (3, 4, "plate_mill_spritelayout_metal_1"),
    ],
)
