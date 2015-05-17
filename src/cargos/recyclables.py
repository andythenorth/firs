from cargo import Cargo

cargo = Cargo(id = 'recyclables',
              type_name = 'string(STR_CARGO_NAME_RECYCLABLES)',
              unit_name = 'string(STR_CARGO_NAME_RECYCLABLES)',
              type_abbreviation = 'string(STR_CID_RECYCLABLES)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '181',
              cargo_payment_list_colour = '181',
              is_freight = '1',
              # eh, are these classes a mistake?  The commit history suggests they were just copied unchanged from WOOL
              cargo_classes = 'bitmask(CC_PIECE_GOODS, CC_COVERED)',
              cargo_label = 'RCYC',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '80',
              items_of_cargo = 'string(STR_CARGO_UNIT_RECYCLABLES)',
              penalty_lowerbound = '10',
              single_penalty_length = '128',
              capacity_multiplier = '1',
              price_factor = '104.570388794',
              icon_indices = (11, 0))





