from economy import Economy

economy = Economy(
    id="WAR_ECONOMY",
    numeric_id=7,
    cargos=[
        "coal",
        "coke",
        "mail",
        "oil",
        "passengers",
        "petrol",
        "sulphur",
        "vehicles",
        "salvage",
        "components",
        "diesel",
        "water",
        "bmats",
        "rmats",
        "expowder",
        "hvypowder",
        "cmats",
        "pcmats",
        "enriched_fuel",
        "basassmats",
        "advassmats",
        "itemcrates",
        "shippables",
        "artyshells",
        "advvehicles",
        "frontlinesupplies"
    ],
    cargoflow_graph_tuning={
        "group_edges_subgraphs": [],
        "ranking_subgraphs": [
            ("same", ["port", "goods"]),
        ],
        "clusters": [
            # {"nodes": [], "rank": "", "color": ""},
        ],
    },
)

# some deliberate overlapping of biomes for mixing at boundaries
economy.add_biome(
    "exclude_map_edges",
    min_x_percent=25,
    max_x_percent=75,
    min_y_percent=25,
    max_y_percent=75,
)
