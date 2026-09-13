from cargo import Cargo

cargo = Cargo(
    id="fish",
    type_name="string(STR_CARGO_FISH_NAME)",
    unit_name="string(STR_CARGO_FISH_NAME)",
    type_abbreviation="string(STR_CARGO_FISH_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_REFRIGERATED", "CC_POTABLE"],
    cargo_label="FISH",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_FISH_CARGO_UNIT)",
    penalty_lowerbound="0",
    single_penalty_length="18",
    price_factor=134,
    capacity_multiplier="1",
    icon_indices=(15, 0),
    sprites_complete=True,
)
