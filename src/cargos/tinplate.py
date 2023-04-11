from cargo import Cargo

cargo = Cargo(
    id="tinplate",
    type_name="string(STR_CARGO_NAME_TINPLATE)",
    unit_name="string(STR_CARGO_NAME_TINPLATE)",
    type_abbreviation="string(STR_CID_TINPLATE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="TINP",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_TINPLATE)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=153,
    icon_indices=(12, 4),
    sprites_complete=False,
)
