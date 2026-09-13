from cargo import Cargo

cargo = Cargo(
    id="steel_sheet",
    type_name="string(STR_CARGO_STEEL_SHEET_NAME)",
    unit_name="string(STR_CARGO_STEEL_SHEET_NAME)",
    type_abbreviation="string(STR_CARGO_STEEL_SHEET_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="STSH",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_STEEL_SHEET_CARGO_UNIT)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=142,
    icon_indices=(6, 5),
    sprites_complete=True,
)
