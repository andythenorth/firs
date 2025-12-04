from cargo import Cargo

cargo = Cargo(
    id="pcmats",
    type_name="string(STR_CARGO_NAME_PCMATS)",
    unit_name="string(STR_CARGO_NAME_PCMATS)",
    type_abbreviation="string(STR_CID_PCMATS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="PCMT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_PCMATS)",
    penalty_lowerbound="10",
    single_penalty_length="255",
    price_factor=160,
    capacity_multiplier="1",
    icon_indices=(11, 5),
    # used by FIRS GS
    sprites_complete=True,
)
