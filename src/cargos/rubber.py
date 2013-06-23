from cargo import Cargo

cargo = Cargo(id = 'rubber',
              number = '27',
              type_name = 'TTD_STR_CARGO_PLURAL_RUBBER',
              unit_name = 'TTD_STR_CARGO_SINGULAR_RUBBER',
              type_abbreviation = 'TTD_STR_ABBREV_RUBBER',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '13',
              cargo_payment_list_colour = '13',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_BULK, CC_PIECE_GOODS)',
              cargo_label = '"FICR"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '80',
              items_of_cargo = 'TTD_STR_QUANTITY_RUBBER',
              penalty_lowerbound = '10',
              single_penalty_length = '36',
              capacity_multiplier = '1',
              price_factor = '107.634544373',
              icon_indices = (3, 1))

cargo.economy_variations['FIRS']['disabled'] = True
cargo.economy_variations['BASIC_TEMPERATE']['disabled'] = True
cargo.economy_variations['BASIC_ARCTIC']['disabled'] = True
cargo.economy_variations['BASIC_TROPIC']['disabled'] = True
