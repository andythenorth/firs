from cargo import Cargo

cargo = Cargo(
    id="food_additives",
    type_name="string(STR_CARGO_NAME_FOOD_ADDITIVES)",
    unit_name="string(STR_CARGO_NAME_FOOD_ADDITIVES)",
    type_abbreviation="string(STR_CID_FOOD_ADDITIVES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID", "CC_COVERED_BULK", "CC_PIECE_GOODS", "CC_FOOD_GRADE"],
    cargo_label="ENUM",  # yes it's a terrible pun on several things at once - LordAro suggested it
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_FOOD_ADDITIVES)",
    penalty_lowerbound="20",
    single_penalty_length="255",
    price_factor=117,
    capacity_multiplier="1",
    icon_indices=(10, 1),
    sprites_complete=False,
)
