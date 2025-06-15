from cargo import Cargo

cargo = Cargo(
    id="sugar_beet",
    type_name="string(STR_CARGO_NAME_SUGAR_BEET)",
    unit_name="string(STR_CARGO_NAME_SUGAR_BEET)",
    type_abbreviation="string(STR_CID_SUGAR_BEET)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_POTABLE"],
    cargo_label="SGBT",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_SUGAR_BEET)",
    penalty_lowerbound="5",
    single_penalty_length="30",
    price_factor=99,
    capacity_multiplier="1",
    icon_indices=(14, 1),
)
