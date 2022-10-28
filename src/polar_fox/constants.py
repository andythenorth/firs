"""
This file is generated from the Polar Fox project.
Don't make changes here, make them in the Polar Fox project and redistribute.
Any changes made here are liable to be over-written.
"""

"""
This file is generated from the Polar Fox project.
Don't make changes here, make them in the Polar Fox project and redistribute.
Any changes made here are liable to be over-written.
"""

"""
This file is generated from the Polar Fox project.
Don't make changes here, make them in the Polar Fox project and redistribute.
Any changes made here are liable to be over-written.
"""

# used to construct the cargo table automatically
# ! order is significant ! - openttd will cascade through default cargos in the order specified by the cargo table
cargo_labels = [
    "PASS",  # pax first
    "TOUR",
    # "the mail must get through"
    "MAIL",
    # all other cargos - append new ones to end, don't change order
    "COAL",
    "IORE",
    "GRVL",
    "SAND",
    "AORE",
    "CORE",
    "CLAY",
    "SCMT",
    "WOOD",
    "LIME",
    "GOOD",
    "FOOD",
    "STEL",
    "FMSP",
    "ENSP",
    "BEER",
    "BDMT",
    "MNSP",
    "PAPR",
    "WDPR",
    "COPR",
    "DYES",
    "OIL_",
    "RFPR",
    "PETR",
    "PLAS",
    "WATR",
    "FISH",
    "CERE",
    "FICR",
    "FRVG",
    "FRUT",
    "GRAI",
    "LVST",
    "MAIZ",
    "MILK",
    "RUBR",
    "SGBT",
    "SGCN",
    "WHEA",
    "WOOL",
    "OLSD",
    "SUGR",
    "JAVA",
    "BEAN",
    "NITR",
    "VEHI",
    "EOIL",
    "NUTS",
    "CASS",
    "MNO2",
    "PHOS",
    "POTA",
    "PORE",
    "IRON",
    "NICK",
    "SLAG",
    "QLME",
    "BOOM",
    "METL",
    "SULP",
    "SASH",
    "CMNT",
    "COKE",
    "KAOL",
    "FERT",
    "PIPE",
    "SALT",
    "CBLK",
    "CHLO",
    "VPTS",
    "ACID",
    "ALUM",
    "CTCD",
    "TOFF",
    "URAN",
    "CTAR",
    "O2__",
    "STAL",
    "STCB",
    "STST",
    "CSTI",
    "PEAT",
    "ZINC",
    "TYRE",
    "VBOD",
    "VENG",
    "FECR",
    "GLAS",
    "POWR",
    "STSH",
    "STWR",
    "NH3_",
    "STSE",
    "SEED",
    "TATO",
    "WDCH",
    "BAKE",
    "N7__",
    "WELD",
    "RBAR",
    "STPP",
    "SOAP",
    "H2__",
    "ALO_",
    "NHNO",
    #
    "NULL",
]

# shared lists of allowed classes, shared across multiple vehicle types
base_refits_by_class = {
    "all_freight": [
        "CC_BULK",
        "CC_PIECE_GOODS",
        "CC_EXPRESS",
        "CC_LIQUID",
        "CC_ARMOURED",
        "CC_REFRIGERATED",
        "CC_COVERED",
        "CC_NON_POURABLE",
    ],
    "covered_hopper_freight": [],  # explicit allowal by label instead
    "dump_freight": ["CC_BULK"],
    "empty": [],
    "express_freight": ["CC_EXPRESS", "CC_ARMOURED"],
    "flatbed_freight": ["CC_PIECE_GOODS"],
    "liquids": ["CC_LIQUID"],
    "mail": ["CC_MAIL"],
    "packaged_freight": ["CC_PIECE_GOODS", "CC_EXPRESS", "CC_ARMOURED", "CC_LIQUID"],
    "pax": ["CC_PASSENGERS"],
    "refrigerated_freight": ["CC_REFRIGERATED"],
}

