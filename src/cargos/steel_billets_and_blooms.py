from cargo import Cargo

cargo = Cargo(
    id="steel_billets_and_blooms",
    type_name="string(STR_CARGO_NAME_STEEL_BILLETS_AND_BLOOMS)",
    unit_name="string(STR_CARGO_NAME_STEEL_BILLETS_AND_BLOOMS)",
    type_abbreviation="string(STR_CID_STEEL_BILLETS_AND_BLOOMS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="STBL",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_STEEL_BILLETS_AND_BLOOMS)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=130,
    icon_indices=(12, 4),
    sprites_complete=True,
)
