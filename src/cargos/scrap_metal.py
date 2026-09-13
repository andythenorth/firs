from cargo import Cargo

cargo = Cargo(
    id="scrap_metal",
    type_name="string(STR_CARGO_SCRAP_METAL_NAME)",
    unit_name="string(STR_CARGO_SCRAP_METAL_NAME)",
    type_abbreviation="string(STR_CARGO_SCRAP_METAL_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_NON_POTABLE"],
    cargo_label="SCMT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_SCRAP_METAL_CARGO_UNIT)",
    penalty_lowerbound="36",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=107,
    icon_indices=(2, 1),
    sprites_complete=True,
)
