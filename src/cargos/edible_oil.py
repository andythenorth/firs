from cargo import Cargo

cargo = Cargo(
    id="edible_oil",
    type_name="string(STR_CARGO_NAME_EDIBLE_OIL)",
    unit_name="string(STR_CARGO_NAME_EDIBLE_OIL)",
    type_abbreviation="string(STR_CID_EDIBLE_OIL)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_LIQUID_BULK", "CC_POTABLE"],
    cargo_label="EOIL",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_EDIBLE_OIL)",
    penalty_lowerbound="20",
    single_penalty_length="128",
    price_factor=116,
    capacity_multiplier="1",
    icon_indices=(0, 3),
)
