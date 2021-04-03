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
        "alloy_steel",
        "aluminium",
        "vehicles",  # no goods?
        "carbon_black",
        "carbon_steel",
        "cast_iron",
        "cement",
        "chlorine",
        "food",
        "cleaning_agents",
        "coal",
        "coal_tar",
        "coke",
        "electrical_parts",
        "engineering_supplies",
        "farm_supplies",
        "ferrochrome",
        "glass",
        "iron_ore",
        "limestone",
        "lye",
        "manganese",
        "oxygen",
        "paints_and_coatings",
        "pig_iron",
        "pipe",
        "plastics",
        "quicklime",
        "rubber",
        "salt",
        "sand",
        "scrap_metal",
        "slag",
        "soda_ash",
        "stainless_steel",
        "steel_sections",
        "steel_sheet",
        "steel_wire_rod",
        "sulphur",
        "tyres",
        "vehicle_bodies",
        "vehicle_engines",
        "vehicle_parts",
        "zinc",
        "potash",
    ],
    cargoflow_graph_tuning={
        "ranking_subgraphs": [
            ("source", ["I_potash_mine", "I_quarry", "I_farm", "I_coal_mine"]),
            ("same", ["I_chlor_alkali_plant", "I_lime_kiln", "I_cryo_plant"]),
            ("same", ["I_wire_and_section_mill", "I_sheet_and_pipe_mill"]),
            ("same", ["C_cleaning_agents", "C_zinc", "C_cement"]),
            (
                "same",
                [
                    "I_component_factory",
                    "I_body_plant",
                    "I_engine_plant",
                    "I_tyre_plant",
                ],
            ),
            (
                "same",
                [
                    "C_plastics",
                    "C_alloy_steel",
                    "C_stainless_steel",
                    "C_glass",
                    "C_sulphur",
                    "C_aluminium",
                ],
            ),
            ("sink", ["I_assembly_plant", "C_vehicles", "T_town_industries"]),
        ],
        "clusters": [
            {
                "nodes": ["I_blast_furnace", "C_pig_iron", "I_basic_oxygen_furnace"],
                "rank": "same",
            },
            {"nodes": ["C_oxygen", "C_quicklime"], "rank": "same", "color": "white"},
            {
                "nodes": ["I_junk_yard", "C_scrap_metal", "I_electric_arc_furnace"],
                "rank": "same",
            },
            {
                "nodes": ["I_quarry", "I_limestone_mine"],
                "rank": "source",
                "color": "white",
            },
            {
                "nodes": ["I_bulk_terminal", "C_food", "C_chlorine", "C_potash"],
                "color": "white",
            },
            {
                "nodes": ["C_pipe", "C_steel_sections", "C_cement", "C_lye"],
                "rank": "same",
                "color": "white",
            },
            {"nodes": ["C_coal", "I_coal_mine", "I_coke_oven"], "rank": "same"},
            {"nodes": ["C_carbon_steel", "C_acid"], "rank": "same", "color": "white"},
            {
                "nodes": ["C_coal_tar", "I_carbon_black_plant", "C_carbon_black"],
                "rank": "source",
            },
            {
                "nodes": [
                    "C_stainless_steel",
                    "C_alloy_steel",
                    "C_plastics",
                    "C_electrical_parts",
                ],
                "color": "white",
            },
            {
                "nodes": ["C_glass", "C_paints_and_coatings", "C_steel_sheet"],
                "rank": "same",
                "color": "white",
            },
            {
                "nodes": ["C_sulphur", "C_rubber", "C_steel_wire_rod"],
                "rank": "source",
                "color": "white",
            },
            {
                "nodes": ["C_aluminium", "C_cast_iron"],
                "rank": "source",
                "color": "white",
            },
            {
                "nodes": [
                    "I_assembly_plant",
                    "C_vehicle_parts",
                    "C_tyres",
                    "C_vehicle_engines",
                    "C_vehicle_bodies",
                ],
                "color": "white",
            },
        ],
    },
)
