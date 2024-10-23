from cargo import Cargo

cargo = Cargo(
    id="formic_acid",
    type_name="string(STR_CARGO_NAME_FORMIC_ACID)",
    unit_name="string(STR_CARGO_NAME_FORMIC_ACID)",
    type_abbreviation="string(STR_CID_FORMIC_ACID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.2",
    is_freight="1",
    cargo_classes = ["CC_LIQUID", "CC_NON_FOOD_GRADE"],
    cargo_label="FORM",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_FORMIC_ACID)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=109,
    capacity_multiplier="1",
    icon_indices=(4, 4),
    sprites_complete=False,
)
