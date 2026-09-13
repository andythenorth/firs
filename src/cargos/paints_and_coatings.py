from cargo import Cargo

cargo = Cargo(
    id="paints_and_coatings",
    type_name="string(STR_CARGO_PAINTS_AND_COATINGS_NAME)",
    unit_name="string(STR_CARGO_PAINTS_AND_COATINGS_NAME)",
    type_abbreviation="string(STR_CARGO_PAINTS_AND_COATINGS_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="COAT",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_PAINTS_AND_COATINGS_CARGO_UNIT)",
    penalty_lowerbound="20",
    single_penalty_length="255",
    price_factor=134,
    capacity_multiplier="1",
    icon_indices=(5, 5),
    sprites_complete=True,
)
