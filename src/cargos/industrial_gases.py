from cargo import Cargo

cargo = Cargo(
    id="industrial_gases",
    type_name="string(STR_CARGO_NAME_INDUSTRIAL_GASES)",
    unit_name="string(STR_CARGO_NAME_INDUSTRIAL_GASES)",
    type_abbreviation="string(STR_CID_INDUSTRIAL_GASES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_GAS_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="INGA",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_INDUSTRIAL_GASES)",
    penalty_lowerbound="22",
    single_penalty_length="44",
    price_factor=135,
    capacity_multiplier="1",
    icon_indices=(1, 5),
    sprites_complete=False,
)
