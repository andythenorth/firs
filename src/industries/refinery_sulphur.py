from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="refinery_sulphur",
    accept_cargos_with_input_ratios=[
        ("SULP", 40),
    ],
    prod_cargo_types_with_output_ratios=[
        ("HEPW", 8),
    ],
    life_type = "IND_LIFE_TYPE_BLACK_HOLE"
    prob_in_game="0",  # do not build during gameplay
    prob_map_gen="3",
    map_colour="10",
    colour_scheme_name="scheme_1_elton", # cabbage needs checked
    name="string(STR_IND_REF_COMP)",
    nearby_station_name="string(STR_STATION_FURNACE)",
    fund_cost_multiplier="190",
    pollution_and_squalor_factor=2,
    sprites_complete=True,
    animated_tiles_fixed=True,
)

industry.enable_in_economy(
    "WAR_ECONOMY",
    locate_in_specific_biomes=[
        "exclude_map_edges",
    ],
)

industry.add_tile(
    id="cryo_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 106, -31, -73)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -32)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 84, -31, -52)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -32)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -32)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -32)],
)

industry.add_spritelayout(
    id="cryo_plant_spritelayout_separation_tower",
    tile="cryo_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="cryo_plant_spritelayout_large_shed",
    tile="cryo_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="cryo_plant_spritelayout_purification_unit",
    tile="cryo_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="cryo_plant_spritelayout_horizontal_tanks",
    tile="cryo_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="cryo_plant_spritelayout_storage_tank_blue",
    tile="cryo_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="cryo_plant_spritelayout_storage_tank_yellow",
    tile="cryo_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="cryo_plant_spritelayout_empty",
    tile="cryo_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    add_to_object_num=7,
)

industry.add_industry_layout(
    id="cryo_plant_industry_layout_1",
    layout=[
        (0, 0, "cryo_plant_spritelayout_large_shed"),
        (0, 1, "cryo_plant_spritelayout_horizontal_tanks"),
        (1, 0, "cryo_plant_spritelayout_purification_unit"),
        (1, 1, "cryo_plant_spritelayout_separation_tower"),
        (2, 0, "cryo_plant_spritelayout_horizontal_tanks"),
        (2, 1, "cryo_plant_spritelayout_empty"),
        (3, 0, "cryo_plant_spritelayout_storage_tank_blue"),
        (3, 1, "cryo_plant_spritelayout_storage_tank_yellow"),
    ],
)
industry.add_industry_layout(
    id="cryo_plant_industry_layout_2",
    layout=[
        (0, 0, "cryo_plant_spritelayout_storage_tank_blue"),
        (0, 1, "cryo_plant_spritelayout_storage_tank_yellow"),
        (1, 0, "cryo_plant_spritelayout_large_shed"),
        (1, 1, "cryo_plant_spritelayout_empty"),
        (2, 0, "cryo_plant_spritelayout_purification_unit"),
        (2, 1, "cryo_plant_spritelayout_separation_tower"),
        (3, 0, "cryo_plant_spritelayout_horizontal_tanks"),
        (3, 1, "cryo_plant_spritelayout_horizontal_tanks"),
    ],
)
industry.add_industry_layout(
    id="cryo_plant_industry_layout_3",
    layout=[
        (0, 0, "cryo_plant_spritelayout_large_shed"),
        (0, 1, "cryo_plant_spritelayout_horizontal_tanks"),
        (0, 2, "cryo_plant_spritelayout_horizontal_tanks"),
        (0, 3, "cryo_plant_spritelayout_storage_tank_yellow"),
        (1, 0, "cryo_plant_spritelayout_purification_unit"),
        (1, 1, "cryo_plant_spritelayout_separation_tower"),
        (1, 2, "cryo_plant_spritelayout_empty"),
        (1, 3, "cryo_plant_spritelayout_storage_tank_blue"),
    ],
)
industry.add_industry_layout(
    id="cryo_plant_industry_layout_4",
    layout=[
        (0, 0, "cryo_plant_spritelayout_storage_tank_yellow"),
        (0, 1, "cryo_plant_spritelayout_large_shed"),
        (0, 2, "cryo_plant_spritelayout_purification_unit"),
        (0, 3, "cryo_plant_spritelayout_separation_tower"),
        (1, 0, "cryo_plant_spritelayout_storage_tank_blue"),
        (1, 1, "cryo_plant_spritelayout_empty"),
        (1, 2, "cryo_plant_spritelayout_horizontal_tanks"),
        (1, 3, "cryo_plant_spritelayout_horizontal_tanks"),
    ],
)
industry.add_industry_layout(
    id="cryo_plant_industry_layout_5",
    layout=[
        (0, 0, "cryo_plant_spritelayout_large_shed"),
        (0, 1, "cryo_plant_spritelayout_empty"),
        (0, 2, "cryo_plant_spritelayout_storage_tank_yellow"),
        (1, 0, "cryo_plant_spritelayout_purification_unit"),
        (1, 1, "cryo_plant_spritelayout_separation_tower"),
        (1, 2, "cryo_plant_spritelayout_storage_tank_blue"),
        (2, 0, "cryo_plant_spritelayout_horizontal_tanks"),
        (2, 1, "cryo_plant_spritelayout_horizontal_tanks"),
    ],
)