# generally we want to allow refit on classes, and disallow on labels (see disallowed_refits_by_label)
# BUT for _some_ specialist vehicle types, it's simpler to just allow refit by label
allowed_refits_by_label = {
    # box cars get some extended cargos
    "box_freight": [
        "MAIL",
        "GRAI",
        "WHEA",
        "MAIZ",
        "FRUT",
        "BEAN",
        "NITR",
        "CMNT",
    ],
    # seems to be used by intermodal, otherwise chemicals tankers are deprecated in favour of product tankers
    "chemicals": [
        "ACID",
        "RFPR",
        "CHLO",
    ],
    "metal_coil": [
        "STEL",
        "METL",
        "STCB",
        "STAL",
        "STST",
        "COPR",
        "STSH",
        "STWR",
        "ALUM",
        "RBAR",
    ],
    "covered_hoppers": [
        "GRAI",
        "WHEA",
        "MAIZ",
        "SUGR",
        "FMSP",
        "RFPR",
        "CLAY",
        "BDMT",
        "BEAN",
        "NITR",
        "RUBR",
        "SAND",
        "POTA",
        "QLME",
        "SASH",
        "CMNT",
        "KAOL",
        "FERT",
        "SALT",
        "PLAS",
        "PHOS",
        "BAKE",
        "ALO_",
        "NHNO",
        # not CBLK, gets dedicated vehicles or box
    ],
    "cryo_gases": ["CHLO", "O2__", "NH3_", "N7__", "WELD", "H2__"],
    "edible_liquids": ["MILK", "WATR", "BEER", "FOOD", "EOIL"],
    "farm_products": [
        "BEAN",
        "CASS",
        "CERE",
        "FERT",
        "FMSP",
        "FRUT",
        "GRAI",
        "JAVA",
        "MAIZ",
        "NUTS",
        "OLSD",
        "SEED",
        "SGBT",
        "TATO",
        "WHEA",
    ],
    # for bolster wagon
    "long_products": [
        "STEL",
        "METL",
        "STCB",
        "STAL",
        "STST",
        "COPR",
        "STSH",
        "STSE",
        "STWR",
        "WOOD",
        "WDPR",
        "BDMT",
        "ALUM",
        "PIPE",
        "ZINC",
        "ENSP",
    ],
    # hax for intermodal container sprite selection - reefer car refits work just fine using CC_REFRIGERATED
    "reefer": [
        "FOOD",
        "FRUT",
        "FISH",
    ],
}

# rather than using disallowed classes (can cause breakage), specific labels are disallowed
disallowed_refits_by_label = {
    "non_dump_bulk": [
        "WOOD",
        "SGCN",
        "FICR",
        "BDMT",
        "WDPR",
        "GRAI",
        "WHEA",
        "CERE",
        "MAIZ",
        "FRUT",
        "BEAN",
        "CMNT",
        "CTCD",
        "FERT",
        "OLSD",
        "SUGR",
        "TOFF",
        "URAN",
        "CBLK",
        "PLAS",
        "BAKE",
    ],
    # used to exclude from standard tankers
    "non_generic_liquids": [
        "MILK",
        "WATR",
        "BEER",
        "FOOD",
        "EOIL",
        "O2__",
        "CHLO",
    ],
    "non_flatbed_freight": [
        "FOOD",
        "FISH",
        "LVST",
        "FRUT",
        "BEER",
        "MILK",
        "JAVA",
        "SUGR",
        "NUTS",
        "EOIL",
        "BOOM",
        "FERT",
        "PLAS",
        "CBLK",
    ],
    "non_freight_special_cases": ["TOUR"],
}

