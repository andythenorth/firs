from cargo import Cargo

cargo = Cargo(
    id="coal_tar",
    type_name="string(STR_CARGO_NAME_COAL_TAR)",
    unit_name="string(STR_CARGO_NAME_COAL_TAR)",
    type_abbreviation="string(STR_CID_COAL_TAR)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="CTAR",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_COAL_TAR)",
    penalty_lowerbound="64",
    single_penalty_length="255",
    price_factor=98,  # IRL coal tar is low value, but for gameplay it is transported in low amounts and needs a bonus
    capacity_multiplier="1",
    icon_indices=(14, 4),
)
