"""
This file is generated from the Polar Fox project.
Don't make changes here, make them in the Polar Fox project and redistribute.
Any changes made here are liable to be over-written.
"""

# used to construct the cargo table automatically
# ! order is significant ! - openttd will cascade through default cargos in the order specified by the cargo table
cargo_labels = ['PASS', # pax first
                'TOUR',
                # "the mail must get through"
                'MAIL',
                # all other cargos - append new ones to end, don't change order
                'COAL',
                'IORE',
                'GRVL',
                'SAND',
                'AORE',
                'CORE',
                'CLAY',
                'SCMT',
                'WOOD',
                'LIME',
                'GOOD',
                'FOOD',
                'STEL',
                'FMSP',
                'ENSP',
                'BEER',
                'BDMT',
                'MNSP',
                'PAPR',
                'WDPR',
                'COPR',
                'DYES',
                'OIL_',
                'RFPR',
                'PETR',
                'PLAS',
                'WATR',
                'FISH',
                'CERE',
                'FICR',
                'FRVG',
                'FRUT',
                'GRAI',
                'LVST',
                'MAIZ',
                'MILK',
                'RUBR',
                'SGBT',
                'SGCN',
                'WHEA',
                'WOOL',
                'OLSD',
                'SUGR',
                'JAVA',
                'BEAN',
                'NITR',
                'VEHI',
                'EOIL',
                'NUTS',
                'CASS',
                'MNO2',
                'PHOS',
                'POTA',
                'PORE',
                'IRON',
                'NICK',
                'SLAG',
                'QLME',
                'BOOM',
                'METL',
                'SULP',
                'SASH',
                'CMNT',
                'COKE',
                'KAOL',
                'FERT',
                'PIPE',
                'SALT',
                'CBLK',
                'CHLO',
                'VPTS',
                'ACID',
                'ALUM',
                'CTCD',
                'TOFF',
                'URAN',
                'CTAR',
                'O2__',
                'STAL',
                'STCB',
                'STST',
                'CSTI',
                'PEAT',
                'ZINC',
                'TYRE',
                'VBOD',
                'VENG',
                'FECR',
                'GLAS',
                'POWR',
                'STSH',
                #
                'NULL']

# shared lists of allowed classes, shared across multiple vehicle types
base_refits_by_class = {'empty': [],
                        'all_freight': ['CC_BULK', 'CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_LIQUID', 'CC_ARMOURED', 'CC_REFRIGERATED', 'CC_COVERED', 'CC_NON_POURABLE'],
                        'pax': ['CC_PASSENGERS'],
                        'mail': ['CC_MAIL'],
                        'liquids': ['CC_LIQUID'],
                        'packaged_freight': ['CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_ARMOURED', 'CC_LIQUID'],
                        'flatbed_freight': ['CC_PIECE_GOODS'],
                        'dump_freight': ['CC_BULK'],
                        'covered_hopper_freight': [], # explicit allowal by label instead
                        'refrigerated_freight': ['CC_REFRIGERATED'],
                        'express_freight': ['CC_EXPRESS','CC_ARMOURED']}

# generally we want to allow refit on classes, and disallow on labels (see disallowed_refits_by_label)
# BUT for _some_ specialist vehicle types, it's simpler to just allow refit by label
allowed_refits_by_label = {'edible_liquids': ['MILK', 'WATR', 'BEER', 'FOOD', 'EOIL'],
                           'box_freight': ['MAIL', 'GRAI', 'WHEA', 'MAIZ', 'FRUT', 'BEAN', 'NITR'], # box cars get some extended cargos
                           'chemicals': ['ACID', 'RFPR', 'CHLO'], # seems to be used by intermodal, otherwise chemicals tankers are deprecated in favour of product tankers
                           'covered_hoppers': ['GRAI', 'WHEA', 'MAIZ', 'SUGR', 'FMSP', 'RFPR', 'CLAY', 'BDMT',
                                               'BEAN', 'NITR', 'RUBR', 'SAND', 'POTA', 'QLME', 'SASH', 'CMNT',
                                               'KAOL', 'FERT', 'SALT', 'PLAS'], # not CBLK, gets dedicated vehicles or box
                           'cryo_gases': ['CHLO', 'O2__'],
                           'reefer': ['FOOD', 'FRUT', 'FISH'], # hax for intermodal container sprite selection - reefer car refits work just fine using CC_REFRIGERATED
                           'fruit_veg': ['FRUT', 'BEAN', 'CASS', 'JAVA', 'NUTS'],
                           'cold_metal': ['STEL', 'METL', 'STCB', 'STAL', 'STST', 'COPR', 'STSH']}

