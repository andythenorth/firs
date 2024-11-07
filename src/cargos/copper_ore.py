from cargo import Cargo

cargo = Cargo(
    id="copper_ore",
    type_name="TTD_STR_CARGO_PLURAL_COPPER_ORE",
    unit_name="TTD_STR_CARGO_SINGULAR_COPPER_ORE",
    type_abbreviation="TTD_STR_ABBREV_COPPER_ORE",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_NON_POTABLE"],
    cargo_label="CORE",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="TTD_STR_QUANTITY_COPPER_ORE",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=89,
    capacity_multiplier="1",
    icon_indices=(1, 2),
    sprites_complete=True,
)
