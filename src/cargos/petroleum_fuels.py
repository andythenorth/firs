from cargo import Cargo

cargo = Cargo(
    id="petroleum_fuels",
    type_name="string(STR_CARGO_NAME_PETROLEUM_FUELS)",
    unit_name="string(STR_CARGO_NAME_PETROLEUM_FUELS)",
    type_abbreviation="string(STR_CID_PETROLEUM_FUELS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    # gas bulk included to cover LPG (butane etc) which petroleum fuels encompasses
    cargo_classes = ["CC_LIQUID_BULK", "CC_GAS_BULK", "CC_NON_POTABLE"],
    cargo_label="PETR",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_PETROL)",
    penalty_lowerbound="18",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=145,
    icon_indices=(12, 1),
    sprites_complete=True,
)
