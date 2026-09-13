from cargo import Cargo

cargo = Cargo(
    id="vehicle_engines",
    type_name="string(STR_CARGO_VEHICLE_ENGINES_NAME)",
    unit_name="string(STR_CARGO_VEHICLE_ENGINES_NAME)",
    type_abbreviation="string(STR_CARGO_VEHICLE_ENGINES_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="VENG",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_VEHICLE_ENGINES_CARGO_UNIT)",
    penalty_lowerbound="6",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=156,
    icon_indices=(9, 4),
    sprites_complete=True,
)
