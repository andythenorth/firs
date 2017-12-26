from cargo import Cargo

cargo = Cargo(id='packaging',
              type_name='string(STR_CARGO_NAME_PACKAGING)',
              unit_name='string(STR_CARGO_NAME_PACKAGING)',
              type_abbreviation='string(STR_CID_PACKAGING)',
              sprite='NEW_CARGO_SPRITE',
              weight='0.65',
              cargo_payment_list_colour='145',
              is_freight='1',
              cargo_classes='bitmask(CC_EXPRESS, CC_PIECE_GOODS)',
              cargo_label='MNSP',  # MNSP label preserved in FIRS v3 for backwards compatibility, may remove in v4
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='84',
              items_of_cargo='string(STR_CARGO_UNIT_PACKAGING)',
              penalty_lowerbound='16',
              single_penalty_length='120',
              price_factor='127',
              capacity_multiplier='1',
              icon_indices=(7, 1))
