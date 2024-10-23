from cargo import Cargo

cargo = Cargo(
    id="carbon_black",
    type_name="string(STR_CARGO_NAME_CARBON_BLACK)",
    unit_name="string(STR_CARGO_NAME_CARBON_BLACK)",
    type_abbreviation="string(STR_CID_CARBON_BLACK)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_POWDERIZED", "CC_NON_FOOD_GRADE"],
    cargo_label="CBLK",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_CARBON_BLACK)",
    penalty_lowerbound="40",
    single_penalty_length="255",
    price_factor=154,
    capacity_multiplier="1",
    icon_indices=(13, 4),
    sprites_complete=True,
)
