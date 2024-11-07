from cargo import Cargo

cargo = Cargo(
    id="salt",
    type_name="string(STR_CARGO_NAME_SALT)",
    unit_name="string(STR_CARGO_NAME_SALT)",
    type_abbreviation="string(STR_CID_SALT)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_COVERED_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="SALT",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_SALT)",
    penalty_lowerbound="36",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=94,
    icon_indices=(3, 4),
)
