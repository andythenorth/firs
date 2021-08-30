from cargo import Cargo

cargo = Cargo(
    id="coal",
    type_name="TTD_STR_CARGO_PLURAL_COAL",
    unit_name="TTD_STR_CARGO_SINGULAR_COAL",
    type_abbreviation="TTD_STR_ABBREV_COAL",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK)",
    cargo_label="COAL",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="TTD_STR_QUANTITY_COAL",
    penalty_lowerbound="40",
    single_penalty_length="255",
    price_factor=86,
    capacity_multiplier="1",
    icon_indices=(1, 0),
    sprites_complete=True,
)
