from cargo import Cargo

cargo = Cargo(
    id="ammonia",
    type_name="string(STR_CARGO_NAME_AMMONIA)",
    unit_name="string(STR_CARGO_NAME_AMMONIA)",
    type_abbreviation="string(STR_CID_AMMONIA)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.60",  # extra realism per forum suggestion
    is_freight="1",
    cargo_classes = ["CC_GAS_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="NH3_",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_AMMONIA)",
    penalty_lowerbound="32",
    single_penalty_length="64",
    price_factor=109,
    capacity_multiplier="1",
    icon_indices=(15, 4),
)
