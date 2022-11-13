from industry import IndustryPrimaryPort, TileLocationChecks

industry = IndustryPrimaryPort(
    id="port",
    accept_cargo_types=[],
    prod_cargo_types_with_multipliers=[],
    prob_in_game="2",
    prob_map_gen="8",
    map_colour="47",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    location_checks=dict(same_type_distance=16),
    prospect_chance="0.75",
    name="string(STR_IND_PORT)",
    nearby_station_name="string(STR_STATION_INDUSTRY_HARBOUR_2)",
    fund_cost_multiplier="152",
    override_default_construction_states=True,
)

industry.enable_in_economy(
    "PLAINS_TRAINS_AND_STEEL",
    prod_cargo_types_with_multipliers=[
        ("GOOD", 20)
    ],
    accept_cargo_types=["GOOD",],
    intro_year=1965,
    fund_cost_multiplier="15",
    
)

industry.add_tile(
    id="port_tile_1",
    land_shape_flags="bitmask(LSF_ONLY_ON_FLAT_LAND)",
    location_checks=TileLocationChecks(always_allow_founder=False),
)
industry.add_tile(
    id="port_tile_2",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)
sprite_ground = industry.add_sprite(sprite_number="GROUNDSPRITE_WATER")
spriteset_ground_empty = industry.add_spriteset(type="empty")
spriteset_concrete = industry.add_spriteset(
    sprites=[(10, 10, 64, 39, -31, -8)],
    always_draw=1,
)
spriteset_jetty_se_nw = industry.add_spriteset(
    sprites=[(10, 60, 64, 39, -31, -7)],
    always_draw=1,
)
spriteset_jetty_ne_sw = industry.add_spriteset(
    sprites=[(80, 60, 64, 39, -31, -7)], always_draw=1
)
spriteset_jetty_slope_nw_se = industry.add_spriteset(
    sprites=[(150, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_ne_sw = industry.add_spriteset(
    sprites=[(220, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_se_nw = industry.add_spriteset(
    sprites=[(290, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_sw_ne = industry.add_spriteset(
    sprites=[(360, 60, 64, 39, -31, -7)],
)
spriteset_office = industry.add_spriteset(
    sprites=[(440, 10, 64, 74, -31, -34)], 
    zoffset=18
)
spriteset_containers_1 = industry.add_spriteset(
    sprites=[(510, 10, 64, 74, -31, -34)], 
    zoffset=16
)
spriteset_containers_2 = industry.add_spriteset(
    sprites=[(440, 110, 64, 74, -31, -34)], 
    zoffset=16
)
spriteset_containers_3 = industry.add_spriteset(
    sprites=[(510, 110, 64, 74, -31, -34)], 
    zoffset=16
)

# New crane sprites SW
spriteset_crane_sw_1 = industry.add_spriteset(
    sprites=[(10, 160, 64, 122, -31, -34)], zoffset=40
)
spriteset_crane_sw_2 = industry.add_spriteset(
    sprites=[(80, 160, 64, 122, -31, -34)], zoffset=24
)

# New crane sprites SE
spriteset_crane_se_1 = industry.add_spriteset(
    sprites=[(150, 160, 64, 122, -31, -34)], zoffset=40
)
spriteset_crane_se_2 = industry.add_spriteset(
    sprites=[(220, 160, 64, 122, -31, -34)], zoffset=24
)

# New crane sprites NW
spriteset_crane_nw_1 = industry.add_spriteset(
    sprites=[(290, 160, 64, 122, -31, -34)], zoffset=40
)
spriteset_crane_nw_2 = industry.add_spriteset(
    sprites=[(360, 160, 64, 122, -31, -34)], zoffset=24
)





spriteset_containers_small_a = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, 0)],
    zoffset=16,
)
spriteset_containers_small_b = industry.add_spriteset(
    sprites=[(220, 10, 64, 39, -31, 0)],
    zoffset=16,
)



spriteset_11 = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -35, -15)],
)
spriteset_12 = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -31, -14)],
)
spriteset_13 = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -31, -8)],
)
spriteset_14 = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -27, -12)],
)
spriteset_15 = industry.add_spriteset(
    sprites=[(290, 110, 64, 39, -15, -11)],
)
spriteset_16 = industry.add_spriteset(
    sprites=[(360, 110, 64, 39, -45, -15)],
)
spriteset_truck = industry.add_spriteset(
    sprites=[(360, 10, 64, 39, -31, 0)],
    zoffset=18,
)
spriteset_checkpoint = industry.add_spriteset(
    sprites=[(290, 10, 64, 39, -31, 0)],
    zoffset=18,
)
# spritelayout numbers have gaps for historical reasons
industry.add_spritelayout(
    id="port_spritelayout_truck",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_truck,
    ],
)
industry.add_spritelayout(
    id="port_spritelayout_checkpoint",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_checkpoint,
    ],
)
industry.add_spritelayout(
    id="port_spritelayout_containers_jetty_1",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_concrete, spriteset_containers_1],
)
industry.add_spritelayout(
    id="port_spritelayout_containers_jetty_2",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_ne_sw, spriteset_concrete, spriteset_containers_2],
)
industry.add_spritelayout(
    id="port_spritelayout_13",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_office,
    ],
)
industry.add_spritelayout(
    id="port_spritelayout_21",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_11],
)
industry.add_spritelayout(
    id="port_spritelayout_22",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_12],
)
industry.add_spritelayout(
    id="port_spritelayout_23",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_13],
)
industry.add_spritelayout(
    id="port_spritelayout_24",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_14],
)
industry.add_spritelayout(
    id="port_spritelayout_25",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_14],
)
industry.add_spritelayout(
    id="port_spritelayout_26",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_15],
)
industry.add_spritelayout(
    id="port_spritelayout_27",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_16],
)
industry.add_spritelayout(
    id="port_spritelayout_small_hut",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_containers_small_a,
    ],
)
#New crane SW
industry.add_spritelayout(
    id="port_spritelayout_crane_sw_1",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_crane_sw_1,
    ],
)
industry.add_spritelayout(
    id="port_spritelayout_crane_sw_2",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_crane_sw_2,
    ],
)

