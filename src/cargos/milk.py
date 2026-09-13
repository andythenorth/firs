from cargo import Cargo

cargo = Cargo(
    id="milk",
    type_name="string(STR_CARGO_MILK_NAME)",
    unit_name="string(STR_CARGO_MILK_NAME)",
    type_abbreviation="string(STR_CARGO_MILK_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_LIQUID_BULK", "CC_POTABLE", "CC_REFRIGERATED"],
    cargo_label="MILK",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_MILK_CARGO_UNIT)",
    penalty_lowerbound="0",
    single_penalty_length="16",
    capacity_multiplier="1",
    price_factor=131,
    icon_indices=(13, 0),
    sprites_complete=True,
)
