from cargo import Cargo

cargo = Cargo(
    id="shippables",
    type_name="string(STR_CARGO_NAME_SHIPPABLES)",
    unit_name="string(STR_CARGO_NAME_SHIPPABLES)",
    type_abbreviation="string(STR_CID_SHIPPABLES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="SHIP",
    units_of_cargo="TTD_STR_CRATES",
    items_of_cargo="string(STR_CARGO_UNIT_SHIPPABLES)",
    penalty_lowerbound="12",
    single_penalty_length="255",
    price_factor=133,
    capacity_multiplier="1",
    icon_indices=(1, 1),
    # used by FIRS GS
    vulcan_town_effect="VTE_GROWTH",
    sprites_complete=True,
)
