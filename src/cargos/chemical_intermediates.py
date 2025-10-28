from cargo import Cargo

cargo = Cargo(
    id="chemical_intermediates",
    type_name="string(STR_CARGO_NAME_CHEMICAL_INTERMEDIATES)",
    unit_name="string(STR_CARGO_NAME_CHEMICAL_INTERMEDIATES)",
    type_abbreviation="string(STR_CID_CHEMICAL_INTERMEDIATES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.2",  # extra realism, per forum suggestion Nov 2017
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="CHIM",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_CHEMICAL_INTERMEDIATES)",
    penalty_lowerbound="20",
    single_penalty_length="255",
    price_factor=115,
    capacity_multiplier="1",
    icon_indices=(10, 1),
)
