from cargo import Cargo

cargo = Cargo(
    id="steel_wire_rod",
    type_name="string(STR_CARGO_NAME_STEEL_WIRE_ROD)",
    unit_name="string(STR_CARGO_NAME_STEEL_WIRE_ROD)",
    type_abbreviation="string(STR_CID_STEEL_WIRE_ROD)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="STWR",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_STEEL_WIRE_ROD)",
    penalty_lowerbound="30",
    single_penalty_length="42",
    price_factor=139,
    capacity_multiplier="1",
    icon_indices=(8, 5),
    sprites_complete=True,
)
