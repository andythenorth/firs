from cargo import Cargo

cargo = Cargo(
    id="beans",
    type_name="string(STR_CARGO_BEANS_NAME)",
    unit_name="string(STR_CARGO_BEANS_NAME)",
    type_abbreviation="string(STR_CARGO_BEANS_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_COVERED_BULK", "CC_PIECE_GOODS", "CC_POTABLE"],
    cargo_label="BEAN",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_BEANS_CARGO_UNIT)",
    penalty_lowerbound="4",
    single_penalty_length="40",
    price_factor=119,
    capacity_multiplier="1",
    icon_indices=(6, 2),
    sprites_complete=True,
)
