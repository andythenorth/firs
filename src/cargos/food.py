from cargo import Cargo

cargo = Cargo(
    id="food",
    type_name="TTD_STR_CARGO_PLURAL_FOOD",
    unit_name="TTD_STR_CARGO_SINGULAR_FOOD",
    type_abbreviation="TTD_STR_ABBREV_FOOD",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_EXPRESS)",
    cargo_label="FOOD",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above     snowline
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="TTD_STR_QUANTITY_FOOD",
    penalty_lowerbound="0",
    single_penalty_length="20",
    price_factor=168,
    capacity_multiplier="1",
    icon_indices=(12, 0),
    # used by FIRS GS
    vulcan_town_effect="VTE_HAPPINESS",
    sprites_complete=True,
)
