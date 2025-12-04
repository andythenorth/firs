from cargo import Cargo

cargo = Cargo(
    id="bmats",
    type_name="string(STR_CARGO_NAME_BMATS)",
    unit_name="string(STR_CARGO_NAME_BMATS)",
    type_abbreviation="string(STR_CID_BMATS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="BMAT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_BMATS)",
    penalty_lowerbound="10",
    single_penalty_length="255",
    price_factor=100,
    capacity_multiplier="1",
    icon_indices=(6, 1),
    # used by FIRS GS
    sprites_complete=True,
)
