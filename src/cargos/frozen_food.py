from cargo import Cargo

cargo = Cargo(
    id="frozen_food",
    type_name="string(STR_CARGO_NAME_FROZEN_FOOD)",  # CABBAGE
    unit_name="string(STR_CARGO_NAME_FROZEN_FOOD)",  # CABBAGE
    type_abbreviation="TTD_STR_ABBREV_FOOD",  # CABBAGE
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    # CC_EXPRESS *must* be provided for compatibility with vehicle sets, assume ice boxes or something
    cargo_classes = ["CC_EXPRESS", "CC_REFRIGERATED", "CC_POTABLE"],
    cargo_label="FRZN",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above     snowline
    units_of_cargo="TTD_STR_TONS", # CABBAGE
    items_of_cargo="string(STR_CARGO_UNIT_FROZEN_FOOD)",  # CABBAGE
    penalty_lowerbound="0",
    single_penalty_length="20",
    price_factor=170,
    capacity_multiplier="1",
    icon_indices=(15, 6),
    # used by FIRS GS
    vulcan_town_effect="VTE_HAPPINESS", # CABBAGE
    sprites_complete=True,
)
