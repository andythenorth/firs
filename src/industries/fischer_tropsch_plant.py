from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="fischer_tropsch_plant",
    accept_cargos_with_input_ratios=[("COAL", 8)],
    prod_cargo_types_with_output_ratios=[("NH3_", 2), ("PETR", 6)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="191",
    special_flags=["IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE"],
    fund_cost_multiplier="200",
    name="string(STR_IND_FISCHER_TROPSCH_PLANT)",
    nearby_station_name="string(STR_STATION_REFINERY)",
)

industry.economy_variations['BETTER_LIVING_THROUGH_CHEMISTRY'].enabled = True

industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations["STEELTOWN"].prod_cargo_types_with_output_ratios = [
    ("RFPR", 6),
    ("H2__", 2),
]

# industry.economy_variations['IN_A_HOT_COUNTRY'].enabled = True

industry.add_tile(
    id="fischer_tropsch_plant_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

sprite_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")

spriteset_silo = industry.add_spriteset(
    sprites=[(10, 10, 64, 122, -31, -91)],
)
spriteset_oven_battery = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -91)],
)
spriteset_oven_battery_larry_car = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -91)],
)
spriteset_pusher_rails_base = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -91)], yextent=8  # prevents gantry flickering ??
)
spriteset_pusher_car = industry.add_spriteset(
    sprites=[(10, 234, 64, 64, -31, -32)], yextent=8  # prevents gantry flickering ??
)
spriteset_pipe_gantry = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -91)],
)
spriteset_pipe_gantry_house = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -91)],
)
spriteset_coal_handling_front = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -91)],
)
spriteset_coal_handling_rear = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -91)],
)
spriteset_quench_tower = industry.add_spriteset(
    sprites=[(570, 10, 64, 122, -31, -91)],
)
spriteset_gas_plant_1 = industry.add_spriteset(
    sprites=[(640, 10, 64, 122, -31, -91)],
)
sprite_smoke_big_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=8,
    yoffset=5,
    zoffset=104,
)



industry.add_spritelayout(
    id="fischer_tropsch_plant_spritelayout_empty",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
)
industry.add_spritelayout(
    id="fischer_tropsch_plant_spritelayout_oven_battery_pipes_only",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_oven_battery],
)
industry.add_spritelayout(
    id="fischer_tropsch_plant_spritelayout_oven_battery_larry_car",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_oven_battery_larry_car],
)
industry.add_spritelayout(
    id="fischer_tropsch_plant_spritelayout_silo",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_silo],
    smoke_sprites=[sprite_smoke_big_1],
)
industry.add_spritelayout(
    id="fischer_tropsch_plant_spritelayout_pusher_rails_empty",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_pusher_rails_base, spriteset_pipe_gantry],
)
industry.add_spritelayout(
    id="fischer_tropsch_plant_spritelayout_pusher_rails_animated",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[
        spriteset_pusher_rails_base,
        spriteset_pusher_car,
        spriteset_pipe_gantry,
    ],
)
industry.add_spritelayout(
    id="fischer_tropsch_plant_spritelayout_pusher_rails_with_house",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_pusher_rails_base, spriteset_pipe_gantry_house],
)
industry.add_spritelayout(
    id="fischer_tropsch_plant_spritelayout_quench_tower",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_quench_tower],
)
industry.add_spritelayout(
    id="fischer_tropsch_plant_spritelayout_gas_plant_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_gas_plant_1],
)
industry.add_spritelayout(
    id="fischer_tropsch_plant_spritelayout_coal_handling_front",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_coal_handling_front],
)
industry.add_spritelayout(
    id="fischer_tropsch_plant_spritelayout_coal_handling_rear",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_coal_handling_rear],
)

industry.add_industry_layout(
    id="fischer_tropsch_plant_industry_layout_1",
    layout=[
        (0, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_gas_plant_1"),
        (0, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_larry_car"),
        (0, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_empty"),
        (1, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_rear"),
        (1, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_pipes_only"),
        (1, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_with_house"),
        (2, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_front"),
        (2, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_silo"),
        (2, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_animated"),
        (3, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_rear"),
        (3, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_pipes_only"),
        (3, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_with_house"),
        (4, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_front"),
        (4, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_quench_tower"),
        (4, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_empty"),
    ],
)
industry.add_industry_layout(
    id="fischer_tropsch_plant_industry_layout_2",
    layout=[
        (0, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_rear"),
        (0, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_pipes_only"),
        (0, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_with_house"),
        (0, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_gas_plant_1"),
        (1, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_front"),
        (1, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_larry_car"),
        (1, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_empty"),
        (1, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_empty"),
        (2, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_empty"),
        (2, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_pipes_only"),
        (2, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_with_house"),
        (2, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_rear"),
        (3, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_quench_tower"),
        (3, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_silo"),
        (3, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_animated"),
        (3, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_front"),
    ],
)
industry.add_industry_layout(
    id="fischer_tropsch_plant_industry_layout_3",
    layout=[
        (0, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_larry_car"),
        (0, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_with_house"),
        (0, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_quench_tower"),
        (0, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_gas_plant_1"),
        (0, 4, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_rear"),
        (1, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_silo"),
        (1, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_animated"),
        (1, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_larry_car"),
        (1, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_empty"),
        (1, 4, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_front"),
        (2, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_pipes_only"),
        (2, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_empty"),
        (2, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_silo"),
        (2, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_animated"),
        (2, 4, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_rear"),
        (3, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_quench_tower"),
        (3, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_with_house"),
        (3, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_pipes_only"),
        (3, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_empty"),
        (3, 4, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_front"),
    ],
)
industry.add_industry_layout(
    id="fischer_tropsch_plant_industry_layout_4",
    layout=[
        (0, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_empty"),
        (0, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_pipes_only"),
        (0, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_with_house"),
        (0, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_pipes_only"),
        (0, 4, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_with_house"),
        (1, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_rear"),
        (1, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_silo"),
        (1, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_empty"),
        (1, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_larry_car"),
        (1, 4, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_empty"),
        (2, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_front"),
        (2, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_larry_car"),
        (2, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_animated"),
        (2, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_silo"),
        (2, 4, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_animated"),
        (3, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_gas_plant_1"),
        (3, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_quench_tower"),
        (3, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_empty"),
        (3, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_quench_tower"),
        (3, 4, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_empty"),
    ],
)
industry.add_industry_layout(
    id="fischer_tropsch_plant_industry_layout_5",
    layout=[
        (0, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_empty"),
        (0, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_rear"),
        (0, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_silo"),
        (0, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_quench_tower"),
        (0, 4, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_silo"),
        (0, 5, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_gas_plant_1"),
        (1, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_rear"),
        (1, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_front"),
        (1, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_pipes_only"),
        (1, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_animated"),
        (1, 4, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_larry_car"),
        (1, 5, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_with_house"),
        (2, 0, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_coal_handling_front"),
        (2, 1, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_quench_tower"),
        (2, 2, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_larry_car"),
        (2, 3, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_with_house"),
        (2, 4, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_oven_battery_pipes_only"),
        (2, 5, "fischer_tropsch_plant_tile_1", "fischer_tropsch_plant_spritelayout_pusher_rails_animated"),
    ],
)
