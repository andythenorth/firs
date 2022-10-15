from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="solvay_plant",
    accept_cargos_with_input_ratios=[("SALT", 8)],
    prod_cargo_types_with_output_ratios=[("SASH", 6)],
    prob_in_game="3",
    prob_map_gen="5",
    prod_multiplier="[0, 0]",
    map_colour="191",
    name="string(STR_IND_SOLVAY_PLANT)",
    nearby_station_name="string(STR_STATION_BRINE_WORKS)",
    fund_cost_multiplier="170",
)

industry.economy_variations['BETTER_LIVING_THROUGH_CHEMISTRY'].enabled = True

industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations["STEELTOWN"].accept_cargos_with_input_ratios = [
    ("SALT", 4),
    ("LIME", 2),
    ("NH3_", 2),
]
industry.economy_variations["STEELTOWN"].prod_cargo_types_with_output_ratios = [
    ("SASH", 8),
]



industry.add_tile(
    id="solvay_plant_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)

spriteset_boiler = industry.add_spriteset(
    sprites=[(10, 10, 64, 114, -31, -83)],
)
spriteset_chimneys = industry.add_spriteset(
    sprites=[(80, 10, 64, 114, -31, -83)],
)
spriteset_tanks_group = industry.add_spriteset(
    sprites=[(150, 10, 64, 114, -31, -83)],
)
spriteset_silos = industry.add_spriteset(
    sprites=[(220, 10, 64, 114, -31, -83)],
)
spriteset_silos_with_office = industry.add_spriteset(
    sprites=[(290, 10, 64, 114, -31, -83)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=9,
    yoffset=0,
    zoffset=87,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=2,
    yoffset=6,
    zoffset=71,
)
sprite_smoke_3 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=5,
    yoffset=6,
    zoffset=71,
)

industry.add_spritelayout(
    id="solvay_plant_spritelayout_empty",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
)
industry.add_spritelayout(
    id="solvay_plant_spritelayout_boiler",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_boiler],
)
industry.add_spritelayout(
    id="solvay_plant_spritelayout_chimneys",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_chimneys],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2, sprite_smoke_3],
)
industry.add_spritelayout(
    id="solvay_plant_spritelayout_tanks_group",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_tanks_group],
)
industry.add_spritelayout(
    id="solvay_plant_spritelayout_silos",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_silos],
)
industry.add_spritelayout(
    id="solvay_plant_spritelayout_silos_with_office",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_silos_with_office],
)

industry.add_industry_layout(
    id="solvay_plant_industry_layout_1",
    layout=[
        (0, 0, "solvay_plant_tile_1", "solvay_plant_spritelayout_chimneys"),
        (0, 1, "solvay_plant_tile_1", "solvay_plant_spritelayout_boiler"),
        (
            0,
            2,
            "solvay_plant_tile_1",
            "solvay_plant_spritelayout_tanks_group",
        ),
        (1, 0, "solvay_plant_tile_1", "solvay_plant_spritelayout_chimneys"),
        (1, 1, "solvay_plant_tile_1", "solvay_plant_spritelayout_boiler"),
        (
            1,
            2,
            "solvay_plant_tile_1",
            "solvay_plant_spritelayout_tanks_group",
        ),
        (
            2,
            0,
            "solvay_plant_tile_1",
            "solvay_plant_spritelayout_silos_with_office",
        ),
        (2, 1, "solvay_plant_tile_1", "solvay_plant_spritelayout_silos"),
        (2, 2, "solvay_plant_tile_1", "solvay_plant_spritelayout_empty"),
    ],
)
industry.add_industry_layout(
    id="solvay_plant_industry_layout_2",
    layout=[
        (0, 0, "solvay_plant_tile_1", "solvay_plant_spritelayout_boiler"),
        (
            0,
            1,
            "solvay_plant_tile_1",
            "solvay_plant_spritelayout_tanks_group",
        ),
        (1, 0, "solvay_plant_tile_1", "solvay_plant_spritelayout_boiler"),
        (
            1,
            1,
            "solvay_plant_tile_1",
            "solvay_plant_spritelayout_tanks_group",
        ),
        (2, 0, "solvay_plant_tile_1", "solvay_plant_spritelayout_chimneys"),
        (2, 1, "solvay_plant_tile_1", "solvay_plant_spritelayout_silos"),
        (
            3,
            0,
            "solvay_plant_tile_1",
            "solvay_plant_spritelayout_silos_with_office",
        ),
        (3, 1, "solvay_plant_tile_1", "solvay_plant_spritelayout_empty"),
    ],
)
industry.add_industry_layout(
    id="solvay_plant_industry_layout_3",
    layout=[
        (0, 0, "solvay_plant_tile_1", "solvay_plant_spritelayout_boiler"),
        (
            0,
            1,
            "solvay_plant_tile_1",
            "solvay_plant_spritelayout_tanks_group",
        ),
        (0, 2, "solvay_plant_tile_1", "solvay_plant_spritelayout_chimneys"),
        (0, 3, "solvay_plant_tile_1", "solvay_plant_spritelayout_silos"),
        (1, 0, "solvay_plant_tile_1", "solvay_plant_spritelayout_boiler"),
        (
            1,
            1,
            "solvay_plant_tile_1",
            "solvay_plant_spritelayout_tanks_group",
        ),
        (
            1,
            2,
            "solvay_plant_tile_1",
            "solvay_plant_spritelayout_silos_with_office",
        ),
        (1, 3, "solvay_plant_tile_1", "solvay_plant_spritelayout_empty"),
    ],
)