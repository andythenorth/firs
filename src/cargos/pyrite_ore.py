from cargo import Cargo

cargo = Cargo(
    id="pyrite_ore",
    type_name="string(STR_CARGO_NAME_PYRITE_ORE)",
    unit_name="string(STR_CARGO_NAME_PYRITE_ORE)",
    type_abbreviation="string(STR_CID_PYRITE_ORE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_NON_FOOD_GRADE"],
    cargo_label="PORE",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_PYRITE_ORE)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=87,
    capacity_multiplier="1",
    icon_indices=(13, 2),
    sprites_complete=True,
)
