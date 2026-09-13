from cargo import Cargo

cargo = Cargo(
    id="steel",
    type_name="string(STR_CARGO_STEEL_NAME)",
    unit_name="string(STR_CARGO_STEEL_NAME)",
    type_abbreviation="string(STR_CARGO_STEEL_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="STEL",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_STEEL_CARGO_UNIT)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=127,
    icon_indices=(10, 0),
    # used by FIRS GS
    vulcan_town_effect="VTE_GROWTH",
    sprites_complete=True,
)
