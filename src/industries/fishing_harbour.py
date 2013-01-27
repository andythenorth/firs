"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from firs import Industry, Tile, Sprite, Spriteset, SpriteLayout, IndustryLayout

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='fishing_harbour',
                    accept_cargo_types=['MNSP', 'FISH'],
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['FOOD'],
                    layouts='AUTO',
                    prob_in_game='8',
                    prob_random='14',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='15',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_PROCESSING',
                    min_cargo_distr='5',
                    spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER)',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_FISHING_HARBOUR)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_IND_FISHING_HARBOUR))',
                    fund_cost_multiplier='150',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS')

industry.economy_variations['BASIC_TEMPERATE'].disabled = True
industry.economy_variations['BASIC_TROPIC'].disabled = True


industry.add_industry_layout(
    id = 'fishing_harbour_industry_layout_1',
    layout = [(0, 3, 'fishing_harbour_tile_1', 'foo'),
              (0, 4, 'fishing_harbour_tile_2', 'foo'),
              (1, 0, '255', 'foo'),
              (1, 1, 'fishing_harbour_tile_1', 'foo'),
              (1, 2, 'fishing_harbour_tile_1', 'foo'),
              (1, 3, 'fishing_harbour_tile_1', 'foo'),
              (1, 4, 'fishing_harbour_tile_2', 'foo'),
              (2, 1, 'fishing_harbour_tile_1', 'foo'),
              (2, 2, 'fishing_harbour_tile_1', 'foo'),
    ]
)
industry.add_industry_layout(
    id = 'fishing_harbour_industry_layout_2',
    layout = [(0, 0, '255', 'foo'),
              (0, 1, '255', 'foo'),
              (0, 2, '255', 'foo'),
              (1, 0, 'fishing_harbour_tile_1', 'foo'),
              (1, 1, 'fishing_harbour_tile_1', 'foo'),
              (1, 255, '255', 'foo'),
              (2, 0, 'fishing_harbour_tile_1', 'foo'),
              (2, 1, 'fishing_harbour_tile_1', 'foo'),
              (2, 2, 'fishing_harbour_tile_1', 'foo'),
              (2, 255, '255', 'foo'),
              (3, 1, 'fishing_harbour_tile_2', 'foo'),
              (3, 2, 'fishing_harbour_tile_2', 'foo'),
    ]
)
industry.add_industry_layout(
    id = 'fishing_harbour_industry_layout_3',
    layout = [(0, 0, 'fishing_harbour_tile_2', 'foo'),
              (0, 1, 'fishing_harbour_tile_2', 'foo'),
              (0, 2, 'fishing_harbour_tile_2', 'foo'),
              (1, 0, 'fishing_harbour_tile_1', 'foo'),
              (1, 2, 'fishing_harbour_tile_1', 'foo'),
              (2, 1, 'fishing_harbour_tile_1', 'foo'),
              (2, 2, 'fishing_harbour_tile_1', 'foo'),
              (2, 3, 'fishing_harbour_tile_1', 'foo'),
              (2, 4, '255', 'foo'),
              (3, 2, '255', 'foo'),
              (3, 3, '255', 'foo'),
    ]
)
industry.add_industry_layout(
    id = 'fishing_harbour_industry_layout_4',
    layout = [(0, 0, 'fishing_harbour_tile_2', 'foo'),
              (0, 1, 'fishing_harbour_tile_1', 'foo'),
              (0, 2, 'fishing_harbour_tile_1', 'foo'),
              (0, 3, 'fishing_harbour_tile_1', 'foo'),
              (0, 4, 'fishing_harbour_tile_1', 'foo'),
              (0, 5, '255', 'foo'),
              (1, 0, 'fishing_harbour_tile_2', 'foo'),
              (1, 1, 'fishing_harbour_tile_1', 'foo'),
              (1, 2, 'fishing_harbour_tile_1', 'foo'),
              (1, 4, 'fishing_harbour_tile_1', 'foo'),
              (1, 5, '255', 'foo'),
              (2, 3, '255', 'foo'),
              (2, 4, '255', 'foo'),
              (2, 5, '255', 'foo'),
    ]
)
industry.add_industry_layout(
    id = 'fishing_harbour_industry_layout_5',
    layout = [(0, 0, 'fishing_harbour_tile_2', 'foo'),
              (1, 0, 'fishing_harbour_tile_1', 'foo'),
              (1, 2, '255', 'foo'),
              (2, 0, 'fishing_harbour_tile_1', 'foo'),
              (2, 1, 'fishing_harbour_tile_1', 'foo'),
              (2, 2, 'fishing_harbour_tile_1', 'foo'),
              (2, 3, '255', 'foo'),
              (3, 0, 'fishing_harbour_tile_1', 'foo'),
              (3, 1, 'fishing_harbour_tile_1', 'foo'),
              (3, 2, 'fishing_harbour_tile_1', 'foo'),
              (3, 3, '255', 'foo'),
              (4, 255, '255', 'foo'),
              (4, 0, 'fishing_harbour_tile_1', 'foo'),
              (4, 1, 'fishing_harbour_tile_1', 'foo'),
              (4, 2, 'fishing_harbour_tile_1', 'foo'),
              (4, 3, '255', 'foo'),
              (5, 255, '255', 'foo'),
              (5, 0, '255', 'foo'),
              (5, 1, '255', 'foo'),
              (5, 2, '255', 'foo'),
              (5, 3, '255', 'foo'),
    ]
)
