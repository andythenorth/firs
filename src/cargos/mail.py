from cargo import Cargo

cargo = Cargo(
    id="mail",
    type_name="TTD_STR_CARGO_PLURAL_MAIL",
    unit_name="TTD_STR_CARGO_SINGULAR_MAIL",
    type_abbreviation="TTD_STR_ABBREV_MAIL",
    sprite="NEW_CARGO_SPRITE",
    weight="0.25",
    is_freight="0",  # mail is not freight - consistent with default mail (setting '1' gives 'wrong' livery for mail cars)
    cargo_classes = ["CC_MAIL"],
    cargo_label="MAIL",
    town_growth_effect="TOWNGROWTH_MAIL",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_BAGS",
    items_of_cargo="TTD_STR_QUANTITY_MAIL",
    penalty_lowerbound="6",
    single_penalty_length="24",
    price_factor=167,
    capacity_multiplier="2",
    icon_indices=(2, 0),
)
