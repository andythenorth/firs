from cargo import Cargo

cargo = Cargo(
    id="rubber",
    type_name="TTD_STR_CARGO_PLURAL_RUBBER",
    unit_name="TTD_STR_CARGO_SINGULAR_RUBBER",
    type_abbreviation="TTD_STR_ABBREV_RUBBER",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID", "CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_POWDERIZED", "CC_NON_FOOD_GRADE"],
    cargo_label="RUBR",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="TTD_STR_QUANTITY_RUBBER",
    penalty_lowerbound="10",
    single_penalty_length="36",
    capacity_multiplier="1",
    price_factor=110,
    icon_indices=(2, 2),
    sprites_complete=True,
)
