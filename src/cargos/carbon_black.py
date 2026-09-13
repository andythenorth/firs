from cargo import Cargo

cargo = Cargo(
    id="carbon_black",
    type_name="string(STR_CARGO_CARBON_BLACK_NAME)",
    unit_name="string(STR_CARGO_CARBON_BLACK_NAME)",
    type_abbreviation="string(STR_CARGO_CARBON_BLACK_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_POWDER_BULK", "CC_NON_POTABLE"],
    cargo_label="CBLK",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_CARBON_BLACK_CARGO_UNIT)",
    penalty_lowerbound="40",
    single_penalty_length="255",
    price_factor=154,
    capacity_multiplier="1",
    icon_indices=(13, 4),
    sprites_complete=True,
)
