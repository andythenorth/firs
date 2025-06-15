from cargo import Cargo

cargo = Cargo(
    id="phosphoric_acid",
    type_name="string(STR_CARGO_NAME_PHOSPHORIC_ACID)",
    unit_name="string(STR_CARGO_NAME_PHOSPHORIC_ACID)",
    type_abbreviation="string(STR_CID_PHOSPHORIC_ACID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.5",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="PHAC",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_PHOSPHORIC_ACID)",
    penalty_lowerbound="24",
    single_penalty_length="48",
    price_factor=109,
    capacity_multiplier="1",
    icon_indices=(4, 4),
)
