from cargo import Cargo

# expansion of standard food to explicitly include beverages, allowing alcohol to be dropped in FIRS 6

cargo = Cargo(
    id="food_and_beverages",
    type_name="string(STR_CARGO_FOOD_AND_BEVERAGES_NAME)",
    unit_name="string(STR_CARGO_FOOD_AND_BEVERAGES_NAME)",
    type_abbreviation="TTD_STR_ABBREV_FOOD",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_EXPRESS", "CC_COVERED_BULK", "CC_PIECE_GOODS", "CC_LIQUID_BULK", "CC_POTABLE", "CC_REFRIGERATED"],
    cargo_label="FOOD", # reuse standard FOOD for compatibility
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above     snowline
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_FOOD_AND_BEVERAGES_CARGO_UNIT)",
    penalty_lowerbound="0",
    single_penalty_length="20",
    price_factor=168,
    capacity_multiplier="1",
    icon_indices=(12, 0),
    # used by FIRS GS
    vulcan_town_effect="VTE_HAPPINESS",
    sprites_complete=True,
)
