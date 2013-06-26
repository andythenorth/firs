from cargo import Cargo

cargo = Cargo(id = 'diamonds',
              number = '1',
              type_name = 'TTD_STR_CARGO_PLURAL_DIAMONDS',
              unit_name = 'TTD_STR_CARGO_SINGULAR_DIAMOND',
              type_abbreviation = '144',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '0',
              cargo_payment_list_colour = '0',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_ARMOURED)',
              cargo_label = '"DIAM"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = 'TTD_STR_TONS',
              items_of_cargo = 'TTD_STR_QUANTITY_DIAMONDS',
              penalty_lowerbound = '30',
              single_penalty_length = '255',
              price_factor = '74.2692947388',
              capacity_multiplier = '1',
              icon_indices = (1, 0))

cargo.economy_variations['FIRS']['disabled'] = True
cargo.economy_variations['BASIC_ARCTIC']['disabled'] = True
cargo.economy_variations['BASIC_TROPIC']['disabled'] = True
cargo.economy_variations['BASIC_TEMPERATE']['disabled'] = True
