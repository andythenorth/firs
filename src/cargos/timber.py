from cargo import Cargo

cargo = Cargo(
    id="timber",
    type_name="string(STR_CARGO_NAME_TIMBER)",
    unit_name="string(STR_CARGO_NAME_TIMBER)",
    type_abbreviation="string(STR_CID_TIMBER)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK, CC_PIECE_GOODS)",
    cargo_label="WDPR",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_TIMBER)",
    penalty_lowerbound="18",
    single_penalty_length="255",
    price_factor=117,
    capacity_multiplier="1",
    icon_indices=(6, 1),
    sprites_complete=True,
)
