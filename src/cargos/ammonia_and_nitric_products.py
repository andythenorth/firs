from cargo import Cargo

# basket cargo covering ammonia, nitric acid, urea, and other ammonia derivatives

cargo = Cargo(
    id="ammonia_and_nitric_products",
    type_name="string(STR_CARGO_NAME_AMMONIA_AND_NITRIC_PRODUCTS)",
    unit_name="string(STR_CARGO_NAME_AMMONIA_AND_NITRIC_PRODUCTS)",
    type_abbreviation="string(STR_CID_AMMONIA_AND_NITRIC_PRODUCTS)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.60",  # extra realism per forum suggestion
    is_freight="1",
    # mostly liquid, gas, but urea is dry bulk
    cargo_classes = ["CC_COVERED_BULK", "CC_LIQUID_BULK", "CC_GAS_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="ANPR", # was NH3_, but too specific
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_AMMONIA_AND_NITRIC_PRODUCTS)",
    penalty_lowerbound="32",
    single_penalty_length="64",
    price_factor=119,
    capacity_multiplier="1",
    icon_indices=(15, 4),
    sprites_complete=True,
)
