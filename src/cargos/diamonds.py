from cargo import Cargo

cargo = Cargo(
    id="diamonds",
    type_name="TTD_STR_CARGO_PLURAL_DIAMONDS",
    unit_name="TTD_STR_CARGO_SINGULAR_DIAMOND",
    type_abbreviation="TTD_STR_ABBREV_DIAMONDS",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_ARMOURED"],
    cargo_label="DIAM",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_BAGS",
    items_of_cargo="TTD_STR_QUANTITY_DIAMONDS",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=162,
    capacity_multiplier="1",
    icon_indices=(3, 2),
)
