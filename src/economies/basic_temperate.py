from economy import Economy

economy = Economy(
    id="BASIC_TEMPERATE",
    numeric_id=0,
    cargos=[
        "alcohol",
        "chemicals",
        "coal",
        "engineering_supplies",
        "farm_supplies",
        "fish",
        "fruits",
        "goods",
        "iron_ore",
        "food",
        "kaolin",
        "livestock",
        "mail",
        "milk",
        "passengers",
        "sand",
        "scrap_metal",
        "steel",
    ],
    # as of March 2021 this cargoflow tuning is a temporary patch up, might need more work
    cargoflow_graph_tuning={
        "group_edges_subgraphs": [],
        "ranking_subgraphs": [
            ("sink", ["port"]),
        ],
        "clusters": [
            # {"nodes": [], "rank": "", "color": ""},
        ],
    },
)
