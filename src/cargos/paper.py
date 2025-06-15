from cargo import Cargo

cargo = Cargo(
    id="paper",
    type_name="TTD_STR_CARGO_PLURAL_PAPER",
    unit_name="TTD_STR_CARGO_SINGULAR_PAPER",
    type_abbreviation="TTD_STR_ABBREV_PAPER",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="PAPR",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="TTD_STR_QUANTITY_PAPER",
    penalty_lowerbound="12",
    single_penalty_length="60",
    price_factor=143,
    capacity_multiplier="1",
    icon_indices=(5, 2),
)
