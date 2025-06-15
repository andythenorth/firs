from cargo import Cargo

cargo = Cargo(
    id="rubber",
    type_name="TTD_STR_CARGO_PLURAL_RUBBER",
    unit_name="TTD_STR_CARGO_SINGULAR_RUBBER",
    type_abbreviation="TTD_STR_ABBREV_RUBBER",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_POWDER_BULK", "CC_NON_POTABLE"],
    cargo_label="RUBR",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="TTD_STR_QUANTITY_RUBBER",
    penalty_lowerbound="10",
    single_penalty_length="36",
    capacity_multiplier="1",
    price_factor=110,
    icon_indices=(2, 2),
)