#New crane SW
industry.add_spritelayout(
    id="port_spritelayout_crane_se_1",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_crane_se_1,
    ],
)
industry.add_spritelayout(
    id="port_spritelayout_crane_se_2",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_crane_se_2,
    ],
)

#New crane NW
industry.add_spritelayout(
    id="port_spritelayout_crane_nw_1",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_crane_nw_1,
    ],
)
industry.add_spritelayout(
    id="port_spritelayout_crane_nw_2",
    tile="port_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_crane_nw_2,
    ],
)



industry.add_spritelayout(
    id="port_spritelayout_small_stack",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_containers_small_b,
    ],
)
industry.add_spritelayout(
    id="port_spritelayout_30",
    tile="port_tile_1",
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[
        spriteset_jetty_se_nw,
        spriteset_jetty_ne_sw,
        spriteset_concrete,
        spriteset_containers_small_a,
    ],
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="port_spritelayout_coast_checkpoint",
    tile="port_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_checkpoint],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="port_spritelayout_coast_office",
    tile="port_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_office],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="port_spritelayout_coast_containers_1",
    tile="port_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_containers_1],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)

industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="port_spritelayout_coast_containers_2",
    tile="port_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_containers_2],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)

industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="port_spritelayout_coast_containers_3",
    tile="port_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_containers_3],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)
industry.add_magic_spritelayout(
    type="harbour_coast_foundations",
    base_id="port_spritelayout_coast_truck",
    tile="port_tile_2",
    config={
        "ground_sprite": spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
        "building_sprites": [spriteset_concrete, spriteset_truck],
        "foundation_sprites": {
            "ne_sw": spriteset_jetty_ne_sw,
            "se_nw": spriteset_jetty_se_nw,
            "slope_nw_se": spriteset_jetty_slope_nw_se,
            "slope_ne_sw": spriteset_jetty_slope_ne_sw,
            "slope_se_nw": spriteset_jetty_slope_se_nw,
            "slope_sw_ne": spriteset_jetty_slope_sw_ne,
        },
    },
)

industry.add_industry_layout(
    id="port_industry_layout_1",
    layout=[
        (0, 1, "port_spritelayout_containers_jetty_1"),  
        (0, 2, "port_spritelayout_small_hut"),  
        (0, 3, "port_spritelayout_coast_containers_1"),
        (0, 4, "port_spritelayout_coast_containers_3"),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "port_spritelayout_crane_sw_2"),
        (1, 2, "port_spritelayout_crane_sw_1"),
        (1, 3, "port_spritelayout_truck"),
        (1, 4, "port_spritelayout_coast_containers_2"),
    ],
)
industry.add_industry_layout(
    id="port_industry_layout_2",
    layout=[
        (0, 0, "port_spritelayout_coast_containers_2"),
        (0, 1, "port_spritelayout_coast_office"),
        (0, 2, "port_spritelayout_coast_checkpoint"),
        (0, 3, "port_spritelayout_coast_containers_3"),
        (1, 0, "port_spritelayout_24"),
        (1, 1, "spritelayout_null_water"),
        (1, 2, "port_spritelayout_truck"),
        (2, 1, "port_spritelayout_crane_nw_2"),
        (2, 2, "port_spritelayout_crane_nw_1"),
        (3, 1, "port_spritelayout_26"),
        (3, 2, "port_spritelayout_small_hut"),
        (2, 3, "port_spritelayout_22"),
        (2, 4, "spritelayout_null_water"),
        (3, 3, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="port_industry_layout_3",
    layout=[
        (0, 0, "port_spritelayout_coast_office"),
        (0, 1, "port_spritelayout_truck"),
        (0, 2, "port_spritelayout_crane_sw_2"),
        (0, 3, "port_spritelayout_crane_sw_1"),
        (0, 4, "port_spritelayout_small_stack"),
        (0, 5, "spritelayout_null_water"),
        (1, 0, "port_spritelayout_coast_containers_1"),
        (1, 1, "port_spritelayout_small_hut"),
        (1, 2, "port_spritelayout_25"),
        (1, 4, "port_spritelayout_25"),
        (1, 5, "spritelayout_null_water"),
        (2, 0, "port_spritelayout_coast_containers_2"),
        (2, 1, "port_spritelayout_small_stack"),
        (2, 2, "spritelayout_null_water"),
        (3, 1, "spritelayout_null_water"),
        (3, 2, "spritelayout_null_water"),
    ],
)
