from cargo import Cargo

cargo = Cargo(
    id="scrap_metal",
    type_name="string(STR_CARGO_NAME_SCRAP_METAL)",
    unit_name="string(STR_CARGO_NAME_SCRAP_METAL)",
    type_abbreviation="string(STR_CID_SCRAP_METAL)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_BULK"],
    cargo_label="SCMT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_SCRAP_METAL)",
    penalty_lowerbound="36",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=107,
    icon_indices=(2, 1),
    sprites_complete=True,
)
