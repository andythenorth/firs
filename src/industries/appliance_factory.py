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
        ("SEAL", 3),
    ],
    prod_cargo_types_with_output_ratios=[
        ("GOOD", 3),
        ("PLNT", 2),
        ("ENSP", 2),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="194",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    name="string(STR_IND_APPLIANCE_FACTORY)",
    nearby_station_name="string(STR_STATION_APPLIANCE_FACTORY)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="appliance_factory_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="appliance_factory_tile_2",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="asphalt")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
# spriteset_1 deprecated
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
    sprites=[(10, 84, 64, 120, -31, -89)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(80, 84, 64, 120, -31, -89)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(150, 84, 64, 120, -31, -89)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(220, 84, 64, 120, -31, -89)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=10,
    yoffset=0,
    zoffset=93,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=6,
    yoffset=0,
    zoffset=79,
    animation_frame_offset=1,
)

industry.add_spritelayout(
    id="appliance_factory_spritelayout_paper_store_empty",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_paper_store_full",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_wood_store_forklift",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_wood_store_full",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_chemical_tanks",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_tall_building_1",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_tall_building_2",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_pulp_processor",
    tile="appliance_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="appliance_factory_spritelayout_boilerhouse",
    tile="appliance_factory_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
    add_to_object_num=3,
)

industry.add_industry_layout(
    id="appliance_factory_industry_layout_1",
    layout=[
        (0, 0, "appliance_factory_spritelayout_tall_building_1"),
        (0, 1, "appliance_factory_spritelayout_tall_building_1"),
        (0, 2, "appliance_factory_spritelayout_paper_store_full"),
        (1, 0, "appliance_factory_spritelayout_tall_building_2"),
        (1, 1, "appliance_factory_spritelayout_tall_building_2"),
        (1, 2, "appliance_factory_spritelayout_paper_store_empty"),
        (2, 0, "appliance_factory_spritelayout_tall_building_1"),
        (2, 1, "appliance_factory_spritelayout_tall_building_1"),
        (2, 2, "appliance_factory_spritelayout_paper_store_full"),
        (3, 0, "appliance_factory_spritelayout_tall_building_2"),
        (3, 1, "appliance_factory_spritelayout_tall_building_2"),
        (3, 2, "appliance_factory_spritelayout_wood_store_full"),
        (4, 0, "appliance_factory_spritelayout_boilerhouse"),
        (4, 1, "appliance_factory_spritelayout_boilerhouse"),
        (4, 2, "appliance_factory_spritelayout_wood_store_forklift"),
    ],
)
