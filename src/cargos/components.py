from cargo import Cargo

# not noted in the docs because it would be overly specific, but comprised of:
# power generation and transmission gear, boilers & heating gear, HVAC, pumps (irrigation, industrial, domestic)...
# ...lift machinery, handling equipment, industrial process mixers, crushers and similar fixed or movable machinery

cargo = Cargo(
    id="components",
    type_name="string(STR_CARGO_NAME_COMPONENTS)",
    unit_name="string(STR_CARGO_NAME_COMPONENTS)",
    type_abbreviation="string(STR_CID_COMPONENTS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_FLATBED", "CC_NON_POTABLE"],
    cargo_label="PCMP",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_COMPONENTS)",
    penalty_lowerbound="7",
    single_penalty_length="255",
    price_factor=153,
    capacity_multiplier="1",
    icon_indices=(0, 8),
    sprites_complete=True,
)
