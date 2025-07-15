from cargo import Cargo

cargo = Cargo(
    id="steel_plate",
    type_name="string(STR_CARGO_NAME_STEEL_PLATE)",
    unit_name="string(STR_CARGO_NAME_STEEL_PLATE)",
    type_abbreviation="string(STR_CID_STEEL_PLATE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="STPL",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_STEEL_PLATE)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=128,
    icon_indices=(13, 6),
    sprites_complete=False,
)
