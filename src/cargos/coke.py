from cargo import Cargo

cargo = Cargo(
    id="coke",
    type_name="string(STR_CARGO_COKE_NAME)",
    unit_name="string(STR_CARGO_COKE_NAME)",
    type_abbreviation="string(STR_CARGO_COKE_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_NON_POTABLE"],
    cargo_label="COKE",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_COKE_CARGO_UNIT)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=97,
    capacity_multiplier="1",
    icon_indices=(1, 3),
    sprites_complete=True,
)
