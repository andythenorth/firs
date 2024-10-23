from cargo import Cargo

cargo = Cargo(
    id="oil",
    type_name="TTD_STR_CARGO_PLURAL_OIL",
    unit_name="TTD_STR_CARGO_SINGULAR_OIL",
    type_abbreviation="TTD_STR_ABBREV_OIL",
    sprite="NEW_CARGO_SPRITE",
    weight="0.9",
    is_freight="1",
    cargo_classes = ["CC_LIQUID", "CC_NON_FOOD_GRADE"],
    cargo_label="OIL_",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="TTD_STR_QUANTITY_OIL",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=101,
    capacity_multiplier="1",
    icon_indices=(3, 0),
    sprites_complete=True,
)
