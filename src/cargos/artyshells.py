from cargo import Cargo

cargo = Cargo(
    id="artyshells",
    type_name="string(STR_CARGO_NAME_ARTYSHELLS)",
    unit_name="string(STR_CARGO_NAME_ARTYSHELLS)",
    type_abbreviation="string(STR_CID_ARTYSHELLS)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.5",
    is_freight="1",
    # armoured is a deliberate choice for explosives, tested with 10 of the major vehicle grfs in 2024, worked well
    cargo_classes = ["CC_EXPRESS", "CC_PIECE_GOODS", "CC_FLATBED", "CC_ARMOURED", "CC_NON_POTABLE"],
    cargo_label="ARTY",
    units_of_cargo="TTD_STR_CRATES",
    items_of_cargo="string(STR_CARGO_UNIT_ARTYSHELLS)",
    penalty_lowerbound="6",
    single_penalty_length="42",
    price_factor=180,
    capacity_multiplier="1",
    allow_animated_pixels=True,  # explosives uses fire cycle pixels, by design, so suppress NML pixel warnings
    icon_indices=(2, 3),
    sprites_complete=True,
)
