from cargo import Cargo

cargo = Cargo(
    id="glass",
    type_name="string(STR_CARGO_NAME_GLASS)",
    unit_name="string(STR_CARGO_NAME_GLASS)",
    type_abbreviation="string(STR_CID_GLASS)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.65",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="GLAS",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_GLASS)",
    penalty_lowerbound="12",
    single_penalty_length="180",
    price_factor=132,
    capacity_multiplier="1",
    icon_indices=(7, 1),
)
