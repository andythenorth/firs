from cargo import Cargo

cargo = Cargo(
    id="nuts",
    type_name="string(STR_CARGO_NUTS_NAME)",
    unit_name="string(STR_CARGO_NUTS_NAME)",
    type_abbreviation="string(STR_CARGO_NUTS_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_POTABLE"],
    cargo_label="NUTS",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_NUTS_CARGO_UNIT)",
    penalty_lowerbound="4",
    single_penalty_length="40",
    price_factor=113,
    capacity_multiplier="1",
    icon_indices=(12, 2),
    sprites_complete=True,
)
