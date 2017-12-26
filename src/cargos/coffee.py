from cargo import Cargo

cargo = Cargo(id='coffee',
              type_name='string(STR_CARGO_NAME_COFFEE)',
              unit_name='string(STR_CARGO_NAME_COFFEE)',
              type_abbreviation='string(STR_CID_COFFEE)',
              sprite='NEW_CARGO_SPRITE',
              weight='0.25',  # IRL coffee is lighter even than this, but eh
              cargo_payment_list_colour='71',
              is_freight='1',
              cargo_classes='bitmask(CC_PIECE_GOODS, CC_EXPRESS)',
              cargo_label='JAVA',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='80',
              items_of_cargo='string(STR_CARGO_UNIT_COFFEE)',
              penalty_lowerbound='0',
              single_penalty_length='26',
              price_factor='150',
              capacity_multiplier='1',
              icon_indices=(4, 2))
