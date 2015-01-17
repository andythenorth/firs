from cargo import Cargo

cargo = Cargo(id = 'paper',
              number = '13',
              type_name = 'TTD_STR_CARGO_PLURAL_PAPER',
              unit_name = 'TTD_STR_CARGO_SINGULAR_PAPER',
              type_abbreviation = 'TTD_STR_ABBREV_PAPER',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '48',
              cargo_payment_list_colour = '20',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_PIECE_GOODS)',
              cargo_label = '"PAPR"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = 'TTD_STR_TONS',
              items_of_cargo = 'TTD_STR_QUANTITY_PAPER',
              penalty_lowerbound = '7',
              single_penalty_length = '60',
              price_factor = '134.506702423',
              capacity_multiplier = '1',
              icon_indices = (1, 0))

cargo.economy_variations['FIRS']['disabled'] = True
cargo.economy_variations['BASIC_TEMPERATE']['disabled'] = True
cargo.economy_variations['BASIC_TROPIC']['disabled'] = True
cargo.economy_variations['MISTAH_KURTZ']['disabled'] = True
