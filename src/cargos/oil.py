from firs import Cargo

cargo = Cargo(id = 'oil',
              number = '3',
              type_name = '18',
              unit_name = '50',
              type_abbreviation = '146',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '0.875',
              station_list_colour = '172',
              cargo_payment_list_colour = '172',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_LIQUID)',
              cargo_label = '"OIL_"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '82',
              items_of_cargo = '114',
              penalty_lowerbound = '30',
              single_penalty_length = '255',
              price_factor = '93.3108329773',
              capacity_multiplier = '1',
              icon_indices = (3, 0))

cargo.economy_variations['BASIC_TEMPERATE']['disabled'] = True
