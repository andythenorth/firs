from cargo import Cargo

cargo = Cargo(
    id="fruits",
    type_name="string(STR_CARGO_NAME_FRUITS)",
    unit_name="string(STR_CARGO_NAME_FRUITS)",
    type_abbreviation="TTD_STR_ABBREV_FRUIT",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_PIECE_GOODS", "CC_REFRIGERATED", "CC_COVERED_BULK", "CC_POTABLE"],
    cargo_label="FRUT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_FRUITS)",
    penalty_lowerbound="0",
    single_penalty_length="26",
    price_factor=124,
    capacity_multiplier="1",
    icon_indices=(14, 0),
    sprites_complete=True,
)
