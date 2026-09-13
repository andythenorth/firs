from cargo import Cargo

cargo = Cargo(
    id="soda_ash",
    type_name="string(STR_CARGO_SODA_ASH_NAME)",
    unit_name="string(STR_CARGO_SODA_ASH_NAME)",
    type_abbreviation="string(STR_CARGO_SODA_ASH_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_COVERED_BULK", "CC_PIECE_GOODS",  "CC_POWDER_BULK", "CC_NON_POTABLE"],
    cargo_label="SASH",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_SODA_ASH_CARGO_UNIT)",
    penalty_lowerbound="40",
    single_penalty_length="255",
    price_factor=96,
    capacity_multiplier="1",
    icon_indices=(12, 3),
    sprites_complete=True,
)
