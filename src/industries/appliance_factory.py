from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="appliance_factory",
    accept_cargos_with_input_ratios=[
        # lots of inputs, but only 3 are required (see industry.py for the kludge to make that work)
        # all input ratios *must* be 3
        # note also that it's deliberately easy to get a partly-efficient supply of Goods from a Wharf by combining POWR and COAT
        ("STSH", 3),
        ("POWR", 3),
        ("PUMP", 3),
        ("COAT", 3),
        ("ELAS", 3),
    ],
    prod_cargo_types_with_output_ratios=[
        ("GOOD", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="194",
    name="string(STR_IND_APPLIANCE_FACTORY)",
    nearby_station_name="string(STR_STATION_APPLIANCE_FACTORY)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
    sprites_complete=False,
)

industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="appliance_factory_tile_1",
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
    id="appliance_factory_spritelayout_empty",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=[],
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_shed_1",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_1],
    fences=["nw", "ne"],
    # add_to_object_num=5,
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_shed_2",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed_2],
    fences=["ne"],
    # add_to_object_num=5,
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_office",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_office],
    fences=["nw", "ne", "se", "sw"],
    # add_to_object_num=5,
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_tanks",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_tanks],
    fences=["nw", "ne", "se", "sw"],
    # add_to_object_num=5,
)
industry.add_industry_layout(
    id="appliance_factory_industry_layout_1",
    layout=[
        (0, 0, "appliance_factory_spritelayout_shed_1"),
        (0, 1, "appliance_factory_spritelayout_shed_1"),
        (0, 2, "appliance_factory_spritelayout_shed_1"),
        (0, 3, "appliance_factory_spritelayout_shed_2"),
        (1, 0, "appliance_factory_spritelayout_shed_1"),
        (1, 1, "appliance_factory_spritelayout_shed_1"),
        (1, 2, "appliance_factory_spritelayout_empty"),
        (1, 3, "appliance_factory_spritelayout_office"),
        (2, 0, "appliance_factory_spritelayout_shed_1"),
        (2, 1, "appliance_factory_spritelayout_shed_1"),
        (2, 2, "appliance_factory_spritelayout_shed_2"),
        (2, 3, "appliance_factory_spritelayout_tanks"),
    ],
)
