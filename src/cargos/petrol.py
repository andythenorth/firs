from cargo import Cargo

# the EN GB lang string for this was changed to 'Petroleum Fuels' Jan 2016, it feels more widely usable as a cargo

cargo = Cargo(id='petrol',
              type_name='string(STR_CARGO_NAME_PETROL)',
              unit_name='string(STR_CARGO_NAME_PETROL)',
              type_abbreviation='string(STR_CID_PETROL)',
              sprite='NEW_CARGO_SPRITE',
              weight='0.8',
              is_freight='1',
              cargo_classes='bitmask(CC_LIQUID)',
              cargo_label='PETR',
              town_growth_effect='TOWNGROWTH_GOODS',
              town_growth_multiplier='1.0',
              units_of_cargo='TTD_STR_LITERS',
              items_of_cargo='string(STR_CARGO_UNIT_PETROL)',
              penalty_lowerbound='18',
              single_penalty_length='255',
              capacity_multiplier='1',
              price_factor=187,
              icon_indices=(12, 1))
