from cargo import Cargo

cargo = Cargo(
    id="potash",
    type_name="string(STR_CARGO_NAME_POTASH)",
    unit_name="string(STR_CARGO_NAME_POTASH)",
    type_abbreviation="string(STR_CID_POTASH)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK)",
    cargo_label="POTA",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_POTASH)",
    penalty_lowerbound="40",
    single_penalty_length="255",
    price_factor=102,
    capacity_multiplier="1",
    icon_indices=(2, 5),
    sprites_complete=True,
)
