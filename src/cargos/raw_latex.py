from cargo import Cargo

cargo = Cargo(
    id="raw_latex",
    type_name="string(STR_CARGO_RAW_LATEX_NAME)",
    unit_name="string(STR_CARGO_RAW_LATEX_NAME)",
    type_abbreviation="string(STR_CARGO_RAW_LATEX_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="LATX",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_RAW_LATEX_CARGO_UNIT)",
    penalty_lowerbound="10",
    single_penalty_length="36",
    capacity_multiplier="1",
    price_factor=110,
    icon_indices=(2, 2),
    sprites_complete=False,
)
