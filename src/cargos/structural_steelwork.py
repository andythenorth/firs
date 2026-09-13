from cargo import Cargo

cargo = Cargo(
    id="structural_steelwork",
    type_name="string(STR_CARGO_STRUCTURAL_STEELWORK_NAME)",
    unit_name="string(STR_CARGO_STRUCTURAL_STEELWORK_NAME)",
    type_abbreviation="string(STR_CARGO_STRUCTURAL_STEELWORK_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="STSW",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_STRUCTURAL_STEELWORK_CARGO_UNIT)",
    penalty_lowerbound="30",
    single_penalty_length="42",
    price_factor=148,
    capacity_multiplier="1",
    icon_indices=(7, 5),
    # used by FIRS GS
    vulcan_town_effect="VTE_GROWTH",
    sprites_complete=True,
)
