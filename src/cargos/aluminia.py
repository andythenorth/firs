from cargo import Cargo

cargo = Cargo(
    id="aluminia",
    type_name="string(STR_CARGO_NAME_ALUMINIA)",
    unit_name="string(STR_CARGO_NAME_ALUMINIA)",
    type_abbreviation="string(STR_CID_ALUMINIA)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_NON_POTABLE"],
    cargo_label="ALO_",  # Aluminium Oxide
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_ALUMINIA)",
    penalty_lowerbound="15",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=98,
    icon_indices=(1, 7),
    sprites_complete=False,
)
