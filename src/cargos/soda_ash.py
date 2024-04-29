from cargo import Cargo

cargo = Cargo(
    id="soda_ash",
    type_name="string(STR_CARGO_NAME_SODA_ASH)",
    unit_name="string(STR_CARGO_NAME_SODA_ASH)",
    type_abbreviation="string(STR_CID_SODA_ASH)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK, CC_COVERED)",
    cargo_label="SASH",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_SODA_ASH)",
    penalty_lowerbound="40",
    single_penalty_length="255",
    price_factor=96,
    capacity_multiplier="1",
    icon_indices=(12, 3),
    sprites_complete=True,
)
