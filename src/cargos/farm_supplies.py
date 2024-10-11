from cargo import Cargo

cargo = Cargo(
    id="farm_supplies",
    type_name="string(STR_CARGO_NAME_FARM_SUPPLIES)",
    unit_name="string(STR_CARGO_NAME_FARM_SUPPLIES)",
    type_abbreviation="string(STR_CID_FARM_SUPPLIES)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.65",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_PIECE_GOODS"],
    cargo_label="FMSP",
    units_of_cargo="TTD_STR_CRATES",
    items_of_cargo="string(STR_CARGO_UNIT_FMSP)",
    penalty_lowerbound="2",
    single_penalty_length="32",
    price_factor=174,
    capacity_multiplier="1",
    icon_indices=(8, 1),
    sprites_complete=True,
)
