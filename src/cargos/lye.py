from cargo import Cargo

cargo = Cargo(
    id="lye",
    type_name="string(STR_CARGO_NAME_LYE)",
    unit_name="string(STR_CARGO_NAME_LYE)",
    type_abbreviation="string(STR_CID_LYE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.5",  # extra realism, per forum suggestion Nov 2017
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="LYE_",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_LYE)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=108,
    capacity_multiplier="1",
    icon_indices=(4, 5),
)
