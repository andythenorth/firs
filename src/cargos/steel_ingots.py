from cargo import Cargo

cargo = Cargo(
    id="steel_ingots",
    type_name="string(STR_CARGO_NAME_STEEL_INGOTS)",
    unit_name="string(STR_CARGO_NAME_STEEL_INGOTS)",
    type_abbreviation="string(STR_CID_STEEL_INGOTS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="STIG",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_STEEL_INGOTS)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=127,
    icon_indices=(12, 6),
    sprites_complete=False,
)
