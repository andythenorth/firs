from cargo import Cargo

cargo = Cargo(
    id="tin",
    type_name="string(STR_CARGO_TIN_NAME)",
    unit_name="string(STR_CARGO_TIN_NAME)",
    type_abbreviation="string(STR_CARGO_TIN_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="TIN_",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_TIN_CARGO_UNIT)",
    penalty_lowerbound="12",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=141,
    icon_indices=(6, 7),
    sprites_complete=True,
)
