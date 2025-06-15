from cargo import Cargo

cargo = Cargo(
    id="goods",
    type_name="TTD_STR_CARGO_PLURAL_GOODS",
    unit_name="TTD_STR_CARGO_SINGULAR_GOODS",
    type_abbreviation="TTD_STR_ABBREV_GOODS",
    sprite="NEW_CARGO_SPRITE",
    weight="0.5",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="GOOD",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_CRATES",
    items_of_cargo="TTD_STR_QUANTITY_GOODS",
    penalty_lowerbound="10",
    single_penalty_length="56",
    price_factor=163,
    capacity_multiplier="2",
    icon_indices=(5, 0),
)
