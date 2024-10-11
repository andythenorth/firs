from cargo import Cargo

cargo = Cargo(
    id="coffee",
    type_name="string(STR_CARGO_NAME_COFFEE)",
    unit_name="string(STR_CARGO_NAME_COFFEE)",
    type_abbreviation="string(STR_CID_COFFEE)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.25",  # IRL coffee is lighter even than this, but eh
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_EXPRESS"],
    cargo_label="JAVA",
    units_of_cargo="TTD_STR_BAGS",
    items_of_cargo="string(STR_CARGO_UNIT_COFFEE)",
    penalty_lowerbound="0",
    single_penalty_length="26",
    price_factor=181,
    capacity_multiplier="1",
    icon_indices=(4, 2),
    sprites_complete=True,
)
