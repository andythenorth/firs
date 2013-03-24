from cargo import Cargo

cargo = Cargo(id = 'plant_fibres',
              number = '22',
              type_name = 'string(STR_CARGO_NAME_FIBRES)',
              unit_name = 'string(STR_CARGO_NAME_FIBRES)',
              type_abbreviation = 'string(STR_CID_FIBRES)',
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
              items_of_cargo = 'string(STR_CARGO_UNIT_FIBRES)',
              penalty_lowerbound = '10',
              single_penalty_length = '36',
              capacity_multiplier = '1',
              price_factor = '107.634544373',
              icon_indices = (3, 1))

cargo.economy_variations['BASIC_TEMPERATE']['disabled'] = True
cargo.economy_variations['BASIC_ARCTIC']['disabled'] = True
cargo.economy_variations['BASIC_TROPIC']['disabled'] = True
