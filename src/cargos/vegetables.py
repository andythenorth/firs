from cargo import Cargo

cargo = Cargo(
    id="vegetables",
    type_name="string(STR_CARGO_NAME_VEGETABLES)",
    unit_name="string(STR_CARGO_NAME_VEGETABLES)",
    type_abbreviation="string(STR_CID_VEGETABLES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_REFRIGERATED", "CC_POTABLE"],
    cargo_label="VEG_",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_VEGETABLES)",
    penalty_lowerbound="0",
    single_penalty_length="26",
    price_factor=113,
    capacity_multiplier="1",
    icon_indices=(14, 0),
)
