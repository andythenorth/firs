from cargo import Cargo

# cast iron
cargo = Cargo(
    id="cast_iron",
    type_name="string(STR_CARGO_NAME_CAST_IRON)",
    unit_name="string(STR_CARGO_NAME_CAST_IRON)",
    type_abbreviation="string(STR_CID_CAST_IRON)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="CSTI",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_CAST_IRON)",
    penalty_lowerbound="15",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=120,
    icon_indices=(0, 5),
    sprites_complete=True,
)
