from firs import Cargo

cargo = Cargo(id = 'building_materials',
              number = '28',
              type_name = 'string(STR_CARGO_NAME_BUILDING_MATERIALS)',
              unit_name = 'string(STR_CARGO_NAME_BUILDING_MATERIALS)',
              type_abbreviation = 'string(STR_CID_BUILDING_MATERIALS)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '184',
              cargo_payment_list_colour = '184',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_PIECE_GOODS, CC_BULK)',
              cargo_label = '"BDMT"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '80',
              items_of_cargo = 'string(STR_CARGO_UNIT_BUILDING_MATERIALS)',
              penalty_lowerbound = '12',
              single_penalty_length = '255',
              price_factor = '136.233329773')

cargo.economy_variations['BASIC_TEMPERATE']['disabled'] = True
cargo.economy_variations['BASIC_ARCTIC']['disabled'] = True
cargo.economy_variations['BASIC_TROPIC']['disabled'] = True
