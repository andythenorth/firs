from cargo import Cargo

cargo = Cargo(
    id="mineral_fillers",
    type_name="string(STR_CARGO_MINERAL_FILLERS_NAME)",
    unit_name="string(STR_CARGO_MINERAL_FILLERS_NAME)",
    type_abbreviation="string(STR_CARGO_MINERAL_FILLERS_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_POWDER_BULK", "CC_NON_POTABLE"],
    cargo_label="MIFI",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_MINERAL_FILLERS_CARGO_UNIT)",
    penalty_lowerbound="40",
    single_penalty_length="255",
    price_factor=154,
    capacity_multiplier="1",
    icon_indices=(13, 4),
    sprites_complete=False,
)
