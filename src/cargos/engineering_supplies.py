from cargo import Cargo

cargo = Cargo(
    id="engineering_supplies",
    type_name="string(STR_CARGO_NAME_ENGINEERING_SUPPLIES)",
    unit_name="string(STR_CARGO_NAME_ENGINEERING_SUPPLIES)",
    type_abbreviation="string(STR_CID_ENGINEERING_SUPPLIES)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.65",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="ENSP",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_CRATES",
    items_of_cargo="string(STR_CARGO_UNIT_ENGINEERING_SUPPLIES)",
    penalty_lowerbound="2",
    single_penalty_length="32",
    price_factor=172,
    capacity_multiplier="1",
    icon_indices=(11, 1),
)
