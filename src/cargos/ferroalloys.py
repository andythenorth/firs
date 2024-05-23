from cargo import Cargo

cargo = Cargo(
    id="ferroalloys",
    type_name="string(STR_CARGO_NAME_FERROALLOYS)",
    unit_name="string(STR_CARGO_NAME_FERROALLOYS)",
    type_abbreviation="string(STR_CID_FERROALLOYS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK, CC_PIECE_GOODS)",
    cargo_label="FEAL",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_FERROALLOYS)",
    penalty_lowerbound="40",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=106,
    icon_indices=(8, 4),
    sprites_complete=True,
)
