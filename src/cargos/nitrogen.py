from cargo import Cargo

cargo = Cargo(
    id="nitrogen",
    type_name="string(STR_CARGO_NITROGEN_NAME)",
    unit_name="string(STR_CARGO_NITROGEN_NAME)",
    type_abbreviation="string(STR_CARGO_NITROGEN_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_GAS_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="N7__",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_NITROGEN_CARGO_UNIT)",
    penalty_lowerbound="22",
    single_penalty_length="44",
    price_factor=136,
    capacity_multiplier="1",
    icon_indices=(1, 6),
    sprites_complete=True,
)
