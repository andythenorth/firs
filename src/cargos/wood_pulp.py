from cargo import Cargo

cargo = Cargo(
    id="wood_pulp",
    type_name="string(STR_CARGO_NAME_WOOD_PULP)",
    unit_name="string(STR_CARGO_NAME_WOOD_PULP)",
    type_abbreviation="string(STR_CID_WOOD_PULP)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.65",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="WDPP",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_WOOD_PULP)",
    penalty_lowerbound="16",
    single_penalty_length="120",
    price_factor=129,
    capacity_multiplier="1",
    icon_indices=(3, 8),
    sprites_complete=True,
)
