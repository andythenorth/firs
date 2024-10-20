from cargo import Cargo

cargo = Cargo(
    id="passengers",
    type_name="TTD_STR_CARGO_PLURAL_PASSENGERS",
    unit_name="TTD_STR_CARGO_SINGULAR_PASSENGER",
    type_abbreviation="TTD_STR_ABBREV_PASSENGERS",
    sprite="NEW_CARGO_SPRITE",
    weight="0.0625",
    is_freight="0",
    cargo_classes = ["CC_PASSENGERS"],
    cargo_label="PASS",
    town_growth_effect="TOWNGROWTH_PASSENGERS",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_PASSENGERS",
    items_of_cargo="TTD_STR_QUANTITY_PASSENGERS",
    penalty_lowerbound="0",
    single_penalty_length="22",
    capacity_multiplier="4",
    price_factor=137,  # pax payment rate is much higher than default; this makes a much wider range of vehicle types and costs viable for pax; the downside is that vehicles balancing for FIRS won't work so well in default
    icon_indices=(0, 0),
)
