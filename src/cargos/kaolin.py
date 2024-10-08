from cargo import Cargo

cargo = Cargo(
    id="kaolin",
    type_name="string(STR_CARGO_NAME_KAOLIN)",
    unit_name="string(STR_CARGO_NAME_KAOLIN)",
    type_abbreviation="string(STR_CID_KAOLIN)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK, CC_LIQUID)",
    cargo_label="KAOL",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_KAOLIN)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=100,
    capacity_multiplier="1",
    icon_indices=(5, 3),
    sprites_complete=True,
)
