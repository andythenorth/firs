"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryExtractive

industry = IndustryPrimaryExtractive(id='oil_wells',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='152',
                    prospect_chance='0.75',
                    name='TTD_STR_INDUSTRY_NAME_OIL_WELLS',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    spec_flags='0',
                    prod_cargo_types=['OIL_'],
                    layouts='AUTO',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    prob_in_game='3',
                    prob_random='5',
                    fund_cost_multiplier='230',
                    prod_multiplier='[28]',
                    substitute='0',
                    template="refactor_oil_wells.pypnml",
                    intro_year=1830)

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True

industry.add_tile(id='oil_wells_tile_pump')
industry.add_tile(id='oil_wells_tile_building')

spriteset_ground_pump = industry.add_spriteset(
    id = 'oil_wells_spriteset_ground_pump',
    type='empty',
)
sprite_ground_overlay_pump = industry.add_sprite(
    sprite_number = 2173
)
sprite_pump = industry.add_sprite(
    sprite_number = '2174 + (((animation_frame % 11) < 6) ? (animation_frame % 11) : 10 - (animation_frame % 11))',
    xoffset= 1,
    yoffset= 2,
    xextent= 15,
    yextent= 14
)
industry.add_spritelayout(
    id = 'oil_wells_spritelayout_pump',
    ground_sprite = spriteset_ground_pump,
    ground_overlay = sprite_ground_overlay_pump,
    building_sprites = [sprite_pump],
    fences = ['nw','ne','se','sw']
)

spriteset_ground_building = industry.add_spriteset(
    id = 'oil_wells_spriteset_ground_overlay_building',
    type='empty',
)
sprite_ground_overlay_building = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS',
)
spriteset_building = industry.add_spriteset(
    id = 'oil_wells_spriteset_building',
    sprites = [(10, 10, 64, 38, -31, -9)],
    xoffset= 1,
    yoffset= 2,
    xextent= 15,
    yextent= 14
)
industry.add_spritelayout(
    id = 'oil_wells_spritelayout_building',
    ground_sprite = spriteset_ground_building,
    ground_overlay = sprite_ground_overlay_building,
    building_sprites = [spriteset_building],
    fences = ['nw','ne','se','sw']
)


industry.add_industry_layout(
    id = 'oil_wells_industry_layout_1',
    layout = [(0, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (0, 7, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (1, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (2, 1, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (3, 5, 'oil_wells_tile_building', 'oil_wells_spritelayout_building'),
              (4, 8, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (5, 1, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (5, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
    ]
)
industry.add_industry_layout(
    id = 'oil_wells_industry_layout_2',
    layout = [(0, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (0, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (1, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (2, 8, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (4, 4, 'oil_wells_tile_building', 'oil_wells_spritelayout_building'),
              (4, 8, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (5, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (6, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (6, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
    ]
)
industry.add_industry_layout(
    id = 'oil_wells_industry_layout_3',
    layout = [(0, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (0, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (1, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (1, 6, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (2, 0, 'oil_wells_tile_building', 'oil_wells_spritelayout_building'),
              (3, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (3, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
    ]
)
industry.add_industry_layout(
    id = 'oil_wells_industry_layout_4',
    layout = [(0, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (0, 4, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (0, 6, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (1, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (1, 8, 'oil_wells_tile_building', 'oil_wells_spritelayout_building'),
              (2, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (2, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (3, 1, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (5, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (5, 2, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
              (6, 0, 'oil_wells_tile_pump', 'oil_wells_spritelayout_pump'),
    ]
)
