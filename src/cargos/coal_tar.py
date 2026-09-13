from cargo import Cargo

cargo = Cargo(
    id="coal_tar",
    type_name="string(STR_CARGO_COAL_TAR_NAME)",
    unit_name="string(STR_CARGO_COAL_TAR_NAME)",
    type_abbreviation="string(STR_CARGO_COAL_TAR_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="CTAR",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_COAL_TAR_CARGO_UNIT)",
    penalty_lowerbound="64",
    single_penalty_length="255",
    price_factor=98,  # IRL coal tar is low value, but for gameplay it is transported in low amounts and needs a bonus
    capacity_multiplier="1",
    icon_indices=(14, 4),
    sprites_complete=True,
)
