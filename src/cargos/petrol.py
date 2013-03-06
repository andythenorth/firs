from firs import Cargo

cargo = Cargo(id = 'petrol',
              number = '25',
              type_name = 'string(STR_CARGO_NAME_PETROL)',
              unit_name = 'string(STR_CARGO_NAME_PETROL)',
              type_abbreviation = 'string(STR_CID_PETROL)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '0.6875',
              station_list_colour = '175',
              cargo_payment_list_colour = '175',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_LIQUID)',
              cargo_label = '"PETR"',
              town_growth_effect = 'TOWNGROWTH_GOODS',
              town_growth_multiplier = '1.0',
              units_of_cargo = '82',
              items_of_cargo = 'string(STR_CARGO_UNIT_PETROL)',
              penalty_lowerbound = '18',
              single_penalty_length = '255',
              capacity_multiplier = '1',
              price_factor = '126.749038696')

cargo.economy_variations['BASIC_TEMPERATE']['disabled'] = True

