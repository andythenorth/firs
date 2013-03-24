from cargo import Cargo

cargo = Cargo(id = 'gravel',
              number = '26',
              type_name = 'string(STR_CARGO_NAME_STONE)',
              unit_name = 'string(STR_CARGO_NAME_STONE)',
              type_abbreviation = 'string(STR_CID_STONE)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '16',
              cargo_payment_list_colour = '16',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_BULK)',
              cargo_label = '"GRVL"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '80',
              items_of_cargo = 'string(STR_CARGO_UNIT_STONE)',
              penalty_lowerbound = '30',
              single_penalty_length = '255',
              price_factor = '74.1233825684',
              capacity_multiplier = '1',
              icon_indices = (5, 1))

cargo.economy_variations['BASIC_TEMPERATE']['disabled'] = True
cargo.economy_variations['BASIC_ARCTIC']['disabled'] = True
cargo.economy_variations['BASIC_TROPIC']['disabled'] = True
