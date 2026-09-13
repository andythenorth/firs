from cargo import Cargo

# barytes and fluorspar are often co-occuring

cargo = Cargo(
    id="barytes_and_fluorspar",
    type_name="string(STR_CARGO_BARYTES_AND_FLUORSPAR_NAME)",
    unit_name="string(STR_CARGO_BARYTES_AND_FLUORSPAR_NAME)",
    type_abbreviation="string(STR_CARGO_BARYTES_AND_FLUORSPAR_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_COVERED_BULK", "CC_POWDER_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="BYFL",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_BARYTES_AND_FLUORSPAR_CARGO_UNIT)",
    penalty_lowerbound="18",
    single_penalty_length="255",
    price_factor=118,
    capacity_multiplier="1",
    icon_indices=(8, 3), # CABBAGE
    sprites_complete=False,
)
