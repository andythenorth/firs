from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="smithy_forge",
    accept_cargos_with_input_ratios=[
        ("STEL", 8),
    ],
    prod_cargo_types_with_output_ratios=[
        ("ENSP", 4),
        ("FMSP", 4),
    ],
    prob_in_game="2",
    prob_map_gen="5",
    map_colour="143",
    special_flags=["IND_FLAG_ONLY_IN_TOWNS"],
    name="string(STR_IND_SMITHY_FORGE)",
    nearby_station_name="string(STR_STATION_FORGE)",
    fund_cost_multiplier="63",
    expiry_year=1948,
    provides_snow=True,
)


industry.add_tile(
    id="smithy_forge_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

sprite_ground = industry.add_sprite(
    sprite_number="GROUNDTILE_MUD_TRACKS",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 80, -31, -49)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 80, -31, -49)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=0,
    yoffset=1,
    zoffset=44,
)

industry.add_spritelayout(
    id="smithy_forge_spritelayout_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke],
    fences=["se", "sw"],
)
industry.add_spritelayout(
    id="smithy_forge_spritelayout_2",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["se", "sw"],
)
industry.add_industry_layout(
    id="smithy_forge_industry_layout",
    layout=[
        (0, 0, "smithy_forge_tile_1", "smithy_forge_spritelayout_2"),
        (1, 0, "smithy_forge_tile_1", "smithy_forge_spritelayout_1"),
    ],
)
