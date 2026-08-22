from cargo import Cargo

cargo = Cargo(
    id="seafood_products",
    type_name="string(STR_CARGO_NAME_SEAFOOD_PRODUCTS)",
    unit_name="string(STR_CARGO_NAME_SEAFOOD_PRODUCTS)",
    type_abbreviation="TTD_STR_ABBREV_FOOD", # CABBAGE
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_PIECE_GOODS", "CC_POTABLE", "CC_REFRIGERATED"],
    cargo_label="CLAM",
    units_of_cargo="TTD_STR_TONS", # CABBAGE
    items_of_cargo="string(STR_CARGO_UNIT_SEAFOOD_PRODUCTS)",
    penalty_lowerbound="0",
    single_penalty_length="20",
    price_factor=168,
    capacity_multiplier="1",
    icon_indices=(12, 0), # CABBAGE
    # used by FIRS GS
    vulcan_town_effect="VTE_HAPPINESS", # CABBAGE
    sprites_complete=False,
)
