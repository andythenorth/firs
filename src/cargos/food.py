from cargo import Cargo

cargo = Cargo(
    id="food",
    type_name="TTD_STR_CARGO_PLURAL_FOOD",
    unit_name="TTD_STR_CARGO_SINGULAR_FOOD",
    type_abbreviation="TTD_STR_ABBREV_FOOD",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_REFRIGERATED, CC_EXPRESS)",
    cargo_label="FOOD",
    town_growth_effect="TOWNGROWTH_FOOD",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="TTD_STR_QUANTITY_FOOD",
    penalty_lowerbound="0",
    single_penalty_length="20",
    price_factor=192,
    capacity_multiplier="1",
    icon_indices=(12, 0),
)
