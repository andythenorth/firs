from cargo import Cargo

cargo = Cargo(
    id="nickel",
    type_name="string(STR_CARGO_NAME_NICKEL)",
    unit_name="string(STR_CARGO_NAME_NICKEL)",
    type_abbreviation="string(STR_CID_NICKEL)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS"],
    cargo_label="NICK",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_NICKEL)",
    penalty_lowerbound="15",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=141,
    icon_indices=(15, 3),
    sprites_complete=False,
)
