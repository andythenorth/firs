from cargo import Cargo

cargo = Cargo(
    id="steel_forgings",
    type_name="string(STR_CARGO_STEEL_FORGINGS_NAME)",
    unit_name="string(STR_CARGO_STEEL_FORGINGS_NAME)",
    type_abbreviation="string(STR_CARGO_STEEL_FORGINGS_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="FOCA",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_STEEL_FORGINGS_CARGO_UNIT)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=147,
    icon_indices=(4, 6),
    sprites_complete=True,
)
