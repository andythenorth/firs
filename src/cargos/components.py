from cargo import Cargo

cargo = Cargo(
    id="components",
    type_name="string(STR_CARGO_NAME_COMPONENTS)",
    unit_name="string(STR_CARGO_NAME_COMPONENTS)",
    type_abbreviation="string(STR_CID_COMPONENTS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_NON_POTABLE"],
    cargo_label="COMP",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_COMPONENTS)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=127,
    icon_indices=(10, 0),
    sprites_complete=True,
)
