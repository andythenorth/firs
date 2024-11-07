from cargo import Cargo

cargo = Cargo(
    id="soda_ash",
    type_name="string(STR_CARGO_NAME_SODA_ASH)",
    unit_name="string(STR_CARGO_NAME_SODA_ASH)",
    type_abbreviation="string(STR_CID_SODA_ASH)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_COVERED_BULK", "CC_PIECE_GOODS",  "CC_POWDER_BULK", "CC_NON_POTABLE"],
    cargo_label="SASH",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_SODA_ASH)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    price_factor=96,
    capacity_multiplier="1",
    icon_indices=(12, 3),
)
