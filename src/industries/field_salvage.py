from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(
    id="field_salvage",
    prod_cargo_types_with_multipliers=[("SALV", 20)],
    accept_cargo_types = "AVEH"
    life_type = "IND_LIFE_TYPE_BLACK_HOLE"
    prob_in_game="0",
    prob_map_gen="7",
    map_colour="209",
    colour_scheme_name="scheme_1_elton",
    location_checks=dict(require_cluster=[70, 3]),
    prospect_chance="0.0",
    name="string(STR_IND_FIELD_SALVAGE)",
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
    prob_map_gen="10",
)

industry.add_tile(
    id="peatlands_tile_1",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    autoslope="return CB_RESULT_NO_AUTOSLOPE",
    location_checks=TileLocationChecks(
        disallow_slopes=True,
        disallow_desert=True,
        disallow_coast=True,
        disallow_industry_adjacent=True,
    ),
)

sprite_ground = industry.add_sprite(sprite_number="4126")
sprite_ground_tracks = industry.add_sprite(sprite_number="GROUNDTILE_MUD_TRACKS")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 64, -31, -31)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -31)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -31)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -31)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -31)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -31)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 64, -31, -31)],
)
industry.add_spritelayout(
    id="peatlands_spritelayout_bare_ground",
    tile="peatlands_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[],
)
industry.add_spritelayout(
    id="peatlands_spritelayout_tractor",
    tile="peatlands_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="peatlands_spritelayout_harvester",
    tile="peatlands_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id="peatlands_spritelayout_nissen_hut",
    tile="peatlands_tile_1",
    ground_sprite=sprite_ground_tracks,
    ground_overlay=sprite_ground_tracks,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id="peatlands_spritelayout_crane",
    tile="peatlands_tile_1",
    ground_sprite=sprite_ground_tracks,
    ground_overlay=sprite_ground_tracks,
    building_sprites=[spriteset_6, spriteset_5],
)
industry.add_spritelayout(
    id="peatlands_spritelayout_peat_pile",
    tile="peatlands_tile_1",
    ground_sprite=sprite_ground_tracks,
    ground_overlay=sprite_ground_tracks,
    building_sprites=[spriteset_7],
)

industry.add_industry_layout(
    id="peatlands_layout_1",
    layout=[
        (0, 0, "peatlands_spritelayout_nissen_hut"),
        (0, 1, "peatlands_spritelayout_peat_pile"),
        (0, 2, "peatlands_spritelayout_crane"),
        (1, 0, "peatlands_spritelayout_bare_ground"),
        (1, 1, "peatlands_spritelayout_bare_ground"),
        (1, 2, "peatlands_spritelayout_bare_ground"),
        (2, 0, "peatlands_spritelayout_tractor"),
        (2, 1, "peatlands_spritelayout_bare_ground"),
        (2, 2, "peatlands_spritelayout_harvester"),
        (3, 0, "peatlands_spritelayout_bare_ground"),
        (3, 1, "peatlands_spritelayout_harvester"),
        (3, 2, "peatlands_spritelayout_bare_ground"),
        (4, 0, "peatlands_spritelayout_bare_ground"),
        (4, 1, "peatlands_spritelayout_bare_ground"),
        (4, 2, "peatlands_spritelayout_bare_ground"),
    ],
)
industry.add_industry_layout(
    id="peatlands_layout_2",
    layout=[
        (0, 0, "peatlands_spritelayout_bare_ground"),
        (0, 1, "peatlands_spritelayout_harvester"),
        (0, 2, "peatlands_spritelayout_bare_ground"),
        (1, 0, "peatlands_spritelayout_bare_ground"),
        (1, 1, "peatlands_spritelayout_bare_ground"),
        (1, 2, "peatlands_spritelayout_bare_ground"),
        (2, 0, "peatlands_spritelayout_tractor"),
        (2, 1, "peatlands_spritelayout_bare_ground"),
        (2, 2, "peatlands_spritelayout_bare_ground"),
        (3, 0, "peatlands_spritelayout_bare_ground"),
        (3, 1, "peatlands_spritelayout_harvester"),
        (3, 2, "peatlands_spritelayout_bare_ground"),
        (4, 0, "peatlands_spritelayout_nissen_hut"),
        (4, 1, "peatlands_spritelayout_peat_pile"),
        (4, 2, "peatlands_spritelayout_crane"),
    ],
)
industry.add_industry_layout(
    id="peatlands_layout_3",
    layout=[
        (0, 0, "peatlands_spritelayout_bare_ground"),
        (0, 1, "peatlands_spritelayout_harvester"),
        (0, 2, "peatlands_spritelayout_bare_ground"),
        (0, 3, "peatlands_spritelayout_peat_pile"),
        (1, 0, "peatlands_spritelayout_bare_ground"),
        (1, 1, "peatlands_spritelayout_bare_ground"),
        (1, 2, "peatlands_spritelayout_bare_ground"),
        (1, 3, "peatlands_spritelayout_crane"),
        (2, 0, "peatlands_spritelayout_harvester"),
        (2, 1, "peatlands_spritelayout_bare_ground"),
        (2, 2, "peatlands_spritelayout_tractor"),
        (2, 3, "peatlands_spritelayout_nissen_hut"),
        (3, 0, "peatlands_spritelayout_bare_ground"),
        (3, 1, "peatlands_spritelayout_bare_ground"),
        (3, 2, "peatlands_spritelayout_bare_ground"),
        (3, 3, "peatlands_spritelayout_peat_pile"),
    ],
)
industry.add_industry_layout(
    id="peatlands_layout_4",
    layout=[
        (0, 0, "peatlands_spritelayout_peat_pile"),
        (0, 1, "peatlands_spritelayout_bare_ground"),
        (0, 2, "peatlands_spritelayout_harvester"),
        (0, 3, "peatlands_spritelayout_bare_ground"),
        (1, 0, "peatlands_spritelayout_nissen_hut"),
        (1, 1, "peatlands_spritelayout_harvester"),
        (1, 2, "peatlands_spritelayout_bare_ground"),
        (1, 3, "peatlands_spritelayout_bare_ground"),
        (2, 0, "peatlands_spritelayout_crane"),
        (2, 1, "peatlands_spritelayout_bare_ground"),
        (2, 2, "peatlands_spritelayout_bare_ground"),
        (2, 3, "peatlands_spritelayout_tractor"),
        (3, 0, "peatlands_spritelayout_peat_pile"),
        (3, 1, "peatlands_spritelayout_bare_ground"),
        (3, 2, "peatlands_spritelayout_bare_ground"),
        (3, 3, "peatlands_spritelayout_bare_ground"),
    ],
)
