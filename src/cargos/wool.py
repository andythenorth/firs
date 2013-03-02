from firs import Cargo

cargo = Cargo(id = 'wool',
              number = '15',
              type_name = 'string(STR_CARGO_NAME_WOOL)',
              unit_name = 'string(STR_CARGO_NAME_WOOL)',
              type_abbreviation = 'string(STR_CID_WOOL)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '134',
              cargo_payment_list_colour = '134',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_PIECE_GOODS, CC_COVERED)',
              cargo_label = '"WOOL"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '80',
              items_of_cargo = 'string(STR_CARGO_UNIT_WOOL)',
              penalty_lowerbound = '8',
              single_penalty_length = '90',
              price_factor = '105.202674866',
              capacity_multiplier = '1')

cargo.economy_variations['BASIC_TEMPERATE']['disabled'] = True
cargo.economy_variations['BASIC_ARCTIC']['disabled'] = True
