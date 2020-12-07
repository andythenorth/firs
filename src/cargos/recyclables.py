from cargo import Cargo

cargo = Cargo(id='recyclables',
              type_name='string(STR_CARGO_NAME_RECYCLABLES)',
              unit_name='string(STR_CARGO_NAME_RECYCLABLES)',
              type_abbreviation='string(STR_CID_RECYCLABLES)',
              sprite='NEW_CARGO_SPRITE',
              weight='1.0',
              is_freight='1',
              cargo_classes='bitmask(CC_BULK, CC_PIECE_GOODS)',
              cargo_label='RCYC',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='TTD_STR_TONS',
              items_of_cargo='string(STR_CARGO_UNIT_RECYCLABLES)',
              penalty_lowerbound='10',
              single_penalty_length='128',
              capacity_multiplier='1',
              price_factor=100,
              icon_indices=(10, 3))
              
