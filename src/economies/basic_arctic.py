from economy import Economy

economy = Economy(
    id="BASIC_ARCTIC",
    numeric_id=1,
    cargos=[
        "ammonia",
        "engineering_supplies",
        "explosives",
        "farm_supplies",
        "fertiliser",
        "fish",
        "food",
        "kaolin",
        "logs",
        "mail",
        "paper",
        "passengers",
        "peat",
        "phosphate",
        "potash",
        "pyrite_ore",
        "sulphur",
        "timber",
        "zinc",
    ],
    # as of March 2021 this cargoflow tuning is a temporary patch up, might need more work
    cargoflow_graph_tuning={
        "group_edges_subgraphs": [],
        "ranking_subgraphs": [
            # ("sink", ["industry_foo"]),
        ],
        "clusters": [
            # {"nodes": [], "rank": "", "color": ""},
        ],
    },
)
