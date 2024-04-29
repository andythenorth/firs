from cargo import Cargo

cargo = Cargo(
    id="quicklime",
    type_name="string(STR_CARGO_NAME_QUICKLIME)",
    unit_name="string(STR_CARGO_NAME_QUICKLIME)",
    type_abbreviation="string(STR_CID_QUICKLIME)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK, CC_COVERED)",
    cargo_label="QLME",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_QUICKLIME)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    price_factor=112,
    capacity_multiplier="1",
    icon_indices=(9, 3),
    sprites_complete=True,
)
