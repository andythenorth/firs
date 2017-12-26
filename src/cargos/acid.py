from cargo import Cargo

cargo = Cargo(id='acid',
              type_name='string(STR_CARGO_NAME_ACID)',
              unit_name='string(STR_CARGO_NAME_ACID)',
              type_abbreviation='string(STR_CID_ACID)',
              sprite='NEW_CARGO_SPRITE',
              weight='1.5',  # extra realism, per forum suggestion Nov 2017
              cargo_payment_list_colour='184',
              is_freight='1',
              cargo_classes='bitmask(CC_LIQUID, CC_HAZARDOUS)',
              cargo_label='ACID',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='80',
              items_of_cargo='string(STR_CARGO_UNIT_ACID)',
              penalty_lowerbound='30',
              single_penalty_length='255',
              price_factor='109',
              capacity_multiplier='1',
              icon_indices=(4, 4))
