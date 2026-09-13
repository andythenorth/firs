from cargo import Cargo

cargo = Cargo(
    id="cleaning_agents",
    type_name="string(STR_CARGO_CLEANING_AGENTS_NAME)",
    unit_name="string(STR_CARGO_CLEANING_AGENTS_NAME)",
    type_abbreviation="string(STR_CARGO_CLEANING_AGENTS_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="SOAP",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_CLEANING_AGENTS_CARGO_UNIT)",
    penalty_lowerbound="20",
    single_penalty_length="255",
    price_factor=121,
    capacity_multiplier="1",
    icon_indices=(9, 5),
    sprites_complete=True,
)
