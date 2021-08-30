from cargo import Cargo

cargo = Cargo(
    id="elastomer_products",
    type_name="string(STR_CARGO_NAME_ELASTOMER_PRODUCTS)",
    unit_name="string(STR_CARGO_NAME_ELASTOMER_PRODUCTS)",
    type_abbreviation="string(STR_CID_ELASTOMER_PRODUCTS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="ELAS",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_ELASTOMER_PRODUCTS)",
    penalty_lowerbound="7",
    single_penalty_length="255",
    price_factor=133,
    capacity_multiplier="1",
    icon_indices=(14, 2),
    sprites_complete=False,
)
