from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="textile_mill",
    accept_cargos_with_input_ratios=[
        ("FICR", 6),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("TEXT", 8),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="37",
    name="string(STR_IND_TEXTILE_MILL)",
    nearby_station_name="string(STR_STATION_WEAVE_AND_DYE)",
    fund_cost_multiplier="120",
    provides_snow=True,
)


"""
industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
    accept_cargos_with_input_ratios=[("YARN", 6)],
    prod_cargo_types_with_output_ratios=[("TEXT", 8)],
)
"""
industry.add_tile(
    id="textile_mill_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="cobble")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_large_chimney = industry.add_spriteset(
    sprites=[(10, 60, 64, 103, -31, -74)],
)
spriteset_large_building_lh_part = industry.add_spriteset(
    sprites=[(80, 60, 64, 103, -31, -72)],
)
spriteset_large_building_rh_part = industry.add_spriteset(
    sprites=[(150, 60, 64, 103, -31, -72)],
)
spriteset_crates_greeble = industry.add_spriteset(
    sprites=[(220, 60, 64, 103, -31, -72)],
)
spriteset_small_warehouse = industry.add_spriteset(
    sprites=[(290, 60, 64, 103, -31, -72)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=0,
    yoffset=9,
    zoffset=78,
)

industry.add_spritelayout(
    id="textile_mill_spritelayout_1_anim",
    tile="textile_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_chimney],
    smoke_sprites=[sprite_smoke],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="textile_mill_spritelayout_2",
    tile="textile_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_building_lh_part],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="textile_mill_spritelayout_3",
    tile="textile_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_large_building_rh_part],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="textile_mill_spritelayout_4",
    tile="textile_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_crates_greeble],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="textile_mill_spritelayout_5",
    tile="textile_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_small_warehouse],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="textile_mill_spritelayout_6",
    tile="textile_mill_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="textile_mill_industry_layout_1",
    layout=[
        (0, 0, "textile_mill_spritelayout_3"),
        (0, 1, "textile_mill_spritelayout_1_anim"),
        (1, 0, "textile_mill_spritelayout_2"),
        (1, 1, "textile_mill_spritelayout_5"),
        (2, 0, "textile_mill_spritelayout_3"),
        (2, 1, "textile_mill_spritelayout_3"),
        (3, 0, "textile_mill_spritelayout_2"),
        (3, 1, "textile_mill_spritelayout_2"),
        (4, 0, "textile_mill_spritelayout_5"),
        (4, 1, "textile_mill_spritelayout_4"),
    ],
)
industry.add_industry_layout(
    id="textile_mill_industry_layout_2",
    layout=[
        (0, 0, "textile_mill_spritelayout_3"),
        (0, 1, "textile_mill_spritelayout_4"),
        (0, 2, "textile_mill_spritelayout_1_anim"),
        (1, 0, "textile_mill_spritelayout_2"),
        (1, 1, "textile_mill_spritelayout_6"),
        (1, 2, "textile_mill_spritelayout_5"),
        (2, 0, "textile_mill_spritelayout_5"),
        (2, 1, "textile_mill_spritelayout_6"),
    ],
)
industry.add_industry_layout(
    id="textile_mill_industry_layout_3",
    layout=[
        (0, 0, "textile_mill_spritelayout_3"),
        (0, 1, "textile_mill_spritelayout_5"),
        (1, 0, "textile_mill_spritelayout_2"),
        (1, 1, "textile_mill_spritelayout_4"),
        (2, 0, "textile_mill_spritelayout_1_anim"),
    ],
)
industry.add_industry_layout(
    id="textile_mill_industry_layout_4",
    layout=[
        (0, 0, "textile_mill_spritelayout_3"),
        (0, 1, "textile_mill_spritelayout_3"),
        (1, 0, "textile_mill_spritelayout_2"),
        (1, 1, "textile_mill_spritelayout_2"),
        (2, 0, "textile_mill_spritelayout_5"),
        (2, 1, "textile_mill_spritelayout_4"),
        (3, 0, "textile_mill_spritelayout_3"),
        (3, 1, "textile_mill_spritelayout_5"),
        (4, 0, "textile_mill_spritelayout_2"),
        (4, 1, "textile_mill_spritelayout_1_anim"),
    ],
)
industry.add_industry_layout(
    id="textile_mill_industry_layout_5",
    layout=[
        (0, 0, "textile_mill_spritelayout_3"),
        (0, 1, "textile_mill_spritelayout_3"),
        (0, 2, "textile_mill_spritelayout_5"),
        (0, 3, "textile_mill_spritelayout_5"),
        (1, 0, "textile_mill_spritelayout_2"),
        (1, 1, "textile_mill_spritelayout_2"),
        (1, 2, "textile_mill_spritelayout_4"),
        (1, 3, "textile_mill_spritelayout_1_anim"),
    ],
)
industry.add_industry_layout(
    id="textile_mill_industry_layout_6",
    layout=[
        (0, 0, "textile_mill_spritelayout_5"),
        (0, 1, "textile_mill_spritelayout_3"),
        (0, 2, "textile_mill_spritelayout_3"),
        (1, 0, "textile_mill_spritelayout_5"),
        (1, 1, "textile_mill_spritelayout_2"),
        (1, 2, "textile_mill_spritelayout_2"),
        (2, 0, "textile_mill_spritelayout_5"),
        (2, 1, "textile_mill_spritelayout_1_anim"),
        (2, 2, "textile_mill_spritelayout_4"),
    ],
)
