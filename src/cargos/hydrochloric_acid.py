from cargo import Cargo

cargo = Cargo(
    id="hydrochloric_acid",
    type_name="string(STR_CARGO_NAME_HYDROCHLORIC_ACID)",
    unit_name="string(STR_CARGO_NAME_HYDROCHLORIC_ACID)",
    type_abbreviation="string(STR_CID_HYDROCHLORIC_ACID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.5",
    is_freight="1",
    cargo_classes = ["CC_LIQUID", "CC_NON_FOOD_GRADE"],
    cargo_label="HYAC",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_HYDROCHLORIC_ACID)",
    penalty_lowerbound="24",
    single_penalty_length="48",
    price_factor=109,
    capacity_multiplier="1",
    icon_indices=(4, 4),
    sprites_complete=False,
)
