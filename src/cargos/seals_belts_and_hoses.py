from cargo import Cargo

cargo = Cargo(
    id="seals_belts_and_hoses",
    type_name="string(STR_CARGO_NAME_SEALS_HOSES_AND_BELTS)",
    unit_name="string(STR_CARGO_NAME_SEALS_HOSES_AND_BELTS)",
    type_abbreviation="string(STR_CID_SEALS_HOSES_AND_BELTS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="SEAL", # could have been HOSE or BELT or SHAB, but eh
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_SEALS_HOSES_AND_BELTS)",
    penalty_lowerbound="7",
    single_penalty_length="255",
    price_factor=133,
    capacity_multiplier="1",
    icon_indices=(13, 5),
    sprites_complete=True,
)
