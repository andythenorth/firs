from cargo import Cargo

cargo = Cargo(
    id="forgings_and_castings",
    type_name="string(STR_CARGO_NAME_FORGINGS_AND_CASTINGS)",
    unit_name="string(STR_CARGO_NAME_FORGINGS_AND_CASTINGS)",
    type_abbreviation="string(STR_CID_FORGINGS_AND_CASTINGS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS"],
    cargo_label="FOCA",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_FORGINGS_AND_CASTINGS)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=147,
    icon_indices=(4, 6),
    sprites_complete=True,
)
