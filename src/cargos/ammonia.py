from cargo import Cargo

cargo = Cargo(id='ammonia',
              type_name='string(STR_CARGO_NAME_AMMONIA)',
              unit_name='string(STR_CARGO_NAME_AMMONIA)',
              type_abbreviation='string(STR_CID_AMMONIA)',
              sprite='NEW_CARGO_SPRITE',
              weight='0.60',  # extra realism per forum suggestion
              cargo_payment_list_colour='189',
              is_freight='1',
              cargo_classes='bitmask(CC_LIQUID, CC_HAZARDOUS)',
              cargo_label='NH3_',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='TTD_STR_LITERS',
              items_of_cargo='string(STR_CARGO_UNIT_AMMONIA)',
              penalty_lowerbound='30',
              single_penalty_length='255',
              price_factor='109',
              capacity_multiplier='1',
              icon_indices=(4, 4))
