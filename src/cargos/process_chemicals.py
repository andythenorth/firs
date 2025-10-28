from cargo import Cargo

cargo = Cargo(
    id="process_chemicals",
    type_name="string(STR_CARGO_NAME_PROCESS_CHEMICALS)",
    unit_name="string(STR_CARGO_NAME_PROCESS_CHEMICALS)",
    type_abbreviation="string(STR_CID_PROCESS_CHEMICALS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="PRCH",  # yes it's a terrible pun on several things at once - LordAro suggested it
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_PROCESS_CHEMICALS)",
    penalty_lowerbound="20",
    single_penalty_length="121",
    price_factor=117,
    capacity_multiplier="1",
    icon_indices=(10, 1),
)
