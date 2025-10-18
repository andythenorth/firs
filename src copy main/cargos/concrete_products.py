from cargo import Cargo

cargo = Cargo(
    id="concrete_products",
    type_name="string(STR_CARGO_NAME_CONCRETE_PRODUCTS)",
    unit_name="string(STR_CARGO_NAME_CONCRETE_PRODUCTS)",
    type_abbreviation="string(STR_CID_CONCRETE_PRODUCTS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="CCPR",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_CONCRETE_PRODUCTS)",
    penalty_lowerbound="12",
    single_penalty_length="255",
    price_factor=150,
    capacity_multiplier="1",
    icon_indices=(5, 6),
    # used by FIRS GS
    vulcan_town_effect="VTE_GROWTH",
    sprites_complete=True,
)
