from cargo import Cargo

cargo = Cargo(
    id="paints_and_coatings",
    type_name="string(STR_CARGO_NAME_PAINTS_AND_COATINGS)",
    unit_name="string(STR_CARGO_NAME_PAINTS_AND_COATINGS)",
    type_abbreviation="string(STR_CID_PAINTS_AND_COATINGS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="COAT",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_PAINTS_AND_COATINGS)",
    penalty_lowerbound="20",
    single_penalty_length="255",
    price_factor=135,
    capacity_multiplier="1",
    icon_indices=(5, 5),
)
