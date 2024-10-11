from cargo import Cargo

cargo = Cargo(
    id="clay",
    type_name="string(STR_CARGO_NAME_CLAY)",
    unit_name="string(STR_CARGO_NAME_CLAY)",
    type_abbreviation="string(STR_CID_CLAY)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_BULK"],
    cargo_label="CLAY",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_CLAY)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=100,
    capacity_multiplier="1",
    icon_indices=(9, 1),
    sprites_complete=True,
)
