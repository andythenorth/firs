from cargo import Cargo

cargo = Cargo(
    id="steel_sheet",
    type_name="string(STR_CARGO_NAME_STEEL_SHEET)",
    unit_name="string(STR_CARGO_NAME_STEEL_SHEET)",
    type_abbreviation="string(STR_CID_STEEL_SHEET)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="STSH",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_STEEL_SHEET)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=142,
    icon_indices=(6, 5),
    sprites_complete=True,
)