# cascading lists of default cargos, if the first cargo(s) are not available, all will be tried in order
# avoids an issue where default cargo was weird for, e.g. some FIRS economies
# don't conflate this with general refittability, they're different concerns ;)
# vehicle classes can also just provide their own list locally, using this is convenient, not obligatory
# !! the names of these deliberately don't match to the names of the vehicle types in a specific grf, as each grf will use these differently to suit vehicle types
default_cargos = {
    "box": ["GOOD", "TYRE", "GLAS", "VPTS", "BOOM"],
    "box_curtain_side": ["VBOD", "BDMT", "FRUT", "FERT", "WDPR", "GOOD"],
    "box_goods": ["GOOD", "GLAS", "FRUT", "BOOM"],
    "box_intermodal": ["POWR", "GOOD", "PAPR"],
    "box_sliding_wall": ["VENG", "BOOM", "PAPR", "JAVA", "GOOD"],
    "box_vehicle_parts": ["VPTS", "PAPR", "RUBR", "STEL", "WOOL", "GOOD"],
    "bulkhead": ["STCB", "PIPE", "STPP", "WDPR", "ALUM", "ZINC", "STEL", "COPR"],
    "coil": ["STST", "STAL", "STEL"],
    "coil_covered": ["STSH", "STEL"],
    "covered_ag": ["GRAI", "MAIZ", "BEAN", "NUTS", "FERT", "QLME"],
    "covered_chemical": ["RFPR", "POTA", "PHOS", "SALT", "SAND"],
    "covered_mineral": ["QLME", "SALT", "PHOS", "POTA", "SAND", "KAOL", "NITR"],
    "covered_pellet": ["PLAS", "RUBR", "KAOL", "FERT", "SAND", "SASH", "BEAN"],
    "covered_roller_roof": ["KAOL", "QLME", "SALT"],
    "cryo_gases": ["O2__", "CHLO"],
    "dump": ["MNO2", "FECR", "NITR", "PHOS", "SAND", "GRVL"],
    "dump_aggregates": ["LIME", "GRVL", "SAND", "CLAY"],
    "dump_high_sides": ["COKE", "PEAT", "COAL", "WDCH"],
    "dump_ore": ["IORE", "PHOS", "PORE", "CORE"],
    "dump_scrap": ["SCMT", "COAL"],
    "edibles_tank": ["WATR", "MILK", "BEER"],
    # ENSP was tried as default for express, but confusing when attached express cars for mail to pax trains
    "express": [
        "MAIL",
        "ENSP",
        "FMSP",
        "GOOD",
        "FOOD",
    ],
    "farm_products_box": ["FRUT", "BEAN", "CASS", "JAVA", "NUTS"],
    "farm_products_hopper": [
        "MAIZ",
        "GRAI",
        "WHEA",
        "CERE",
        "SGBT",
        "OLSD",
        "CASS",
        "NUTS",
    ],
    "flat": ["ALUM", "WDPR", "STEL", "COPR", "METL"],
    # possibly sliding roof shouldn't be flat at all?
    "flat_sliding_roof": [
        "ZINC",
        "ALUM",
        "WOOL",
        "BDMT",
    ],
    # possibly tarpaulin roof shouldn't be flat at all?
    "flat_tarpaulin_roof": [
        "STAL",
        "PAPR",
        "FERT",
        "WOOL",
        "FMSP",
        "WDPR",
    ],
    # fruit_veg should be deprecated
    "fruit_veg": ["FRUT", "BEAN", "CASS", "JAVA", "NUTS"],
    "hopper_coal": ["COAL", "COKE", "NITR", "POTA"],
    "hopper_ore": ["IORE", "CORE", "PORE", "PHOS", "COKE"],
    "hopper_rock": ["LIME", "GRVL", "SAND", "PORE", "SALT", "IORE", "CORE"],
    "long_products": ["STSE", "WOOD", "PIPE", "STPP", "STEL"],
    "mail": ["MAIL"],
    "metal": ["STEL", "COPR"],
    "open": ["GOOD", "STWR", "WDPR"],
    "pax": ["PASS"],
    "plate": ["CSTI", "IRON", "ZINC", "METL", "STEL", "COPR", "WDPR"],
    "product_tank": ["ACID", "RFPR", "CHLO"],
    "reefer": ["FOOD"],
    "silo_cement": ["CMNT", "BDMT", "QLME"],
    "silo_chemical": ["SASH", "RFPR", "QLME", "SAND", "FMSP"],
    "supplies": ["ENSP"],
    "tank": ["OIL_", "CTAR", "SULP", "KAOL", "RUBR"],
}


# chameleon templating goes faster if a cache dir is used; this specifies which dir is cache dir
chameleon_cache_dir = ".chameleon_cache"

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir = "generated"

# this is for nml, don't need to use python path module here
graphics_path = generated_files_dir + "/graphics/"

# OpenTTD's max date
max_game_date = 5000001

# mailbags are < 1t, multiply capacity appropriately
mail_multiplier = 2

# Graphics Constants
# ------------------

# colour defaults
CC1 = 198
CC2 = 80

# locations of the bounding boxes for (piece) cargo spritesheets
cargo_spritesheet_bounding_boxes_base = (
    (10, 10, 18, 36),
    (22, 10, 44, 26),
    (48, 10, 80, 22),
    (84, 10, 106, 26),
)

