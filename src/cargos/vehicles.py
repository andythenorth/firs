from cargo import Cargo

cargo = Cargo(
    id="vehicles",
    type_name="string(STR_CARGO_NAME_VEHICLES)",
    unit_name="string(STR_CARGO_NAME_VEHICLES)",
    type_abbreviation="string(STR_CID_VEHICLES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="VEHI",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_VEHICLES)",
    penalty_lowerbound="15",
    single_penalty_length="128",
    price_factor=175,
    capacity_multiplier="1",
    icon_indices=(15, 2),
    # used by FIRS GS
    vulcan_town_effect="VTE_HAPPINESS",
    sprites_complete=True,
)
