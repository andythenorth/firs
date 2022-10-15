from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="civil_explosives_facility",
    accept_cargos_with_input_ratios=[("NHNO", 6), ("PETR", 2)],
    prod_cargo_types_with_output_ratios=[("BOOM", 8)],
    combined_cargos_boost_prod=True,
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="191",
    location_checks=dict(same_type_distance=128),
    name="string(STR_IND_CIVIL_EXPLOSIVES_FACILITY)",
    nearby_station_name="string(STR_STATION_HEAVY_INDUSTRY_2)",
    fund_cost_multiplier="170",
)

industry.economy_variations['BETTER_LIVING_THROUGH_CHEMISTRY'].enabled = True

industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations["STEELTOWN"].accept_cargos_with_input_ratios = [
    ("NH3_", 4),
    ("ACID", 2),
    ("PLAS", 1),
    ("PETR", 1),
]
industry.economy_variations["STEELTOWN"].prod_cargo_types_with_output_ratios = [
    ("NHNO", 6),
    ("ENSP", 2),
]

industry.add_tile(
    id="civil_explosives_facility_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="dirty_concrete")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
# spriteset_1 deprecated
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -33)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -33)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -33)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -33)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -33)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(10, 84, 64, 120, -31, -89)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(80, 84, 64, 120, -31, -89)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(150, 84, 64, 120, -31, -89)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(220, 84, 64, 120, -31, -89)],
)
"""
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=10,
    yoffset=0,
    zoffset=93,
)
"""
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=-1,
    yoffset=0,
    zoffset=73,
)

industry.add_spritelayout(
    id="civil_explosives_facility_spritelayout_paper_store_empty",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id="civil_explosives_facility_spritelayout_paper_store_full",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="civil_explosives_facility_spritelayout_wood_store_forklift",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id="civil_explosives_facility_spritelayout_wood_store_full",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
)
industry.add_spritelayout(
    id="civil_explosives_facility_spritelayout_chemical_tanks",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
)
industry.add_spritelayout(
    id="civil_explosives_facility_spritelayout_tall_building_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
)
industry.add_spritelayout(
    id="civil_explosives_facility_spritelayout_tall_building_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
)
industry.add_spritelayout(
    id="civil_explosives_facility_spritelayout_pulp_processor",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    smoke_sprites=[sprite_smoke_1],
)
industry.add_spritelayout(
    id="civil_explosives_facility_spritelayout_boilerhouse",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
)

industry.add_industry_layout(
    id="civil_explosives_facility_industry_layout_1",
    layout=[
        (0, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_1"),
        (0, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_1"),
        (0, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_paper_store_full"),
        (1, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_2"),
        (1, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_pulp_processor"),
        (1, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_paper_store_empty"),
        (2, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_1"),
        (2, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_chemical_tanks"),
        (2, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_paper_store_full"),
        (3, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_2"),
        (3, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_forklift"),
        (3, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_full"),
        (4, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_boilerhouse"),
        (4, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_full"),
        (4, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_forklift"),
    ],
)
industry.add_industry_layout(
    id="civil_explosives_facility_industry_layout_2",
    layout=[
        (0, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_1"),
        (0, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_1"),
        (0, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_chemical_tanks"),
        (1, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_2"),
        (1, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_2"),
        (1, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_paper_store_empty"),
        (2, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_boilerhouse"),
        (2, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_pulp_processor"),
        (2, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_paper_store_full"),
        (3, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_forklift"),
        (3, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_full"),
        (3, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_full"),
    ],
)
industry.add_industry_layout(
    id="civil_explosives_facility_industry_layout_3",
    layout=[
        (0, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_1"),
        (0, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_1"),
        (0, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_pulp_processor"),
        (0, 3, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_chemical_tanks"),
        (1, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_2"),
        (1, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_2"),
        (1, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_boilerhouse"),
        (1, 3, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_forklift"),
        (2, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_paper_store_full"),
        (2, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_paper_store_empty"),
        (2, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_forklift"),
        (2, 3, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_full"),
    ],
)
industry.add_industry_layout(
    id="civil_explosives_facility_industry_layout_4",
    layout=[
        (0, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_1"),
        (0, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_1"),
        (0, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_2"),
        (0, 3, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_forklift"),
        (1, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_2"),
        (1, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_tall_building_2"),
        (1, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_boilerhouse"),
        (1, 3, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_full"),
        (2, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_pulp_processor"),
        (2, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_paper_store_full"),
        (2, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_forklift"),
        (2, 3, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_wood_store_full"),
        (3, 0, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_chemical_tanks"),
        (3, 1, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_paper_store_empty"),
        (3, 2, "civil_explosives_facility_tile_1", "civil_explosives_facility_spritelayout_paper_store_full"),
    ],
)