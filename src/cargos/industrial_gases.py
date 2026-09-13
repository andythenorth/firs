from cargo import Cargo

cargo = Cargo(
    id="industrial_gases",
    type_name="string(STR_CARGO_INDUSTRIAL_GASES_NAME)",
    unit_name="string(STR_CARGO_INDUSTRIAL_GASES_NAME)",
    type_abbreviation="string(STR_CARGO_INDUSTRIAL_GASES_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_GAS_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="INGA",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_INDUSTRIAL_GASES_CARGO_UNIT)",
    penalty_lowerbound="22",
    single_penalty_length="44",
    price_factor=135,
    capacity_multiplier="1",
    icon_indices=(5, 7),
    sprites_complete=True,
)
