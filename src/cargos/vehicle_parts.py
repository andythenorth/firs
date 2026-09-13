from cargo import Cargo

cargo = Cargo(
    id="vehicle_parts",
    type_name="string(STR_CARGO_VEHICLE_PARTS_NAME)",
    unit_name="string(STR_CARGO_VEHICLE_PARTS_NAME)",
    type_abbreviation="string(STR_CARGO_VEHICLE_PARTS_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="VPTS",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_VEHICLE_PARTS_CARGO_UNIT)",
    penalty_lowerbound="7",
    single_penalty_length="255",
    price_factor=151,
    capacity_multiplier="1",
    icon_indices=(14, 2),
    sprites_complete=True,
)
