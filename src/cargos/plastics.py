from cargo import Cargo

cargo = Cargo(
    id="plastics",
    type_name="string(STR_CARGO_PLASTICS_NAME)",
    unit_name="string(STR_CARGO_PLASTICS_NAME)",
    type_abbreviation="string(STR_CARGO_PLASTICS_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_LIQUID_BULK", "CC_COVERED_BULK", "CC_POWDER_BULK", "CC_NON_POTABLE"],
    cargo_label="PLAS",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_PLASTICS_CARGO_UNIT)",
    penalty_lowerbound="12",
    single_penalty_length="36",
    capacity_multiplier="1",
    price_factor=133,
    icon_indices=(6, 4),
    sprites_complete=True,
)
