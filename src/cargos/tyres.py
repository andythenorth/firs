from cargo import Cargo

cargo = Cargo(
    id="tyres",
    type_name="string(STR_CARGO_NAME_TYRES)",
    unit_name="string(STR_CARGO_NAME_TYRES)",
    type_abbreviation="string(STR_CID_TYRES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="TYRE",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_TYRES)",
    penalty_lowerbound="8",
    single_penalty_length="255",
    price_factor=149,
    capacity_multiplier="1",
    icon_indices=(7, 4),
    sprites_complete=True,
)
