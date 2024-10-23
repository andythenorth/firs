from cargo import Cargo

cargo = Cargo(
    id="raw_latex",
    type_name="string(STR_CARGO_NAME_RAW_LATEX)",
    unit_name="string(STR_CARGO_NAME_RAW_LATEX)",
    type_abbreviation="string(STR_CID_RAW_LATEX)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID", "CC_NON_FOOD_GRADE"],
    cargo_label="LATX",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_RAW_LATEX)",
    penalty_lowerbound="10",
    single_penalty_length="36",
    capacity_multiplier="1",
    price_factor=110,
    icon_indices=(2, 2),
    sprites_complete=False,
)
