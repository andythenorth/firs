from cargo import Cargo

cargo = Cargo(
    id="logs",
    type_name="string(STR_CARGO_NAME_LOGS)",
    unit_name="string(STR_CARGO_NAME_LOGS)",
    type_abbreviation="string(STR_CID_LOGS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    # for legacy compatibility WOOD label is used as there is very wide support for it
    # but as a name string that has proven ambiguous in games - conflates with finished wood products (lumber, finished timber etc)
    cargo_label="WOOD",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_LOGS)",
    penalty_lowerbound="24",
    single_penalty_length="255",
    price_factor=104,
    capacity_multiplier="1",
    icon_indices=(8, 0),
)