# rather than using disallowed classes (can cause breakage), specific labels are disallowed
disallowed_refits_by_label = {'non_dump_bulk': ['WOOD', 'SGCN', 'FICR', 'BDMT', 'WDPR', 'GRAI', 'WHEA', 'CERE', 'MAIZ', 'FRUT', 'BEAN', 'CMNT',
                                                'CTCD', 'FERT', 'OLSD', 'SUGR', 'TOFF', 'URAN', 'CBLK', 'PLAS'],
                              'non_generic_liquids': ['MILK', 'WATR', 'BEER', 'FOOD', 'EOIL', 'O2__', 'CHLO'], # used to exclude from standard tankers
                              'non_flatbed_freight': ['FOOD', 'FISH', 'LVST', 'FRUT', 'BEER', 'MILK', 'JAVA', 'SUGR', 'NUTS', 'EOIL', 'BOOM',
                                                      'FERT', 'PLAS', 'CBLK'],
                              'non_freight_special_cases': ['TOUR']}

# cascading lists of default cargos, if the first cargo(s) are not available, all will be tried in order
# avoids an issue where default cargo was weird for, e.g. some FIRS economies
# don't conflate this with general refittability, they're different concerns ;)
# vehicle classes can also just provide their own list locally, using this is convenient, not obligatory
default_cargos = {'box': ['GOOD', 'VPTS', 'FOOD'],
                  'coal_hopper': ['COAL', 'COKE', 'NITR', 'POTA'],
                  'cryo_gases': ['O2__', 'CHLO'],
                  'covered_hopper': ['SAND', 'KAOL', 'PLAS'],
                  'dump': ['MNO2', 'FECR', 'NITR', 'PHOS', 'SAND', 'GRVL'],
                  'dump_high_sides': ['COKE', 'PEAT', 'COAL'],
                  'dump_scrap': ['SCMT', 'COAL'],
                  'edibles_tank': ['WATR', 'MILK', 'BEER'],
                  'express': ['MAIL', 'ENSP', 'FMSP', 'GOOD', 'FOOD'], # ENSP was tried as default, but confusing when attached express cars for mail to pax trains
                  'flat': ['STEL', 'STCB', 'COPR', 'METL'],
                  'fruit_veg': ['FRUT', 'BEAN', 'CASS', 'JAVA', 'NUTS'],
                  'grain_hopper': ['GRAI', 'PLAS'],
                  'hopper': ['LIME', 'GRVL', 'SAND', 'PORE', 'SALT', 'IORE', 'CORE'],
                  # intermodal, uses box
                  'mail': ['MAIL'],
                  'metal': ['STEL', 'COPR'],
                  'open': ['GOOD'],
                  'ore_hopper': ['IORE', 'CORE', 'PORE', 'PHOS', 'COKE'],
                  'pax': ['PASS'],
                  'plate': ['IRON', 'CSTI', 'ZINC', 'METL'],
                  'product_tank': ['ACID', 'RFPR', 'CHLO'],
                  'reefer': ['FOOD'],
                  'silo': ['CMNT', 'BDMT', 'RFPR', 'QLME', 'FMSP'],
                  'stake': ['WOOD'],
                  'supplies': ['ENSP'],
                  'tank': ['OIL_', 'CTAR', 'SULP', 'KAOL', 'RUBR'],
                  }


# chameleon templating goes faster if a cache dir is used; this specifies which dir is cache dir
chameleon_cache_dir = '.chameleon_cache'

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir = 'generated'

# this is for nml, don't need to use python path module here
graphics_path = generated_files_dir + '/graphics/'

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
cargo_spritesheet_bounding_boxes_base = ((10, 10, 18, 36), (22, 10, 44, 26), (48, 10, 80, 22), (84, 10, 106, 26))

