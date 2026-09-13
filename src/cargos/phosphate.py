from cargo import Cargo

cargo = Cargo(
    id="phosphate",
    type_name="string(STR_CARGO_PHOSPHATE_NAME)",
    unit_name="string(STR_CARGO_PHOSPHATE_NAME)",
    type_abbreviation="string(STR_CARGO_PHOSPHATE_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_COVERED_BULK", "CC_NON_POTABLE"],
    cargo_label="PHOS",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_PHOSPHATE_CARGO_UNIT)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=99,
    capacity_multiplier="1",
    icon_indices=(10, 2),
    sprites_complete=True,
)
