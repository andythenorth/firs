from cargo import Cargo

cargo = Cargo(
    id="alcohol",
    type_name="string(STR_CARGO_NAME_ALCOHOL)",
    unit_name="string(STR_CARGO_NAME_ALCOHOL)",
    type_abbreviation="string(STR_CID_ALCOHOL)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.1",  # such realism - I looked up the weight of 1L of beer, heavier than water :P
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_PIECE_GOODS", "CC_LIQUID_BULK", "CC_POTABLE"],
    cargo_label="BEER",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_ALCOHOL)",
    penalty_lowerbound="9",
    single_penalty_length="36",
    price_factor=166,
    capacity_multiplier="1",
    icon_indices=(7, 0),
    # used by FIRS GS
    vulcan_town_effect="VTE_HAPPINESS",
    sprites_complete=True,
)
