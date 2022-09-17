from cargo import Cargo

cargo = Cargo(
    id="pulp_wood",
    type_name="string(STR_CARGO_NAME_PULP_WOOD)",
    unit_name="string(STR_CARGO_NAME_PULP_WOOD)",
    type_abbreviation="string(STR_CID_PULP_WOOD)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="PULP",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_PULP_WOOD)",
    penalty_lowerbound="24",
    single_penalty_length="255",
    price_factor=95,
    capacity_multiplier="1",
    icon_indices=(8, 0),
)
