from cargo import Cargo

cargo = Cargo(
    id="cassava",
    type_name="string(STR_CARGO_NAME_CASSAVA)",
    unit_name="string(STR_CARGO_NAME_CASSAVA)",
    type_abbreviation="string(STR_CID_CASSAVA)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_COVERED_BULK", "CC_POTABLE"],
    cargo_label="CASS",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_CASSAVA)",
    penalty_lowerbound="4",
    single_penalty_length="40",
    price_factor=105,
    capacity_multiplier="1",
    icon_indices=(11, 2),
)
