from cargo import Cargo

cargo = Cargo(
    id="acid",
    type_name="string(STR_CARGO_NAME_ACID)",
    unit_name="string(STR_CARGO_NAME_ACID)",
    type_abbreviation="string(STR_CID_ACID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.5",  # extra realism, per forum suggestion Nov 2017
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="ACID",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_ACID)",
    penalty_lowerbound="24",
    single_penalty_length="48",
    price_factor=109,
    capacity_multiplier="1",
    icon_indices=(4, 4),
    sprites_complete=True,
)
