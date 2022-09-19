from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="dredging_site",
    prod_cargo_types_with_multipliers=[
        ("SAND", 17),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="194",
    special_flags=["IND_FLAG_BUILT_ON_WATER, IND_FLAG_AI_CREATES_AIR_AND_SHIP_ROUTES"],
    location_checks=dict(location_check_industry_disallow_too_far_from_coast=True),
    prospect_chance="0.75",
    name="string(STR_IND_DREDGING_SITE)",
    nearby_station_name="string(STR_STATION_WATER)",
    fund_cost_multiplier="180",
)

industry.enable_in_economy(
    "BASIC_TEMPERATE",
)

industry.add_tile(
    id="dredging_site_tile_1",
    location_checks=TileLocationChecks(
        disallow_industry_adjacent=True, disallow_slopes=True
    ),
)

sprite_ground = industry.add_sprite(
    sprite_number="GROUNDSPRITE_WATER",
)

spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)

spriteset_platform = industry.add_spriteset(
    sprites=[(10, 10, 64, 100, -31, -67)],
)
spriteset_greeble = industry.add_spriteset(
    sprites=[(80, 10, 64, 39, -31, -12)],
)
spriteset_crane_animated = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -33, -37)],
)

industry.add_spritelayout(
    id="dredging_site_spritelayout_1",
    tile="dredging_site_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_platform,
    building_sprites=[spriteset_crane_animated, spriteset_greeble],
)

industry.add_industry_layout(
    id="dredging_site_industry_layout_1",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "spritelayout_null_station"),
        (0, 2, "spritelayout_null_station"),
        (0, 4, "spritelayout_null_water"),
        (1, 0, "spritelayout_null_water"),
        (1, 4, "spritelayout_null_water"),
        (2, 0, "spritelayout_null_water"),
        (2, 2, "spritelayout_null_water"),
        (2, 3, "dredging_site_spritelayout_1"),
        (2, 4, "spritelayout_null_water"),
    ],
)
