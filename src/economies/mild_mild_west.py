from economy import Economy

economy = Economy(
    id="MILD_MILD_WEST",
    numeric_id=6,
    cargos=[
        "aggregates",
        "alcohol",
        "aluminia",
        "aluminium",
        "ammonia",
        "apples",
        "bitumen",
        "cement",
        "chemical_intermediates",
        "coal",
        "coke",
        "dairy_products",
        "engineering_supplies",
        "explosives",
        "farm_supplies",
        "fish",
        "food",
        "food_additives",
        "flour",
        "glass",
        "goods",
        "grain",
        "hardware",
        "iron_ore",
        "kaolin",
        "limestone",
        "livestock",
        "logs",
        "mail",
        "meat_products",
        "milk",
        "molasses",
        "naphtha",
        "wood_pulp", # cabbage out of order (savegame preservation issues)
        "sulphur", # cabbage out of order (savegame preservation issues)
        "plant_and_machinery", # cabbage savegame preservation issues
        "oil",
        "packaging",
        "diamonds", # cabbage savegame preservation issues
        "process_chemicals",
        "passengers",
        "petcoke",
        "petroleum_fuels",
        "phosphate",
        "phosphoric_acid",
        "plastics",
        "potash",
        "quicklime",
        "salt",
        "scrap_metal",
        "seafood_products",
        "slag",
        "steel",
        "industrial_gases", # cabbage out of order (savegame preservation issues)
        "components", # cabbage out of order (savegame preservation issues)
        "sulphuric_acid",
        "timber",
        "tin",
        "tinplate",
        "vegetables",
        "methanol", # cabbage out of order (savegame preservation issues)
        "zinc",
        "zinc_ore",
        "concrete_products", # cabbage out of order (savegame preservation issues)
    ],
    cargoflow_graph_tuning={
        "wormhole_industries": [
            "liquids_terminal",
            "port",
            "wharf",
        ],
        "cargos_with_individual_produce_nodes": [
            "livestock",
        ],
        "cargos_with_individual_accept_nodes": [
            "limestone",
            "naphtha",
            "petroleum_fuels",
            "process_chemicals",
        ],
        "group_edges_subgraphs": [],
        "ranking_subgraphs": [],
        "clusters": [
            # {"nodes": [], "rank": "", "color": ""},
        ],
    },
)
