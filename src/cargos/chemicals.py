from cargo import Cargo

cargo = Cargo(
    id="chemicals",
    type_name="string(STR_CARGO_NAME_CHEMICALS)",
    unit_name="string(STR_CARGO_NAME_CHEMICALS)",
    type_abbreviation="string(STR_CID_CHEMICALS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    # very generic organic and inorganic chemicals, wide refits
    cargo_classes = ["CC_LIQUID_BULK", "CC_GAS_BULK", "CC_COVERED_BULK", "CC_POWDER_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="CHEM",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_CHEMICALS)",
    penalty_lowerbound="20",
    single_penalty_length="255",
    price_factor=115,
    capacity_multiplier="1",
    icon_indices=(10, 1),
    sprites_complete=True,
)
