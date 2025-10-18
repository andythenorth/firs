from cargo import Cargo

cargo = Cargo(
    id="liquefied_petroleum_gas",
    type_name="string(STR_CARGO_NAME_LIQUEFIED_PETROLEUM_GAS)",
    unit_name="string(STR_CARGO_NAME_LIQUEFIED_PETROLEUM_GAS)",
    type_abbreviation="string(STR_CID_LIQUEFIED_PETROLEUM_GAS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_GAS_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="LPG_",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_LIQUEFIED_PETROLEUM_GAS)",
    penalty_lowerbound="22",
    single_penalty_length="44",
    price_factor=135,
    capacity_multiplier="1",
    icon_indices=(1, 5),
    sprites_complete=False,
)
