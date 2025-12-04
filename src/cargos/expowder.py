from cargo import Cargo

cargo = Cargo(
    id="expowder",
    type_name="string(STR_CARGO_NAME_EXPLOSIVE_POWDER)",
    unit_name="string(STR_CARGO_NAME_EXPLOSIVE_POWDER)",
    type_abbreviation="string(STR_CID_EXPLOSIVE_POWDER)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_POWDER_BULK", "CC_NON_POTABLE"],
    cargo_label="EXPW",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_EXPLOSIVE_POWDER)",
    penalty_lowerbound="40",
    single_penalty_length="255",
    price_factor=119,
    capacity_multiplier="1",
    icon_indices=(0, 4),
    sprites_complete=True,
)