# Piece maps
# vehicle types are mapped to specific cargo sprites
# 1. provides predictable order for cargo rows (by arranging in list), required for nml template to match spritesheet
# 2. this permits fine-grained control, e.g. cargos that can only go in open vehicles, outsized cargo that needs flats etc
# also supports multiple cargo sprite types to suit vehicle, e.g. piled fruit, fruit in crates etc
# keep alphabetised for general quality-of-life
piece_vehicle_type_to_sprites_maps = {
    # tarps_grey_1 for DFLT
    "coil": [
        "copper_coils_eye_longitudinal_1",
        "steel_coils_eye_longitudinal_1",
        "tarps_grey_1",
    ],
    "flat": [
        "barrels_silver_1",
        "copper_coils_eye_to_sky_1",
        "crates_1",
        "ingots_1",
        "logs_1",
        "lumber_planks_1",
        "paper_coils_eye_to_sky_1",
        "pipes_1",
        "steel_coils_eye_to_sky_1",
        "steel_slab_1",
        "steel_wire_rod_1",
        "tarps_grey_1",
        "tarps_blue_1",
        "tarps_gold_1",
        "tarps_red_1",
    ],
    # tarps_grey_1 for DFLT
    "long_products": [
        "ingots_1",
        "logs_1",
        "lumber_planks_1",
        "pipes_1",
        "steel_slab_1",
        "steel_wire_rod_1",
        "tarps_grey_1",
    ],
    "open": [
        "barrels_silver_1",
        "coffee_1",
        "copper_coils_eye_to_sky_1",
        "crates_1",
        "fruit_1",
        "ingots_1",
        "logs_1",
        "lumber_planks_1",
        "nuts_1",
        "paper_coils_eye_to_sky_1",
        "pipes_1",
        "steel_coils_eye_to_sky_1",
        "steel_slab_1",
        "steel_wire_rod_1",
        "sugarcane_1",
        "tarps_grey_1",
        "tarps_blue_1",
        "tarps_gold_1",
        "tarps_red_1",
    ],
    "tree_length_logs": ["logs_2"],
}

# cargo labels can be repeated for different sprites, they'll be used selectively by vehicle types and/or randomised as appropriate
# keep alphabetised for general quality-of-life
# DFLT label is a hack to support cargos with no specific sprites (including unknown cargos), and should not be added to cargo translation table
piece_sprites_to_cargo_labels_maps = {
    "barrels_silver_1": [
        "BEER",
        "DYES",
        "EOIL",
        "MILK",
        "OIL_",
        "PETR",
        "RFPR",
        "WATR",
    ],
    "coffee_1": ["JAVA"],
    "copper_coils_eye_longitudinal_1": ["COPR"],
    "copper_coils_eye_to_sky_1": ["COPR"],
    "crates_1": ["GOOD"],
    "fruit_1": ["FRUT"],
    "ingots_1": ["ALUM", "ZINC"],
    "logs_1": ["WOOD"],
    # logs_2 is intended for vehicles that *only* use the log sprite, so just provide DFLT to avoid duplicate warnings from nmlc
    "logs_2": ["DFLT"],
    "lumber_planks_1": ["WDPR"],
    "nuts_1": ["NUTS"],
    "paper_coils_eye_to_sky_1": ["PAPR"],
    "pipes_1": ["PIPE", "STPP"],
    "sugarcane_1": ["SGCN"],
    "steel_coils_eye_longitudinal_1": ["STEL", "METL", "STAL", "STCB", "STST", "STSH"],
    "steel_coils_eye_to_sky_1": ["STEL", "METL", "STSH"],
    "steel_slab_1": ["STAL", "STCB", "STST"],
    "steel_wire_rod_1": ["STWR"],
    "tarps_blue_1": ["FMSP"],
    "tarps_gold_1": ["ENSP"],
    "tarps_red_1": ["BDMT"],
    # see note on use of DFLT above
    "tarps_grey_1": ["DFLT"],
}

