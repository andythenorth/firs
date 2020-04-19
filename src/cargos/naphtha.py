from cargo import Cargo

# the specific petrochemical feedstock rather than the generic term for petroleum spirits

cargo = Cargo(id='naphtha',
              type_name='string(STR_CARGO_NAME_NAPHTHA)',
              unit_name='string(STR_CARGO_NAME_NAPHTHA)',
              type_abbreviation='string(STR_CID_NAPHTHA)',
              sprite='NEW_CARGO_SPRITE',
              weight='0.8',
              cargo_payment_list_colour='175',
              is_freight='1',
              cargo_classes='bitmask(CC_LIQUID)',
              cargo_label='NAPH',
              town_growth_effect='TOWNGROWTH_GOODS',
              town_growth_multiplier='1.0',
              units_of_cargo='TTD_STR_LITERS',
              items_of_cargo='string(STR_CARGO_UNIT_NAPHTHA)',
              penalty_lowerbound='18',
              single_penalty_length='255',
              capacity_multiplier='1',
              price_factor=151,
              icon_indices=(12, 1))
