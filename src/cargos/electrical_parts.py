from cargo import Cargo

cargo = Cargo(
    id="electrical_parts",
    type_name="string(STR_CARGO_ELECTRICAL_PARTS_NAME)",
    unit_name="string(STR_CARGO_ELECTRICAL_PARTS_NAME)",
    type_abbreviation="string(STR_CARGO_ELECTRICAL_PARTS_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="POWR",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_ELECTRICAL_PARTS_CARGO_UNIT)",
    penalty_lowerbound="7",
    single_penalty_length="255",
    price_factor=153,
    capacity_multiplier="1",
    icon_indices=(5, 4),
    sprites_complete=True,
)
