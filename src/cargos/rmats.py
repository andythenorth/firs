from cargo import Cargo

cargo = Cargo(
    id="rmats",
    type_name="string(STR_CARGO_NAME_RMATS)",
    unit_name="string(STR_CARGO_NAME_RMATS)",
    type_abbreviation="string(STR_CID_RMATS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="RMAT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_RMATS)",
    penalty_lowerbound="10",
    single_penalty_length="255",
    price_factor=150,
    capacity_multiplier="1",
    icon_indices=(12, 4),
    # used by FIRS GS
    sprites_complete=True,
)
