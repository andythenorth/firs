from cargo import Cargo

cargo = Cargo(
    id="paper",
    type_name="TTD_STR_CARGO_PLURAL_PAPER",
    unit_name="TTD_STR_CARGO_SINGULAR_PAPER",
    type_abbreviation="TTD_STR_ABBREV_PAPER",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_FOOD_GRADE"],
    cargo_label="PAPR",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="TTD_STR_QUANTITY_PAPER",
    penalty_lowerbound="12",
    single_penalty_length="60",
    price_factor=143,
    capacity_multiplier="1",
    icon_indices=(5, 2),
    sprites_complete=True,
)
