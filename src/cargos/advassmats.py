from cargo import Cargo

cargo = Cargo(
    id="advassmats",
    type_name="string(STR_CARGO_NAME_ADVASSMATS)",
    unit_name="string(STR_CARGO_NAME_ADVASSMATS)",
    type_abbreviation="string(STR_CID_ADVASSMATS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="AASS",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_ADVASSMATS)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=128,
    icon_indices=(14, 6),
    sprites_complete=True,
)
