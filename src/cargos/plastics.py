from cargo import Cargo

cargo = Cargo(
    id="plastics",
    type_name="string(STR_CARGO_NAME_PLASTICS)",
    unit_name="string(STR_CARGO_NAME_PLASTICS)",
    type_abbreviation="string(STR_CID_PLASTICS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_NON_FOOD_GRADE"],
    cargo_label="PLAS",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_PLASTICS)",
    penalty_lowerbound="12",
    single_penalty_length="36",
    capacity_multiplier="1",
    price_factor=133,
    icon_indices=(6, 4),
    sprites_complete=True,
)
