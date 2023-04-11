from cargo import Cargo

cargo = Cargo(
    id="wool",
    type_name="string(STR_CARGO_NAME_WOOL)",
    unit_name="string(STR_CARGO_NAME_WOOL)",
    type_abbreviation="string(STR_CID_WOOL)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.2",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS, CC_COVERED)",
    cargo_label="WOOL",
    units_of_cargo="TTD_STR_ITEMS",
    items_of_cargo="string(STR_CARGO_UNIT_WOOL)",
    penalty_lowerbound="8",
    single_penalty_length="48",
    price_factor=111,
    capacity_multiplier="1",
    icon_indices=(4, 1),
    sprites_complete=True,
)
