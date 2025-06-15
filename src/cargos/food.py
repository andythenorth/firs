from cargo import Cargo

cargo = Cargo(
    id="food",
    type_name="TTD_STR_CARGO_PLURAL_FOOD",
    unit_name="TTD_STR_CARGO_SINGULAR_FOOD",
    type_abbreviation="TTD_STR_ABBREV_FOOD",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_COVERED_BULK", "CC_PIECE_GOODS", "CC_LIQUID_BULK", "CC_POTABLE", "CC_REFRIGERATED"],
    cargo_label="FOOD",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above     snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="TTD_STR_QUANTITY_FOOD",
    penalty_lowerbound="0",
    single_penalty_length="20",
    price_factor=168,
    capacity_multiplier="1",
    icon_indices=(12, 0),
)
