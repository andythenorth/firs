from cargo import Cargo

cargo = Cargo(
    id="lifting_equipment",
    type_name="string(STR_CARGO_NAME_LIFTING_EQUIPMENT)",
    unit_name="string(STR_CARGO_NAME_LIFTING_EQUIPMENT)",
    type_abbreviation="string(STR_CID_LIFTING_EQUIPMENT)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="LFEQ",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_LIFTING_EQUIPMENT)",
    penalty_lowerbound="7",
    single_penalty_length="255",
    price_factor=163,
    capacity_multiplier="1",
    icon_indices=(10, 6),
    sprites_complete=True,
)
