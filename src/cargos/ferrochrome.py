from cargo import Cargo

cargo = Cargo(
    id="ferrochrome",
    type_name="string(STR_CARGO_NAME_FERROCHROME)",
    unit_name="string(STR_CARGO_NAME_FERROCHROME)",
    type_abbreviation="string(STR_CID_FERROCHROME)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_BULK"],
    cargo_label="FECR",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_FERROCHROME)",
    penalty_lowerbound="40",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=106,
    icon_indices=(8, 4),
    sprites_complete=True,
)
