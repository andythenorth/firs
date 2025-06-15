from cargo import Cargo

cargo = Cargo(
    id="sugarcane",
    type_name="string(STR_CARGO_NAME_SUGARCANE)",
    unit_name="string(STR_CARGO_NAME_SUGARCANE)",
    type_abbreviation="string(STR_CID_SUGARCANE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_WEIRD"],
    cargo_label="SGCN",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_SUGARCANE)",
    penalty_lowerbound="5",
    single_penalty_length="30",
    price_factor=116,
    capacity_multiplier="1",
    icon_indices=(15, 1),
)
