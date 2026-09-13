from cargo import Cargo

cargo = Cargo(
    id="peat",
    type_name="string(STR_CARGO_PEAT_NAME)",
    unit_name="string(STR_CARGO_PEAT_NAME)",
    type_abbreviation="string(STR_CARGO_PEAT_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_NON_POTABLE"],
    cargo_label="PEAT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_PEAT_CARGO_UNIT)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=89,
    capacity_multiplier="1",
    icon_indices=(6, 3),
    sprites_complete=True,
)
