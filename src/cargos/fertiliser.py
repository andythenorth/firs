from cargo import Cargo

cargo = Cargo(
    id="fertiliser",
    type_name="string(STR_CARGO_FERTILISER_NAME)",
    unit_name="string(STR_CARGO_FERTILISER_NAME)",
    type_abbreviation="string(STR_CARGO_FERTILISER_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_NON_POTABLE"],
    cargo_label="FERT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_FERTILISER_CARGO_UNIT)",
    penalty_lowerbound="22",
    single_penalty_length="44",
    price_factor=123,
    capacity_multiplier="1",
    icon_indices=(3, 3),
    sprites_complete=True,
)
