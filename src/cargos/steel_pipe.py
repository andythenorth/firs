from cargo import Cargo

cargo = Cargo(
    id="steel_pipe",
    type_name="string(STR_CARGO_STEEL_PIPE_NAME)",
    unit_name="string(STR_CARGO_STEEL_PIPE_NAME)",
    type_abbreviation="string(STR_CARGO_STEEL_PIPE_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="STPP",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_STEEL_PIPE_CARGO_UNIT)",
    penalty_lowerbound="30",
    single_penalty_length="42",
    price_factor=145,
    capacity_multiplier="1",
    icon_indices=(7, 3),
    sprites_complete=True,
)
