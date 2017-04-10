from industry import IndustryPrimaryExtractive

industry = IndustryPrimaryExtractive(id='oil_rig',
                    prod_cargo_types=['OIL_', 'PASS'],
                    prob_in_game='6',
                    prob_random='6',
                    prod_multiplier='[29, 4]',
                    substitute='5',
                    map_colour='152',
                    spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER, IND_FLAG_AI_CREATES_AIR_AND_SHIP_ROUTES)',
                    location_checks=dict(coast_distance=True),
                    prospect_chance='0.75',
                    name='TTD_STR_INDUSTRY_NAME_OIL_RIG',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_WATER))',
                    fund_cost_multiplier='255',
                    override='5',
                    template="refactor/refactor_oil_rig.pynml",
                    intro_year=1967)

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True

# industry uses layouts and sprites from default game, no custom layouts etc
"""
To-do
- put tile in
- get sprite numbers of default sprites using in-game tools
- put spritesets in
- put spritelayouts in
- figure out where the station tiles are
- put industry layouts in, as per https://newgrf-specs.tt-wiki.net/wiki/IndustryDefaultProps
- set layouts flag to 'AUTO'
- remove custom template from filesystem, and the property declaring it here
"""
