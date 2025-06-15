from cargo import Cargo

cargo = Cargo(
    id="vehicle_bodies",
    type_name="string(STR_CARGO_NAME_VEHICLE_BODIES)",
    unit_name="string(STR_CARGO_NAME_VEHICLE_BODIES)",
    type_abbreviation="string(STR_CID_VEHICLE_BODIES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="VBOD",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_VEHICLE_BODIES)",
    penalty_lowerbound="5",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=147,
    icon_indices=(14, 3),
)
