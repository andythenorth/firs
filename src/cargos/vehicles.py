from cargo import Cargo

cargo = Cargo(
    id="vehicles",
    type_name="string(STR_CARGO_NAME_VEHICLES)",
    unit_name="string(STR_CARGO_NAME_VEHICLES)",
    type_abbreviation="string(STR_CID_VEHICLES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="VEHI",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",  # intended for desert Steeltown, may not be appropriate in other cases
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_VEHICLES)",
    penalty_lowerbound="15",
    single_penalty_length="128",
    price_factor=164,
    capacity_multiplier="1",
    icon_indices=(15, 2),
)
