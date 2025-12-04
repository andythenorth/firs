from cargo import Cargo

cargo = Cargo(
    id="frontlinesupplies",
    type_name="string(STR_CARGO_NAME_FRONTSUP)",
    unit_name="string(STR_CARGO_NAME_FRONTSUP)",
    type_abbreviation="string(STR_CID_FRONTSUP)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.5",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="FRNT",
    units_of_cargo="TTD_STR_CRATES",
    items_of_cargo="string(STR_CARGO_UNIT_FRONTSUP)",
    penalty_lowerbound="0",
    single_penalty_length="8",
    price_factor=250,
    capacity_multiplier="2",
    icon_indices=(5, 0),
    # used by FIRS GS
    vulcan_town_effect="VTE_HAPPINESS",
    sprites_complete=True,
)
