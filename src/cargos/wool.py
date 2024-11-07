from cargo import Cargo

cargo = Cargo(
    id="wool",
    type_name="string(STR_CARGO_NAME_WOOL)",
    unit_name="string(STR_CARGO_NAME_WOOL)",
    type_abbreviation="string(STR_CID_WOOL)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.2",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="WOOL",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_ITEMS",
    items_of_cargo="string(STR_CARGO_UNIT_WOOL)",
    penalty_lowerbound="8",
    single_penalty_length="48",
    price_factor=111,
    capacity_multiplier="1",
    icon_indices=(4, 1),
)
