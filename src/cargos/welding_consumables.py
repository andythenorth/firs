from cargo import Cargo

cargo = Cargo(
    id="welding_consumables",
    type_name="string(STR_CARGO_NAME_WELDING_CONSUMABLES)",
    unit_name="string(STR_CARGO_NAME_WELDING_CONSUMABLES)",
    type_abbreviation="string(STR_CID_WELDING_CONSUMABLES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_LIQUID, CC_HAZARDOUS)",
    cargo_label="WELD",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_WELDING_CONSUMABLES)",
    penalty_lowerbound="22",
    single_penalty_length="44",
    price_factor=171,
    capacity_multiplier="1",
    icon_indices=(1, 5),
)
