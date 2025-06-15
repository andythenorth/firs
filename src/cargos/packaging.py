from cargo import Cargo

cargo = Cargo(
    id="packaging",
    type_name="string(STR_CARGO_NAME_PACKAGING)",
    unit_name="string(STR_CARGO_NAME_PACKAGING)",
    type_abbreviation="string(STR_CID_PACKAGING)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.65",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="MNSP",  # MNSP label preserved in FIRS v3 for backwards compatibility, may remove in v4
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_PACKAGING)",
    penalty_lowerbound="16",
    single_penalty_length="120",
    price_factor=131,
    capacity_multiplier="1",
    icon_indices=(7, 1),
)
