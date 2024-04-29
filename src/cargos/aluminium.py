from cargo import Cargo

cargo = Cargo(
    id="aluminium",
    type_name="string(STR_CARGO_NAME_ALUMINIUM)",
    unit_name="string(STR_CARGO_NAME_ALUMINIUM)",
    type_abbreviation="string(STR_CID_ALUMINIUM)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="ALUM",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_ALUMINIUM)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=140,
    icon_indices=(0, 6),
    sprites_complete=True,
)