# Tanker recolour maps
# DFLT label is a hack to support cargos with no specific sprites (including unknown cargos), and should not be added to cargo translation table
# the extended format includes information for intermodal that isn't needed in common cases
# this is parsed and the intermodal information is dropped for tanker_livery_recolour_maps
tanker_livery_recolour_maps_extended = (
    (
        "OIL_",
        # second value is body recolour map for intermodal bulk containers
        "1CC",
        {136: 1, 137: 2, 138: 3, 139: 4, 140: 5, 141: 6, 142: 7, 143: 8},
        # weathered variant
        {136: 104, 137: 1, 138: 2, 139: 3, 140: 4, 141: 5, 142: 6, 143: 7},
    ),
    (
        "CTAR",
        "1CC",
        {136: 104, 137: 1, 138: 2, 139: 3, 140: 4, 141: 5, 142: 6, 143: 7},
        # weathered variant
        {136: 70, 137: 104, 138: 1, 139: 2, 140: 3, 141: 4, 142: 5, 143: 6},
    ),
    # see note on DFLT above
    (
        "DFLT",
        "2CC",
        {
            136: 198,
            137: 199,
            138: 200,
            139: 201,
            140: 202,
            141: 203,
            142: 204,
            143: 205,
        },
        # weathered variant
        {
            136: 198,
            137: 199,
            138: 200,
            139: 201,
            140: 202,
            141: 203,
            142: 204,
            143: 205,
        },
    ),
    (
        "SULP",
        "1CC",
        {136: 62, 137: 63, 138: 64, 139: 65, 140: 66, 141: 67, 142: 68, 143: 69},
        # weathered variant
        {136: 62, 137: 63, 138: 64, 139: 193, 140: 194, 141: 50, 142: 51, 143: 52},
    ),
    # RFPR deliberately 2CC to allow combining with 1CC livery details
    (
        "RFPR",
        "1CC",
        {136: 80, 137: 81, 138: 82, 139: 83, 140: 84, 141: 85, 142: 86, 143: 87},
        # weathered variant
        {136: 80, 137: 81, 138: 82, 139: 83, 140: 84, 141: 85, 142: 86, 143: 87},
    ),
    (
        "RUBR",
        "1CC",
        {136: 40, 137: 41, 138: 42, 139: 43, 140: 44, 141: 45, 142: 46, 143: 47},
        # weathered variant
        {136: 71, 137: 72, 138: 73, 139: 43, 140: 44, 141: 76, 142: 77, 143: 47},
    ),
    (
        "PETR",
        "1CC",
        {136: 16, 137: 17, 138: 18, 139: 19, 140: 20, 141: 21, 142: 22, 143: 23},
        # weathered variant
        {136: 16, 137: 5, 138: 6, 139: 8, 140: 9, 141: 21, 142: 22, 143: 23},
    ),
)

