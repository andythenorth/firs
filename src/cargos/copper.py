from cargo import Cargo

cargo = Cargo(
    id="copper",
    type_name="string(STR_CARGO_NAME_COPPER)",
    unit_name="string(STR_CARGO_NAME_COPPER)",
    type_abbreviation="string(STR_CID_COPPER)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_FOOD_GRADE"],
    cargo_label="COPR",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_COPPER)",
    penalty_lowerbound="7",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=146,
    icon_indices=(8, 2),
    sprites_complete=True,
)
