from cargo import Cargo

cargo = Cargo(
    id="molasses",
    type_name="string(STR_CARGO_MOLASSES_NAME)",
    unit_name="string(STR_CARGO_MOLASSES_NAME)",
    type_abbreviation="string(STR_CARGO_MOLASSES_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"], # molasses treated as non-potable, as it's primarily an animal feed cargo, suitable for transport in chemical product tankers
    cargo_label="MOLA",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_MOLASSES_CARGO_UNIT)",
    penalty_lowerbound="0",
    single_penalty_length="16",
    capacity_multiplier="1",
    price_factor=106,
    icon_indices=(11, 7),
    sprites_complete=True,
)
