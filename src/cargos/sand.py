from cargo import Cargo

cargo = Cargo(
    id="sand",
    type_name="string(STR_CARGO_SAND_NAME)",
    unit_name="string(STR_CARGO_SAND_NAME)",
    type_abbreviation="string(STR_CARGO_SAND_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_COVERED_BULK", "CC_POWDER_BULK", "CC_NON_POTABLE"],
    cargo_label="SAND",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_SAND_CARGO_UNIT)",
    penalty_lowerbound="40",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=93,
    icon_indices=(0, 1),
    sprites_complete=True,
)
