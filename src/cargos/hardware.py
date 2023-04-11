from cargo import Cargo

cargo = Cargo(
    id="hardware",
    type_name="string(STR_CARGO_NAME_HARDWARE)",
    unit_name="string(STR_CARGO_NAME_HARDWARE)",
    type_abbreviation="string(STR_CID_HARDWARE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="HWAR",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_HARDWARE)",
    penalty_lowerbound="7",
    single_penalty_length="255",
    price_factor=165,
    capacity_multiplier="1",
    icon_indices=(8, 6),
    # used by FIRS GS
    vulcan_town_effect="VTE_GROWTH",
    sprites_complete=True,
)
