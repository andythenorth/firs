from cargo import Cargo

cargo = Cargo(
    id="livestock",
    type_name="TTD_STR_CARGO_PLURAL_LIVESTOCK",
    unit_name="TTD_STR_CARGO_SINGULAR_LIVESTOCK",
    type_abbreviation="TTD_STR_ABBREV_LIVESTOCK",
    sprite="NEW_CARGO_SPRITE",
    weight="0.1875",  # average weight of a shetland pony apparently (and no we don't eat ponies, but eh)
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_WEIRD", "CC_NON_POTABLE"],
    cargo_label="LVST",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_ITEMS",
    items_of_cargo="TTD_STR_QUANTITY_LIVESTOCK",
    penalty_lowerbound="0",
    single_penalty_length="15",
    price_factor=122,
    capacity_multiplier="1",
    icon_indices=(4, 0),
)
