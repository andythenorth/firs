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
    # as of April 2021 this cargoflow graph is really as optimised as can be
    # the pacemaker is the salt -> chlor-alkali -> acid chain which requires 15 steps in horizontal rank
    # this limits how big the font / industry images can be
    # I've tried using vertical edges or reversed edges to cut the number of steps, but it makes the overall flow less legible
    cargoflow_graph_tuning={
        "group_edges_subgraphs": [
            ["basic_oxygen_furnace", "electric_arc_furnace"],
            ["pig_iron"],  # groups edges can be set for a single node
        ],
        "ranking_subgraphs": [
            ("source", ["potash_mine", "quarry", "farm", "coal_mine"]),
            ("same", ["chlor_alkali_plant", "lime_kiln", "cryo_plant"]),
            ("same", ["wire_and_section_mill", "sheet_and_pipe_mill"]),
            ("same", ["cleaning_agents", "zinc", "cement"]),
            (
                "same",
                [
                    "component_factory",
                    "body_plant",
                    "engine_plant",
                    "tyre_plant",
                ],
            ),
            (
                "same",
                [
                    "plastics",
                    "alloy_steel",
                    "stainless_steel",
                    "glass",
                    "sulphur",
                    "aluminium",
                ],
            ),
            (
                "sink",
                ["assembly_plant", "vehicles", "T_town_industries", "T_towns_vehicles"],
            ),
        ],
        "clusters": [
            {
                "nodes": ["blast_furnace", "pig_iron", "basic_oxygen_furnace"],
                "rank": "same",
            },
            {"nodes": ["oxygen", "quicklime"], "rank": "same", "color": "white"},
            {
                "nodes": ["scrap_yard", "scrap_metal", "electric_arc_furnace"],
                "rank": "same",
            },
            {
                "nodes": ["quarry", "limestone_mine"],
                "rank": "source",
                "color": "white",
            },
            {
                "nodes": ["bulk_terminal", "food", "chlorine", "potash"],
                "color": "white",
            },
            {
                "nodes": ["pipe", "steel_sections", "cement", "lye"],
                "rank": "same",
                "color": "white",
            },
            {"nodes": ["coal", "coal_mine", "coke_oven"], "rank": "same"},
            {"nodes": ["carbon_steel", "acid"], "rank": "same", "color": "white"},
            {
                "nodes": ["coal_tar", "carbon_black_plant", "carbon_black"],
                "rank": "source",
            },
            {
                "nodes": [
                    "stainless_steel",
                    "alloy_steel",
                    "plastics",
                    "electrical_parts",
                ],
                "color": "white",
            },
            {
                "nodes": ["glass", "paints_and_coatings", "steel_sheet"],
                "rank": "same",
                "color": "white",
            },
            {
                "nodes": ["sulphur", "rubber", "steel_wire_rod"],
                "rank": "source",
                "color": "white",
            },
            {
                "nodes": ["aluminium", "cast_iron"],
                "rank": "source",
                "color": "white",
            },
            {
                "nodes": [
                    "assembly_plant",
                    "vehicle_parts",
                    "tyres",
                    "vehicle_engines",
                    "vehicle_bodies",
                ],
                "color": "white",
            },
        ],
    },
)
