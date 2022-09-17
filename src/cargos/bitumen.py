from cargo import Cargo

cargo = Cargo(
    id="bitumen",
    type_name="string(STR_CARGO_NAME_BITUMEN)",
    unit_name="string(STR_CARGO_NAME_BITUMEN)",
    type_abbreviation="string(STR_CID_BITUMEN)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.8",
    is_freight="1",
    cargo_classes="bitmask(CC_LIQUID)",
    cargo_label="BITU",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_BITUMEN)",
    penalty_lowerbound="18",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=98,
    icon_indices=(12, 1),
)
