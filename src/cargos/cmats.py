from cargo import Cargo

cargo = Cargo(
    id="cmats",
    type_name="string(STR_CARGO_NAME_CMATS)",
    unit_name="string(STR_CARGO_NAME_CMATS)",
    type_abbreviation="string(STR_CID_CMATS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="CMAT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_CMATS)",
    penalty_lowerbound="10",
    single_penalty_length="255",
    price_factor=110,
    capacity_multiplier="1",
    icon_indices=(15, 3),
    # used by FIRS GS
    sprites_complete=True,
)
