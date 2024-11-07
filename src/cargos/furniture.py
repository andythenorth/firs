from cargo import Cargo

cargo = Cargo(
    id="furniture",
    type_name="string(STR_CARGO_NAME_FURNITURE)",
    unit_name="string(STR_CARGO_NAME_FURNITURE)",
    type_abbreviation="string(STR_CID_FURNITURE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="FURN",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_FURNITURE)",
    penalty_lowerbound="12",
    single_penalty_length="255",
    price_factor=146,
    capacity_multiplier="1",
    icon_indices=(1, 1),
)
