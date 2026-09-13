from cargo import Cargo

# the specific petrochemical feedstock rather than the generic term for petroleum spirits

cargo = Cargo(
    id="light_hydrocarbons",
    type_name="string(STR_CARGO_LIGHT_HYDROCARBONS_NAME)",
    unit_name="string(STR_CARGO_LIGHT_HYDROCARBONS_NAME)",
    type_abbreviation="string(STR_CARGO_LIGHT_HYDROCARBONS_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    # gas bulk included to cover lightest hydrocarbons which are transported as liquified gas under pressure
    cargo_classes = ["CC_LIQUID_BULK", "CC_GAS_BULK", "CC_NON_POTABLE"],
    cargo_label="LHYC",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_LIGHT_HYDROCARBONS_CARGO_UNIT)",
    penalty_lowerbound="18",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=103,
    icon_indices=(8, 7),
    sprites_complete=True,
)
