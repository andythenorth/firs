from cargo import Cargo

cargo = Cargo(
    id="tinplate",
    type_name="string(STR_CARGO_TINPLATE_NAME)",
    unit_name="string(STR_CARGO_TINPLATE_NAME)",
    type_abbreviation="string(STR_CARGO_TINPLATE_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="TINP",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_TINPLATE_CARGO_UNIT)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=149,
    icon_indices=(14, 7),
    sprites_complete=True,
)
