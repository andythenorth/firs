from cargo import Cargo

cargo = Cargo(
    id="ferroalloys",
    type_name="string(STR_CARGO_FERROALLOYS_NAME)",
    unit_name="string(STR_CARGO_FERROALLOYS_NAME)",
    type_abbreviation="string(STR_CARGO_FERROALLOYS_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="FEAL",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_FERROALLOYS_CARGO_UNIT)",
    penalty_lowerbound="40",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=106,
    icon_indices=(8, 4),
    sprites_complete=True,
)
