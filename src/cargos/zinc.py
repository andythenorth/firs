from cargo import Cargo

cargo = Cargo(
    id="zinc",
    type_name="string(STR_CARGO_ZINC_NAME)",
    unit_name="string(STR_CARGO_ZINC_NAME)",
    type_abbreviation="string(STR_CARGO_ZINC_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="ZINC",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_ZINC_CARGO_UNIT)",
    penalty_lowerbound="12",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=126,
    icon_indices=(15, 3),
    sprites_complete=True,
)
