from cargo import Cargo

cargo = Cargo(
    id="slag",
    type_name="string(STR_CARGO_NAME_SLAG)",
    unit_name="string(STR_CARGO_NAME_SLAG)",
    type_abbreviation="string(STR_CID_SLAG)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_NON_POTABLE"],
    cargo_label="SLAG",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_SLAG)",
    penalty_lowerbound="64",
    single_penalty_length="255",
    price_factor=85,  # deliberately low, needed to space out cargo payments to allow unique rates
    capacity_multiplier="1",
    allow_animated_pixels=True,  # slag uses fire cycle pixels, by design, so suppress NML pixel warnings
    icon_indices=(11, 3),
)
