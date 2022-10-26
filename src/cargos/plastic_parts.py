from cargo import Cargo

cargo = Cargo(
    id="plastic_parts",
    type_name="string(STR_CARGO_NAME_PLASTIC_PARTS)",
    unit_name="string(STR_CARGO_NAME_PLASTIC_PARTS)",
    type_abbreviation="string(STR_CID_PLASTIC_PARTS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="PPAR",  
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_PLASTIC_PARTS)",
    penalty_lowerbound="16",
    single_penalty_length="120",
    price_factor=131,
    capacity_multiplier="1",
    icon_indices=(12, 5),
    sprites_complete=False,
)
