from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="oil_wells",
    prod_cargo_types_with_multipliers=[
        ("OIL_", 28),
    ],
    prob_in_game="6",
    prob_map_gen="8",
    map_colour="151",
    prospect_chance="0.75",
    name="TTD_STR_INDUSTRY_NAME_OIL_WELLS",
    fund_cost_multiplier="230",
    nearby_station_name="string(STR_STATION_WELLS)",
    pollution_and_squalor_factor=1,
    provides_snow=True,
)

industry.enable_in_economy(
    "BASIC_TROPIC",
)
industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
)

industry.add_tile(
    id="oil_wells_tile_1",
    location_checks=TileLocationChecks(disallow_industry_adjacent=True),
    animation_length=20,
    animation_looping=True,
    animation_speed=3,
    special_flags=["INDTILE_FLAG_RANDOM_ANIMATION"],
    random_trigger="oil_wells_tile_1_industry_anim_control",
    custom_animation_next_frame="oil_wells_tile_1_anim_next_frame",
    custom_animation_control={
        "macro": "oil_wells",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_TILE_LOOP)",
    },
)
"""
item(FEAT_INDUSTRYTILES, oil_wells_tile_1, ${global_constants.tile_numeric_ids['oil_wells_tile_1']}) {
	property {
		special_flags:      bitmask(INDTILE_FLAG_RANDOM_ANIMATION);
	}
	graphics {
		anim_control:       ${industry.id}_tile_oil_well_random_trigger;
		random_trigger:     ${industry.id}_tile_oil_well_random_trigger;
		${industry.id}_tile_fences;
	}
}

"""
industry.add_tile(
    id="oil_wells_tile_2",
    location_checks=TileLocationChecks(disallow_industry_adjacent=True),
)

spriteset_ground_pump = industry.add_spriteset(
    type="empty",
)
sprite_ground_overlay_pump = industry.add_sprite(sprite_number=2173)
sprite_pump = industry.add_sprite(
    sprite_number="2174 + (((animation_frame % 11) < 6) ? (animation_frame % 11) : 10 - (animation_frame % 11))",
    xoffset=1,
    yoffset=2,
    xextent=15,
    yextent=14,
)
spriteset_ground_building = industry.add_spriteset(
    type="empty",
)
sprite_ground_overlay_building = industry.add_sprite(
    sprite_number="GROUNDTILE_MUD_TRACKS",
)
spriteset_building = industry.add_spriteset(
    sprites=[(10, 10, 64, 38, -31, -9)], xoffset=1, yoffset=2, xextent=15, yextent=14
)

industry.add_spritelayout(
    id="oil_wells_spritelayout_pump",
    tile="oil_wells_tile_1",
    ground_sprite=spriteset_ground_pump,
    ground_overlay=sprite_ground_overlay_pump,
    building_sprites=[sprite_pump],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="oil_wells_spritelayout_building",
    tile="oil_wells_tile_2",
    ground_sprite=spriteset_ground_building,
    ground_overlay=sprite_ground_overlay_building,
    building_sprites=[spriteset_building],
    fences=["nw", "ne", "se", "sw"],
)


industry.add_industry_layout(
    id="oil_wells_industry_layout_1",
    layout=[
        (0, 0, "oil_wells_spritelayout_pump"),
        (0, 7, "oil_wells_spritelayout_pump"),
        (1, 4, "oil_wells_spritelayout_pump"),
        (2, 1, "oil_wells_spritelayout_pump"),
        (3, 5, "oil_wells_spritelayout_building"),
        (4, 8, "oil_wells_spritelayout_pump"),
        (5, 1, "oil_wells_spritelayout_pump"),
        (5, 4, "oil_wells_spritelayout_pump"),
    ],
)
industry.add_industry_layout(
    id="oil_wells_industry_layout_2",
    layout=[
        (0, 0, "oil_wells_spritelayout_pump"),
        (0, 4, "oil_wells_spritelayout_pump"),
        (1, 4, "oil_wells_spritelayout_pump"),
        (2, 8, "oil_wells_spritelayout_pump"),
        (4, 4, "oil_wells_spritelayout_building"),
        (4, 8, "oil_wells_spritelayout_pump"),
        (5, 2, "oil_wells_spritelayout_pump"),
        (6, 2, "oil_wells_spritelayout_pump"),
        (6, 4, "oil_wells_spritelayout_pump"),
    ],
)
industry.add_industry_layout(
    id="oil_wells_industry_layout_3",
    layout=[
        (0, 0, "oil_wells_spritelayout_pump"),
        (0, 2, "oil_wells_spritelayout_pump"),
        (1, 4, "oil_wells_spritelayout_pump"),
        (1, 6, "oil_wells_spritelayout_pump"),
        (2, 0, "oil_wells_spritelayout_building"),
        (3, 2, "oil_wells_spritelayout_pump"),
        (3, 4, "oil_wells_spritelayout_pump"),
    ],
)
industry.add_industry_layout(
    id="oil_wells_industry_layout_4",
    layout=[
        (0, 0, "oil_wells_spritelayout_pump"),
        (0, 4, "oil_wells_spritelayout_pump"),
        (0, 6, "oil_wells_spritelayout_pump"),
        (1, 2, "oil_wells_spritelayout_pump"),
        (1, 8, "oil_wells_spritelayout_building"),
        (2, 0, "oil_wells_spritelayout_pump"),
        (2, 2, "oil_wells_spritelayout_pump"),
        (3, 1, "oil_wells_spritelayout_pump"),
        (5, 0, "oil_wells_spritelayout_pump"),
        (5, 2, "oil_wells_spritelayout_pump"),
        (6, 0, "oil_wells_spritelayout_pump"),
    ],
)
