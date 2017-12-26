from cargo import Cargo

# pig iron, although the label implies it could be more generic iron
cargo = Cargo(id='pig_iron',
              type_name='string(STR_CARGO_NAME_PIG_IRON)',
              unit_name='string(STR_CARGO_NAME_PIG_IRON)',
              type_abbreviation='string(STR_CID_PIG_IRON)',
              sprite='NEW_CARGO_SPRITE',
              weight='1.0',
              cargo_payment_list_colour='112',
              is_freight='1',
              cargo_classes='bitmask(CC_PIECE_GOODS)',
              cargo_label='IRON',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='80',
              items_of_cargo='string(STR_CARGO_UNIT_PIG_IRON)',
              penalty_lowerbound='15',
              single_penalty_length='255',
              capacity_multiplier='1',
              price_factor='121',
              icon_indices=(4, 3))
