from cargo import Cargo

cargo = Cargo(
    id="glass",
    type_name="string(STR_CARGO_NAME_GLASS)",
    unit_name="string(STR_CARGO_NAME_GLASS)",
    type_abbreviation="string(STR_CID_GLASS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="GLAS",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_GLASS)",
    penalty_lowerbound="12",
    single_penalty_length="180",
    price_factor=132,
    capacity_multiplier="1",
    icon_indices=(10, 5),
    # used by FIRS GS
    vulcan_town_effect="VTE_GROWTH",
    sprites_complete=True,
)
