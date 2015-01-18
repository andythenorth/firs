from cargo import Cargo

cargo = Cargo(id = 'beans',
              number = '6',
              type_name = 'string(STR_CARGO_NAME_BEANS)',
              unit_name = 'string(STR_CARGO_NAME_BEANS)',
              type_abbreviation = 'string(STR_CID_BEANS)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '191',
              cargo_payment_list_colour = '191',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_BULK)',
              cargo_label = '"BEAN"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = 'TTD_STR_TONS',
              items_of_cargo = 'string(STR_CARGO_UNIT_BEANS)',
              penalty_lowerbound = '4',
              single_penalty_length = '40',
              price_factor = '116.194725037',
              capacity_multiplier = '1',
              icon_indices = (6, 2))

cargo.economy_variations['FIRS']['disabled'] = True
cargo.economy_variations['BASIC_ARCTIC']['disabled'] = True
cargo.economy_variations['BASIC_TEMPERATE']['disabled'] = True
cargo.economy_variations['MISTAH_KURTZ']['disabled'] = True
