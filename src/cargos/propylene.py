from cargo import Cargo

cargo = Cargo(
    id="propylene",
    type_name="string(STR_CARGO_NAME_PROPYLENE)",
    unit_name="string(STR_CARGO_NAME_PROPYLENE)",
    type_abbreviation="string(STR_CID_PROPYLENE)",
    sprite="NEW_CARGO_SPRITE",
    weight="2.0",
    is_freight="1",
    cargo_classes = ["CC_GAS_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="C3H6",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_PROPYLENE)",
    penalty_lowerbound="20",
    single_penalty_length="40",
    price_factor=157,
    capacity_multiplier="1",
    icon_indices=(2, 4),
)
