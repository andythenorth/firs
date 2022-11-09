from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(
    id="inland_grain_terminal",
    prod_cargo_types_with_multipliers=[("GRAI", 16)],
    prob_in_game="3",
    prob_map_gen="6",
    map_colour="69",
    
    # basic inland_grain_terminal doesn't cluster, by design - no industry location checks needed
    prospect_chance="0.75",
    name="string(STR_IND_INLAND_GRAIN_TERMINAL)",
    extra_text_fund="string(STR_FUND_TERMINAL)",
    nearby_station_name="string(STR_STATION_TERMINAL)",
    fund_cost_multiplier="40",
)

industry.enable_in_economy(
    "PLAINS_TRAINS_AND_STEEL",
    intro_year=1930,
    fund_cost_multiplier="2",
)

industry.add_tile(
    id="inland_grain_terminal_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True,
        disallow_above_snowline=True,
        disallow_desert=True,
        disallow_coast=True,
        disallow_industry_adjacent=True,
    ),
)

spriteset_ground = industry.add_spriteset(type="concrete")
spriteset_ground_overlay = industry.add_spriteset(type="empty")

spriteset_1 = industry.add_spriteset(sprites=[(10, 10, 64, 114, -31, -85)])
spriteset_2 = industry.add_spriteset(sprites=[(80, 10, 64, 114, -31, -85)])
spriteset_3 = industry.add_spriteset(sprites=[(150, 10, 64, 114, -31, -85)])
spriteset_4 = industry.add_spriteset(sprites=[(220, 10, 64, 114, -31, -85)])
spriteset_5 = industry.add_spriteset(sprites=[(290, 10, 64, 114, -31, -85)])
spriteset_6 = industry.add_spriteset(sprites=[(360, 10, 64, 114, -31, -85)])

industry.add_spritelayout(
    id="inland_grain_terminal_spritelayout_1",
    tile="inland_grain_terminal_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)

industry.add_spritelayout(
    id="inland_grain_terminal_spritelayout_2",
    tile="inland_grain_terminal_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)

industry.add_spritelayout(
    id="inland_grain_terminal_spritelayout_3",
    tile="inland_grain_terminal_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)

industry.add_spritelayout(
    id="inland_grain_terminal_spritelayout_4",
    tile="inland_grain_terminal_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)

industry.add_spritelayout(
    id="inland_grain_terminal_spritelayout_5",
    tile="inland_grain_terminal_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
)

industry.add_spritelayout(
    id="inland_grain_terminal_spritelayout_6",
    tile="inland_grain_terminal_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
)

industry.add_industry_layout(
    id="inland_grain_terminal_industry_layout_1",
    layout=[
        (0, 0, "inland_grain_terminal_spritelayout_3"),
        (1, 0, "inland_grain_terminal_spritelayout_2"),
        (2, 0, "inland_grain_terminal_spritelayout_1"),
        (0, 1, "inland_grain_terminal_spritelayout_6"),
        (1, 1, "inland_grain_terminal_spritelayout_5"),
        (2, 1, "inland_grain_terminal_spritelayout_4"),

    ],
)

