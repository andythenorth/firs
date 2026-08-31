from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="grain_mill",
    accept_cargos_with_input_ratios=[
        ("GRAI", 6),
    ],
    prod_cargo_types_with_output_ratios=[
        ("FOOD", 8),
    ],
    prob_map_gen="10",
    prob_in_game="10",
    map_colour="49",
    colour_scheme_name="scheme_3_hendrix",
    name="string(STR_IND_GRAIN_MILL)",
    nearby_station_name="string(STR_STATION_MILL)",
    fund_cost_multiplier="50",
    provides_snow=True,
    sprites_complete=False,
    animated_tiles_fixed=False,
)

industry.enable_in_economy(
    "BASIC_TROPIC",
    accept_cargos_with_input_ratios = [
        ("GRAI", 6)
    ],
)
industry.enable_in_economy(
    "IN_A_HOT_COUNTRY",
    accept_cargos_with_input_ratios=[
        ("CASS", 6),
        ("MAIZ", 6),
    ],
)
industry.enable_in_economy(
    "MILD_MILD_WEST",
    accept_cargos_with_input_ratios=[
        ("GRAI", 6),
    ],
    prod_cargo_types_with_output_ratios=[
        ("BAKE", 8),
    ],
)

# !! CABBAGE remove the windill layout, then de-animate the tile

industry.add_tile(
    id="grain_mill_tile_1",
    animation_length=6,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True,
        require_houses_nearby=True,
    ),
)

spriteset_ground_bakery = industry.add_spriteset(
    type="asphalt",
)
spriteset_ground_overlay_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_ground_overlay_2 = industry.add_spriteset(sprites=[(80, 10, 64, 31, -31, 0)])
spriteset_ground_overlay_3 = industry.add_spriteset(sprites=[(150, 10, 64, 31, -31, 0)])
spriteset_ground_overlay_4 = industry.add_spriteset(sprites=[(220, 10, 64, 31, -31, 0)])
spriteset_1 = industry.add_spriteset(sprites=[(10, 10, 64, 31, -31, 0)])
spriteset_2 = industry.add_spriteset(sprites=[(80, 10, 64, 31, -31, 0)])
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 82, -31, -51)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 82, -31, -51)],
)

industry.add_spritelayout(
    id="grain_mill_spritelayout_brickbakery_1",
    tile="grain_mill_tile_1",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_1,
    building_sprites=[],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="grain_mill_spritelayout_brickbakery_2",
    tile="grain_mill_tile_1",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_2,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="grain_mill_spritelayout_brickbakery_3",
    tile="grain_mill_tile_1",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_3,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="grain_mill_spritelayout_brickbakery_4",
    tile="grain_mill_tile_1",
    ground_sprite=spriteset_ground_bakery,
    ground_overlay=spriteset_ground_overlay_4,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_industry_layout(
    id="grain_mill_industry_layout_1",
    layout=[
        (0, 0, "grain_mill_spritelayout_brickbakery_3"),
        (0, 1, "grain_mill_spritelayout_brickbakery_4"),
        (1, 0, "grain_mill_spritelayout_brickbakery_1"),
        (1, 1, "grain_mill_spritelayout_brickbakery_2"),
    ],
)
industry.add_industry_layout(
    id="grain_mill_industry_layout_2",
    layout=[
        (0, 0, "grain_mill_spritelayout_brickbakery_3"),
        (0, 1, "grain_mill_spritelayout_brickbakery_4"),
        (1, 0, "grain_mill_spritelayout_brickbakery_3"),
        (1, 1, "grain_mill_spritelayout_brickbakery_4"),
        (2, 0, "grain_mill_spritelayout_brickbakery_1"),
        (2, 1, "grain_mill_spritelayout_brickbakery_2"),
    ],
)
industry.add_industry_layout(
    id="grain_mill_industry_layout_3",
    layout=[
        (0, 0, "grain_mill_spritelayout_brickbakery_3"),
        (0, 1, "grain_mill_spritelayout_brickbakery_4"),
        (0, 2, "grain_mill_spritelayout_brickbakery_3"),
        (0, 3, "grain_mill_spritelayout_brickbakery_4"),
        (1, 0, "grain_mill_spritelayout_brickbakery_1"),
        (1, 1, "grain_mill_spritelayout_brickbakery_2"),
        (1, 2, "grain_mill_spritelayout_brickbakery_1"),
        (1, 3, "grain_mill_spritelayout_brickbakery_2"),
    ],
)
