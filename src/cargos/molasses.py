from cargo import Cargo

cargo = Cargo(
    id="molasses",
    type_name="string(STR_CARGO_NAME_MOLASSES)",
    unit_name="string(STR_CARGO_NAME_MOLASSES)",
    type_abbreviation="string(STR_CID_MOLASSES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.1",
    is_freight="1",
    cargo_classes="bitmask(CC_LIQUID)",
    cargo_label="MOLA",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_MOLASSES)",
    penalty_lowerbound="0",
    single_penalty_length="16",
    capacity_multiplier="1",
    price_factor=105,
    icon_indices=(13, 0),
)
