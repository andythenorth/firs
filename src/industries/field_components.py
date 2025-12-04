from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="field_components",
    prod_cargo_types_with_multipliers=[("COMP", 20)],
    accept_cargo_types = "AVEH"
    life_type = "IND_LIFE_TYPE_BLACK_HOLE"
    prob_in_game="0",
    prob_map_gen="7",
    map_colour="177",
    colour_scheme_name="scheme_1_elton",
    location_checks=dict(require_cluster=[70, 3]),
    prospect_chance="0.0",
    name="string(STR_IND_FIELD_COMPONENTS)",
    nearby_station_name="string(STR_STATION_COLLIERY)",
    fund_cost_multiplier="252",
    pollution_and_squalor_factor=1,
    provides_snow=True,
    primary_production_random_factor_set="wide_range",
    sprites_complete=True,
    animated_tiles_fixed=True,
)
industry.enable_in_economy(
    "WAR_ECONOMY",
    prob_map_gen="3",
)


industry.add_tile(
    id="scrap_yard_tile_1",
    location_checks=TileLocationChecks(
        disallow_steep_slopes=True,
        require_houses_nearby=True,
        disallow_industry_adjacent=True,
    ),
)

sprite_ground = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 55, -31, -24)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 55, -31, -24)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 55, -31, -24)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 55, -31, -24)],
    always_draw=True,
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 55, -31, -24)],
    always_draw=True,
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 55, -31, -24)],
    always_draw=True,
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 55, -31, -24)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 55, -31, -24)],
    always_draw=True,
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 55, -31, -24)],
)

industry.add_spritelayout(
    id="scrap_yard_spritelayout_1",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_2",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_3",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_4",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_5",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_6",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_6],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_7",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_7],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_8",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_8],
    add_to_object_num=8,
)
industry.add_spritelayout(
    id="scrap_yard_spritelayout_9",
    tile="scrap_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=None,
    building_sprites=[spriteset_9],
    add_to_object_num=9,
)

industry.add_industry_layout(
    id="scrap_yard_industry_layout_1",
    layout=[
        (0, 2, "scrap_yard_spritelayout_2"),
        (1, 1, "scrap_yard_spritelayout_2"),
        (1, 2, "scrap_yard_spritelayout_9"),
        (2, 1, "scrap_yard_spritelayout_1"),
        (2, 2, "scrap_yard_spritelayout_8"),
        (3, 1, "scrap_yard_spritelayout_4"),
        (3, 2, "scrap_yard_spritelayout_7"),
        (4, 0, "scrap_yard_spritelayout_5"),
        (4, 1, "scrap_yard_spritelayout_3"),
        (4, 2, "scrap_yard_spritelayout_6"),
    ],
)
industry.add_industry_layout(
    id="scrap_yard_industry_layout_2",
    layout=[
        (0, 1, "scrap_yard_spritelayout_7"),
        (1, 1, "scrap_yard_spritelayout_1"),
        (1, 2, "scrap_yard_spritelayout_8"),
        (2, 0, "scrap_yard_spritelayout_5"),
        (2, 1, "scrap_yard_spritelayout_3"),
        (2, 2, "scrap_yard_spritelayout_6"),
    ],
)
industry.add_industry_layout(
    id="scrap_yard_industry_layout_3",
    layout=[
        (0, 3, "scrap_yard_spritelayout_2"),
        (1, 1, "scrap_yard_spritelayout_2"),
        (1, 3, "scrap_yard_spritelayout_9"),
        (2, 1, "scrap_yard_spritelayout_1"),
        (2, 3, "scrap_yard_spritelayout_8"),
        (3, 1, "scrap_yard_spritelayout_4"),
        (3, 3, "scrap_yard_spritelayout_7"),
        (4, 0, "scrap_yard_spritelayout_5"),
        (4, 1, "scrap_yard_spritelayout_3"),
        (4, 3, "scrap_yard_spritelayout_6"),
    ],
)
