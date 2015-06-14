from cargo import Cargo

cargo = Cargo(id = 'metal',
              type_name = 'string(STR_CARGO_NAME_METAL)',
              unit_name = 'string(STR_CARGO_NAME_METAL)',
              type_abbreviation = 'string(STR_CID_METAL)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '10',
              cargo_payment_list_colour = '10',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_PIECE_GOODS)',
              cargo_label = 'STEL', # 'stel' stands in for generic metal; this ensures easy cargo support
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '80',
              items_of_cargo = 'string(STR_CARGO_UNIT_METAL)',
              penalty_lowerbound = '7',
              single_penalty_length = '255',
              capacity_multiplier = '1',
              price_factor = '126.165390015',
              icon_indices = (10, 0))




