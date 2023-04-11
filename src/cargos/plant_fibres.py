from cargo import Cargo

cargo = Cargo(
    id="plant_fibres",
    type_name="string(STR_CARGO_NAME_FIBRES)",
    unit_name="string(STR_CARGO_NAME_FIBRES)",
    type_abbreviation="string(STR_CID_FIBRES)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.2",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK, CC_PIECE_GOODS)",
    cargo_label="FICR",
    units_of_cargo="TTD_STR_ITEMS",
    items_of_cargo="string(STR_CARGO_UNIT_FIBRES)",
    penalty_lowerbound="10",
    single_penalty_length=36,
    capacity_multiplier="1",
    price_factor=107,
    icon_indices=(3, 1),
    sprites_complete=False,
)
