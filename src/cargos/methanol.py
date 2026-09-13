from cargo import Cargo

cargo = Cargo(
    id="methanol",
    type_name="string(STR_CARGO_METHANOL_NAME)",
    unit_name="string(STR_CARGO_METHANOL_NAME)",
    type_abbreviation="string(STR_CARGO_METHANOL_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="MEOH",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_METHANOL_CARGO_UNIT)",
    penalty_lowerbound="20",
    single_penalty_length="40",
    price_factor=157,
    capacity_multiplier="1",
    icon_indices=(3, 7),
    sprites_complete=True,
)
