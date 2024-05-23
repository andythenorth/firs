from cargo import Cargo

cargo = Cargo(
    id="steel_slab",
    type_name="string(STR_CARGO_NAME_STEEL_SLAB)",
    unit_name="string(STR_CARGO_NAME_STEEL_SLAB)",
    type_abbreviation="string(STR_CID_STEEL_SLAB)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="STSL",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_STEEL_SLAB)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=128,
    icon_indices=(13, 6),
    sprites_complete=True,
)
