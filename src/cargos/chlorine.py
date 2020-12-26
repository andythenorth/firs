from cargo import Cargo

cargo = Cargo(
    id="chlorine",
    type_name="string(STR_CARGO_NAME_CHLORINE)",
    unit_name="string(STR_CARGO_NAME_CHLORINE)",
    type_abbreviation="string(STR_CID_CHLORINE)",
    sprite="NEW_CARGO_SPRITE",
    weight="2.0",
    is_freight="1",
    cargo_classes="bitmask(CC_LIQUID, CC_HAZARDOUS)",
    cargo_label="CHLO",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_CHLORINE)",
    penalty_lowerbound="20",
    single_penalty_length="40",
    price_factor=120,
    capacity_multiplier="1",
    icon_indices=(2, 4),
)
