from cargo import Cargo

cargo = Cargo(id='slag',
              type_name='string(STR_CARGO_NAME_SLAG)',
              unit_name='string(STR_CARGO_NAME_SLAG)',
              type_abbreviation='string(STR_CID_SLAG)',
              sprite='NEW_CARGO_SPRITE',
              weight='1.0',
              cargo_payment_list_colour='24',
              is_freight='1',
              cargo_classes='bitmask(CC_BULK)',
              cargo_label='SLAG',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='80',
              items_of_cargo='string(STR_CARGO_UNIT_SLAG)',
              penalty_lowerbound='30',
              single_penalty_length='255',
              price_factor='50',  # deliberately low, needed to space out cargo payments to allow unique rates
              capacity_multiplier='1',
              allow_animated_pixels=True,  # slag uses fire cycle pixels, by design, so suppress NML pixel warnings
              icon_indices=(11, 3))
