from cargo import Cargo

cargo = Cargo(
    id="nuts",
    type_name="string(STR_CARGO_NAME_NUTS)",
    unit_name="string(STR_CARGO_NAME_NUTS)",
    type_abbreviation="string(STR_CID_NUTS)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.25",  # IRL sacks of nuts are lighter even than this, but eh
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_FOOD_GRADE"],
    cargo_label="NUTS",
    units_of_cargo="TTD_STR_BAGS",
    items_of_cargo="string(STR_CARGO_UNIT_NUTS)",
    penalty_lowerbound="4",
    single_penalty_length="40",
    price_factor=113,
    capacity_multiplier="1",
    icon_indices=(12, 2),
    sprites_complete=True,
)
