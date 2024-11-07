from cargo import Cargo

cargo = Cargo(
    id="pipe",
    type_name="string(STR_CARGO_NAME_PIPE)",
    unit_name="string(STR_CARGO_NAME_PIPE)",
    type_abbreviation="string(STR_CID_PIPE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="PIPE",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_PIPE)",
    penalty_lowerbound="30",
    single_penalty_length="42",
    price_factor=144,
    capacity_multiplier="1",
    icon_indices=(7, 3),
)
