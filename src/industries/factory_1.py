from industry import IndustrySecondary, TileLocationChecks

# !! layout names will need set correctly
industry = IndustrySecondary(
    id="factory_1",
    accept_cargos_with_input_ratios=[("GLAS", 2), ("STEL", 2), ("PLAS", 2)],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("GOOD", 8)],
    prob_in_game="7",
    prob_map_gen="8",
    map_colour="166",
    name="string(STR_IND_APPLIANCE_FACTORY)",
    nearby_station_name="string(STR_STATION_INDUSTRY_ESTATE_1)",
    fund_cost_multiplier="95",
)

industry.economy_variations['BETTER_LIVING_THROUGH_CHEMISTRY'].enabled = True

industry.economy_variations['STEELTOWN'].enabled = True
industry.economy_variations["STEELTOWN"].accept_cargos_with_input_ratios = [
    ("STAL", 2),
    ("STSH", 2),  
    ("GLAS", 1),
    ("PPAR", 1),
    ("POWR", 1),
    ("TYRE", 1),
]



industry.add_tile(
    id="factory_1_tile_1",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 80, -31, -49)],
)

spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 80, -31, -49)],
)

spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 80, -31, -49)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 80, -31, -49)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 80, -31, -49)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 80, -31, -49)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 80, -31, -49)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 80, -31, -49)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 80, -31, -49)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(640, 10, 64, 80, -31, -49)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(710, 10, 64, 80, -31, -49)],
)
spriteset_12 = industry.add_spriteset(
    sprites=[(640, 100, 64, 80, -31, -49)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=13,
    yoffset=0,
    zoffset=73,
)

industry.add_spritelayout(
    id="factory_1_spritelayout_blank",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_central_assembly_hall",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_offices_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_front_assembly_hall",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_rear_assembly_hall",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_chimney",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_middle_assembly_hall",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_offices_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_tyres",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
)
industry.add_spritelayout(
    id="factory_1_spritelayout_metal",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
)

# min 6x4 or 5x5 as there are lots of output cargos
industry.add_industry_layout(
    id="factory_1_industry_layout_1",
    layout=[
        (
            0,
            0,
            "factory_1_tile_1",
            "factory_1_spritelayout_front_assembly_hall",
        ),
        (
            0,
            1,
            "factory_1_tile_1",
            "factory_1_spritelayout_front_assembly_hall",
        ),
        (
            0,
            2,
            "factory_1_tile_1",
            "factory_1_spritelayout_front_assembly_hall",
        ),
        (
            0,
            3,
            "factory_1_tile_1",
            "factory_1_spritelayout_front_assembly_hall",
        ),
        (
            1,
            0,
            "factory_1_tile_1",
            "factory_1_spritelayout_middle_assembly_hall",
        ),
        (
            1,
            1,
            "factory_1_tile_1",
            "factory_1_spritelayout_middle_assembly_hall",
        ),
        (
            1,
            2,
            "factory_1_tile_1",
            "factory_1_spritelayout_middle_assembly_hall",
        ),
        (
            1,
            3,
            "factory_1_tile_1",
            "factory_1_spritelayout_middle_assembly_hall",
        ),
        (
            2,
            0,
            "factory_1_tile_1",
            "factory_1_spritelayout_rear_assembly_hall",
        ),
        (
            2,
            1,
            "factory_1_tile_1",
            "factory_1_spritelayout_rear_assembly_hall",
        ),
        (
            2,
            2,
            "factory_1_tile_1",
            "factory_1_spritelayout_rear_assembly_hall",
        ),
        (
            2,
            3,
            "factory_1_tile_1",
            "factory_1_spritelayout_rear_assembly_hall",
        ),
        (3, 0, "factory_1_tile_1", "factory_1_spritelayout_offices_2"),
        (3, 1, "factory_1_tile_1", "factory_1_spritelayout_offices_2"),
        (3, 2, "factory_1_tile_1", "factory_1_spritelayout_offices_1"),
        (3, 3, "factory_1_tile_1", "factory_1_spritelayout_tyres"),
        (4, 0, "factory_1_tile_1", "factory_1_spritelayout_chimney"),
        (4, 1, "factory_1_tile_1", "factory_1_spritelayout_metal"),
        (4, 2, "factory_1_tile_1", "factory_1_spritelayout_tyres"),
        (4, 3, "factory_1_tile_1", "factory_1_spritelayout_metal"),
    ],
)
industry.add_industry_layout(
    id="factory_1_industry_layout_2",
    layout=[
        (
            0,
            0,
            "factory_1_tile_1",
            "factory_1_spritelayout_tyres",
        ),
        (
            0,
            1,
            "factory_1_tile_1",
            "factory_1_spritelayout_metal",
        ),
        (
            0,
            2,
            "factory_1_tile_1",
            "factory_1_spritelayout_middle_assembly_hall",
        ),
        (
            0,
            3,
            "factory_1_tile_1",
            "factory_1_spritelayout_middle_assembly_hall",
        ),
        (
            0,
            4,
            "factory_1_tile_1",
            "factory_1_spritelayout_metal",
        ),
        (
            1,
            0,
            "factory_1_tile_1",
            "factory_1_spritelayout_front_assembly_hall",
        ),
        (
            1,
            1,
            "factory_1_tile_1",
            "factory_1_spritelayout_front_assembly_hall",
        ),
        (
            1,
            2,
            "factory_1_tile_1",
            "factory_1_spritelayout_middle_assembly_hall",
        ),
        (
            1,
            3,
            "factory_1_tile_1",
            "factory_1_spritelayout_rear_assembly_hall",
        ),
        (
            1,
            4,
            "factory_1_tile_1",
            "factory_1_spritelayout_metal",
        ),
        (
            2,
            0,
            "factory_1_tile_1",
            "factory_1_spritelayout_middle_assembly_hall",
        ),
        (
            2,
            1,
            "factory_1_tile_1",
            "factory_1_spritelayout_middle_assembly_hall",
        ),
        (
            2,
            2,
            "factory_1_tile_1",
            "factory_1_spritelayout_rear_assembly_hall",
        ),
        (
            2,
            3,
            "factory_1_tile_1",
            "factory_1_spritelayout_offices_1",
        ),
        (
            2,
            4,
            "factory_1_tile_1",
            "factory_1_spritelayout_tyres",
        ),
        (3, 0, "factory_1_tile_1", "factory_1_spritelayout_rear_assembly_hall"),
        (3, 1, "factory_1_tile_1", "factory_1_spritelayout_rear_assembly_hall"),
        (3, 2, "factory_1_tile_1", "factory_1_spritelayout_chimney"),
        (3, 3, "factory_1_tile_1", "factory_1_spritelayout_offices_1"),
    ],
)

industry.add_industry_layout(
    id="factory_1_industry_layout_3",
    layout=[
        (
            0,
            0,
            "factory_1_tile_1",
            "factory_1_spritelayout_chimney",
        ),
        (
            0,
            1,
            "factory_1_tile_1",
            "factory_1_spritelayout_front_assembly_hall",
        ),
        (
            0,
            2,
            "factory_1_tile_1",
            "factory_1_spritelayout_front_assembly_hall",
        ),
        (
            0,
            3,
            "factory_1_tile_1",
            "factory_1_spritelayout_front_assembly_hall",
        ),
        (
            1,
            0,
            "factory_1_tile_1",
            "factory_1_spritelayout_metal",
        ),
        (
            1,
            1,
            "factory_1_tile_1",
            "factory_1_spritelayout_rear_assembly_hall",
        ),
        (
            1,
            2,
            "factory_1_tile_1",
            "factory_1_spritelayout_rear_assembly_hall",
        ),
        (
            1,
            3,
            "factory_1_tile_1",
            "factory_1_spritelayout_rear_assembly_hall",
        ),
        (
            2,
            0,
            "factory_1_tile_1",
            "factory_1_spritelayout_front_assembly_hall",
        ),
        (
            2,
            1,
            "factory_1_tile_1",
            "factory_1_spritelayout_front_assembly_hall",
        ),
        (
            2,
            2,
            "factory_1_tile_1",
            "factory_1_spritelayout_front_assembly_hall",
        ),
        (
            2,
            3,
            "factory_1_tile_1",
            "factory_1_spritelayout_metal",
        ),
        (3, 0, "factory_1_tile_1", "factory_1_spritelayout_offices_1"),
        (3, 1, "factory_1_tile_1", "factory_1_spritelayout_rear_assembly_hall"),
        (3, 2, "factory_1_tile_1", "factory_1_spritelayout_rear_assembly_hall"),
        (3, 3, "factory_1_tile_1", "factory_1_spritelayout_tyres"),
        (4, 0, "factory_1_tile_1", "factory_1_spritelayout_offices_1"),
        (4, 1, "factory_1_tile_1", "factory_1_spritelayout_metal"),
        (4, 2, "factory_1_tile_1", "factory_1_spritelayout_tyres"),
        (4, 3, "factory_1_tile_1", "factory_1_spritelayout_metal"),
    ],
)