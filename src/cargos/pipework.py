from cargo import Cargo

cargo = Cargo(
    id="pipework",
    type_name="string(STR_CARGO_NAME_PIPEWORK)",
    unit_name="string(STR_CARGO_NAME_PIPEWORK)",
    type_abbreviation="string(STR_CID_PIPEWORK)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS, CC_OVERSIZED)",
    cargo_label="PPWK",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_PIPEWORK)",
    penalty_lowerbound="30",
    single_penalty_length="42",
    price_factor=161,
    capacity_multiplier="1",
    icon_indices=(2, 6),
    # used by FIRS GS
    vulcan_town_effect="VTE_GROWTH",
    sprites_complete=True,
)
