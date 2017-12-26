from cargo import Cargo

cargo = Cargo(id='vehicles',
              type_name='string(STR_CARGO_NAME_VEHICLES)',
              unit_name='string(STR_CARGO_NAME_VEHICLES)',
              type_abbreviation='string(STR_CID_VEHICLES)',
              sprite='NEW_CARGO_SPRITE',
              weight='1.0',
              cargo_payment_list_colour='141',
              is_freight='1',
              cargo_classes='bitmask(CC_PIECE_GOODS)',
              cargo_label='VEHI',
              town_growth_effect='TOWNGROWTH_WATER',  # intended for desert Steeltown, may not be appropriate in other cases
              town_growth_multiplier='1.0',
              units_of_cargo='84',
              items_of_cargo='string(STR_CARGO_UNIT_VEHICLES)',
              penalty_lowerbound='8',
              single_penalty_length='60',
              price_factor='162',
              capacity_multiplier='1',
              icon_indices=(15, 2))