# Piece maps
# vehicle types are mapped to specific cargo sprites
# 1. provides predictable order for cargo rows (by arranging in list), required for nml template to match spritesheet
# 2. this permits fine-grained control, e.g. cargos that can only go in open vehicles, outsized cargo that needs flats etc
# also supports multiple cargo sprite types to suit vehicle, e.g. piled fruit, fruit in crates etc
# keep alphabetised for general quality-of-life
piece_vehicle_type_to_sprites_maps = {'flat': ['barrels_silver', 'copper_coils', 'crates_1', 'logs',
                                              'lumber_planks', 'paper_coils', 'steel_coils',
                                              'tarps_2cc_1', 'tarps_blue_1', 'tarps_gold_1', 'tarps_red_1'],
                                      'open':['barrels_silver', 'coffee', 'copper_coils', 'crates_1', 'fruit', 'logs',
                                              'lumber_planks', 'nuts', 'paper_coils', 'steel_coils',
                                              'tarps_2cc_1', 'tarps_blue_1', 'tarps_gold_1', 'tarps_red_1'],
                                      'stake':['logs', 'lumber_planks', 'tarps_2cc_1'] # tarps_2cc_1 for DFLT
                                      }

# cargo labels can be repeated for different sprites, they'll be used selectively by vehicle types and/or randomised as appropriate
# keep alphabetised for general quality-of-life
# DFLT label is a hack to support cargos with no specific sprites (including unknown cargos), and should not be added to cargo translation table
piece_sprites_to_cargo_labels_maps = {'barrels_silver': ['BEER', 'DYES', 'EOIL', 'MILK', 'OIL_', 'PETR', 'RFPR', 'WATR'],
                                      'coffee': ['JAVA'],
                                      'copper_coils': ['COPR'],
                                      'crates_1': ['GOOD'],
                                      'fruit': ['FRUT'],
                                      'logs': ['WOOD'],
                                      'lumber_planks': ['WDPR'],
                                      'nuts': ['NUTS'],
                                      'paper_coils': ['PAPR'],
                                      'steel_coils': ['STEL', 'METL', 'STAL', 'STCB', 'STST'],
                                      'tarps_blue_1': ['FMSP'],
                                      'tarps_gold_1': ['ENSP'],
                                      'tarps_red_1': ['BDMT'],
                                      'tarps_2cc_1': ['DFLT']}  # see note on use of DFLT above

# Tanker recolour maps
# DFLT label is a hack to support cargos with no specific sprites (including unknown cargos), and should not be added to cargo translation table
# the extended format includes information for intermodal that isn't needed in common cases
# this is parsed and the intermodal information is dropped for tanker_livery_recolour_maps
tanker_livery_recolour_maps_extended = (("OIL_", "1CC", # second value is body recolour map for intermodal bulk containers
                                        {136: 1, 137: 2, 138: 3, 139: 4, 140: 5, 141: 6, 142: 7, 143: 8}),
                                       ("CTAR", "1CC",
                                        {136: 1, 137: 2, 138: 3, 139: 4, 140: 5, 141: 6, 142: 7, 143: 8}),
                                       # see note on DFLT above
                                       ("DFLT",  "2CC",
                                        {136: 198, 137: 199, 138: 200, 139: 201, 140: 202, 141: 203, 142: 204, 143: 205}),
                                       ("SULP",  "1CC",
                                        {136: 62, 137: 63, 138: 64, 139: 65, 140: 66, 141: 67, 142: 68, 143: 69}),
                                       # RFPR deliberately 2CC to allow combining with 1CC livery details
                                       ("RFPR",  "1CC",
                                        {136: 80, 137: 81, 138: 82, 139: 83, 140: 84, 141: 85, 142: 86, 143: 87}),
                                       ("RUBR",  "1CC",
                                        {136: 40, 137: 41, 138: 42, 139: 43, 140: 44, 141: 45, 142: 46, 143: 47}),
                                       ("PETR", "1CC",
                                        {136: 16, 137: 17, 138: 18, 139: 19, 140: 20, 141: 21, 142: 22, 143: 23}))

tanker_livery_recolour_maps = [(i[0], i[2]) for i in tanker_livery_recolour_maps_extended]

