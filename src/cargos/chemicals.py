from cargo import Cargo

cargo = Cargo(id='chemicals',
              type_name='string(STR_CARGO_NAME_CHEMICALS)',
              unit_name='string(STR_CARGO_NAME_CHEMICALS)',
              type_abbreviation='string(STR_CID_CHEMICALS)',
              sprite='NEW_CARGO_SPRITE',
              weight='1.2',  # extra realism, per forum suggestion Nov 2017
              cargo_payment_list_colour='177',
              is_freight='1',
              cargo_classes='bitmask(CC_LIQUID)',
              cargo_label='RFPR',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='82',
              items_of_cargo='string(STR_CARGO_UNIT_CHEMICALS)',
              penalty_lowerbound='20',
              single_penalty_length='255',
              price_factor='117',
              capacity_multiplier='1',
              icon_indices=(10, 1))
