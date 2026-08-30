from cargo import Cargo

cargo = Cargo(
    id="food_additives",
    type_name="string(STR_CARGO_NAME_FOOD_ADDITIVES)",
    unit_name="string(STR_CARGO_NAME_FOOD_ADDITIVES)",
    type_abbreviation="string(STR_CID_FOOD_ADDITIVES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    # lot of classes eh?
    cargo_classes = ["CC_EXPRESS", "CC_PIECE_GOODS", "CC_LIQUID_BULK", "CC_COVERED_BULK", "CC_POWDER_BULK", "CC_GAS_BULK", "CC_REFRIGERATED", "CC_POTABLE"],
    cargo_label="ENUM",  # yes it's a terrible pun on several things at once - LordAro suggested it
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_FOOD_ADDITIVES)",
    penalty_lowerbound="20",
    single_penalty_length="255",
    price_factor=125,
    capacity_multiplier="1",
    icon_indices=(1, 8),
    sprites_complete=True,
)
