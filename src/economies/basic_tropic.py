from economy import Economy

economy = Economy(
    id="BASIC_TROPIC",
    numeric_id=4,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",
        "alcohol",
        "mail",
        "beans",
        "chemicals",
        "goods",
        "coffee",
        "copper",
        "copper_ore",
        "engineering_supplies",
        "farm_supplies",
        "food",  # has to be out of order for compatibility
        "fish",
        "fruits",
        "grain",
        "livestock",
        "nitrates",
        "oil",
        "wool",
    ],
    # as of April 2021 this cargoflow graph is really as optimised as can be
    # the main driver is preventing ugly appearance of the edges that converge on food, most of the layout is arranged around preventing that
    cargoflow_graph_tuning={
        "group_edges_subgraphs": [
        ],
        "ranking_subgraphs": [
            ("same", ["I_nitrate_mine", "I_coffee_estate", "I_ranch", "I_arable_farm"]),
            ("same", ["I_food_processor", "I_stockyard", "I_flour_mill"]),
            ("same", ["I_port", "C_food", "I_fishing_harbour", "C_fish"]),
            ("sink", ["C_goods", "T_town_industries"]),
        ],
        "clusters": [
            {"nodes": ["C_chemicals", "C_copper_ore"], "rank": "", "color": "white"},
            {"nodes": ["C_nitrates", "C_oil"], "rank": "same", "color": "white"},
            {"nodes": ["C_fruits", "C_beans"], "rank": "same", "color": "white"},
            {
                "nodes": ["C_wool", "C_coffee", "C_alcohol", "C_copper"],
                "rank": "same",
                "color": "white",
            },
        ],
    },
)
