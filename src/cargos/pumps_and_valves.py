from cargo import Cargo

cargo = Cargo(
    id="pumps_and_valves",
    type_name="string(STR_CARGO_NAME_PUMPS_AND_VALVES)",
    unit_name="string(STR_CARGO_NAME_PUMPS_AND_VALVES)",
    type_abbreviation="string(STR_CID_PUMPS_AND_VALVES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="PUMP",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_PUMPS_AND_VALVES)",
    penalty_lowerbound="7",
    single_penalty_length="255",
    price_factor=152,
    capacity_multiplier="1",
    icon_indices=(3, 6),
    sprites_complete=True,
)
