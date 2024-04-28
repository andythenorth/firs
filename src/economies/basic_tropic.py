from economy import Economy

economy = Economy(
    id="BASIC_TROPIC",
    numeric_id=4,
    cargos=[
        "alcohol",
        "beans",
        "chemicals",
        "coffee",
        "copper",
        "copper_ore",
        "engineering_supplies",
        "farm_supplies",
        "fish",
        "food",
        "fruits",
        "goods",
        "grain",
        "livestock",
        "mail",
        "nitrates",
        "oil",
        "passengers",
        "wool",
    ],
    # as of April 2021 this cargoflow graph is really as optimised as can be
    # the main driver is preventing ugly appearance of the edges that converge on food, most of the layout is arranged around preventing that
    cargoflow_graph_tuning={
        "group_edges_subgraphs": [],
        "ranking_subgraphs": [
            ("same", ["nitrate_mine", "coffee_estate", "ranch", "arable_farm"]),
            ("same", ["food_processor", "stockyard", "flour_mill"]),
            ("same", ["port", "food", "fishing_harbour", "fish"]),
        ],
        "clusters": [
            {"nodes": ["chemicals", "copper_ore"], "rank": "", "color": "white"},
            {"nodes": ["nitrates", "oil"], "rank": "same", "color": "white"},
            {"nodes": ["fruits", "beans"], "rank": "same", "color": "white"},
            {
                "nodes": ["wool", "coffee", "alcohol", "copper"],
                "rank": "same",
                "color": "white",
            },
        ],
    },
)

# some deliberate overlapping of biomes for mixing at boundaries
economy.add_biome(
    "more_west",
    min_x_percent=0,
    max_x_percent=100,
    min_y_percent=0,
    max_y_percent=60,
)
economy.add_biome(
    "less_west",
    min_x_percent=0,
    max_x_percent=100,
    min_y_percent=40,
    max_y_percent=100,
)
