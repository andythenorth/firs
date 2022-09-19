from economy import Economy

economy = Economy(
    id="BASIC_TEMPERATE",
    numeric_id=0,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",
        "alcohol",
        "mail",
        "chemicals",
        "coal",
        "goods",
        "engineering_supplies",
        "farm_supplies",
        "fish",
        "fruits",
        "iron_ore",
        "food",
        "kaolin",
        "livestock",
        "milk",
        "sand",
        "scrap_metal",
        "steel",
    ],
    # as of March 2021 this cargoflow tuning is a temporary patch up, might need more work
    cargoflow_graph_tuning={
        "group_edges_subgraphs": [],
        "ranking_subgraphs": [
            ("sink", ["port", "T_town_industries"]),
        ],
        "clusters": [
            # {"nodes": [], "rank": "", "color": ""},
        ],
    },
)

# some deliberate overlapping of biomes for mixing at boundaries
economy.add_biome(
    "more_south_west",
    min_x_percent = 35,
    max_x_percent = 100,
    min_y_percent = 0,
    max_y_percent = 100,
)
economy.add_biome(
    "less_south_west",
    min_x_percent = 0,
    max_x_percent = 65,
    min_y_percent = 0,
    max_y_percent = 100,
)
