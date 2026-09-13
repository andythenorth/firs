from cargo import Cargo

cargo = Cargo(
    id="welding_consumables",
    type_name="string(STR_CARGO_WELDING_CONSUMABLES_NAME)",
    unit_name="string(STR_CARGO_WELDING_CONSUMABLES_NAME)",
    type_abbreviation="string(STR_CARGO_WELDING_CONSUMABLES_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_EXPRESS", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="WELD",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_WELDING_CONSUMABLES_CARGO_UNIT)",
    penalty_lowerbound="22",
    single_penalty_length="44",
    price_factor=171,
    capacity_multiplier="1",
    icon_indices=(7, 6),
    sprites_complete=True,
)
