from cargo import Cargo

cargo = Cargo(
    id="quicklime",
    type_name="string(STR_CARGO_QUICKLIME_NAME)",
    unit_name="string(STR_CARGO_QUICKLIME_NAME)",
    type_abbreviation="string(STR_CARGO_QUICKLIME_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_COVERED_BULK", "CC_POWDER_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="QLME",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_QUICKLIME_CARGO_UNIT)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    price_factor=112,
    capacity_multiplier="1",
    icon_indices=(9, 3),
    sprites_complete=True,
)
