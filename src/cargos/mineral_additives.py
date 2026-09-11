from cargo import Cargo

cargo = Cargo(
    id="mineral_additives",
    type_name="string(STR_CARGO_NAME_MINERAL_ADDITIVES)",
    unit_name="string(STR_CARGO_NAME_MINERAL_ADDITIVES)",
    type_abbreviation="string(STR_CID_MINERAL_ADDITIVES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_COVERED_BULK", "CC_POWDER_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="MADD",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_MINERAL_ADDITIVES)",
    penalty_lowerbound="18",
    single_penalty_length="255",
    price_factor=118,
    capacity_multiplier="1",
    icon_indices=(8, 3), # CABBAGE
    sprites_complete=False,
)
