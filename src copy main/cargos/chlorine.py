from cargo import Cargo

cargo = Cargo(
    id="chlorine",
    type_name="string(STR_CARGO_NAME_CHLORINE)",
    unit_name="string(STR_CARGO_NAME_CHLORINE)",
    type_abbreviation="string(STR_CID_CHLORINE)",
    sprite="NEW_CARGO_SPRITE",
    weight="2.0",
    is_freight="1",
    cargo_classes = ["CC_GAS_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="CHLO",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_CHLORINE)",
    penalty_lowerbound="20",
    single_penalty_length="40",
    price_factor=115,
    capacity_multiplier="1",
    icon_indices=(2, 4),
    sprites_complete=True,
)
