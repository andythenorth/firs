from cargo import Cargo

cargo = Cargo(
    id="oxygen",
    type_name="string(STR_CARGO_NAME_OXYGEN)",
    unit_name="string(STR_CARGO_NAME_OXYGEN)",
    type_abbreviation="string(STR_CID_OXYGEN)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_LIQUID)",
    cargo_label="O2__",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_OXYGEN)",
    penalty_lowerbound="22",
    single_penalty_length="44",
    price_factor=135,
    capacity_multiplier="1",
    icon_indices=(1, 5),
    sprites_complete=True,
)
