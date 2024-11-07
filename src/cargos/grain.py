from cargo import Cargo

cargo = Cargo(
    id="grain",
    type_name="TTD_STR_CARGO_PLURAL_GRAIN",
    unit_name="TTD_STR_CARGO_SINGULAR_GRAIN",
    type_abbreviation="TTD_STR_ABBREV_GRAIN",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_COVERED_BULK", "CC_PIECE_GOODS", "CC_POTABLE"],
    cargo_label="GRAI",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="TTD_STR_QUANTITY_GRAIN",
    penalty_lowerbound="4",
    single_penalty_length="40",
    price_factor=114,
    capacity_multiplier="1",
    icon_indices=(6, 0),
)
