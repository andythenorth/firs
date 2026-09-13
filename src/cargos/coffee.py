from cargo import Cargo

cargo = Cargo(
    id="coffee",
    type_name="string(STR_CARGO_COFFEE_NAME)",
    unit_name="string(STR_CARGO_COFFEE_NAME)",
    type_abbreviation="string(STR_CARGO_COFFEE_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_EXPRESS", "CC_POTABLE"],
    cargo_label="JAVA",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_COFFEE_CARGO_UNIT)",
    penalty_lowerbound="0",
    single_penalty_length="26",
    price_factor=181,
    capacity_multiplier="1",
    icon_indices=(4, 2),
    sprites_complete=True,
)
