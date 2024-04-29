from cargo import Cargo

cargo = Cargo(
    id="sand",
    type_name="string(STR_CARGO_NAME_SAND)",
    unit_name="string(STR_CARGO_NAME_SAND)",
    type_abbreviation="string(STR_CID_SAND)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK, CC_COVERED)",
    cargo_label="SAND",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_SAND)",
    penalty_lowerbound="40",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=93,
    icon_indices=(0, 1),
    sprites_complete=True,
)