# Bulk
# keep cargos in alphabetical order for ease of reading
# the extended format includes information for intermodal that isn't needed in common cases
# this is parsed and the intermodal information is dropped for bulk_cargo_recolour_maps
# SCMT *is* bulk cargo in this set, realism is not relevant here, went back and forth on this a few times :P
bulk_cargo_recolour_maps_extended = (("AORE", "1CC", # second value is body recolour map for intermodal bulk containers
                                      {170: 42, 171: 123, 172: 74, 173: 125, 174: 162, 175: 126, 176: 78}),
                                     ("CASS", "1CC",
                                      {170: 53, 171: 54, 172: 55, 173: 56, 174: 57, 175: 58, 176: 59}),
                                     ("CLAY", "1CC",
                                      {170: 55, 171: 56, 172: 57, 173: 77, 174: 78, 175: 79, 176: 80}),
                                     ("COAL", "grey",
                                      {170: 1, 171: 1, 172: 2, 173: 2, 174: 3, 175: 4, 176: 5}),
                                     ("COKE", "red",
                                      {170: 1, 171: 1, 172: 2, 173: 2, 174: 3, 175: 4, 176: 5}),
                                     ("CORE", "2CC",
                                      {170: 1, 171: 32, 172: 25, 173: 27, 174: 34, 175: 56, 176: 59}),
                                     ("GRVL", "1CC",
                                      {170: 6, 171: 4, 172: 7, 173: 8, 174: 21, 175: 11, 176: 12}),
                                     ("IORE", "1CC",
                                      {170: 75, 171: 76, 172: 123, 173: 122, 174: 124, 175: 74, 176: 104}),
                                     ("LIME", "1CC",
                                      {170: 35, 171: 58, 172: 36, 173: 37, 174: 38, 175: 38, 176: 39}),
                                     ("KAOL", "1CC",
                                      {170: 11, 171: 12, 172: 13, 173: 14, 174: 14, 175: 15, 176: 15}),
                                     ("MNO2", "1CC",
                                      {170: 1, 171: 16, 172: 3, 173: 17, 174: 18, 175: 19, 176: 20}),
                                     ("NITR", "1CC",
                                      {170: 37, 171: 38, 172: 38, 173: 39, 174: 39, 175: 69, 176: 69}),
                                     ("PHOS", "1CC",
                                      {170: 63, 171: 64, 172: 192, 173: 65, 174: 193, 175: 64, 176: 194}),
                                     ("PORE", "1CC",
                                      {170: 40, 171: 72, 172: 73, 173: 33, 174: 33, 175: 63, 176: 63}),
                                     ("POTA", "1CC",
                                      {170: 63, 171: 64, 172: 192, 173: 65, 174: 193, 175: 64, 176: 194}),
                                     ("SALT", "red",
                                      {170: 58, 171: 12, 172: 13, 173: 14, 174: 14, 175: 15, 176: 15}),
                                     ("SAND", "2CC",
                                      {170: 108, 171: 64, 172: 65, 173: 197, 174: 36, 175: 196, 176: 197}),
                                     ("SASH", "1CC",
                                      {170: 11, 171: 12, 172: 13, 173: 14, 174: 14, 175: 15, 176: 15}),
                                     ("SCMT", "1CC",
                                      {170: 104, 171: 3, 172: 2, 173: 70, 174: 71, 175: 72, 176: 3}),
                                     ("SGBT", "1CC",
                                      {170: 60, 171: 53, 172: 54, 173: 55, 174: 56, 175: 57, 176: 58}),
                                     ("SLAG", "1CC",
                                      {170: 24, 171: 3, 172: 2, 173: 3, 174: 4, 175: 5, 176: 5}),
                                     ("SULP", "1CC",
                                      {170: 65, 171: 67, 172: 66, 173: 67, 174: 68, 175: 69, 176: 69}))

bulk_cargo_recolour_maps = [(i[0], i[2]) for i in bulk_cargo_recolour_maps_extended]

chemicals_tanker_livery_recolour_maps_extended = (("DFLT", "1CC",
                                                   {136: CC1, 137: CC1+1, 138: CC1+2, 139: CC1+3, 140: CC1+4, 141: CC1+5, 142: CC1+6, 143: CC1+7}),)

chemicals_tanker_livery_recolour_maps = [(i[0], i[2]) for i in chemicals_tanker_livery_recolour_maps_extended]

cryo_tanker_livery_recolour_maps_extended = (("DFLT", "1CC",
                                              {136: 5, 137: 7, 138: 9, 139: 11, 140: 12, 141: 13, 142: 14, 143: 15}),
                                             ("CHLO", "1CC",
                                              {136: 154, 137: 155, 138: 157, 139: 158, 140: 159, 141: 159, 142: 160, 143: 161}),)

cryo_tanker_livery_recolour_maps = [(i[0], i[2]) for i in cryo_tanker_livery_recolour_maps_extended]

curtain_side_livery_recolour_maps_extended = (("DFLT", "1CC", {}),
                                              ("TYRE", "black", {}),
                                              ("VENG", "grey", {}),
                                              ("VPTS", "2CC", {}))

curtain_side_livery_recolour_maps = [(i[0], i[2]) for i in curtain_side_livery_recolour_maps_extended]
