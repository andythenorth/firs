from cargo import Cargo

cargo = Cargo(
    id="apples",
    type_name="string(STR_CARGO_NAME_APPLES)",
    unit_name="string(STR_CARGO_NAME_APPLES)",
    type_abbreviation="string(STR_CID_APPLES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_PIECE_GOODS", "CC_REFRIGERATED", "CC_POTABLE"],
    cargo_label="AAPL",
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_APPLES)",
    penalty_lowerbound="0",
    single_penalty_length="26",
    price_factor=106,
    capacity_multiplier="1",
    icon_indices=(14, 0),
)
