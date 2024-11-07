from cargo import Cargo

cargo = Cargo(
    id="plastics",
    type_name="string(STR_CARGO_NAME_PLASTICS)",
    unit_name="string(STR_CARGO_NAME_PLASTICS)",
    type_abbreviation="string(STR_CID_PLASTICS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_NON_POTABLE"],
    cargo_label="PLAS",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_PLASTICS)",
    penalty_lowerbound="12",
    single_penalty_length="36",
    capacity_multiplier="1",
    price_factor=141,
    icon_indices=(6, 4),
)
