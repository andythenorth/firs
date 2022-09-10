from economy import Economy

economy = Economy(
    id="IN_A_HOT_COUNTRY",
    numeric_id=3,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",
        "alcohol",
        "mail",
        "building_materials",
        "cassava",
        "goods",
        "chemicals",
        "clay",
        "coffee",
        "copper",
        "copper_ore",
        "food",
        "diamonds",
        "edible_oil",
        "engineering_supplies",
        "farm_supplies",
        "fruits",
        "livestock",
        "logs",
        "timber",
        "maize",
        "manganese",
        "nuts",
        "oil",
        "petrol",
        "phosphate",
        "rubber",
        "sand",
        "stone",
    ],
    cargoflow_graph_tuning={
        "group_edges_subgraphs": [],
        "ranking_subgraphs": [
            ("same", ["port", "goods"]),
            ("sink", ["T_town_industries", "N_force_rank"]),
        ],
        "clusters": [
            # {"nodes": [], "rank": "", "color": ""},
        ],
    },
)
