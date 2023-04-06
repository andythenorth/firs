from economy import Economy

economy = Economy(
    id="STEELTOWN",
    numeric_id=5,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",
        "acid",
        "mail",
        "aggregates",
        "steel_slab", # !! out of order to preserve testing savegame, needs moved
        "goods",
        "hardware", # !! out of order to preserve testing savegame, needs moved
        "carbon_black",
        "steel_billets_and_blooms", # !! out of order to preserve testing savegame, needs moved
        "cast_iron",
        "cement",
        "food",
        "chlorine",
        "cleaning_agents",
        "coal",
        "coal_tar",
        "coke",
        "concrete_products",
        "cranes_and_hoists",
        "electrical_parts",
        "engineering_supplies",
        "farm_supplies",
        "ferroalloys",
        "forgings_and_castings",
        "glass",
        "iron_ore",
        "lifting_equipment",
        "limestone",
        "lye",
        "elastomer_products", # !! out of order to preserve testing savegame, needs moved
        "nitrogen",
        "oxygen",
        "paints_and_coatings",
        "pig_iron",
        "potash",
        "pipework",
        "aluminium", # !! out of order to preserve testing savegame, needs moved
        "pumps_and_valves",
        "quicklime",
        "rebar",
        "rubber",
        "salt",
        "sand",
        "scrap_metal",
        "slag",
        "soda_ash",
        "steel_ingots",
        "steel_merchant_bar",
        "steel_pipe",
        "steel_sections",
        "steel_sheet",
        "steel_tube",
        "steel_wire_rod",
        "steel_wire_rope",
        "sulphur",
        "tyre_cord",
        "tyres",
        "vehicles",
        "vehicle_bodies",
        "vehicle_engines",
        "vehicle_parts",
        "welding_consumables",
        "zinc",
    ],
    cargoflow_graph_tuning={
        # also any industries with !!!!??????? will be automatically added to wormhole_industries
        "wormhole_industries": ["wharf", "bulk_terminal", "hardware_factory"],
        "cargos_with_individual_produce_nodes": [
            "steel_ingots",
            "steel_slab",
            "steel_billets_and_blooms",
            "slag",
        ],
        "cargos_with_individual_accept_nodes": [
            "sand",
            "acid",
            "limestone",
            "paints_and_coatings",
            "cleaning_agents",
        ],
        "group_edges_subgraphs": [
            ["basic_oxygen_furnace", "electric_arc_furnace"],
            ["pig_iron"],  # groups edges can be set for a single node
        ],
        "ranking_subgraphs": [
            ("source", ["quarry", "coal_mine", "iron_ore_mine"]),
            ("same", ["lime_kiln", "glass_works"]),
            ("same", ["engine_plant", "tyre_plant", "body_plant"]),
            ("same", ["oxygen", "coke", "iron_ore"]),
            ("sink", ["cranes_and_hoists", "hardware", "goods", "vehicles", "pipework", "assembly_plant", "machine_shop", "pipework_fabricator", "crane_and_hoist_factory"]),
        ],
        "clusters": [
            {
                "nodes": ["hardware_factory", "component_factory"],
                "rank": "same",
                "color": "white",
            },
            {
                "nodes": ["blast_furnace", "pig_iron", "basic_oxygen_furnace"],
                "rank": "same",
            },
            {
                "nodes": ["scrap_yard", "scrap_metal", "electric_arc_furnace"],
                "rank": "same",
            },
            {
                "nodes": ["coke", "iron_ore"],
                "rank": "same",
                "color": "white",
            },
            {"nodes": ["coal", "coal_mine", "coke_oven"], "rank": "same"},
            {
                "nodes": ["sulphur", "rubber", "carbon_black"],
                "rank": "same",
                "color": "white",
            },
            {
                "nodes": ["glass", "paints_and_coatings"],
                "rank": "same",
                "color": "white",
            },
            {
                "nodes": ["concrete_plant", "concrete_products"],
                "rank": "same",
                "color": "white",
            },
            {
                "nodes": [
                    "vehicle_parts",
                    "vehicle_bodies",
                    "vehicle_engines",
                    "tyres",
                ],
                "rank": "same",
                "color": "white",
            },
            {
                "nodes": ["cement", "rebar"],
                "rank": "same",
                "color": "white",
            },
        ],
    },
)
