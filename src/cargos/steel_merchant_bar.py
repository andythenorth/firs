from cargo import Cargo

cargo = Cargo(
    id="steel_merchant_bar",
    type_name="string(STR_CARGO_NAME_STEEL_MERCHANT_BAR)",
    unit_name="string(STR_CARGO_NAME_STEEL_MERCHANT_BAR)",
    type_abbreviation="string(STR_CID_STEEL_MERCHANT_BAR)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_FOOD_GRADE"],
    cargo_label="STBR",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_STEEL_MERCHANT_BAR)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=144,
    icon_indices=(9, 6),
    sprites_complete=True,
)
