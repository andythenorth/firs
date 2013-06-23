from cargo import Cargo

cargo = Cargo(id = 'sugar',
              number = '20',
              type_name = 'TTD_STR_CARGO_PLURAL_SUGAR',
              unit_name = 'TTD_STR_CARGO_SINGULAR_SUGAR',
              type_abbreviation = 'TTD_STR_ABBREV_SUGAR',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '48',
              cargo_payment_list_colour = '48',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_REFRIGERATED, CC_EXPRESS)',
              cargo_label = '"FOOD"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '94',
              items_of_cargo = 'TTD_STR_QUANTITY_SUGAR',
              penalty_lowerbound = '0',
              single_penalty_length = '24',
              price_factor = '149.803161621',
              capacity_multiplier = '1',
              icon_indices = (12, 0))

cargo.economy_variations['FIRS']['disabled'] = True
cargo.economy_variations['BASIC_ARCTIC']['disabled'] = True
cargo.economy_variations['BASIC_TROPIC']['disabled'] = True
cargo.economy_variations['BASIC_TEMPERATE']['disabled'] = True