tanker_livery_recolour_maps = [
    (i[0], i[2]) for i in tanker_livery_recolour_maps_extended
]
tanker_livery_recolour_maps_weathered = [
    (i[0], i[3]) for i in tanker_livery_recolour_maps_extended
]
# drop the weathered variant for containers, the container handling expects a 3-tuple only (oof)
tanker_livery_recolour_maps_containers = [
    (i[0], i[1], i[2]) for i in tanker_livery_recolour_maps_extended
]
# Bulk
# keep cargos in alphabetical order for ease of reading
# the extended format includes information for intermodal that isn't needed in common cases
# this is parsed and the intermodal information is dropped for bulk_cargo_recolour_maps
# SCMT *is* bulk cargo in this set, realism is not relevant here, went back and forth on this a few times :P
bulk_cargo_recolour_maps_extended = (
    (
        "AORE",
        # second value is body recolour map for intermodal bulk containers
        "1CC",
        {170: 122, 171: 123, 172: 74, 173: 125, 174: 162, 175: 126, 176: 78},
    ),
    ("CASS", "1CC", {170: 53, 171: 54, 172: 55, 173: 56, 174: 57, 175: 58, 176: 59}),
    ("CLAY", "1CC", {170: 55, 171: 56, 172: 57, 173: 77, 174: 78, 175: 79, 176: 80}),
    ("COAL", "grey", {170: 1, 171: 1, 172: 2, 173: 2, 174: 3, 175: 4, 176: 5}),
    ("COKE", "red", {170: 1, 171: 1, 172: 2, 173: 2, 174: 3, 175: 4, 176: 5}),
    ("CORE", "2CC", {170: 1, 171: 32, 172: 25, 173: 27, 174: 34, 175: 56, 176: 59}),
    ("GRVL", "1CC", {170: 6, 171: 4, 172: 7, 173: 8, 174: 21, 175: 11, 176: 12}),
    (
        "IORE",
        "1CC",
        {170: 75, 171: 76, 172: 123, 173: 122, 174: 124, 175: 74, 176: 104},
    ),
    ("LIME", "1CC", {170: 35, 171: 58, 172: 36, 173: 37, 174: 38, 175: 38, 176: 39}),
    ("KAOL", "1CC", {170: 11, 171: 12, 172: 13, 173: 14, 174: 14, 175: 15, 176: 15}),
    ("MNO2", "1CC", {170: 1, 171: 16, 172: 3, 173: 17, 174: 18, 175: 19, 176: 20}),
    ("NITR", "1CC", {170: 37, 171: 38, 172: 38, 173: 39, 174: 39, 175: 69, 176: 69}),
    (
        "PEAT",
        "1CC",
        {170: 104, 171: 105, 172: 106, 173: 107, 174: 108, 175: 24, 176: 25},
    ),
    ("PHOS", "1CC", {170: 63, 171: 64, 172: 192, 173: 65, 174: 193, 175: 64, 176: 194}),
    ("PORE", "1CC", {170: 71, 171: 72, 172: 73, 173: 33, 174: 34, 175: 63, 176: 64}),
    ("POTA", "1CC", {170: 63, 171: 64, 172: 192, 173: 65, 174: 193, 175: 64, 176: 194}),
    ("SALT", "red", {170: 58, 171: 12, 172: 13, 173: 14, 174: 14, 175: 15, 176: 15}),
    (
        "SAND",
        "2CC",
        {170: 108, 171: 64, 172: 65, 173: 197, 174: 36, 175: 196, 176: 197},
    ),
    ("SASH", "1CC", {170: 11, 171: 12, 172: 13, 173: 14, 174: 14, 175: 15, 176: 15}),
    ("SCMT", "1CC", {170: 104, 171: 3, 172: 2, 173: 70, 174: 71, 175: 72, 176: 3}),
    ("SGBT", "1CC", {170: 60, 171: 53, 172: 54, 173: 55, 174: 56, 175: 57, 176: 58}),
    ("SLAG", "1CC", {170: 24, 171: 3, 172: 2, 173: 3, 174: 4, 175: 5, 176: 5}),
    ("SULP", "1CC", {170: 65, 171: 67, 172: 66, 173: 67, 174: 68, 175: 69, 176: 69}),
    (
        "WDCH",
        "2CC",
        {170: 108, 171: 64, 172: 65, 173: 197, 174: 36, 175: 196, 176: 197},
    ),
)

bulk_cargo_recolour_maps = [(i[0], i[2]) for i in bulk_cargo_recolour_maps_extended]

chemicals_tanker_livery_recolour_maps_extended = (
    (
        "DFLT",
        "1CC",
        {
            136: CC1,
            137: CC1 + 1,
            138: CC1 + 2,
            139: CC1 + 3,
            140: CC1 + 4,
            141: CC1 + 5,
            142: CC1 + 6,
            143: CC1 + 7,
        },
    ),
)

chemicals_tanker_livery_recolour_maps = [
    (i[0], i[2]) for i in chemicals_tanker_livery_recolour_maps_extended
]

cryo_tanker_livery_recolour_maps_extended = (
    (
        "DFLT",
        "1CC",
        {136: 5, 137: 7, 138: 9, 139: 11, 140: 12, 141: 13, 142: 14, 143: 15},
        # weathered
        {136: 34, 137: 7, 138: 9, 139: 11, 140: 12, 141: 38, 142: 14, 143: 15},
    ),
    (
        "CHLO",
        "1CC",
        {
            136: 154,
            137: 155,
            138: 156,
            139: 157,
            140: 158,
            141: 159,
            142: 160,
            143: 161,
        },
        # weathered
        {
            136: 96,
            137: 155,
            138: 156,
            139: 157,
            140: 158,
            141: 151,
            142: 152,
            143: 161,
        },
    ),
)

cryo_tanker_livery_recolour_maps = [
    (i[0], i[2]) for i in cryo_tanker_livery_recolour_maps_extended
]
cryo_tanker_livery_recolour_maps_weathered = [
    (i[0], i[3]) for i in cryo_tanker_livery_recolour_maps_extended
]
cryo_tanker_livery_recolour_maps_containers = [
    (i[0], i[1], i[2]) for i in cryo_tanker_livery_recolour_maps_extended
]

