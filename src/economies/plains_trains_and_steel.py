from economy import Economy

economy = Economy(
    id="PLAINS_TRAINS_AND_STEEL",
    numeric_id=7,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",
        "aluminium",
        "mail",
        "ammonia",
        "bauxite",
        "goods", 
        "building_materials",
        "carbon_steel",
        "cement",
        "chemicals",
        "coal",
        "food",
        "coke",
        "engineering_supplies",
        "farm_supplies",
        "fertiliser",
        "grain",
        "iron_ore",
        "limestone",
        "logs",
        "oil",
        "petrol",
        "pig_iron",
        "potash",
        "phosphate",
        "quicklime",
        "slag",
        "steel",
        "steel_sections",
        "stone",
        "timber",
        "vehicle_parts",
        "vehicles",
        
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
