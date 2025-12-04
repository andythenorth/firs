from cargo import Cargo

cargo = Cargo(
    id="itemcrates",
    type_name="string(STR_CARGO_NAME_ICRATES)",
    unit_name="string(STR_CARGO_NAME_ICRATES)",
    type_abbreviation="string(STR_CID_ICRATES)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.5",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="ITEM",
    units_of_cargo="TTD_STR_CRATES",
    items_of_cargo="string(STR_CARGO_UNIT_ICRATES)",
    penalty_lowerbound="10",
    single_penalty_length="56",
    price_factor=169,
    capacity_multiplier="2",
    icon_indices=(5, 0),
    # used by FIRS GS
    vulcan_town_effect="VTE_HAPPINESS",
    sprites_complete=True,
)
