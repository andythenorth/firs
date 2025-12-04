from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="refinery_components",
    accept_cargos_with_input_ratios=[
        ("COMP", 160),
    ],
    prod_cargo_types_with_output_ratios=[
        ("RMAT", 8),
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
    id="carbon_black_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="carbon_black_plant_tile_2",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
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
spriteset_boiler = industry.add_spriteset(
    sprites=[(10, 10, 64, 114, -31, -83)],
)
spriteset_chimneys = industry.add_spriteset(
    sprites=[(80, 10, 64, 114, -31, -83)],
)
spriteset_tanks_group = industry.add_spriteset(
    sprites=[(150, 10, 64, 114, -31, -83)],
)
spriteset_silos = industry.add_spriteset(
    sprites=[(220, 10, 64, 114, -31, -83)],
)
spriteset_silos_with_office = industry.add_spriteset(
    sprites=[(290, 10, 64, 114, -31, -83)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=9,
    yoffset=0,
    zoffset=87,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=2,
    yoffset=6,
    zoffset=71,
)
sprite_smoke_3 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=5,
    yoffset=6,
    zoffset=71,
)

industry.add_spritelayout(
    id="carbon_black_plant_spritelayout_empty",
    tile="carbon_black_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="carbon_black_plant_spritelayout_boiler",
    tile="carbon_black_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_boiler],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="carbon_black_plant_spritelayout_chimneys",
    tile="carbon_black_plant_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_chimneys],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2, sprite_smoke_3],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="carbon_black_plant_spritelayout_tanks_group",
    tile="carbon_black_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_tanks_group],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="carbon_black_plant_spritelayout_silos",
    tile="carbon_black_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_silos],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="carbon_black_plant_spritelayout_silos_with_office",
    tile="carbon_black_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_silos_with_office],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)

industry.add_industry_layout(
    id="carbon_black_plant_industry_layout_1",
    layout=[
        (0, 0, "carbon_black_plant_spritelayout_chimneys"),
        (0, 1, "carbon_black_plant_spritelayout_boiler"),
        (
            0,
            2,
            "carbon_black_plant_spritelayout_tanks_group",
        ),
        (1, 0, "carbon_black_plant_spritelayout_chimneys"),
        (1, 1, "carbon_black_plant_spritelayout_boiler"),
        (
            1,
            2,
            "carbon_black_plant_spritelayout_tanks_group",
        ),
        (
            2,
            0,
            "carbon_black_plant_spritelayout_silos_with_office",
        ),
        (2, 1, "carbon_black_plant_spritelayout_silos"),
        (2, 2, "carbon_black_plant_spritelayout_empty"),
    ],
)
industry.add_industry_layout(
    id="carbon_black_plant_industry_layout_2",
    layout=[
        (0, 0, "carbon_black_plant_spritelayout_boiler"),
        (
            0,
            1,
            "carbon_black_plant_spritelayout_tanks_group",
        ),
        (1, 0, "carbon_black_plant_spritelayout_boiler"),
        (
            1,
            1,
            "carbon_black_plant_spritelayout_tanks_group",
        ),
        (2, 0, "carbon_black_plant_spritelayout_chimneys"),
        (2, 1, "carbon_black_plant_spritelayout_silos"),
        (
            3,
            0,
            "carbon_black_plant_spritelayout_silos_with_office",
        ),
        (3, 1, "carbon_black_plant_spritelayout_empty"),
    ],
)
industry.add_industry_layout(
    id="carbon_black_plant_industry_layout_3",
    layout=[
        (0, 0, "carbon_black_plant_spritelayout_boiler"),
        (
            0,
            1,
            "carbon_black_plant_spritelayout_tanks_group",
        ),
        (0, 2, "carbon_black_plant_spritelayout_chimneys"),
        (0, 3, "carbon_black_plant_spritelayout_silos"),
        (1, 0, "carbon_black_plant_spritelayout_boiler"),
        (
            1,
            1,
            "carbon_black_plant_spritelayout_tanks_group",
        ),
        (
            1,
            2,
            "carbon_black_plant_spritelayout_silos_with_office",
        ),
        (1, 3, "carbon_black_plant_spritelayout_empty"),
    ],
)
