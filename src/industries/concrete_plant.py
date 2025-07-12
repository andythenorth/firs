from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="concrete_plant",
    accept_cargos_with_input_ratios=[
        ("CMNT", 3),
        ("GRVL", 3),
        ("RBAR", 2),
    ],
    prod_cargo_types_with_output_ratios=[
        ("CCPR", 7),
        ("ENSP", 1),  # small ENSP output
    ],
    prob_in_game="6",
    prob_map_gen="9",
    prod_multiplier="[0, 0]",
    map_colour="10",
    colour_scheme_name="scheme_2_dylan",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    name="string(STR_IND_CONCRETE_PLANT)",
    nearby_station_name="string(STR_STATION_CONCRETE_PLANT)",
    fund_cost_multiplier="80",
    sprites_complete=True,  # done enough for v5
)


industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="concrete_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True,
        disallow_industry_adjacent=True,
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
shed_1_interior = industry.add_spriteset(
    sprites=[(10, 10, 64, 84, -31, -53)],
)
shed_1 = industry.add_spriteset(
    sprites=[(80, 10, 64, 84, -31, -53)],
)
overhead_crane_ground_blocks = industry.add_spriteset(
    sprites=[(150, 10, 64, 84, -31, -53)],
)
overhead_crane_rails_front = industry.add_spriteset(
    sprites=[(220, 10, 64, 84, -31, -53)],
)
overhead_crane_rails_rear = industry.add_spriteset(
    sprites=[(290, 10, 64, 84, -31, -53)],
)
silo_1 = industry.add_spriteset(
    sprites=[(360, 10, 64, 84, -31, -53)],
)
gatehouse_and_rebar = industry.add_spriteset(
    sprites=[(430, 10, 64, 84, -31, -53)],
)
blocks_1 = industry.add_spriteset(
    sprites=[(10, 100, 64, 56, -31, -26)],
)
blocks_2 = industry.add_spriteset(
    sprites=[(80, 100, 64, 56, -31, -26)],
)
pipes = industry.add_spriteset(
    sprites=[(150, 100, 64, 56, -31, -26)],
)
travelling_crane_rails_and_blocks = industry.add_spriteset(
    sprites=[(220, 100, 64, 56, -31, -26)],
)
travelling_crane_rear = industry.add_spriteset(
    sprites=[(290, 100, 64, 56, -31, -26)],
)
travelling_crane_front = industry.add_spriteset(
    sprites=[(360, 100, 64, 56, -31, -26)],
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_gatehouse_and_rebar",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[gatehouse_and_rebar],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_silo_1",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[silo_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_shed_1",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[shed_1_interior, shed_1],
    fences=[],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_overhead_crane_1",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[overhead_crane_ground_blocks, overhead_crane_rails_rear, overhead_crane_rails_front],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_pipes",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[pipes],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_blocks_1",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[blocks_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_blocks_2",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[blocks_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_travelling_crane_rails_and_blocks",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[travelling_crane_rails_and_blocks],
    add_to_object_num=8,
)
industry.add_spritelayout(
    id="concrete_plant_spritelayout_travelling_crane",
    tile="concrete_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[
        travelling_crane_rear,
        travelling_crane_rails_and_blocks,
        travelling_crane_front,
    ],
    add_to_object_num=9,
)

# this industry needs outpost layout as there are lots of cargos
industry.add_industry_outpost_layout(
    id="concrete_plant_industry_outpost_layout_1",
    layout=[
        (
            0,
            0,
            "concrete_plant_spritelayout_silo_1",
        ),
        (
            0,
            1,
            "concrete_plant_spritelayout_gatehouse_and_rebar",
        ),
        (
            1,
            0,
            "concrete_plant_spritelayout_shed_1",
        ),
        (
            1,
            1,
            "concrete_plant_spritelayout_pipes",
        ),
        (
            2,
            0,
            "concrete_plant_spritelayout_overhead_crane_1",
        ),
        (
            2,
            1,
            "concrete_plant_spritelayout_blocks_1",
        ),
    ],
)
industry.add_industry_outpost_layout(
    id="concrete_plant_industry_outpost_layout_2",
    layout=[
        (
            0,
            0,
            "concrete_plant_spritelayout_silo_1",
        ),
        (
            0,
            1,
            "concrete_plant_spritelayout_shed_1",
        ),
        (
            0,
            2,
            "concrete_plant_spritelayout_gatehouse_and_rebar",
        ),
        (
            1,
            0,
            "concrete_plant_spritelayout_pipes",
        ),
        (
            1,
            1,
            "concrete_plant_spritelayout_overhead_crane_1",
        ),
        (
            1,
            2,
            "concrete_plant_spritelayout_blocks_1",
        ),
    ],
)

# relatively large IRL, and these are probably regional, not town-local
industry.add_industry_layout(
    id="concrete_plant_industry_layout_1",
    layout=[
        (0, 0, "concrete_plant_spritelayout_silo_1"),
        (0, 1, "concrete_plant_spritelayout_pipes"),
        (0, 2, "concrete_plant_spritelayout_pipes"),
        (1, 0, "concrete_plant_spritelayout_shed_1"),
        (1, 1, "concrete_plant_spritelayout_shed_1"),
        (1, 2, "concrete_plant_spritelayout_travelling_crane_rails_and_blocks"),
        (2, 0, "concrete_plant_spritelayout_shed_1"),
        (2, 1, "concrete_plant_spritelayout_shed_1"),
        (2, 2, "concrete_plant_spritelayout_travelling_crane"),
        (3, 0, "concrete_plant_spritelayout_blocks_1"),
        (3, 1, "concrete_plant_spritelayout_overhead_crane_1"),
        (3, 2, "concrete_plant_spritelayout_travelling_crane_rails_and_blocks"),
        (4, 0, "concrete_plant_spritelayout_gatehouse_and_rebar"),
        (4, 1, "concrete_plant_spritelayout_blocks_1"),
        (4, 2, "concrete_plant_spritelayout_blocks_1"),
    ],
)
industry.add_industry_layout(
    id="concrete_plant_industry_layout_2",
    layout=[
        (0, 0, "concrete_plant_spritelayout_travelling_crane_rails_and_blocks"),
        (0, 1, "concrete_plant_spritelayout_silo_1"),
        (0, 2, "concrete_plant_spritelayout_shed_1"),
        (0, 3, "concrete_plant_spritelayout_shed_1"),
        (0, 4, "concrete_plant_spritelayout_gatehouse_and_rebar"),
        (1, 0, "concrete_plant_spritelayout_travelling_crane"),
        (1, 1, "concrete_plant_spritelayout_blocks_1"),
        (1, 2, "concrete_plant_spritelayout_shed_1"),
        (1, 3, "concrete_plant_spritelayout_shed_1"),
        (1, 4, "concrete_plant_spritelayout_pipes"),
        (2, 0, "concrete_plant_spritelayout_travelling_crane_rails_and_blocks"),
        (2, 1, "concrete_plant_spritelayout_blocks_1"),
        (2, 2, "concrete_plant_spritelayout_blocks_1"),
        (2, 3, "concrete_plant_spritelayout_overhead_crane_1"),
        (2, 4, "concrete_plant_spritelayout_pipes"),
    ],
)
industry.add_industry_layout(
    id="concrete_plant_industry_layout_3",
    layout=[
        (0, 0, "concrete_plant_spritelayout_pipes"),
        (0, 1, "concrete_plant_spritelayout_pipes"),
        (0, 2, "concrete_plant_spritelayout_gatehouse_and_rebar"),
        (1, 0, "concrete_plant_spritelayout_silo_1"),
        (1, 1, "concrete_plant_spritelayout_shed_1"),
        (1, 2, "concrete_plant_spritelayout_blocks_1"),
        (2, 0, "concrete_plant_spritelayout_shed_1"),
        (2, 1, "concrete_plant_spritelayout_shed_1"),
        (2, 2, "concrete_plant_spritelayout_travelling_crane_rails_and_blocks"),
        (3, 0, "concrete_plant_spritelayout_shed_1"),
        (3, 1, "concrete_plant_spritelayout_overhead_crane_1"),
        (3, 2, "concrete_plant_spritelayout_travelling_crane"),
        (4, 0, "concrete_plant_spritelayout_blocks_1"),
        (4, 1, "concrete_plant_spritelayout_travelling_crane_rails_and_blocks"),
        (4, 2, "concrete_plant_spritelayout_travelling_crane_rails_and_blocks"),
    ],
)
industry.add_industry_layout(
    id="concrete_plant_industry_layout_4",
    layout=[
        (0, 0, "concrete_plant_spritelayout_pipes"),
        (0, 1, "concrete_plant_spritelayout_silo_1"),
        (0, 2, "concrete_plant_spritelayout_blocks_1"),
        (0, 3, "concrete_plant_spritelayout_gatehouse_and_rebar"),
        (1, 0, "concrete_plant_spritelayout_shed_1"),
        (1, 1, "concrete_plant_spritelayout_shed_1"),
        (1, 2, "concrete_plant_spritelayout_travelling_crane_rails_and_blocks"),
        (1, 3, "concrete_plant_spritelayout_pipes"),
        (2, 0, "concrete_plant_spritelayout_shed_1"),
        (2, 1, "concrete_plant_spritelayout_shed_1"),
        (2, 2, "concrete_plant_spritelayout_travelling_crane"),
        (2, 3, "concrete_plant_spritelayout_pipes"),
        (3, 0, "concrete_plant_spritelayout_blocks_1"),
        (3, 1, "concrete_plant_spritelayout_overhead_crane_1"),
        (3, 2, "concrete_plant_spritelayout_travelling_crane_rails_and_blocks"),
        (3, 3, "concrete_plant_spritelayout_blocks_1"),
    ],
)
