from cargo import Cargo

cargo = Cargo(id='explosives',
              type_name='string(STR_CARGO_NAME_EXPLOSIVES)',
              unit_name='string(STR_CARGO_NAME_EXPLOSIVES)',
              type_abbreviation='string(STR_CID_EXPLOSIVES)',
              sprite='NEW_CARGO_SPRITE',
              weight='0.25',
              cargo_payment_list_colour='182',
              is_freight='1',
              cargo_classes='bitmask(CC_EXPRESS, CC_PIECE_GOODS)',
              cargo_label='BOOM',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='84',
              items_of_cargo='string(STR_CARGO_UNIT_EXPLOSIVES)',
              penalty_lowerbound='6',
              single_penalty_length='36',
              price_factor='154',
              capacity_multiplier='1',
              allow_animated_pixels=True,  # explosives uses fire cycle pixels, by design, so suppress NML pixel warnings
              icon_indices=(2, 3))
