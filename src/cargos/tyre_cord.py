from cargo import Cargo

cargo = Cargo(
    id="tyre_cord",
    type_name="string(STR_CARGO_NAME_TYRE_CORD)",
    unit_name="string(STR_CARGO_NAME_TYRE_CORD)",
    type_abbreviation="string(STR_CID_TYRE_CORD)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="TYCO",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_TYRE_CORD)",
    penalty_lowerbound="30",
    single_penalty_length="42",
    price_factor=141,
    capacity_multiplier="1",
    icon_indices=(12, 5),
    sprites_complete=True,
)
