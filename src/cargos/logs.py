from cargo import Cargo

cargo = Cargo(
    id="logs",
    type_name="string(STR_CARGO_LOGS_NAME)",
    unit_name="string(STR_CARGO_LOGS_NAME)",
    type_abbreviation="string(STR_CARGO_LOGS_CID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    # for legacy compatibility WOOD label is used as there is very wide support for it
    # but as a name string that has proven ambiguous in games - conflates with finished wood products (lumber, finished timber etc)
    cargo_label="WOOD",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_LOGS_CARGO_UNIT)",
    penalty_lowerbound="24",
    single_penalty_length="255",
    price_factor=104,
    capacity_multiplier="1",
    icon_indices=(8, 0),
    sprites_complete=True,
)