# only intended for intermodal containers, curtain side vehicles will be CC
curtain_side_livery_recolour_maps_extended = (
    ("DFLT", "1CC", {}),
    ("TYRE", "black", {}),
    ("VENG", "grey", {}),
    ("VPTS", "2CC", {}),
)

curtain_side_livery_recolour_maps = [
    (i[0], i[2]) for i in curtain_side_livery_recolour_maps_extended
]

# intermodal mapping of types to cargos with recolour options
# first result is known refits which will fallback to xxxxx_DFLT
# second result is known cargo sprites / livery recolours, which will map explicitly
container_recolour_cargo_maps = (
    (
        "box",
        ([], []),
    ),  # box currently generic, and is fallback for all unknown cargos / classes
    ("bulk", ([], bulk_cargo_recolour_maps)),
    (
        "chemicals_tank",
        (allowed_refits_by_label["chemicals"], chemicals_tanker_livery_recolour_maps),
    ),
    (
        "cryo_tank",
        (allowed_refits_by_label["cryo_gases"], cryo_tanker_livery_recolour_maps),
    ),
    (
        "curtain_side",
        (
            # this single label is a dirty trick to stop warnings about unused DFLT spritesets
            ["VBOD"],
            curtain_side_livery_recolour_maps,
        ),
    ),
    ("edibles_tank", (allowed_refits_by_label["edible_liquids"], [])),
    (
        "livestock",
        # one label only - extend if other livestock labels added in future
        (["LVST"], []),
    ),
    ("reefer", (allowed_refits_by_label["reefer"], [])),
    ("tank", ([], tanker_livery_recolour_maps)),
    (
        "wood",
        # one label only - note that wood container sprites are slightly different to stake flatrack
        (["WOOD"], []),
    ),
)

# intermodal flatracks use selected entries from piece_sprites_to_cargo_labels_maps
# for intermodal, we don't always want to use a flatrack with visible cargo, even if the sprites are available; in some cases a box, tank etc is better
# for simplicity of maintenance though, we do just use all the cargo labels for a specific type of cargo sprite
container_piece_cargo_maps = {
    "ingots_1": piece_sprites_to_cargo_labels_maps["ingots_1"],
    "pipes_1": piece_sprites_to_cargo_labels_maps["pipes_1"],
    "steel_slab_1": piece_sprites_to_cargo_labels_maps["steel_slab_1"],
}

# indexes into the DOS palette for a company colour name
# find these from https://github.com/frosch123/TTDViewer/blob/master/src/recolor.xml#L186
company_colour_maps = {
    "COLOUR_DARK_BLUE": (198, 199, 200, 201, 202, 203, 204, 205),
    "COLOUR_PALE_GREEN": (96, 97, 98, 99, 100, 101, 102, 103),
    "COLOUR_PINK": (42, 43, 44, 45, 46, 47, 48, 49),
    "COLOUR_YELLOW": (62, 63, 64, 65, 66, 67, 68, 69),
    "COLOUR_RED": (179, 180, 181, 182, 183, 164, 165, 166),
    "COLOUR_LIGHT_BLUE": (154, 155, 156, 157, 158, 159, 160, 161),
    "COLOUR_GREEN": (82, 83, 84, 85, 206, 207, 208, 209),
    "COLOUR_DARK_GREEN": (88, 89, 90, 91, 92, 93, 94, 95),
    "COLOUR_BLUE": (146, 147, 148, 149, 150, 151, 152, 153),
    "COLOUR_CREAM": (114, 115, 116, 117, 118, 119, 120, 121),
    "COLOUR_MAUVE": (128, 129, 130, 131, 132, 133, 134, 135),
    "COLOUR_PURPLE": (136, 137, 138, 139, 140, 141, 142, 143),
    "COLOUR_ORANGE": (64, 192, 193, 194, 195, 196, 197, 39),
    "COLOUR_BROWN": (32, 33, 34, 35, 36, 37, 38, 39),
    "COLOUR_GREY": (4, 5, 6, 7, 8, 9, 10, 11),
    "COLOUR_WHITE": (8, 9, 10, 11, 12, 13, 14, 15),
}
