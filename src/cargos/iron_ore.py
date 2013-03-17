from firs import Cargo

cargo = Cargo(id = 'iron_ore',
              number = '8',
              type_name = '23',
              unit_name = '55',
              type_abbreviation = '151',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '181',
              cargo_payment_list_colour = '181',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_BULK)',
              cargo_label = '"IORE"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '87',
              items_of_cargo = '119',
              penalty_lowerbound = '30',
              single_penalty_length = '255',
              price_factor = '75.4852294922',
              capacity_multiplier = '1',
              icon_indices = (9, 0))

cargo.economy_variations['BASIC_ARCTIC']['disabled'] = True
cargo.economy_variations['BASIC_TROPIC']['disabled'] = True
