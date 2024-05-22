from cargo import Cargo

cargo = Cargo(
    id="welding_consumables",
    type_name="string(STR_CARGO_NAME_WELDING_CONSUMABLES)",
    unit_name="string(STR_CARGO_NAME_WELDING_CONSUMABLES)",
    type_abbreviation="string(STR_CID_WELDING_CONSUMABLES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_LIQUID, CC_EXPRESS, CC_PIECE_GOODS)",
    cargo_label="WELD",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_WELDING_CONSUMABLES)",
    penalty_lowerbound="22",
    single_penalty_length="44",
    price_factor=171,
    capacity_multiplier="1",
    icon_indices=(7, 6),
    sprites_complete=True,
)
