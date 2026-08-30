from cargo import Cargo

cargo = Cargo(
    id="industrial_carbons",
    type_name="string(STR_CARGO_NAME_INDUSTRIAL_CARBONS)",
    unit_name="string(STR_CARGO_NAME_INDUSTRIAL_CARBONS)",
    type_abbreviation="string(STR_CID_INDUSTRIAL_CARBONS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_COVERED_BULK", "CC_POWDER_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="INCA",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_INDUSTRIAL_CARBONS)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=110,
    capacity_multiplier="1",
    icon_indices=(10, 7),
    sprites_complete=True,
)
