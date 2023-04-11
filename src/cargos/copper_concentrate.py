from cargo import Cargo

cargo = Cargo(
    id="copper_concentrate",
    type_name="string(STR_CARGO_NAME_COPPER_CONCENTRATE)",
    unit_name="string(STR_CARGO_NAME_COPPER_CONCENTRATE)",
    type_abbreviation="string(STR_CID_COPPER_CONCENTRATE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK, CC_COVERED)",
    cargo_label="COCO",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_COPPER_CONCENTRATE)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=109,
    capacity_multiplier="1",
    icon_indices=(4, 4),
    sprites_complete=False,
)
