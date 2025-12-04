from cargo import Cargo

cargo = Cargo(
    id="diesel",
    type_name="string(STR_CARGO_NAME_DIESEL)",
    unit_name="string(STR_CARGO_NAME_DIESEL)",
    type_abbreviation="string(STR_CID_DIESEL)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.9",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="DIES",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_DIESEL)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=101,
    capacity_multiplier="1",
    icon_indices=(3, 0),
    sprites_complete=True,
)
