from cargo import Cargo

cargo = Cargo(
    id="yeast",
    type_name="string(STR_CARGO_NAME_YEAST)",
    unit_name="string(STR_CARGO_NAME_YEAST)",
    type_abbreviation="string(STR_CID_YEAST)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.1",
    is_freight="1",
    cargo_classes = ["CC_COVERED_BULK", "CC_POWDER_BULK", "CC_PIECE_GOODS", "CC_POTABLE"],
    cargo_label="YST_",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_YEAST)",
    penalty_lowerbound="0",
    single_penalty_length="16",
    capacity_multiplier="1",
    price_factor=116,
    icon_indices=(13, 0),
)
