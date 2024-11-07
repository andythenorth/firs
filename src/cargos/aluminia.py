from cargo import Cargo

cargo = Cargo(
    id="aluminia",
    type_name="string(STR_CARGO_NAME_ALUMINIA)",
    unit_name="string(STR_CARGO_NAME_ALUMINIA)",
    type_abbreviation="string(STR_CID_ALUMINIA)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_NON_POTABLE"],
    cargo_label="ALO_",  # Aluminium Oxide
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_ALUMINIA)",
    penalty_lowerbound="15",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=101,
    icon_indices=(8, 4),
)
