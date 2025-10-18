from cargo import Cargo

cargo = Cargo(
    id="maize",
    type_name="TTD_STR_CARGO_PLURAL_MAIZE",
    unit_name="TTD_STR_CARGO_SINGULAR_MAIZE",
    type_abbreviation="TTD_STR_ABBREV_MAIZE",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_COVERED_BULK", "CC_PIECE_GOODS", "CC_POTABLE"],
    cargo_label="MAIZ",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="TTD_STR_QUANTITY_MAIZE",
    penalty_lowerbound="4",
    single_penalty_length="40",
    price_factor=111,
    capacity_multiplier="1",
    icon_indices=(11, 0),
    sprites_complete=True,
)
