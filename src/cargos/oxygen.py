from cargo import Cargo

cargo = Cargo(id='oxygen',
              type_name='string(STR_CARGO_NAME_OXYGEN)',
              unit_name='string(STR_CARGO_NAME_OXYGEN)',
              type_abbreviation='string(STR_CID_OXYGEN)',
              sprite='NEW_CARGO_SPRITE',
              weight='1.0',
              cargo_payment_list_colour='95',
              is_freight='1',
              cargo_classes='bitmask(CC_LIQUID, CC_HAZARDOUS)',
              cargo_label='O2__',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='TTD_STR_LITERS',
              items_of_cargo='string(STR_CARGO_UNIT_OXYGEN)',
              penalty_lowerbound='12',
              single_penalty_length='255',
              price_factor='89',
              capacity_multiplier='1',
              icon_indices=(2, 4))