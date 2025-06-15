from cargo import Cargo

cargo = Cargo(
    id="ammonium_nitrate",
    type_name="string(STR_CARGO_NAME_AMMONIUM_NITRATE)",
    unit_name="string(STR_CARGO_NAME_AMMONIUM_NITRATE)",
    type_abbreviation="string(STR_CID_AMMONIUM_NITRATE)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.60",  # extra realism per forum suggestion
    is_freight="1",
    cargo_classes = ["CC_COVERED_BULK", "CC_PIECE_GOODS", "CC_GAS_BULK", "CC_NON_POTABLE"],
    cargo_label="NHNO",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_AMMONIUM_NITRATE)",
    penalty_lowerbound="32",
    single_penalty_length="64",
    price_factor=109,
    capacity_multiplier="1",
    icon_indices=(15, 4),
)
