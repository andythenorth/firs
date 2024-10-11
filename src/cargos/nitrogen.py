from cargo import Cargo

cargo = Cargo(
    id="nitrogen",
    type_name="string(STR_CARGO_NAME_NITROGEN)",
    unit_name="string(STR_CARGO_NAME_NITROGEN)",
    type_abbreviation="string(STR_CID_NITROGEN)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID"],
    cargo_label="N7__",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_NITROGEN)",
    penalty_lowerbound="22",
    single_penalty_length="44",
    price_factor=136,
    capacity_multiplier="1",
    icon_indices=(1, 6),
    sprites_complete=True,
)
