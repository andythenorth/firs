from cargo import Cargo

cargo = Cargo(
    id="copper_concentrate",
    type_name="string(STR_CARGO_COPPER_CONCENTRATE_NAME)",
    unit_name="string(STR_CARGO_COPPER_CONCENTRATE_NAME)",
    type_abbreviation="string(STR_CARGO_COPPER_CONCENTRATE_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1",
    is_freight="1",
    cargo_classes = ["CC_COVERED_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="COCO",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_COPPER_CONCENTRATE_CARGO_UNIT)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=109,
    capacity_multiplier="1",
    icon_indices=(4, 4),
    sprites_complete=False,
)
