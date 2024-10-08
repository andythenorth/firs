from cargo import Cargo

cargo = Cargo(
    id="fertiliser",
    type_name="string(STR_CARGO_NAME_FERTILISER)",
    unit_name="string(STR_CARGO_NAME_FERTILISER)",
    type_abbreviation="string(STR_CID_FERTILISER)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS, CC_BULK)",
    cargo_label="FERT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_FERTILISER)",
    penalty_lowerbound="22",
    single_penalty_length="44",
    price_factor=123,
    capacity_multiplier="1",
    icon_indices=(3, 3),
    sprites_complete=True,
)
