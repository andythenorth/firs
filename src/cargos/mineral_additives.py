from cargo import Cargo

cargo = Cargo(
    id="mineral_additives",
    type_name="string(STR_CARGO_MINERAL_ADDITIVES_NAME)",
    unit_name="string(STR_CARGO_MINERAL_ADDITIVES_NAME)",
    type_abbreviation="string(STR_CARGO_MINERAL_ADDITIVES_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_COVERED_BULK", "CC_POWDER_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="MADD",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_MINERAL_ADDITIVES_CARGO_UNIT)",
    penalty_lowerbound="18",
    single_penalty_length="255",
    price_factor=118,
    capacity_multiplier="1",
    icon_indices=(8, 3), # CABBAGE
    sprites_complete=False,
)
